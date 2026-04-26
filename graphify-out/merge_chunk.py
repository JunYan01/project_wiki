#!/usr/bin/env python3
"""Merge a chunk's JSON result into the semantic and progress files.
Usage: python merge_chunk.py <chunk_number> < result.json
"""
import json, sys
from pathlib import Path
from datetime import datetime, timezone

SEMANTIC = Path('graphify-out/.graphify_semantic_new.json')
PROGRESS = Path('graphify-out/.graphify_progress.json')

chunk_num = int(sys.argv[1])
# Support both file path argument and stdin
if len(sys.argv) > 2:
    data = json.loads(Path(sys.argv[2]).read_text())
else:
    data = json.loads(sys.stdin.read())

sem = json.loads(SEMANTIC.read_text())
prog = json.loads(PROGRESS.read_text())

seen = {n['id'] for n in sem['nodes'] if isinstance(n, dict) and 'id' in n}
added = 0
for n in data.get('nodes', []):
    if isinstance(n, dict) and n.get('id') not in seen:
        sem['nodes'].append(n)
        seen.add(n['id'])
        added += 1
sem['edges'].extend([e for e in data.get('edges', []) if isinstance(e, dict)])
for h in data.get('hyperedges', []):
    if isinstance(h, dict):
        if 'id' not in h:
            h['id'] = f'chunk{chunk_num}_he_{len(sem.get("hyperedges",[]))}'
        sem.setdefault('hyperedges', []).append(h)

SEMANTIC.write_text(json.dumps(sem, indent=2))
if chunk_num not in prog['completed_chunks']:
    prog['completed_chunks'].append(chunk_num)
prog['total_nodes'] = len(sem['nodes'])
prog['total_edges'] = len(sem['edges'])
prog['total_hyperedges'] = len(sem.get('hyperedges', []))
prog['last_updated'] = datetime.now(timezone.utc).isoformat()
PROGRESS.write_text(json.dumps(prog, indent=2))

print(f'Chunk {chunk_num}: +{added} nodes. Total: {len(sem["nodes"])} nodes, {len(sem["edges"])} edges, {len(prog["completed_chunks"])}/77 done')
