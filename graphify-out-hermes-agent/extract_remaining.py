#!/usr/bin/env python3
"""
Batch graphify semantic extraction for remaining chunks.
Reads each chunk file, reads the files, extracts entities/relationships,
and merges results into .graphify_semantic_new.json.

This runs locally without subagents - it does file-reading and basic extraction.
"""
import json
import re
import sys
from pathlib import Path
from datetime import datetime, timezone

PROGRESS_FILE = Path('graphify-out/.graphify_progress.json')
SEMANTIC_FILE = Path('graphify-out/.graphify_semantic_new.json')
CHUNKS_DIR = Path('graphify-out')

def load_progress():
    return json.loads(PROGRESS_FILE.read_text())

def save_progress(p):
    PROGRESS_FILE.write_text(json.dumps(p, indent=2))

def load_semantic():
    return json.loads(SEMANTIC_FILE.read_text())

def save_semantic(s):
    SEMANTIC_FILE.write_text(json.dumps(s, indent=2))

def extract_from_file(filepath):
    """Basic extraction: identify key entities from file content."""
    nodes = []
    edges = []
    try:
        content = Path(filepath).read_text(errors='replace')
    except Exception:
        return nodes, edges

    fname = Path(filepath)
    stem = fname.stem
    ftype = 'code' if fname.suffix in ('.py', '.js', '.ts', '.swift', '.go', '.rs') else 'document'

    # Extract YAML frontmatter metadata
    author = None
    name = None
    desc = None
    if content.startswith('---'):
        end = content.find('---', 3)
        if end > 0:
            fm = content[3:end]
            for line in fm.split('\n'):
                if line.startswith('name:'):
                    name = line.split(':', 1)[1].strip().strip('"').strip("'")
                elif line.startswith('description:'):
                    desc = line.split(':', 1)[1].strip().strip('"').strip("'")[:80]
                elif line.startswith('author:'):
                    author = line.split(':', 1)[1].strip().strip('"').strip("'")

    label = name or stem.replace('_', ' ').replace('-', ' ').title()
    node_id = f"{stem}_{re.sub(r'[^a-zA-Z0-9_]', '_', stem)[:40]}"

    node = {
        'id': node_id,
        'label': label,
        'file_type': ftype,
        'source_file': str(filepath),
        'source_location': None,
        'source_url': None,
        'captured_at': None,
        'author': author,
        'contributor': None
    }
    nodes.append(node)

    # Extract imports from code files
    if ftype == 'code':
        for match in re.finditer(r'^(?:from|import)\s+(\S+)', content, re.MULTILINE):
            imp = match.group(1).split('.')[0]
            if imp not in ('os', 'sys', 'json', 'pathlib', 're', 'typing', 'datetime', 'time', 'collections', 'functools', 'dataclasses', 'abc', 'io', 'copy', 'hashlib', 'math', 'uuid', 'logging', 'contextlib', 'argparse', 'textwrap', 'urllib', 'enum', 'threading', 'subprocess', 'shutil', 'tempfile', 'unittest', 'asyncio', 'struct', 'base64', 'csv', 'xml', 'html'):
                edges.append({
                    'source': node_id,
                    'target': f"ext_{imp}",
                    'relation': 'references',
                    'confidence': 'EXTRACTED',
                    'confidence_score': 1.0,
                    'source_file': str(filepath),
                    'source_location': match.start(),
                    'weight': 1.0
                })

    # Extract class/function names from code
    if ftype == 'code':
        for match in re.finditer(r'^class\s+(\w+)', content, re.MULTILINE):
            cname = match.group(1)
            cnode_id = f"{stem}_{cname}"
            nodes.append({
                'id': cnode_id,
                'label': cname,
                'file_type': 'code',
                'source_file': str(filepath),
                'source_location': match.start(),
                'source_url': None,
                'captured_at': None,
                'author': None,
                'contributor': None
            })
            edges.append({
                'source': node_id,
                'target': cnode_id,
                'relation': 'implements',
                'confidence': 'EXTRACTED',
                'confidence_score': 1.0,
                'source_file': str(filepath),
                'source_location': match.start(),
                'weight': 1.0
            })

        for match in re.finditer(r'^def\s+(\w+)', content, re.MULTILINE):
            fn = match.group(1)
            if fn.startswith('_'):
                continue
            fn_id = f"{stem}_{fn}"
            nodes.append({
                'id': fn_id,
                'label': fn,
                'file_type': 'code',
                'source_file': str(filepath),
                'source_location': match.start(),
                'source_url': None,
                'captured_at': None,
                'author': None,
                'contributor': None
            })
            edges.append({
                'source': node_id,
                'target': fn_id,
                'relation': 'implements',
                'confidence': 'EXTRACTED',
                'confidence_score': 1.0,
                'source_file': str(filepath),
                'source_location': match.start(),
                'weight': 1.0
            })

    # Extract cross-file references
    for match in re.finditer(r'(?:hermes-agent/[^\s\)"\']+\.(?:py|md|txt|yaml|yml|json))', content):
        ref = match.group(0)
        ref_stem = Path(ref).stem
        ref_id = f"{ref_stem}_{re.sub(r'[^a-zA-Z0-9_]', '_', ref_stem)[:40]}"
        edges.append({
            'source': node_id,
            'target': ref_id,
            'relation': 'references',
            'confidence': 'EXTRACTED',
            'confidence_score': 1.0,
            'source_file': str(filepath),
            'source_location': match.start(),
            'weight': 1.0
        })

    return nodes, edges

def process_chunk(chunk_idx):
    chunk_file = CHUNKS_DIR / f'chunk_{chunk_idx}.json'
    if not chunk_file.exists():
        return 0, 0, 0

    chunk = json.loads(chunk_file.read_text())
    files = chunk.get('files', [])

    all_nodes = []
    all_edges = []

    for f in files:
        if Path(f).exists():
            nodes, edges = extract_from_file(f)
            all_nodes.extend(nodes)
            all_edges.extend(edges)

    return len(all_nodes), len(all_edges), 0

def main():
    progress = load_progress()
    total_chunks = progress['total_chunks']
    completed = set(progress['completed_chunks'])

    remaining = [i for i in range(total_chunks) if i not in completed]
    print(f"Remaining chunks: {len(remaining)}/{total_chunks}")

    semantic = load_semantic()
    seen_ids = {n['id'] for n in semantic['nodes'] if isinstance(n, dict) and 'id' in n}

    for chunk_idx in remaining:
        n_nodes, n_edges, n_he = process_chunk(chunk_idx)

        # Load chunk results and merge
        chunk_file = CHUNKS_DIR / f'chunk_{chunk_idx}.json'
        chunk = json.loads(chunk_file.read_text())
        files = chunk.get('files', [])

        added_nodes = 0
        for f in files:
            if not Path(f).exists():
                continue
            nodes, edges = extract_from_file(f)
            for n in nodes:
                if isinstance(n, dict) and n.get('id') not in seen_ids:
                    semantic['nodes'].append(n)
                    seen_ids.add(n['id'])
                    added_nodes += 1
            semantic['edges'].extend([e for e in edges if isinstance(e, dict)])

        progress['completed_chunks'].append(chunk_idx)
        progress['total_nodes'] = len(semantic['nodes'])
        progress['total_edges'] = len(semantic['edges'])
        progress['last_updated'] = datetime.now(timezone.utc).isoformat()

        if chunk_idx % 10 == 0 or chunk_idx == remaining[-1]:
            save_progress(progress)
            save_semantic(semantic)
            print(f"Chunk {chunk_idx}: +{added_nodes} nodes. Total: {len(semantic['nodes'])} nodes, {len(semantic['edges'])} edges. Progress: {len(progress['completed_chunks'])}/{total_chunks}")

    # Final save
    save_progress(progress)
    save_semantic(semantic)
    print(f"Done! Total: {len(semantic['nodes'])} nodes, {len(semantic['edges'])} edges, {len(progress['completed_chunks'])} chunks")

if __name__ == '__main__':
    main()
