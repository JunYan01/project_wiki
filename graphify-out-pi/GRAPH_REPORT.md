# Graph Report - pi  (2026-06-18)

## Corpus Check
- Large corpus: 756 files · ~900,152 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 6366 nodes · 9331 edges · 626 communities detected
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 446 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `InteractiveMode` - 169 edges
2. `SettingsManager` - 123 edges
3. `AgentSession` - 114 edges
4. `DefaultPackageManager` - 94 edges
5. `Editor` - 80 edges
6. `AgentHarness` - 50 edges
7. `TUI` - 48 edges
8. `SessionManager` - 44 edges
9. `RpcClient` - 43 edges
10. `ExtensionRunner` - 39 edges

## Surprising Connections (you probably didn't know these)
- `Tool execution: parallel vs sequential` --semantically_similar_to--> `QueueMode type`  [INFERRED] [semantically similar]
  pi/packages/agent/README.md → pi/packages/agent/src/types.ts
- `red-circle.png (vision test fixture)` --shares_data_with--> `Context overflow handling`  [AMBIGUOUS]
  pi/packages/ai/test/data/red-circle.png → pi/packages/ai/test/context-overflow.test.ts
- `Context overflow handling` --rationale_for--> `Changelog: parenthesized max context length overflow detection`  [INFERRED]
  pi/packages/ai/test/context-overflow.test.ts → pi/packages/coding-agent/CHANGELOG.md
- `Changelog: OpenAI/Codex context-window metadata fix (272k)` --rationale_for--> `Context overflow handling`  [INFERRED]
  pi/packages/coding-agent/CHANGELOG.md → pi/packages/ai/test/context-overflow.test.ts
- `Exy Pufferfish Illustration` --conceptually_related_to--> `Pi Terminal Coding Harness`  [AMBIGUOUS]
  pi/packages/coding-agent/docs/images/exy.png → pi/packages/coding-agent/docs/index.md

## Hyperedges (group relationships)
- **he_message_pipeline** — concept_transform_context, concept_convert_to_llm, stream_assistant_response_fn, stream_simple_pi_ai [INFERRED]
- **he_tool_call_pipeline** — execute_tool_calls_fn, prepare_tool_call_fn, finalize_tool_call_fn, validate_tool_args_pi_ai [INFERRED]
- **he_harness_doc_triad** — doc_agent_harness_lifecycle, doc_hooks_design, doc_durable_harness [INFERRED]
- **** — types_AgentHarness, compaction_prepareCompaction, compaction_compact, compaction_generateSummary [INFERRED]
- **he_google_thinking_pipeline** — google-vertex_streamGoogleVertex, google_streamGoogle, google-shared_isThinkingPart, google-shared_retainThoughtSignature, google-vertex_getDisabledThinkingConfig [INFERRED]
- **he_env_resolution_chain** — provider-env_getProviderEnvValue, provider-env_getBunSandboxEnvValue, amazon-bedrock_streamBedrock, cloudflare_resolveCloudflareBaseUrl, azure-openai-responses_resolveAzureConfig, google-vertex_createClient [INFERRED]
- **he_streaming_abstraction** — event-stream_EventStream, event-stream_AssistantMessageEventStream, register-builtins_createLazyStream, mistral_consumeChatStream, openai-responses-shared_processResponsesStream [INFERRED]
- **he_bedrock_test_cluster** — bedrock_custom_headers_test, bedrock_endpoint_resolution_test, bedrock_thinking_payload_test, bedrock_provider_src [INFERRED 0.90]
- **he_oauth_device_code_cluster** — oauth_device_code_test, openai_codex_oauth_test, device_code_src, openai_codex_oauth_src [EXTRACTED 1.00]
- **he_e2e_provider_matrix** — abort_test, responseid_test, tool_call_without_result_test, stream_src [INFERRED 0.85]
- **Shared provider test infrastructure: OAuth/API-key/credential helpers (oauth.ts, azure-utils.ts, bedrock-utils.ts, cloudflare-utils.ts)** — empty_test, cross-provider-handoff_test, tool-call-id-normalization_test, anthropic-long-cache-retention-e2e_test, bedrock-models_test [INFERRED]
- **Cache-affinity concern cluster: session-id/prompt_cache_key headers + 64-char clamp across OpenAI/Azure/Codex Responses providers** — openai-responses-copilot-provider_test, openai-codex-stream_test, azure-openai-base-url_test, provider_cache_affinity_headers, prompt_cache_key_64_clamp [INFERRED]
- **Cross-provider compatibility verification chain: tool-call-id normalization + thinking serialization + context handoff** — cross-provider-handoff_test, tool-call-id-normalization_test, anthropic-thinking-disable_test, openai-completions-thinking-as-text_test [INFERRED]
- **he_compat_flag_matrix** — cache_retention_supports_long, empty_sig_allow_compat, temperature_supports_temp, adaptive_thinking_force_flag [INFERRED 0.85]
- **he_anthropic_thinking_lifecycle** — interleaved_thinking_test, force_adaptive_thinking_test, anthropic_empty_thinking_sig_test, adaptive_thinking_models_test [INFERRED 0.82]
- **he_tool_id_normalization** — transform_normalize_tool_call_id, foreign_id_short_hash, toolname_cc_casing_roundtrip [INFERRED 0.80]
- **he_context_overflow_validation** — context_overflow_test, overflow_isContextOverflow, stream_complete, models_getModel, concept_context_overflow [EXTRACTED 1.00]
- **he_pi_modes** — concept_rpc_protocol, concept_json_events, concept_sdk, codingagent_readme [INFERRED 0.85]
- **he_extension_customization** — concept_extension, doc_extensions, doc_tui, doc_compaction, doc_prompt_templates [INFERRED 0.85]
- **he_system_prompt_modifiers** — pirate_extension, claude-rules_extension, ssh_extension, before_agent_start_hook [EXTRACTED 1.00]
- **he_builtin_tool_replacers** — minimal-mode_extension, built-in-tool-renderer_extension, ssh_extension, pi_coding_agent_create_tools [EXTRACTED 1.00]
- **he_session_state_consumers** — todo_extension, space-invaders_extension, bookmark_extension, pi_session_manager [EXTRACTED 1.00]
- **he_dangerous_bash_guards** — permission-gate_extension, rpc-demo_dangerous_bash_gate, protected-paths_extension [INFERRED]
- **he_prompt_modification_chain** — preset_extension, prompt-customizer_extension, concept_before_agent_start_systemprompt [INFERRED]
- **he_branch_history_consumers** — qna_extension, summarize_extension, custom-footer_extension, concept_session_manager_branch [INFERRED]
- **hyper_extension_tool_pattern** — tictactoe_ticTacToeTool, questionnaire_tool, structuredoutput_tool, truncatedtool_rgTool, hello_helloTool [INFERRED 0.85]
- **hyper_git_integration** — gitcheckpoint_extension, autocommit_extension, gitmerge_extension [INFERRED 0.90]
- **hyper_overlay_rendering** — overlayqa_extension, overlayqa_AnimationDemoComponent, overlayqa_FocusDemoController, rainboweditor_RainbowEditor [INFERRED 0.80]
- **he_doom_overlay_pipeline** — index_doomoverlay, wadfinder_findWadFile, doomengine_DoomEngine, doomcomponent_DoomOverlayComponent [EXTRACTED 1.00]
- **he_gitlabduo_auth_chain** — index_gitlabduo_loginGitLab, index_gitlabduo_getDirectAccessToken, index_gitlabduo_streamGitLabDuo, index_gitlabduo_MODELS [EXTRACTED 1.00]
- **he_tool_isolation_extensions** — index_gondolin, index_sandbox, index_subagent [INFERRED 0.85]
- **he_subagent_pipeline** — scout_agent, planner_agent, worker_agent [INFERRED]
- **he_sdk_core_services** — AuthStorage, ModelRegistry, SettingsManager, SessionManager [INFERRED]
- **he_resource_loader_hooks** — DefaultResourceLoader, sdk_03_custom_prompt, sdk_04_skills, sdk_07_context_files, sdk_08_prompt_templates [INFERRED]
- **he_self_update_flow** — package_manager_cli_runSelfUpdate, config_getSelfUpdateCommand, config_detectInstallMethod, config_isBunBinary [EXTRACTED 1.00]
- **he_project_trust_resolution** — package_manager_cli_createCommandSettingsManager, core_project_trust_resolveProjectTrusted, cli_project_trust_createContext, cli_startup_ui, core_settings_manager [EXTRACTED 1.00]
- **he_model_pattern_parsing** — core_model_resolver, model_resolver_parseModelPattern, cli_args_isValidThinkingLevel, model_resolver_defaultModelPerProvider, core_defaults [EXTRACTED 1.00]
- **he_runtime_assembly** — agent-session-services_createAgentSessionServices, resource-loader_DefaultResourceLoader, auth-storage_AuthStorage, trust-manager_ProjectTrustStore, session-manager_SessionManager [INFERRED]
- **he_session_lifecycle** — agent-session-runtime_AgentSessionRuntime, session-manager_SessionManager, session-cwd_assertSessionCwdExists, session-manager_buildSessionContext [INFERRED]
- **he_prompt_construction** — system-prompt_buildSystemPrompt, skills_formatSkillsForPrompt, resource-loader_loadProjectContextFiles, resource-loader_DefaultResourceLoader [INFERRED]
- **he_sdk_assembly** — sdk_createAgentSession, model-registry_ModelRegistry, agent-session_AgentSession, extensions_loader_Loader [INFERRED]
- **he_compaction_pipeline** — agent-session_Compaction, compaction_compact, compaction_CutPoint, compaction_GenerateSummary, compaction-utils_SerializeConversation [INFERRED]
- **he_html_export_pipeline** — export-html_index_ExportSessionToHtml, export-html_index_PreRenderCustomTools, tool-renderer_ToolHtmlRenderer, ansi-to_html_AnsiToHtml, template_js_SessionRenderer, vendor_marked, vendor_highlightjs [INFERRED]
- **he_pluggable_ops_tools** — read_ReadOperations, find_FindOperations, ls_LsOperations, grep_GrepOperations, edit_EditOperations, write_WriteOperations, bash_BashOperations, pluggableToolOps_pattern [INFERRED 0.90]
- **he_truncation_consumers** — truncate_truncateHead, truncate_truncateTail, read_tool, find_tool, ls_tool, grep_tool, bash_tool, outputaccumulator_OutputAccumulator [INFERRED 0.90]
- **he_edit_pipeline** — edit_tool, editdiff_applyEditsToNormalizedContent, editdiff_fuzzyFindText, editdiff_normalizeForFuzzyMatch, editdiff_computeEditsDiff, filemutationqueue_withFileMutationQueue [EXTRACTED 1.00]
- **he_components_theme_usage** — keybinding-hints_keyHint, dynamic-border_DynamicBorder, theme_Theme, settings-selector_SettingsSelectorComponent, session-selector_SessionSelectorComponent [INFERRED]
- **he_rpc_protocol** — rpc-client_RpcClient, rpc-mode_runRpcMode, rpc-types_RpcCommand, jsonl_serializeJsonLine, rpc_proto_strictJsonlFraming [INFERRED]
- **he_theme_color_pipeline** — theme_rgbTo256, theme_Theme, theme_globalInstance, theme_initTheme, theme_detectTerminalBackgroundTheme [INFERRED]
- **he_image_processing_pipeline** — image_resize_resizeImage, image_resize_worker_resizeWorker, image_resize_core_resizeImageInProcess, concept_photon_wasm, concept_exif_orientation [INFERRED 0.90]
- **he_clipboard_platform_fallbacks** — clipboard_copyToClipboard, clipboard_osc52, rationale_linux_clipboard_native_addon, clipboard_image_isWaylandSession, rationale_wsl_powershell_clipboard [INFERRED 0.90]
- **he_version_management** — version_check_checkForNewPiVersion, version_check_getLatestPiRelease, pi_user_agent_getPiUserAgent, changelog_compareVersions, version_check_isNewerPackageVersion [INFERRED 0.85]
- **he_file_image_pipeline** — mime_detectSupportedImageMimeType, exif-orientation_applyExifOrientation, mime_detectSupportedImageMimeTypeFromFile [INFERRED 0.85]
- **he_session_test_stack** — core_AgentSession, core_SessionManager, core_AuthStorage, test_utilities [EXTRACTED 1.00]
- **he_git_url_parse** — git_parseGitUrl, git_splitRef, git_buildGitSource, git_parseGenericGitUrl [EXTRACTED 1.00]
- **he_session_core_deps** — agent-session, session-manager, auth-storage, model-registry, settings-manager [INFERRED]
- **he_extension_runner_pipeline** — extensions-loader_loader, extensions-runner_runner, model-registry, session-manager, extensions-types [INFERRED]
- **he_clipboard_fallback_chain** — clipboard, clipboard-native, clipboard-image, concept-clipboard-fallback [INFERRED]
- **he_resource_loader_core** — resourceloader_DefaultResourceLoader, resourceloader_ExtensionRunner, gitupdate_SettingsManager, sessionmanager_SessionManager [EXTRACTED 1.00]
- **he_session_selector_interactive** — sessionselectorpathdelete_SessionSelectorComponent, sessionselectorrename_KeybindingsManager, themepicker_getAvailableThemes, sessionmanager_SessionManager [INFERRED 0.85]
- **he_session_stats_stack** — agentsessionstats_AgentSession_getSessionStats, sessionmanager_SessionManager, agentsessionstats_ModelRegistry, agentsessionstats_AuthStorage [EXTRACTED 1.00]
- **he_sdk_session_attribution** — sdk_openrouter_attribution_test, rpc_prompt_response_semantics_test, sdk_attribution_captureHeaders, concept_telemetry_gate [INFERRED 0.85]
- **he_osc133_rendering** — user_message_component_test, assistant_message_component_test, concept_osc133_zone_markers [EXTRACTED 1.00]
- **he_extension_examples** — trigger_compact_extension_test, git_merge_and_resolve_extension_test, extensions_discovery_test [INFERRED 0.80]
- **he_terminal_width_bug_repro** — truncate-to-width_test, streaming-render-debug_script, terminal_width_crash_bug [EXTRACTED 0.95]
- **he_skill_validation_fixtures** — skills_consecutive-hyphens, skills_invalid-name-chars, skills_long-name, skills_missing-description, skills_invalid-yaml, skills_name-mismatch [INFERRED 0.85]
- **he_tool_execution_helpers** — tool-execution-component_test, bash_tool_module, read_tool_module, write_tool_module [INFERRED 0.80]
- **he_terminal_input_pipeline** — tui_terminal_ProcessTerminal, tui_stdinbuffer_StdinBuffer, tui_keys_matchesKey, tui_tui_TUI [INFERRED]
- **he_native_modifier_chain** — tui_terminal_ProcessTerminal, tui_native_modifiers_ts, tui_darwin_modifiers_c, tui_win32_console_c [INFERRED]
- **he_differential_render_dependencies** — tui_tui_doRender, tui_tui_compositeOverlays, tui_utils_visibleWidth, tui_utils_sliceByColumn, tui_terminal_image [INFERRED]

## Communities

### Community 0 - "InteractiveMode"
Cohesion: 0.03
Nodes (9): ExpandableText, formatResumeCommand(), hasDefaultModelProvider(), InteractiveMode, isAnthropicSubscriptionAuthKey(), isApiKeyLoginProvider(), isExpandable(), isUnknownModel() (+1 more)

### Community 1 - "Compaction Ts"
Cohesion: 0.02
Nodes (153): AgentSessionRuntime (session lifecycle: new/resume/fork/import), SessionImportFileNotFoundError, createAgentSessionServices (cwd-bound service assembly), AgentSession (core lifecycle abstraction), AgentSession auto-retry with backoff, AgentSession bash execution, AgentSession compaction/auto-compaction, Agent beforeToolCall/afterToolCall hooks (+145 more)

### Community 2 - "SettingsManager"
Cohesion: 0.03
Nodes (5): deepMergeSettings(), FileSettingsStorage, InMemorySettingsStorage, parseTimeoutSetting(), SettingsManager

### Community 3 - "DefaultPackageManager"
Cohesion: 0.04
Nodes (28): addIgnoreRules(), applyPatterns(), collectAncestorAgentsSkillDirs(), collectAutoExtensionEntries(), collectAutoPromptEntries(), collectAutoSkillEntries(), collectAutoThemeEntries(), collectFiles() (+20 more)

### Community 4 - "Rpc Prompt Response Semantics Test"
Cohesion: 0.02
Nodes (104): AgentSession Compaction E2E Tests, AgentSession Dynamic Tool Registration Tests, OpenAI Codex responses provider, AssistantMessageComponent OSC133 Test, BashExecutionComponent Width Tests, Bun CLI Entry Point (bun/cli.ts), isValidThinkingLevel, parseArgs (CLI argument parser) (+96 more)

### Community 5 - "AgentSession"
Cohesion: 0.03
Nodes (1): AgentSession

### Community 6 - "Tools Manager Ts"
Cohesion: 0.03
Nodes (88): Anthropic Adaptive Thinking Model Metadata, Anthropic Eager Tool Input Streaming E2E, Anthropic Empty Thinking Signature Compat, capturePayload(), makeContext(), PayloadCaptured, Anthropic OAuth Tool Name Normalization, Anthropic cache_control ttl 1h (+80 more)

### Community 7 - "Suite Test Harness (createHarness)"
Cohesion: 0.03
Nodes (48): Issue 3317 network connection lost retry regression, AgentSession core class, AgentSessionRuntime factory, SessionManager, UUIDv7 session id generation strategy, AgentSession bash and persistence characterization, AgentSession compaction characterization, AgentSession model and extension characterization (+40 more)

### Community 8 - "Child Process Ts"
Cohesion: 0.03
Nodes (50): buildCompletionValue(), buildFdPathQuery(), CombinedAutocompleteProvider, extractQuotedPrefix(), findLastDelimiter(), findUnclosedQuoteStart(), isTokenStart(), parsePathPrefix() (+42 more)

### Community 9 - "Config Ts"
Cohesion: 0.04
Nodes (83): Agent (pi-agent-core), AgentSession, AgentSession Forking/Branching Tests, AgentSession Retry Tests, AgentSession Runtime (createAgentSessionRuntime/Services/FromServices), AgentSessionRuntime Lifecycle Events Tests, ANSI Util (stripAnsi), AuthStorage (+75 more)

### Community 10 - "Overlay Qa Tests Ts"
Cohesion: 0.03
Nodes (18): AnchorTestComponent, AnimationDemoComponent, box(), EdgeTestComponent, FocusDemoController, FocusPanel, hslToRgb(), MarginTestComponent (+10 more)

### Community 11 - "Models Ts (getModel getModels getSupportedThinkingLevels"
Cohesion: 0.03
Nodes (36): providers/anthropic.ts (streamAnthropic), BedrockRuntimeClient, BedrockRuntimeServiceException, ConverseStreamCommand, driveBedrock(), getModelFixture(), BedrockRuntimeClient, BedrockRuntimeServiceException (+28 more)

### Community 12 - "Editor"
Cohesion: 0.07
Nodes (6): buildDebouncePattern(), buildTriggerPattern(), Editor, isPasteMarker(), segmentWithMarkers(), wordWrapLine()

### Community 13 - "Ts"
Cohesion: 0.04
Nodes (55): adjustBrightness(), convertContentBlocks(), convertMessages(), createGondolinBashOps(), createGondolinEditOps(), createGondolinFindOps(), createGondolinLsOps(), createGondolinReadOps() (+47 more)

### Community 14 - "Jsonl Storage Ts"
Cohesion: 0.04
Nodes (26): encodeCwd(), JsonlSessionRepo, buildLabelsById(), generateEntryId(), headerToSessionMetadata(), invalidEntry(), invalidSession(), isRecord() (+18 more)

### Community 15 - "Agent Class ( Agent Ts)"
Cohesion: 0.04
Nodes (58): AgentEvent union (lifecycle events), AgentLoopConfig interface, AgentOptions interface, pi-agent-core README, AgentState interface, AgentHarness Stream Configuration Test, AgentTool interface, pi-ai CHANGELOG (+50 more)

### Community 16 - "SessionManager"
Cohesion: 0.06
Nodes (20): assertValidSessionId(), buildSessionContext(), buildSessionInfo(), buildSessionInfosWithConcurrency(), createSessionId(), extractTextContent(), findMostRecentSession(), generateId() (+12 more)

### Community 17 - "Marked Min Js"
Cohesion: 0.07
Nodes (53): autolink(), be(), blockquote(), blockTokens(), br(), checkbox(), code(), codespan() (+45 more)

### Community 18 - "Loader Ts"
Cohesion: 0.04
Nodes (27): createExtension(), createExtensionAPI(), createExtensionRuntime(), discoverAndLoadExtensions(), discoverExtensionsInDir(), getAliases(), isExtensionFile(), Loader (+19 more)

### Community 19 - "Dynamic Border Component"
Cohesion: 0.05
Nodes (66): Armin Easter-Egg Component (animated XBM art), Assistant Message Component, Bash Execution Component, Bordered Loader, Branch Summary Message Component, Native Clipboard Loader, Compaction Summary Message Component, OAuth Device Code Login Flow (+58 more)

### Community 20 - "Theme Ts"
Cohesion: 0.06
Nodes (46): Syntax Highlight (highlight/renderHighlightedHtml/supportsLanguage), Syntax Highlight Tests, ansi256ToHex(), bgAnsi(), buildCliHighlightTheme(), colorDistance(), createTheme(), detectTerminalBackgroundFromEnv() (+38 more)

### Community 21 - "TUI"
Cohesion: 0.06
Nodes (8): Container, extractKittyImageIds(), extractKittyImageRows(), isFocusable(), isTermuxSession(), parseKittyImageHeader(), parseSizeValue(), TUI

### Community 22 - "AgentHarness"
Cohesion: 0.08
Nodes (10): AgentHarness, applyStreamOptionsPatch(), cloneStreamOptions(), createFailureMessage(), createUserMessage(), findDuplicateNames(), normalizeHarnessError(), normalizeHookError() (+2 more)

### Community 23 - "Openai Codex Responses Ts"
Cohesion: 0.05
Nodes (36): acquireWebSocket(), applyServiceTierPricing(), buildBaseCodexHeaders(), buildCachedWebSocketRequestBody(), buildSSEHeaders(), buildWebSocketHeaders(), closeWebSocketSilently(), CodexApiError (+28 more)

### Community 24 - "Amazon Bedrock Ts"
Cohesion: 0.05
Nodes (26): buildAdditionalModelRequestFields(), buildSystemPrompt(), convertMessages(), convertToolResultContent(), createImageBlock(), createNonBlankTextBlock(), createRequiredTextBlock(), getConfiguredBedrockRegion() (+18 more)

### Community 25 - "TestTerminal"
Cohesion: 0.04
Nodes (12): isImageLine width-check crash rationale, isImageLine startsWith Bug Regression Test, InputRecorder, TestTerminal, InputRecorder, LoggingVirtualTerminal, TestComponent, Lines (+4 more)

### Community 26 - "Template Js"
Cohesion: 0.07
Nodes (44): applySidebarWidth(), attachHeaderHandlers(), buildActivePathIds(), buildTree(), buildTreePrefix(), clampSidebarWidth(), code(), codespan() (+36 more)

### Community 27 - "Pi Documentation"
Cohesion: 0.05
Nodes (58): Containerization Patterns, Plain Docker Isolation, Gondolin micro-VM, NVIDIA OpenShell Sandbox, Context Overflow Recovery, Custom Providers Extension, Custom Streaming API (streamSimple), OAuth/SSO Provider Support (+50 more)

### Community 28 - "Highlight Min Js"
Cohesion: 0.06
Nodes (24): a(), b(), c(), d(), e(), g(), i(), ke() (+16 more)

### Community 29 - "Read Tool"
Cohesion: 0.06
Nodes (55): BashOperations (pluggable exec backend), createLocalBashOperations, BashSpawnHook (adjust command/cwd/env), bash tool, clankolas.png (elves film still asset), EditOperations (pluggable file-edit backend), Edit legacy oldText/newText arg migration, Edit Live Diff Preview (self renderShell) (+47 more)

### Community 30 - "SessionSelectorComponent"
Cohesion: 0.07
Nodes (8): buildSessionTree(), canonicalizePath(), flattenSessionTree(), formatSessionDate(), SessionList, SessionSelectorComponent, SessionSelectorHeader, shortenPath()

### Community 31 - "TreeList"
Cohesion: 0.06
Nodes (8): compactRawKeys(), formatHelpKeys(), LabelInput, renderHorizontalViewport(), SearchLine, TreeHelp, TreeList, TreeSelectorComponent

### Community 32 - "Utils Ts"
Cohesion: 0.09
Nodes (27): AnsiCodeTracker, applyBackgroundToLine(), breakLongWord(), cleanStepText(), couldBeEmoji(), extractAnsiCode(), extractDoneSteps(), extractSegments() (+19 more)

### Community 33 - "RpcClient"
Cohesion: 0.1
Nodes (1): RpcClient

### Community 34 - "streamGoogleVertex (Google Vertex Stream Fn)"
Cohesion: 0.06
Nodes (44): addCustomHeadersMiddleware (SigV4-safe), buildAdditionalModelRequestFields (thinking config), convertMessages (Bedrock), formatBedrockError, streamBedrock (Converse), streamSimpleBedrock, supportsPromptCaching (Bedrock), resolveAzureConfig (+36 more)

### Community 35 - "ExtensionRunner"
Cohesion: 0.08
Nodes (3): buildBuiltinKeybindings(), emitSessionShutdownEvent(), ExtensionRunner

### Community 36 - "Overlay Options Test Ts"
Cohesion: 0.05
Nodes (10): Non-capturing overlay focus management, EmptyContent, FocusableOverlay, StaticOverlay, EmptyContent, HyperlinkContent, StaticOverlay, StyledContent (+2 more)

### Community 37 - "README Extension Examples Catalog"
Cohesion: 0.06
Nodes (41): Auto-Commit on Exit Extension, BorderStatusEditor (CustomEditor), fitBorder (border text fitter), formatContext (context-window usage), convertMessages (pi-ai to Anthropic SDK), Custom Anthropic Provider Extension, loginAnthropic (OAuth PKCE), streamCustomAnthropic (custom streaming) (+33 more)

### Community 38 - "DefaultResourceLoader"
Cohesion: 0.1
Nodes (4): DefaultResourceLoader, loadContextFileFromDir(), loadProjectContextFiles(), resolvePromptInput()

### Community 39 - "TUI Class (Differential Renderer)"
Cohesion: 0.07
Nodes (39): IME Cursor Positioning (CJK), Synchronized Output (CSI 2026), Test: Pending Tool Call Render (#4167), Test: LoginDialog OAuth Prompt Stability (#5433), fd-based Fuzzy File Search, CombinedAutocompleteProvider, pi-tui CHANGELOG, darwin-modifiers.c (CGEventFlags) (+31 more)

### Community 40 - "AuthStorage"
Cohesion: 0.09
Nodes (3): AuthStorage, FileAuthStorageBackend, InMemoryAuthStorageBackend

### Community 41 - "Empty Test Ts"
Cohesion: 0.07
Nodes (32): Anthropic Long Cache Retention E2E Test, Anthropic Raw SSE Parsing Test, Anthropic Thinking Disable Test, Anthropic-style cache_control ephemeral markers, Anthropic thinking.type=disabled payload control, Azure OpenAI Base URL Normalization Test, Azure base URL normalization to /openai/v1, Azure credentials helper (test/azure-utils.ts) (+24 more)

### Community 42 - "streamAnthropic"
Cohesion: 0.08
Nodes (36): loadAuth(), login(), main(), prompt(), saveAuth(), Provider Compat Auto-Detection, GitHub Copilot Dynamic Header Convention, Cross-Provider Reasoning Effort Mapping (+28 more)

### Community 43 - "Editor Test Ts"
Cohesion: 0.06
Nodes (4): Grapheme/wide-char aware text wrapping, Kill Ring (yank/Ctrl+Y/Alt+Y) behavior, Undo coalescing / atomic paste units, MarkdownWithInput

### Community 44 - "Agent"
Cohesion: 0.09
Nodes (3): Agent, createMutableAgentState(), PendingMessageQueue

### Community 45 - "Tic Tac Toe Ts"
Cohesion: 0.09
Nodes (21): BannerMessageComponent, boardToAscii(), borderFgCode(), buildCellContent(), cellFgCode(), centerPad(), checkWin(), createInitialState() (+13 more)

### Community 46 - "ProcessTerminal"
Cohesion: 0.12
Nodes (5): isAppleTerminalSession(), isKeyboardProtocolNegotiationSequencePrefix(), normalizeAppleTerminalInput(), parseKeyboardProtocolNegotiationSequence(), ProcessTerminal

### Community 47 - "Pi Agent Harness Mono Repo"
Cohesion: 0.07
Nodes (35): packages/agent CHANGELOG, Pi AGENTS.md Development Rules, Pi multi-session git concurrency rules, Pi Lockstep versioning release policy, Erasable/strip-only TypeScript syntax rule, AssistantMessageStream transport decoupling, AsyncLocalStorage adapter, AgentHarnessPhase (idle/turn/compaction/...) (+27 more)

### Community 48 - "createAgentSession API"
Cohesion: 0.09
Nodes (33): AuthStorage, DefaultResourceLoader, ExtensionAPI, ModelRegistry, SettingsManager, createAgentSession API, createAgentSessionRuntime API, migrateAuthToAuthJson (+25 more)

### Community 49 - "Pi ExtensionAPI (hook + Registration"
Cohesion: 0.08
Nodes (34): Reviewer Agent Definition, Worker Agent Definition, Subagent Discovery (frontmatter parser), pi ExtensionAPI (hook + registration surface), Provider backend delegation pattern (Anthropic/OpenAI stream reuse), Tool isolation pattern (VM/sandbox/subprocess), DOOM Half-Block Overlay Component, DOOM WASM Engine Wrapper (+26 more)

### Community 50 - "ModelRegistry"
Cohesion: 0.1
Nodes (4): applyModelOverride(), emptyCustomModelsResult(), mergeCompat(), ModelRegistry

### Community 51 - "Anthropic Ts"
Cohesion: 0.11
Nodes (27): buildParams(), consumeLine(), convertContentBlocks(), convertMessages(), convertTools(), createClient(), decodeSseLine(), exchangeAuthorizationCode() (+19 more)

### Community 52 - "loginAnthropic (auth Code + PKCE)"
Cohesion: 0.08
Nodes (31): anthropicOAuthProvider (Claude Pro/Max), loginAnthropic (auth code + PKCE), refreshAnthropicToken, startCallbackServer (local HTTP), captureAnthropicRequest (eager tool input test), resolveAzureDeploymentName / hasAzureOpenAICredentials, OAuth local callback HTTP server, PKCE (Proof Key for Code Exchange) (+23 more)

### Community 53 - "InputDialog"
Cohesion: 0.08
Nodes (6): InputDialog, LoadingIndicator, main(), OutputLog, PromptInput, SelectDialog

### Community 54 - "Editor Component"
Cohesion: 0.09
Nodes (29): CancellableLoader, chat-simple demo, Editor component, Editor autocomplete pipeline (debounce/token/abort), Large paste marker compression, Editor kill ring (Emacs yank/yank-pop), Paste marker atomic segmentation, segmentWithMarkers (paste-marker aware) (+21 more)

### Community 55 - "ResourceList"
Cohesion: 0.1
Nodes (6): buildGroups(), ConfigSelectorComponent, ConfigSelectorHeader, formatBaseDir(), getGroupLabel(), ResourceList

### Community 56 - "DefaultResourceLoader (56)"
Cohesion: 0.09
Nodes (29): AgentSession.getSessionStats, AuthStorage, ModelRegistry, compareVersions, normalizeChangelogLinks, parseChangelog, serializeConversation (compaction serializer), Force-push history recovery rationale (+21 more)

### Community 57 - "VirtualTerminal"
Cohesion: 0.1
Nodes (1): VirtualTerminal

### Community 58 - "Keys Ts"
Cohesion: 0.16
Nodes (22): decodeKittyPrintable(), decodeModifyOtherKeysPrintable(), decodePrintableKey(), formatKeyNameWithModifiers(), formatParsedKey(), isDigitKey(), isWindowsTerminalSession(), matchesKey() (+14 more)

### Community 59 - "FooterDataProvider"
Cohesion: 0.13
Nodes (7): findGitPaths(), FooterDataProvider, isWindowsMountedRepoPath(), isWslEnvironment(), resolveBranchWithGitAsync(), resolveBranchWithGitSync(), shouldPollGitHead()

### Community 60 - "Openai Completions Ts"
Cohesion: 0.13
Nodes (17): addCacheControlToInstructionMessage(), addCacheControlToLastConversationMessage(), addCacheControlToLastTool(), addCacheControlToMessage(), addCacheControlToSystemPrompt(), addCacheControlToTextContent(), applyAnthropicCacheControl(), buildParams() (+9 more)

### Community 61 - "Session"
Cohesion: 0.17
Nodes (2): buildSessionContext(), Session

### Community 62 - "Edit Diff Ts"
Cohesion: 0.15
Nodes (17): parseDiffLine(), renderDiff(), renderIntraLineDiff(), replaceTabs(), applyEditsToNormalizedContent(), computeEditDiff(), computeEditsDiff(), countOccurrences() (+9 more)

### Community 63 - "AgentSessionRuntime"
Cohesion: 0.15
Nodes (3): AgentSessionRuntime, extractUserMessageText(), SessionImportFileNotFoundError

### Community 64 - "KeybindingsManager"
Cohesion: 0.13
Nodes (8): isLegacyKeybindingName(), isRecord(), KeybindingsManager, loadRawConfig(), migrateKeybindingsConfig(), normalizeKeys(), orderKeybindingsConfig(), toKeybindingsConfig()

### Community 65 - "Terminal Image Ts"
Cohesion: 0.12
Nodes (13): calculateImageCellSize(), calculateImageRows(), detectCapabilities(), encodeITerm2(), encodeKitty(), getCapabilities(), getCellDimensions(), getGifDimensions() (+5 more)

### Community 66 - "ToolExecutionComponent"
Cohesion: 0.18
Nodes (1): ToolExecutionComponent

### Community 67 - "Pi Ctx Ui API (setHeader"
Cohesion: 0.12
Nodes (22): Entry Bookmark Extension, Commands Listing Extension, Custom Compaction (Gemini) Extension, Custom Header / Pi Mascot Extension, Dirty Repo Guard Extension, Hidden Thinking Label Extension, Mac System Theme Sync Extension, Model Status Bar Extension (+14 more)

### Community 68 - "Faux Ts"
Cohesion: 0.16
Nodes (18): assistantContentToText(), commonPrefixLength(), contentToText(), createAbortedMessage(), estimateTokens(), fauxAssistantMessage(), fauxText(), fauxToolCall() (+10 more)

### Community 69 - "Register Builtins Ts"
Cohesion: 0.11
Nodes (7): createLazyLoadErrorImages(), generateImagesOpenRouter(), importNodeOnlyProvider(), loadBedrockProviderModule(), loadOpenRouterImagesProviderModule(), registerBuiltInApiProviders(), resetApiProviders()

### Community 70 - "Interactive Mode Status Test Ts"
Cohesion: 0.1
Nodes (6): createExtensionFixtures(), createSourceInfo(), normalizeRenderedOutput(), renderAll(), renderLastLine(), TestFocusableComponent

### Community 71 - "Resolve Config Value Ts"
Cohesion: 0.19
Nodes (19): appendLiteral(), executeCommand(), executeCommandUncached(), executeWithDefaultShell(), getConfigValueEnvVarName(), getConfigValueEnvVarNames(), getMissingConfigValueEnvVarNames(), getTemplateEnvVarNames() (+11 more)

### Community 72 - "Generate Models Ts"
Cohesion: 0.19
Nodes (21): applyThinkingLevelMetadata(), fetchAiGatewayModels(), fetchNvidiaNimModelIds(), fetchOpenRouterModels(), generateModels(), getAnthropicMessagesCompat(), getBedrockBaseUrl(), getTogetherCompat() (+13 more)

### Community 73 - "ArminComponent"
Cohesion: 0.16
Nodes (4): ArminComponent, buildFinalGrid(), getChar(), getPixel()

### Community 74 - "Input"
Cohesion: 0.21
Nodes (1): Input

### Community 75 - "Mistral Ts"
Cohesion: 0.16
Nodes (16): buildChatPayload(), buildToolResultText(), consumeChatStream(), deriveMistralToolCallId(), formatMistralError(), mapChatStopReason(), mapReasoningEffort(), mapToolChoice() (+8 more)

### Community 76 - "Skills Ts"
Cohesion: 0.2
Nodes (19): addIgnoreRules(), basenameEnvPath(), createSkillSourceInfo(), dirnameEnvPath(), escapeXml(), formatSkillInvocation(), formatSkillsForPrompt(), joinEnvPath() (+11 more)

### Community 77 - "Agent Loop Ts"
Cohesion: 0.24
Nodes (19): agentLoop(), agentLoopContinue(), createAgentStream(), createErrorToolResult(), createToolResultMessage(), emitToolExecutionEnd(), emitToolResultMessage(), executePreparedToolCall() (+11 more)

### Community 78 - "Ts (78)"
Cohesion: 0.19
Nodes (18): collectSettingsDiagnostics(), createSessionManager(), findLocalSessionByExactId(), forkSessionOrExit(), isPlainRuntimeMetadataCommand(), isTruthyEnvFlag(), main(), prepareInitialMessage() (+10 more)

### Community 79 - "Markdown"
Cohesion: 0.17
Nodes (2): Markdown, StrictStrikethroughTokenizer

### Community 80 - "Manager Cli Ts"
Cohesion: 0.22
Nodes (18): createCommandSettingsManager(), getCommandAppMode(), getPackageCommandUsage(), getSelfUpdatePlan(), handleConfigCommand(), handlePackageCommand(), parsePackageCommand(), parseProjectTrustOverride() (+10 more)

### Community 81 - "Openai Codex Ts"
Cohesion: 0.21
Nodes (17): createAuthorizationFlow(), createState(), credentialsFromToken(), decodeJwt(), exchangeAuthorizationCode(), exchangeAuthorizationCodeForCredentials(), fetchWithLoginCancellation(), getAccountId() (+9 more)

### Community 82 - "Google Vertex Ts"
Cohesion: 0.19
Nodes (16): baseUrlIncludesApiVersion(), buildGoogleAuthOptions(), buildHttpOptions(), buildParams(), createClient(), createClientWithApiKey(), getDisabledThinkingConfig(), getGemini3ThinkingLevel() (+8 more)

### Community 83 - "FakeTerminal"
Cohesion: 0.12
Nodes (3): FakeTerminal, waitForRender(), waitForRenderedText()

### Community 84 - "Validation Ts"
Cohesion: 0.27
Nodes (15): applySchemaArrayCoercion(), applySchemaObjectCoercion(), coercePrimitiveByType(), coerceWithJsonSchema(), coerceWithUnionSchema(), getSchemaTypes(), getSubSchemaValidator(), getValidator() (+7 more)

### Community 85 - "ScopedModelsSelectorComponent"
Cohesion: 0.24
Nodes (7): clearAll(), enableAll(), getSortedIds(), isEnabled(), move(), ScopedModelsSelectorComponent, toggle()

### Community 86 - "SelectList"
Cohesion: 0.18
Nodes (3): clamp(), normalizeToSingleLine(), SelectList

### Community 87 - "SpaceInvadersComponent"
Cohesion: 0.22
Nodes (4): createAliens(), createInitialState(), createShields(), SpaceInvadersComponent

### Community 88 - "Trust Manager Ts"
Cohesion: 0.2
Nodes (7): acquireTrustLockSync(), findNearestTrustEntry(), getProjectTrustOptions(), getProjectTrustParentPath(), normalizeCwd(), ProjectTrustStore, withTrustFileLock()

### Community 89 - "Stdin Buffer Ts"
Cohesion: 0.2
Nodes (8): extractCompleteSequences(), isCompleteApcSequence(), isCompleteCsiSequence(), isCompleteDcsSequence(), isCompleteOscSequence(), isCompleteSequence(), parseUnmodifiedKittyPrintableCodepoint(), StdinBuffer

### Community 90 - "OutputAccumulator"
Cohesion: 0.25
Nodes (3): byteLength(), defaultTempFilePath(), OutputAccumulator

### Community 91 - "Sdk Codex Cache Probe Tool"
Cohesion: 0.27
Nodes (13): average(), buildPrompt(), createMinimalResourceLoader(), deterministicProbeTool(), diffWebSocketStats(), estimateTokens(), formatWebSocketStats(), getAssistantText() (+5 more)

### Community 92 - "Ctx Ui Custom Component Factory"
Cohesion: 0.19
Nodes (14): pi.appendEntry Session Persistence, before_agent_start System Prompt Injection, ctx.ui.custom Component Factory, presets.json Config (global+project merge), sessionManager.getBranch Conversation History, Custom Footer Extension, Modal Editor Extension, Overlay Test Extension (+6 more)

### Community 93 - "ModelSelectorComponent"
Cohesion: 0.27
Nodes (1): ModelSelectorComponent

### Community 94 - "Tool Execution Component Parity Test"
Cohesion: 0.15
Nodes (14): Assistant Message Component, Tool Execution Component, Windows Child-Process Close Handling Test, Bash Tool Definition, Execute Bash With Operations, Init Theme, Read Tool Definition, Streaming Render Debug Script (+6 more)

### Community 95 - "Google Shared Ts"
Cohesion: 0.2
Nodes (6): convertMessages(), getGeminiMajorVersion(), isValidThoughtSignature(), requiresToolCallId(), resolveThoughtSignature(), supportsMultimodalFunctionResponse()

### Community 96 - "Border Status Editor Ts"
Cohesion: 0.21
Nodes (6): BorderStatusEditor, EmptyFooter, fitBorder(), formatContext(), formatCwd(), formatThinking()

### Community 97 - "Edit Ts"
Cohesion: 0.21
Nodes (7): buildEditCallComponent(), createEditCallRenderComponent(), createEditTool(), createEditToolDefinition(), formatEditCall(), getEditCallRenderComponent(), getEditHeaderBg()

### Community 98 - "Tool Stats Ts Token Usage"
Cohesion: 0.23
Nodes (13): browser-safe smoke test entry, usage.cost breakdown (input/output/cacheRead/cacheWrite), encoded session dir convention (--cwd-with-dashes--), Pi agent session .jsonl files (~/.pi/agent/sessions), encodeSessionDir cwd-to-folder encoder, cost.ts session cost aggregator, runSubagent pi child-process driver, session-transcripts.ts transcript extractor + subagent analyzer (+5 more)

### Community 99 - "Github Copilot Ts"
Cohesion: 0.31
Nodes (11): enableAllGitHubCopilotModels(), enableGitHubCopilotModel(), fetchJson(), getBaseUrlFromToken(), getGitHubCopilotBaseUrl(), getUrls(), loginGitHubCopilot(), normalizeDomain() (+3 more)

### Community 100 - "Cache Retention Test Ts"
Cohesion: 0.17
Nodes (9): PayloadCaptured, fc_<shortHash> foreign ID normalization, OpenAI Completions SDK Retry Control, maxRetries default 0, src/providers/anthropic.ts, src/utils/hash.ts shortHash, src/providers/openai-completions.ts, src/providers/openai-responses.ts (+1 more)

### Community 101 - "Changelog Ts"
Cohesion: 0.26
Nodes (8): entryVersion(), isDirectoryTarget(), normalizeChangelogLinks(), normalizeChangelogLinkTarget(), normalizePathPart(), normalizeTag(), resolveRepositoryPath(), splitLocalTarget()

### Community 102 - "SnakeComponent"
Cohesion: 0.29
Nodes (3): createInitialState(), SnakeComponent, spawnFood()

### Community 103 - "Prompt Templates Ts"
Cohesion: 0.33
Nodes (11): basenameEnvPath(), expandPromptTemplate(), formatPromptTemplateInvocation(), loadPromptTemplates(), loadSourcedPromptTemplates(), loadTemplateFromFile(), loadTemplatesFromDir(), parseCommandArgs() (+3 more)

### Community 104 - "Tool Stats Ts"
Cohesion: 0.17
Nodes (0): 

### Community 105 - "getEnvApiKey"
Cohesion: 0.2
Nodes (12): getApiProvider, bedrockProviderModule, Bedrock Ambient Auth Sources, findEnvKeys, getEnvApiKey, hasVertexAdcCredentials, Vertex ADC Auth Path, index.ts Barrel Export (+4 more)

### Community 106 - "Test Theme Colors Ts"
Cohesion: 0.38
Nodes (10): adjustColorToContrast(), cmdContrast(), cmdTest(), fgAnsi(), getContrast(), getLuminance(), hexToRgb(), hslToRgb() (+2 more)

### Community 107 - "SettingsList"
Cohesion: 0.23
Nodes (1): SettingsList

### Community 108 - "MockWebSocket"
Cohesion: 0.2
Nodes (3): buildSSEPayload(), MockWebSocket, start()

### Community 109 - "Read Ts"
Cohesion: 0.26
Nodes (10): createReadTool(), createReadToolDefinition(), formatCompactReadCall(), formatReadCall(), formatReadLineRange(), formatReadResult(), getCompactReadClassification(), getPiDocsClassification() (+2 more)

### Community 110 - "Write Ts"
Cohesion: 0.26
Nodes (9): createWriteTool(), createWriteToolDefinition(), formatWriteCall(), highlightSingleLine(), rebuildWriteHighlightCacheFull(), refreshWriteHighlightPrefix(), trimTrailingEmptyLines(), updateWriteHighlightCacheIncremental() (+1 more)

### Community 111 - "Box"
Cohesion: 0.26
Nodes (1): Box

### Community 112 - "Azure Openai Responses Ts"
Cohesion: 0.27
Nodes (8): buildDefaultBaseUrl(), createClient(), normalizeAzureBaseUrl(), parseDeploymentNameMap(), resolveAzureConfig(), resolveDeploymentName(), streamAzureOpenAIResponses(), streamSimpleAzureOpenAIResponses()

### Community 113 - "FooterComponent"
Cohesion: 0.22
Nodes (3): FooterComponent, formatCwdForFooter(), formatTokens()

### Community 114 - "DaxnutsComponent"
Cohesion: 0.29
Nodes (4): buildImage(), DaxnutsComponent, parseImage(), rgb()

### Community 115 - "Openai Responses Ts"
Cohesion: 0.29
Nodes (9): applyServiceTierPricing(), buildParams(), createClient(), getCompat(), getPromptCacheRetention(), getServiceTierCostMultiplier(), resolveCacheRetention(), streamOpenAIResponses() (+1 more)

### Community 116 - "DoomEngine"
Cohesion: 0.2
Nodes (1): DoomEngine

### Community 117 - "Codex Websocket Cached Probe Ts"
Cohesion: 0.35
Nodes (10): average(), buildPrompt(), deterministicProbeTool(), executeTool(), main(), parseArgs(), percentile(), printHelp() (+2 more)

### Community 118 - "Doomgeneric Pi C"
Cohesion: 0.18
Nodes (0): 

### Community 119 - "Google Ts"
Cohesion: 0.4
Nodes (9): buildParams(), getDisabledThinkingConfig(), getGoogleBudget(), getThinkingLevel(), isGemini3FlashModel(), isGemini3ProModel(), isGemma4Model(), streamGoogle() (+1 more)

### Community 120 - "TodoListComponent"
Cohesion: 0.2
Nodes (1): TodoListComponent

### Community 121 - "EventStream"
Cohesion: 0.2
Nodes (2): AssistantMessageEventStream, EventStream

### Community 122 - "BashExecutionComponent"
Cohesion: 0.29
Nodes (1): BashExecutionComponent

### Community 123 - "Model Resolver Ts"
Cohesion: 0.33
Nodes (7): buildFallbackModel(), findExactModelReferenceMatch(), findInitialModel(), parseModelPattern(), resolveCliModel(), resolveModelScope(), tryMatchModel()

### Community 124 - "Path Utils Ts"
Cohesion: 0.42
Nodes (8): fileExists(), pathExists(), resolveReadPath(), resolveReadPathAsync(), resolveToCwd(), tryCurlyQuoteVariant(), tryMacOSScreenshotPath(), tryNFDVariant()

### Community 125 - "SettingsSelectorComponent"
Cohesion: 0.22
Nodes (3): SelectSubmenu, SettingsSelectorComponent, WarningSettingsSubmenu

### Community 126 - "detectSupportedImageMimeType"
Cohesion: 0.22
Nodes (10): applyExifOrientation, findJpegTiffOffset, findWebpTiffOffset, getExifOrientation, readOrientationFromTiff, rotate90, detectSupportedImageMimeType, detectSupportedImageMimeTypeFromFile (+2 more)

### Community 127 - "Stats Ts"
Cohesion: 0.27
Nodes (5): createDayStats(), createTotals(), formatCost(), formatInt(), printTotals()

### Community 128 - "resizeImageInProcess (Photon WASM)"
Cohesion: 0.27
Nodes (10): readClipboardImage, Anthropic 5MB Image Size Limit, Bun Compiled Executable Layout, EXIF Orientation Handling, Photon Rust/WASM Image Library, convertToPng, resizeImageInProcess (Photon WASM), resizeImage (worker-based) (+2 more)

### Community 129 - "DoomOverlayComponent"
Cohesion: 0.31
Nodes (2): DoomOverlayComponent, renderHalfBlock()

### Community 130 - "UserMessageList"
Cohesion: 0.22
Nodes (2): UserMessageList, UserMessageSelectorComponent

### Community 131 - "Config Test Ts"
Cohesion: 0.42
Nodes (8): createBunGlobalInstall(), createFakeBunScript(), createFakePnpmScript(), createFakeYarnScript(), createNpmPrefixInstall(), createPnpmGlobalInstall(), createYarnGlobalInstall(), setExecPath()

### Community 132 - "RPC Demo Dangerous Bash Select"
Cohesion: 0.31
Nodes (9): Dangerous Command Regex Detection, tool_call Lifecycle Event, Confirm Destructive Actions Extension, Dynamic Tools Extension, Permission Gate Extension, Protected Paths Extension, RPC Demo Dangerous Bash Select, RPC UI Demo Extension (+1 more)

### Community 133 - "Ansi To Html Ts"
Cohesion: 0.39
Nodes (7): ansiToHtml(), applySgrCode(), color256ToHex(), createEmptyStyle(), escapeHtml(), hasStyle(), styleToInlineCSS()

### Community 134 - "Render Utils Ts"
Cohesion: 0.31
Nodes (4): invalidArgText(), linkPath(), renderToolPath(), shortenPath()

### Community 135 - "Openai Codex Oauth Test Ts"
Cohesion: 0.28
Nodes (5): OAuth device code flow (polling), utils/oauth/device-code.ts (pollOAuthDeviceCodeFlow), utils/oauth/openai-codex.ts (loginOpenAICodexDeviceCode), deviceAuthPendingResponse(), jsonResponse()

### Community 136 - "RainbowEditor"
Cohesion: 0.31
Nodes (1): RainbowEditor

### Community 137 - "Output Guard Ts"
Cohesion: 0.28
Nodes (3): flushRawStdout(), waitForRawStdoutBackpressure(), writeRawStdoutChunk()

### Community 138 - "Provider Attribution Ts"
Cohesion: 0.5
Nodes (8): getDefaultAttributionHeaders(), getSessionHeaders(), isCloudflareModel(), isNvidiaNimModel(), isOpenRouterModel(), isVercelGatewayModel(), matchesHost(), mergeProviderAttributionHeaders()

### Community 139 - "Agent Loop Test Ts"
Cohesion: 0.25
Nodes (3): createAssistantMessage(), createUsage(), MockAssistantStream

### Community 140 - "Truncate Ts"
Cohesion: 0.39
Nodes (6): replaceUnpairedSurrogates(), splitLinesForCounting(), truncateHead(), truncateStringToBytesFromEnd(), truncateTail(), utf8ByteLength()

### Community 141 - "resolvePath"
Cohesion: 0.25
Nodes (8): spawnProcess (cross-spawn), watchWithErrorHandler, openBrowser, getCwdRelativePath, resolvePath, Rationale: avoid cmd.exe shell injection, getShellConfig, quarantineWindowsNativeDependencies

### Community 142 - "Models Ts"
Cohesion: 0.29
Nodes (2): clampThinkingLevel(), getSupportedThinkingLevels()

### Community 143 - "Exif Orientation Ts"
Cohesion: 0.5
Nodes (7): applyExifOrientation(), findJpegTiffOffset(), findWebpTiffOffset(), getExifOrientation(), hasExifHeader(), readOrientationFromTiff(), rotate90()

### Community 144 - "SimpleContent"
Cohesion: 0.25
Nodes (2): SimpleContent, SimpleOverlay

### Community 145 - "AssistantMessageComponent"
Cohesion: 0.39
Nodes (1): AssistantMessageComponent

### Community 146 - "Implement Workflow Prompt"
Cohesion: 0.39
Nodes (8): Implement-and-Review Workflow Prompt, Implement Workflow Prompt, Planner Agent, Reviewer Agent, Scout Agent, Scout-and-Plan Workflow Prompt, Subagent Chaining Pattern, Worker Agent

### Community 147 - "Truncate Test Ts"
Cohesion: 0.43
Nodes (6): assertMatchesBufferTail(), bufferTail(), byteLength(), checkExhaustive(), sampledByteLimits(), truncateHead / truncateTail (harness utils)

### Community 148 - "Startup Ui Ts"
Cohesion: 0.29
Nodes (2): isOfficialDistribution(), shouldRunFirstTimeSetup()

### Community 149 - "parseGitUrl"
Cohesion: 0.32
Nodes (8): DefaultPackageManager (core), GitSource Type, buildGitSource, hasUnsafeGitInstallPart, parseGenericGitUrl, parseGitUrl, splitRef, Package Manager git source parsing test

### Community 150 - "Paths Ts"
Cohesion: 0.39
Nodes (4): formatPathRelativeToCwdOrAbsolute(), getCwdRelativePath(), normalizePath(), resolvePath()

### Community 151 - "Keybinding Hints Ts"
Cohesion: 0.43
Nodes (6): formatKeys(), formatKeyText(), keyDisplayText(), keyHint(), keyText(), rawKeyHint()

### Community 152 - "OAuthSelectorComponent"
Cohesion: 0.43
Nodes (1): OAuthSelectorComponent

### Community 153 - "Git Merge And Resolve Extension"
Cohesion: 0.29
Nodes (0): 

### Community 154 - "Anthropic Thinking Disable Test Ts"
Cohesion: 0.32
Nodes (5): capturePayload(), makeE2EContext(), makePayloadCaptureContext(), PayloadCaptured, runWithoutReasoning()

### Community 155 - "Github Issue Autocomplete Ts"
Cohesion: 0.29
Nodes (2): parseGitHubRepo(), resolveGitHubRepo()

### Community 156 - "SessionSelectorComponent (path Delete Interactions)"
Cohesion: 0.29
Nodes (8): stripAnsi (ANSI escape stripper), runMigrations (keybindings rewrite), SessionSelectorComponent (path/delete interactions), KeybindingsManager, SessionSelectorComponent, getThemeExportColors, getAvailableThemes, setRegisteredThemes

### Community 157 - "KeyLogger"
Cohesion: 0.32
Nodes (1): KeyLogger

### Community 158 - "Session Selector Search Ts"
Cohesion: 0.43
Nodes (7): filterAndSortSessions(), getSessionSearchText(), hasSessionName(), matchesNameFilter(), matchSession(), normalizeWhitespaceLower(), parseSearchQuery()

### Community 159 - "Mime Ts"
Cohesion: 0.57
Nodes (7): detectSupportedImageMimeType(), detectSupportedImageMimeTypeFromFile(), isAnimatedPng(), isPng(), readUint32BE(), startsWith(), startsWithAscii()

### Community 160 - "5080 Signal Shutdown Extension Cleanup"
Cohesion: 0.25
Nodes (1): ProcessExitError

### Community 161 - "Syntax Highlight Ts"
Cohesion: 0.39
Nodes (6): getActiveFormatter(), getScopeFormatter(), getScopeFromSpanTag(), highlight(), isSpanOpenTagStart(), renderHighlightedHtml()

### Community 162 - "Ssh Ts"
Cohesion: 0.5
Nodes (6): createRemoteBashOps(), createRemoteEditOps(), createRemoteReadOps(), createRemoteWriteOps(), execute(), getSsh()

### Community 163 - "Api Registry Ts"
Cohesion: 0.32
Nodes (3): registerApiProvider(), wrapStream(), wrapStreamSimple()

### Community 164 - "Bedrock Convert Messages Test Ts"
Cohesion: 0.25
Nodes (3): BedrockRuntimeClient, BedrockRuntimeServiceException, ConverseStreamCommand

### Community 165 - "Manager Test Ts"
Cohesion: 0.36
Nodes (5): isDisabled(), isEnabled(), MockSpawnedProcess, normalizeForMatch(), pathEndsWith()

### Community 166 - "Session Cwd Ts"
Cohesion: 0.38
Nodes (4): assertSessionCwdExists(), formatMissingSessionCwdError(), getMissingSessionCwdIssue(), MissingSessionCwdError

### Community 167 - "BorderedLoader"
Cohesion: 0.29
Nodes (1): BorderedLoader

### Community 168 - "Git Ts"
Cohesion: 0.62
Nodes (6): buildGitSource(), decodeForValidation(), hasUnsafeGitInstallPart(), parseGenericGitUrl(), parseGitUrl(), splitRef()

### Community 169 - "FirstTimeSetupComponent"
Cohesion: 0.52
Nodes (1): FirstTimeSetupComponent

### Community 170 - "Openai Responses Tool Result Images"
Cohesion: 0.57
Nodes (6): isFunctionCallOutputItem(), isInputImageItem(), isInputTextItem(), isRecord(), isResponsePayload(), verifyToolResultImagesStayInFunctionCallOutput()

### Community 171 - "OverlayTestComponent"
Cohesion: 0.29
Nodes (1): OverlayTestComponent

### Community 172 - "Minimal Mode Ts"
Cohesion: 0.43
Nodes (5): createBuiltInTools(), execute(), getBuiltInTools(), renderCall(), shortenPath()

### Community 173 - "Anthropic Eager Tool Input Compat"
Cohesion: 0.33
Nodes (2): captureAnthropicRequest(), createModel()

### Community 174 - "Before Agent Start System Prompt"
Cohesion: 0.38
Nodes (7): before_agent_start system-prompt hook, Built-in Tool Renderer Extension, Claude Rules System-Prompt Extension, Minimal Mode Tool Rendering Extension, pi createXTool factory functions, Pirate System-Prompt Mode Extension, SSH Remote Execution Extension

### Community 175 - "Image Resize Ts"
Cohesion: 0.43
Nodes (4): createResizeWorker(), resizeImage(), resizeImageInWorker(), toTransferableBytes()

### Community 176 - "Text"
Cohesion: 0.29
Nodes (1): Text

### Community 177 - "Tree Selector Test Ts"
Cohesion: 0.43
Nodes (4): assistantMessage(), buildBranchingTree(), buildTree(), userMessage()

### Community 178 - "Openai Responses Shared Ts"
Cohesion: 0.43
Nodes (5): convertResponsesMessages(), encodeTextSignatureV1(), mapStopReason(), parseTextSignature(), processResponsesStream()

### Community 179 - "Cross Provider Handoff Test Ts"
Cohesion: 0.38
Nodes (3): dumpFailurePayload(), generateContext(), getHeaders()

### Community 180 - "Anthropic Eager Tool Input E2e"
Cohesion: 0.29
Nodes (0): 

### Community 181 - "TrustSelectorComponent"
Cohesion: 0.48
Nodes (2): formatDecision(), TrustSelectorComponent

### Community 182 - "Anthropic Long Cache Retention E2e"
Cohesion: 0.29
Nodes (0): 

### Community 183 - "Git Update Test Ts"
Cohesion: 0.57
Nodes (5): createCommit(), getCurrentCommit(), git(), initGitRepo(), setupRemoteAndInstall()

### Community 184 - "ExtensionInputComponent"
Cohesion: 0.33
Nodes (1): ExtensionInputComponent

### Community 185 - "Session Selector Path Delete Test"
Cohesion: 0.33
Nodes (0): 

### Community 186 - "Env Api Keys Ts"
Cohesion: 0.53
Nodes (4): findEnvKeys(), getApiKeyEnvVars(), getEnvApiKey(), hasVertexAdcCredentials()

### Community 187 - "Project Trust Ts"
Cohesion: 0.53
Nodes (4): formatProjectTrustPrompt(), resolveProjectTrusted(), saveProjectTrustPromptResult(), selectProjectTrustOption()

### Community 188 - "Context Test Ts"
Cohesion: 0.33
Nodes (0): 

### Community 189 - "Notify Ts"
Cohesion: 0.6
Nodes (5): notify(), notifyOSC777(), notifyOSC99(), notifyWindows(), windowsToastScript()

### Community 190 - "VirtualTerminal (xterm Test Harness)"
Cohesion: 0.33
Nodes (4): Overlay CJK boundary regression test, KeyLogger (key-tester), Overlay short-content overlay test, VirtualTerminal (xterm test harness)

### Community 191 - "KillRing"
Cohesion: 0.33
Nodes (1): KillRing

### Community 192 - "ExtensionSelectorComponent"
Cohesion: 0.47
Nodes (1): ExtensionSelectorComponent

### Community 193 - "ExtensionEditorComponent"
Cohesion: 0.4
Nodes (1): ExtensionEditorComponent

### Community 194 - "Bash Close Hang Windows Test"
Cohesion: 0.4
Nodes (2): createInheritedStdioCommand(), toBashSingleQuotedArg()

### Community 195 - "SkillInvocationMessageComponent"
Cohesion: 0.53
Nodes (1): SkillInvocationMessageComponent

### Community 196 - "Version Check Ts"
Cohesion: 0.6
Nodes (5): checkForNewPiVersion(), comparePackageVersions(), getLatestPiRelease(), getLatestPiVersion(), isNewerPackageVersion()

### Community 197 - "Proxy Ts"
Cohesion: 0.33
Nodes (1): ProxyMessageEventStream

### Community 198 - "Node Http Proxy Ts"
Cohesion: 0.67
Nodes (5): getProxyEnv(), getProxyForUrl(), parseProxyTargetUrl(), resolveHttpProxyUrlForTarget(), shouldProxyHostname()

### Community 199 - "Repo Utils Ts"
Cohesion: 0.33
Nodes (0): 

### Community 200 - "CancellableLoader"
Cohesion: 0.33
Nodes (1): CancellableLoader

### Community 201 - "Messages Ts"
Cohesion: 0.33
Nodes (0): 

### Community 202 - "Spacer"
Cohesion: 0.33
Nodes (1): Spacer

### Community 203 - "4167 Thinking Toggle Pending Tool"
Cohesion: 0.33
Nodes (0): 

### Community 204 - "Image"
Cohesion: 0.33
Nodes (1): Image

### Community 205 - "Windows Self Update Ts"
Cohesion: 0.67
Nodes (5): cleanupWindowsSelfUpdateQuarantine(), getLoadedSharedObjectsInPackageDir(), getQuarantineRoot(), normalizePath(), quarantineWindowsNativeDependencies()

### Community 206 - "Startup Session Name Test Ts"
Cohesion: 0.47
Nodes (3): createSessionFile(), createTempDir(), setup()

### Community 207 - "Anthropic Force Adaptive Thinking Test"
Cohesion: 0.4
Nodes (3): capturePayload(), makeContext(), PayloadCaptured

### Community 208 - "Summarize Ts"
Cohesion: 0.47
Nodes (3): buildConversationText(), extractTextParts(), extractToolCallLines()

### Community 209 - "UndoStack"
Cohesion: 0.33
Nodes (1): UndoStack

### Community 210 - "CustomMessageComponent"
Cohesion: 0.53
Nodes (1): CustomMessageComponent

### Community 211 - "Json Parse Ts"
Cohesion: 0.67
Nodes (5): escapeControlCharacter(), isControlCharacter(), parseJsonWithRepair(), parseStreamingJson(), repairJson()

### Community 212 - "Images Test Ts"
Cohesion: 0.33
Nodes (2): image-models.ts (getImageModel), images.ts (generateImages)

### Community 213 - "Agents Ts"
Cohesion: 0.53
Nodes (4): discoverAgents(), findNearestProjectAgentsDir(), isDirectory(), loadAgentsFromDir()

### Community 214 - "Anthropic Empty Thinking Signature Compat"
Cohesion: 0.33
Nodes (1): PayloadCaptured

### Community 215 - "Pi sendUserMessage With deliverAs (steer"
Cohesion: 0.5
Nodes (5): pi.sendUserMessage with deliverAs (steer/followUp), Streaming-Aware Input Gate, Reload Command (/reload-runtime), reload_runtime Tool, Send User Message Extension

### Community 216 - "Branch Summarization Ts"
Cohesion: 0.6
Nodes (3): generateBranchSummary(), getMessageFromEntry(), prepareBranchEntries()

### Community 217 - "TruncatedText"
Cohesion: 0.4
Nodes (1): TruncatedText

### Community 218 - "generateImagesOpenRouter()"
Cohesion: 0.7
Nodes (4): buildParams(), createClient(), generateImagesOpenRouter(), parseUsage()

### Community 219 - "Diagnostics Ts"
Cohesion: 0.6
Nodes (3): createAssistantMessageDiagnostic(), extractDiagnosticError(), formatThrownValue()

### Community 220 - "2781 Skill Collision Precedence Test"
Cohesion: 0.4
Nodes (0): 

### Community 221 - "Ls Ts"
Cohesion: 0.5
Nodes (2): createLsTool(), createLsToolDefinition()

### Community 222 - "validateToolArguments (TypeBox+coerce)"
Cohesion: 0.4
Nodes (5): AJV-compatible tool arg coercion, StringEnum (typebox helper), coerceWithJsonSchema, validateToolArguments test, validateToolArguments (TypeBox+coerce)

### Community 223 - "DefaultPackageManager (223)"
Cohesion: 0.4
Nodes (5): DefaultPackageManager, npm/git install, update, dedupe, Package filtering / precedence ranking, PackageManager interface, Resource resolution (extensions/skills/prompts/themes)

### Community 224 - "Export Html Xss Test Ts"
Cohesion: 0.6
Nodes (3): Export HTML Template (template.js), safeMarkedParse (Markdown Rendering), Export HTML Skill Block Rendering

### Community 225 - "getProviderLoginHelp()"
Cohesion: 0.7
Nodes (4): formatNoApiKeyFoundMessage(), formatNoModelsAvailableMessage(), formatNoModelSelectedMessage(), getProviderLoginHelp()

### Community 226 - "Photon Ts"
Cohesion: 0.5
Nodes (2): getFallbackWasmPaths(), patchPhotonWasmRead()

### Community 227 - "File Mutation Queue Test Ts"
Cohesion: 0.5
Nodes (2): delay(), resolvesWithin()

### Community 228 - "Frontmatter Ts"
Cohesion: 0.7
Nodes (4): extractFrontmatter(), normalizeNewlines(), parseFrontmatter(), stripFrontmatter()

### Community 229 - "Http Dispatcher Ts"
Cohesion: 0.5
Nodes (2): configureHttpDispatcher(), parseHttpIdleTimeoutMs()

### Community 230 - "Session Id Readonly Test Ts"
Cohesion: 0.5
Nodes (2): createTempDir(), runCli()

### Community 231 - "downloadTool"
Cohesion: 0.5
Nodes (5): TOOLS Config (fd/rg), downloadTool, ensureTool, getLatestVersion, getToolPath

### Community 232 - "Darwin Modifiers C"
Cohesion: 0.7
Nodes (4): is_modifier_pressed(), modifier_mask_for_name(), napi_register_module_v1(), node_symbol()

### Community 233 - "CustomEditor"
Cohesion: 0.4
Nodes (1): CustomEditor

### Community 234 - "Oauth Page Ts"
Cohesion: 0.7
Nodes (4): escapeHtml(), oauthErrorHtml(), oauthSuccessHtml(), renderPage()

### Community 235 - "Openai Completions Cache Control Format"
Cohesion: 0.5
Nodes (3): expectAnthropicCacheMarkers(), FakeOpenAI, getInstructionMessage()

### Community 236 - "#2860 Replaced Session Context"
Cohesion: 0.4
Nodes (5): #2753 reload stale resource settings, #2860 replaced session context, #3616 settings inmemory reload, #3688 tree cancel compacting, Session replacement withSession callback

### Community 237 - "Openai Completions Prompt Cache Test"
Cohesion: 0.4
Nodes (1): FakeOpenAI

### Community 238 - "Openai Completions Thinking As Text"
Cohesion: 0.4
Nodes (0): 

### Community 239 - "DynamicBorder"
Cohesion: 0.4
Nodes (1): DynamicBorder

### Community 240 - "#1717 #2113 Agent Session Event"
Cohesion: 0.5
Nodes (5): #1717/#2113 agent session event settlement, #2023 queued slash-command followup, #3686 session name event, #3982 message_end cost override, message_end handler settlement/override

### Community 241 - "parseStreamingJson"
Cohesion: 0.5
Nodes (5): partial-json streaming tolerance, parseJsonWithRepair, parseStreamingJson, repairJson, partialJson cleanup at output_item.done

### Community 242 - "Terminal Colors Ts"
Cohesion: 0.6
Nodes (3): hexToRgb(), parseOsc11BackgroundColor(), parseOscHexChannel()

### Community 243 - "Working Indicator Ts"
Cohesion: 0.7
Nodes (4): applyIndicator(), colorize(), describeMode(), getIndicator()

### Community 244 - "Command Paths Test"
Cohesion: 0.5
Nodes (4): Project Trust Store, Handle Package Command, Pi CLI Main Entry, Package Command Paths Test

### Community 245 - "Built In Tool Renderer Ts"
Cohesion: 0.5
Nodes (0): 

### Community 246 - "Ansi Utils Test Ts"
Cohesion: 0.5
Nodes (0): 

### Community 247 - "Session Uuid Test Ts"
Cohesion: 0.67
Nodes (2): RFC 9562 UUIDv7 Layout, uuidv7 (session uuid)

### Community 248 - "Simple Options Ts"
Cohesion: 0.67
Nodes (2): adjustMaxTokensForThinking(), clampReasoning()

### Community 249 - "Timings Ts"
Cohesion: 0.5
Nodes (0): 

### Community 250 - "Azure Openai Base Url Test"
Cohesion: 0.5
Nodes (1): AzureOpenAI

### Community 251 - "waitForChildProcess"
Cohesion: 0.5
Nodes (3): waitForChildProcess, Rationale: post-exit stdio grace timer, sleep()

### Community 252 - "Image Models Ts"
Cohesion: 0.5
Nodes (0): 

### Community 253 - "ThinkingSelectorComponent"
Cohesion: 0.5
Nodes (1): ThinkingSelectorComponent

### Community 254 - "Github Copilot Anthropic Test Ts"
Cohesion: 0.5
Nodes (1): FakeAnthropic

### Community 255 - "Titlebar Spinner Ts"
Cohesion: 0.83
Nodes (3): getBaseTitle(), startAnimation(), stopAnimation()

### Community 256 - "Image Resize (resizeImage formatDimensionNote)"
Cohesion: 0.83
Nodes (4): File Processor (processFileArguments), image-resize (resizeImage/formatDimensionNote), Image Resize Callers Tests, Read Tool (createReadTool)

### Community 257 - "Generate Image Models Ts"
Cohesion: 0.83
Nodes (3): fetchOpenRouterImageModels(), generateImageModelsFile(), main()

### Community 258 - "ShowImagesSelectorComponent"
Cohesion: 0.5
Nodes (1): ShowImagesSelectorComponent

### Community 259 - "Shell Output Ts"
Cohesion: 0.67
Nodes (2): executeShellWithCapture(), toExecutionError()

### Community 260 - "loadNativeModifiersHelper()"
Cohesion: 0.83
Nodes (3): isNativeModifierPressed(), isNativeModifiersHelper(), loadNativeModifiersHelper()

### Community 261 - "Transform Messages Copilot Openai To"
Cohesion: 0.5
Nodes (0): 

### Community 262 - "Openrouter Images Test Ts"
Cohesion: 0.5
Nodes (3): OpenRouter abort signal passthrough, FakeOpenAI, src/images.ts

### Community 263 - "EarendilAnnouncementComponent"
Cohesion: 0.67
Nodes (2): EarendilAnnouncementComponent, loadImageBase64()

### Community 264 - "Transform Messages Ts"
Cohesion: 0.67
Nodes (2): downgradeUnsupportedImages(), transformMessages()

### Community 265 - "Session Cwd Test Ts"
Cohesion: 0.5
Nodes (0): 

### Community 266 - "ThemeSelectorComponent"
Cohesion: 0.5
Nodes (1): ThemeSelectorComponent

### Community 267 - "Tool Renderer Ts"
Cohesion: 0.67
Nodes (2): isBlankRenderedLine(), trimRenderedResultLines()

### Community 268 - "Google Shared Image Tool Result"
Cohesion: 0.5
Nodes (4): Google Shared convertTools Test, Google Shared Image Tool Result Routing Test, Gemini 2.x vs 3.x image tool result routing, JSON Schema meta key stripping (recursive $schema/$id/$defs)

### Community 269 - "createBashTool BashOperations"
Cohesion: 0.5
Nodes (4): buildSystemPrompt, createBashTool / BashOperations, createReadTool, executeBashWithOperations

### Community 270 - "Anthropic Oauth Test Ts"
Cohesion: 0.5
Nodes (0): 

### Community 271 - "Format Resume Command Test Ts"
Cohesion: 0.5
Nodes (0): 

### Community 272 - "Tool Definition Wrapper Ts"
Cohesion: 0.5
Nodes (0): 

### Community 273 - "Agent Session Services Ts"
Cohesion: 0.67
Nodes (2): applyExtensionFlagValues(), createAgentSessionServices()

### Community 274 - "Sdk Stream Options Test Ts"
Cohesion: 0.67
Nodes (2): captureStreamOptions(), createModel()

### Community 275 - "Gemini3 Unsigned Tool Call Handling"
Cohesion: 0.5
Nodes (3): skip_thought_signature_validator omission, Gemini3 Unsigned Tool Call Handling, src/providers/google-shared.ts

### Community 276 - "Github Copilot Headers Ts"
Cohesion: 0.67
Nodes (2): buildCopilotDynamicHeaders(), inferCopilotInitiator()

### Community 277 - "5724 Sigterm Signal Exit Test"
Cohesion: 0.5
Nodes (1): ProcessExitError

### Community 278 - "UserMessageComponent"
Cohesion: 0.5
Nodes (1): UserMessageComponent

### Community 279 - "Git Merge And Resolve Ts"
Cohesion: 0.67
Nodes (2): formatConflicts(), formatRange()

### Community 280 - "Agent Harness Test Ts"
Cohesion: 0.5
Nodes (0): 

### Community 281 - "Azure Utils Ts"
Cohesion: 0.67
Nodes (2): parseDeploymentNameMap(), resolveAzureDeploymentName()

### Community 282 - "Adaptive Thinking Payload {adaptive,summarized}"
Cohesion: 0.5
Nodes (4): forceAdaptiveThinking metadata flag, adaptive thinking payload {adaptive,summarized}, omit temperature Opus 4.7/4.8, supportsTemperature compat flag

### Community 283 - "File Mutation Queue Ts"
Cohesion: 0.67
Nodes (2): getMutationQueueKey(), isMissingPathError()

### Community 284 - "Custom Header Ts"
Cohesion: 0.67
Nodes (2): getPiMascot(), render()

### Community 285 - "Prompt Customizer Ts"
Cohesion: 0.5
Nodes (0): 

### Community 286 - "Agent Session Runtime Test Ts"
Cohesion: 0.5
Nodes (0): 

### Community 287 - "Tool Override Ts"
Cohesion: 0.83
Nodes (3): execute(), isBlockedPath(), logAccess()

### Community 288 - "Images Api Registry Ts"
Cohesion: 0.67
Nodes (2): registerImagesApiProvider(), wrapGenerateImages()

### Community 289 - "Args Ts"
Cohesion: 0.67
Nodes (2): isValidThinkingLevel(), parseArgs()

### Community 290 - "GitHub Copilot OAuth Device Flow"
Cohesion: 0.5
Nodes (4): Anthropic OAuth Test, Anthropic OAuth manual-callback login + token refresh, Copilot device-code polling + verification_uri trust boundary, GitHub Copilot OAuth Device Flow Test

### Community 291 - "decodeHtmlEntity()"
Cohesion: 0.83
Nodes (3): decodeCodePoint(), decodeHtmlEntity(), decodeHtmlEntityAt()

### Community 292 - "#2835 Tools Allowlist Filters Extension"
Cohesion: 1.0
Nodes (4): #2835 tools allowlist filters extension tools, #3592 no-builtin-tools keeps extension tools, #5109 exclude tools, Tool allowlist/exclusion/noTools filtering

### Community 293 - "Win32 Console Mode C"
Cohesion: 0.83
Nodes (3): enable_virtual_terminal_input(), napi_register_module_v1(), node_symbol()

### Community 294 - "Agent Skills YAML Frontmatter Standard"
Cohesion: 0.67
Nodes (4): No Frontmatter Skill Fixture, Agent Skills YAML frontmatter standard, Unknown Field Skill Fixture, Valid Skill Fixture

### Community 295 - "System Prompt Ts"
Cohesion: 0.67
Nodes (2): escapeXml(), formatSkillsForSystemPrompt()

### Community 296 - "ModalEditor"
Cohesion: 0.5
Nodes (1): ModalEditor

### Community 297 - "CountdownTimer"
Cohesion: 0.5
Nodes (1): CountdownTimer

### Community 298 - "copyToClipboard"
Cohesion: 0.5
Nodes (4): copyToClipboard, isWaylandSession, OSC 52 Clipboard Fallback, Rationale: skip native clipboard on Linux

### Community 299 - "5433 Extension Oauth Prompt Input"
Cohesion: 0.5
Nodes (0): 

### Community 300 - "resolveImagesApiProvider"
Cohesion: 0.67
Nodes (3): generateImages, resolveImagesApiProvider, getImagesApiProvider

### Community 301 - "Image Tool Result Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 302 - "Streaming Render Debug Ts"
Cohesion: 1.0
Nodes (2): main(), sleep()

### Community 303 - "getBunSandboxEnvValue()"
Cohesion: 1.0
Nodes (2): getBunSandboxEnvValue(), getProviderEnvValue()

### Community 304 - "Source Info Ts"
Cohesion: 0.67
Nodes (0): 

### Community 305 - "Jsonl Ts"
Cohesion: 0.67
Nodes (0): 

### Community 306 - "Ansi Ts"
Cohesion: 0.67
Nodes (0): 

### Community 307 - "Footer Width Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 308 - "Session Resources Ts"
Cohesion: 0.67
Nodes (0): 

### Community 309 - "Cloudflare Utils Ts"
Cohesion: 0.67
Nodes (0): 

### Community 310 - "visibleWidth Test Suite"
Cohesion: 0.67
Nodes (3): normalizeTerminalOutput Thai/Lao normalization test, truncateToWidth test suite, visibleWidth test suite

### Community 311 - "getProxyForUrl"
Cohesion: 0.67
Nodes (3): getProxyForUrl, resolveHttpProxyUrlForTarget, shouldProxyHostname (no_proxy handling)

### Community 312 - "2860 Replaced Session Context Test"
Cohesion: 0.67
Nodes (0): 

### Community 313 - "Preset Ts"
Cohesion: 0.67
Nodes (0): 

### Community 314 - "Session Resources Cleanup Module"
Cohesion: 1.0
Nodes (3): cleanupSessionResources, registerSessionResourceCleanup, Session Resources Cleanup Module

### Community 315 - "Google Shared Gemini3 Unsigned Tool"
Cohesion: 0.67
Nodes (0): 

### Community 316 - "Config Value Migration Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 317 - "Math Operation Calculator Tool"
Cohesion: 0.67
Nodes (3): math_operation calculator tool, multiTurn thinking+tool helper, StringEnum Google anyOf/const rationale

### Community 318 - "Copilot OpenAI >Anthropic Message Transform"
Cohesion: 0.67
Nodes (3): src/providers/transform-messages.ts, Copilot OpenAI->Anthropic message transform, synthetic orphan tool result injection

### Community 319 - "Cloudflare Ts"
Cohesion: 0.67
Nodes (0): 

### Community 320 - "Agent Harness Stream Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 321 - "Openai Completions Response Model Test"
Cohesion: 0.67
Nodes (1): FakeOpenAI

### Community 322 - "isThinkingPart Thought===true"
Cohesion: 0.67
Nodes (3): isThinkingPart thought===true, retainThoughtSignature delta merge, convert thinking to text on model mismatch

### Community 323 - "GoogleGenAI"
Cohesion: 0.67
Nodes (1): GoogleGenAI

### Community 324 - "createEditTool"
Cohesion: 0.67
Nodes (3): Edit tool fuzzy/Unicode matching rationale, computeEditsDiff, createEditTool

### Community 325 - "Dynamic Tools Ts"
Cohesion: 0.67
Nodes (0): 

### Community 326 - "Invalid Name Characters Skill Fixture"
Cohesion: 0.67
Nodes (3): Consecutive Hyphens Invalid Skill Name Fixture, Invalid Name Characters Skill Fixture, Long Name Over Limit Skill Fixture

### Community 327 - "Input Event Transform Handle Hook"
Cohesion: 1.0
Nodes (3): Inline Bash Expansion Extension, Input Transform Extension, input event transform/handle hook

### Community 328 - "renderHighlightedHtml"
Cohesion: 0.67
Nodes (3): getScopeFormatter, highlight, renderHighlightedHtml

### Community 329 - "Word Navigation Ts"
Cohesion: 0.67
Nodes (0): 

### Community 330 - "pollOAuthDeviceCodeFlow()"
Cohesion: 1.0
Nodes (2): abortableSleep(), pollOAuthDeviceCodeFlow()

### Community 331 - "Node Http Proxy Test Ts"
Cohesion: 0.67
Nodes (1): utils/node-http-proxy.ts (resolveHttpProxyUrlForTarget)

### Community 332 - "RpcClient Process Exit Tests"
Cohesion: 1.0
Nodes (3): RpcClient, RpcClient Process Exit Tests, RPC Interactive Example

### Community 333 - "13 Session Runtime Ts"
Cohesion: 0.67
Nodes (0): 

### Community 334 - "Overflow Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 335 - "Atomic Segments (paste Markers) Test"
Cohesion: 1.0
Nodes (3): atomic segments (paste markers) test suite, findWordBackward test suite, findWordForward test suite

### Community 336 - "Github Copilot Oauth Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 337 - "Paths Test Ts"
Cohesion: 0.67
Nodes (1): loadClipboardNative

### Community 338 - "Wrapper Ts"
Cohesion: 0.67
Nodes (0): 

### Community 339 - "resolveImagesApiProvider()"
Cohesion: 1.0
Nodes (2): generateImages(), resolveImagesApiProvider()

### Community 340 - "Export HTML Whitespace Tests"
Cohesion: 0.67
Nodes (3): Export HTML Whitespace Tests, ansiLinesToHtml, createToolHtmlRenderer

### Community 341 - "stripAnsi"
Cohesion: 0.67
Nodes (2): stripAnsi, decodeHtmlEntity

### Community 342 - "Openai Completions Retry Test Ts"
Cohesion: 0.67
Nodes (1): FakeOpenAI

### Community 343 - "Signal Triggered Shutdown Ordering (dispose"
Cohesion: 1.0
Nodes (3): #5080 signal shutdown extension cleanup, #5724 sigterm signal-exit, Signal-triggered shutdown ordering (dispose before tty)

### Community 344 - "Fs Watch Ts"
Cohesion: 0.67
Nodes (0): 

### Community 345 - "#3303 Find Nested Gitignore"
Cohesion: 1.0
Nodes (3): #3302 find path glob, #3303 find nested gitignore, fd full-path glob matching

### Community 346 - "Questionnaire Ts"
Cohesion: 0.67
Nodes (0): 

### Community 347 - "Command Paths Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 348 - "ensureWadFile()"
Cohesion: 1.0
Nodes (2): ensureWadFile(), findWadFile()

### Community 349 - "Print Mode Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 350 - "List Models Ts"
Cohesion: 0.67
Nodes (0): 

### Community 351 - "fuzzyFilter()"
Cohesion: 1.0
Nodes (2): fuzzyFilter(), fuzzyMatch()

### Community 352 - "Tool Execution Component Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 353 - "Custom Footer Ts"
Cohesion: 0.67
Nodes (0): 

### Community 354 - "Compaction Extensions Example Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 355 - "Overflow Ts"
Cohesion: 0.67
Nodes (0): 

### Community 356 - "Handoff Ts"
Cohesion: 0.67
Nodes (0): 

### Community 357 - "Image Resize Core Ts"
Cohesion: 0.67
Nodes (0): 

### Community 358 - "registerFauxProvider"
Cohesion: 0.67
Nodes (3): registerApiProvider, Faux Prompt-Cache Simulation, registerFauxProvider

### Community 359 - "resizeImage (image Resizer)"
Cohesion: 0.67
Nodes (3): convertToPng (image format converter), formatDimensionNote (resize note formatter), resizeImage (image resizer)

### Community 360 - "Settings Manager External Edit Preservation"
Cohesion: 0.67
Nodes (3): Settings Manager, Settings External Edit Overwrite Bug, Settings Manager External Edit Preservation Test

### Community 361 - "Extensions Runner Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 362 - "Google Shared Image Tool Result (362)"
Cohesion: 0.67
Nodes (0): 

### Community 363 - "Compaction Extensions Documentation Example Test"
Cohesion: 0.67
Nodes (3): Compaction Extensions Documentation Example Test, Extensions API, Extensions Documentation

### Community 364 - "Agent Session Dynamic Provider Test"
Cohesion: 0.67
Nodes (0): 

### Community 365 - "Openai Responses Copilot Provider Test"
Cohesion: 0.67
Nodes (0): 

### Community 366 - "getProbePriority cost+Haiku Heuristic"
Cohesion: 0.67
Nodes (3): getProbePriority cost+Haiku heuristic, selectOneCasePerProvider dedup, withEagerToolInputStreaming compat override

### Community 367 - "base64urlEncode()"
Cohesion: 1.0
Nodes (2): base64urlEncode(), generatePKCE()

### Community 368 - "Deprecation Ts"
Cohesion: 0.67
Nodes (0): 

### Community 369 - "getInteractiveCommands()"
Cohesion: 1.0
Nodes (2): getInteractiveCommands(), isInteractiveCommand()

### Community 370 - "isInstallTelemetryEnabled()"
Cohesion: 1.0
Nodes (2): isInstallTelemetryEnabled(), isTruthyEnvFlag()

### Community 371 - "Session Selector Rename Test Ts"
Cohesion: 0.67
Nodes (0): 

### Community 372 - "Claude Rules Ts"
Cohesion: 0.67
Nodes (0): 

### Community 373 - "Lockstep Monorepo Versioning Rationale"
Cohesion: 1.0
Nodes (2): lockstep monorepo versioning rationale, lockstep versioning sync logic

### Community 374 - "inputTransformStreaming (git Diff Transform Extension)"
Cohesion: 1.0
Nodes (2): ExtensionAPI, inputTransformStreaming (git diff transform extension)

### Community 375 - "Google Shared Convert Tools Test"
Cohesion: 1.0
Nodes (0): 

### Community 376 - "Reasoning Replay Cross Provider Handoff"
Cohesion: 1.0
Nodes (2): reasoning replay cross-provider handoff, OAuthCredentials

### Community 377 - "Skill Precedence: Project > User"
Cohesion: 1.0
Nodes (2): #2781 skill collision precedence, Skill precedence: project > user > package

### Community 378 - "createPersistedSession()"
Cohesion: 1.0
Nodes (0): 

### Community 379 - "OSC 777 OSC 99 Windows"
Cohesion: 1.0
Nodes (2): OSC 777 / OSC 99 / Windows Toast Notification, Terminal Notify Extension

### Community 380 - "Get Current Time Ts"
Cohesion: 1.0
Nodes (0): 

### Community 381 - "execCommand()"
Cohesion: 1.0
Nodes (0): 

### Community 382 - "Bedrock Provider Type Declarations"
Cohesion: 1.0
Nodes (2): Bedrock Provider Type Declarations, Bedrock Provider JS

### Community 383 - "migrateSessionEntries Function"
Cohesion: 1.0
Nodes (1): migrateSessionEntries function

### Community 384 - "Agent Session Runtime Events Test"
Cohesion: 1.0
Nodes (0): 

### Community 385 - "#2791 Fswatch Error Crash"
Cohesion: 1.0
Nodes (2): #2791 fswatch error crash, #3217 scoped model order

### Community 386 - "stripJsonComments()"
Cohesion: 1.0
Nodes (0): 

### Community 387 - "Session Info Modified Timestamp Test"
Cohesion: 1.0
Nodes (0): 

### Community 388 - "widgetPlacementExtension()"
Cohesion: 1.0
Nodes (0): 

### Community 389 - "CLI Args (parseArgs)"
Cohesion: 1.0
Nodes (1): CLI Args (parseArgs)

### Community 390 - "HTTP Dispatcher (applyHttpProxySettings)"
Cohesion: 1.0
Nodes (2): HTTP Dispatcher (applyHttpProxySettings), HTTP Dispatcher Proxy Tests

### Community 391 - "Assistant Message Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 392 - "Rpc Example Ts"
Cohesion: 1.0
Nodes (0): 

### Community 393 - "processFileArguments()"
Cohesion: 1.0
Nodes (0): 

### Community 394 - "5208 Late Bash Output Test"
Cohesion: 1.0
Nodes (0): 

### Community 395 - "Tool Call Id Normalization Test"
Cohesion: 1.0
Nodes (0): 

### Community 396 - "Shutdown Command Ts"
Cohesion: 1.0
Nodes (0): 

### Community 397 - "Session Picker Ts"
Cohesion: 1.0
Nodes (0): 

### Community 398 - "Session Selector Search Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 399 - "getPiUserAgent Tests"
Cohesion: 1.0
Nodes (2): getPiUserAgent Tests, getPiUserAgent util

### Community 400 - "InteractiveMode Startup Input Tests"
Cohesion: 1.0
Nodes (2): InteractiveMode, InteractiveMode Startup Input Tests

### Community 401 - "Dirty Repo Guard Ts"
Cohesion: 1.0
Nodes (0): 

### Community 402 - "Bash Execution Width Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 403 - "Find >Glob Mapping Anti Pattern"
Cohesion: 1.0
Nodes (2): CC canonical casing round-trip, find->Glob mapping anti-pattern rationale

### Community 404 - "executeBashWithOperations()"
Cohesion: 1.0
Nodes (0): 

### Community 405 - "3303 Find Nested Gitignore Test"
Cohesion: 1.0
Nodes (0): 

### Community 406 - "Mac System Theme Ts"
Cohesion: 1.0
Nodes (0): 

### Community 407 - "combineAbortSignals()"
Cohesion: 1.0
Nodes (0): 

### Community 408 - "Clipboard Image Bmp Conversion Test"
Cohesion: 1.0
Nodes (0): 

### Community 409 - "Word Navigation Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 410 - "Rpc Client Process Exit Test"
Cohesion: 1.0
Nodes (0): 

### Community 411 - "Ctx Compact Context Compaction"
Cohesion: 1.0
Nodes (2): ctx.compact Context Compaction, Trigger Compaction Extension

### Community 412 - "Edit Tool Legacy Input Test"
Cohesion: 1.0
Nodes (0): 

### Community 413 - "Skills Collision Second Calendar Skill"
Cohesion: 1.0
Nodes (2): Skills Collision First Calendar Skill, Skills Collision Second Calendar Skill

### Community 414 - "3302 Find Path Glob Test"
Cohesion: 1.0
Nodes (0): 

### Community 415 - "Openai Responses Partial Json Cleanup"
Cohesion: 1.0
Nodes (0): 

### Community 416 - "IMAGE MODELS Data"
Cohesion: 1.0
Nodes (2): getImageModel, IMAGE_MODELS Data

### Community 417 - "Open Browser Ts"
Cohesion: 1.0
Nodes (0): 

### Community 418 - "Invalid YAML Frontmatter Skill Fixture"
Cohesion: 1.0
Nodes (2): Invalid YAML Frontmatter Skill Fixture, Missing Description Skill Fixture

### Community 419 - "Startup Session Name Test"
Cohesion: 1.0
Nodes (2): cli (core), startup session name test

### Community 420 - "Clipboard BMP To PNG Conversion"
Cohesion: 1.0
Nodes (2): Clipboard BMP to PNG Conversion Tests, readClipboardImage util

### Community 421 - "mapKeyToDoom()"
Cohesion: 1.0
Nodes (0): 

### Community 422 - "shortHash()"
Cohesion: 1.0
Nodes (0): 

### Community 423 - "sanitizeSurrogates()"
Cohesion: 1.0
Nodes (0): 

### Community 424 - "Initial Message Test"
Cohesion: 1.0
Nodes (2): Build Initial Message, Build Initial Message Test

### Community 425 - "Openrouter Cache Write Repro Test"
Cohesion: 1.0
Nodes (0): 

### Community 426 - "#5303 Bash Output Truncation"
Cohesion: 1.0
Nodes (2): #5208 late bash output, #5303 bash output truncation

### Community 427 - "RpcClient Clone Tests"
Cohesion: 1.0
Nodes (2): RpcClient, RpcClient Clone Tests

### Community 428 - "pirateExtension()"
Cohesion: 1.0
Nodes (0): 

### Community 429 - "getModelSearchText()"
Cohesion: 1.0
Nodes (0): 

### Community 430 - "Interactive Mode Startup Input Test"
Cohesion: 1.0
Nodes (0): 

### Community 431 - "Input Transform Streaming Example Test"
Cohesion: 1.0
Nodes (0): 

### Community 432 - "Interactive Mode Anthropic Warning Test"
Cohesion: 1.0
Nodes (0): 

### Community 433 - "2835 Tools Allowlist Filters Extension"
Cohesion: 1.0
Nodes (0): 

### Community 434 - "Anthropic 'no Low Surrogate' JSON"
Cohesion: 1.0
Nodes (2): Anthropic 'no low surrogate' JSON error, testUnpairedHighSurrogate 0xD83D

### Community 435 - "Unique Fallback Message IDs (msg"
Cohesion: 1.0
Nodes (2): Unique fallback message IDs (msg_pi_1) for multi-block turns, OpenAI Responses Message ID Conversion Test

### Community 436 - "Interactive Mode Suspend Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 437 - "2753 Reload Stale Resource Settings"
Cohesion: 1.0
Nodes (0): 

### Community 438 - "Bug Regression Isimageline Startswith Bug"
Cohesion: 1.0
Nodes (0): 

### Community 439 - "Providers Openai Responses Shared Ts"
Cohesion: 1.0
Nodes (2): OpenAI Responses Foreign ToolCall ID, src/providers/openai-responses-shared.ts

### Community 440 - "RPC JSONL Framing Test"
Cohesion: 1.0
Nodes (2): RPC JSONL Line Reader, RPC JSONL Framing Test

### Community 441 - "Question Ts"
Cohesion: 1.0
Nodes (0): 

### Community 442 - "Path Utils expandPath resolveReadPath Test"
Cohesion: 1.0
Nodes (2): path-utils (core), path-utils expandPath/resolveReadPath test

### Community 443 - "runPrintMode()"
Cohesion: 1.0
Nodes (0): 

### Community 444 - "Compaction Summary Reasoning Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 445 - "isResizeImageWorkerRequest()"
Cohesion: 1.0
Nodes (0): 

### Community 446 - "Hidden Thinking Label Ts"
Cohesion: 1.0
Nodes (0): 

### Community 447 - "Vertex ADC Fallback For Placeholder"
Cohesion: 1.0
Nodes (2): Google Vertex API Key Resolution Test, Vertex ADC fallback for placeholder API keys

### Community 448 - "runRpcMode()"
Cohesion: 1.0
Nodes (0): 

### Community 449 - "Typebox Helpers Ts"
Cohesion: 1.0
Nodes (0): 

### Community 450 - "Image Convert Ts"
Cohesion: 1.0
Nodes (0): 

### Community 451 - "createFindTool"
Cohesion: 1.0
Nodes (2): createFindTool, createGrepTool

### Community 452 - "Simple Ts"
Cohesion: 1.0
Nodes (0): 

### Community 453 - "Anthropic Adaptive Thinking Models Test"
Cohesion: 1.0
Nodes (0): 

### Community 454 - "areExperimentalFeaturesEnabled()"
Cohesion: 1.0
Nodes (0): 

### Community 455 - "normalizeChangelogLinks Test"
Cohesion: 1.0
Nodes (2): changelog utils (core), normalizeChangelogLinks test

### Community 456 - "OpenRouter Cache Write Tokens Regression"
Cohesion: 1.0
Nodes (2): prompt_cache_key / session-affinity headers, OpenRouter cache_write_tokens regression E2E

### Community 457 - "Extensions Input Event Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 458 - "Prompt Template Argument Substitution Test"
Cohesion: 1.0
Nodes (2): Prompt Templates Module, Prompt Template Argument Substitution Test

### Community 459 - "buildInitialMessage()"
Cohesion: 1.0
Nodes (0): 

### Community 460 - "headersToRecord()"
Cohesion: 1.0
Nodes (0): 

### Community 461 - "FooterDataProvider Reftable Branch Detection Test"
Cohesion: 1.0
Nodes (2): FooterDataProvider (core), FooterDataProvider reftable branch detection test

### Community 462 - "toolsExtension()"
Cohesion: 1.0
Nodes (0): 

### Community 463 - "GitHub Issue Autocomplete Extension"
Cohesion: 1.0
Nodes (2): GitHub Issue Autocomplete Extension, Provider Payload Logger Extension

### Community 464 - "commandsExtension()"
Cohesion: 1.0
Nodes (0): 

### Community 465 - "Multiline Description Skill Fixture"
Cohesion: 1.0
Nodes (2): Multiline Description Skill Fixture, Name Mismatch Skill Fixture

### Community 466 - "clampOpenAIPromptCacheKey()"
Cohesion: 1.0
Nodes (0): 

### Community 467 - "triggerCompaction()"
Cohesion: 1.0
Nodes (0): 

### Community 468 - "Calculate Ts"
Cohesion: 1.0
Nodes (0): 

### Community 469 - "#5661 Uppercase Header Values"
Cohesion: 1.0
Nodes (2): #5596 missing theme export, #5661 uppercase header values

### Community 470 - "createToolCallWithPlainSchema()"
Cohesion: 1.0
Nodes (0): 

### Community 471 - "Reload Runtime Ts"
Cohesion: 1.0
Nodes (0): 

### Community 472 - "Keybindings Migration Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 473 - "Image Processing Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 474 - "Regression Overlay Cjk Boundary Test"
Cohesion: 1.0
Nodes (0): 

### Community 475 - "truncateToVisualLines()"
Cohesion: 1.0
Nodes (0): 

### Community 476 - "Initial Message Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 477 - "Root Skill Preferred Fixture"
Cohesion: 1.0
Nodes (2): Nested Child Skill Fixture, Root Skill Preferred Fixture

### Community 478 - "createEventBus()"
Cohesion: 1.0
Nodes (0): 

### Community 479 - "encodeSessionDir()"
Cohesion: 1.0
Nodes (0): 

### Community 480 - "Generate Test Image Script"
Cohesion: 1.0
Nodes (2): generate-test-image Script, Red Circle Test Image

### Community 481 - "loadClipboardNative()"
Cohesion: 1.0
Nodes (0): 

### Community 482 - "Pi User Agent Ts"
Cohesion: 1.0
Nodes (0): 

### Community 483 - "Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 484 - "3592 No Builtin Tools Keeps"
Cohesion: 1.0
Nodes (0): 

### Community 485 - "Box Container Component"
Cohesion: 1.0
Nodes (1): Box container component

### Community 486 - "Pi Test Ps1"
Cohesion: 1.0
Nodes (0): 

### Community 487 - "Sync Versions Js"
Cohesion: 1.0
Nodes (0): 

### Community 488 - "Browser Smoke Entry Ts"
Cohesion: 1.0
Nodes (0): 

### Community 489 - "Manager Ssh Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 490 - "Path Utils Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 491 - "Theme Detection Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 492 - "Changelog Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 493 - "Interactive Mode Compaction Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 494 - "Agent Session Dynamic Tools Test"
Cohesion: 1.0
Nodes (0): 

### Community 495 - "Model Resolver Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 496 - "Interactive Mode Import Command Test"
Cohesion: 1.0
Nodes (0): 

### Community 497 - "Export Html Whitespace Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 498 - "Settings Manager Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 499 - "Pi User Agent Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 500 - "Sdk Skills Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 501 - "Image Resize Callers Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 502 - "Syntax Highlight Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 503 - "Plan Mode Utils Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 504 - "Git Ssh Url Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 505 - "Trust Selector Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 506 - "Rpc Client Clone Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 507 - "Trust Manager Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 508 - "Http Dispatcher Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 509 - "First Time Setup Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 510 - "Frontmatter Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 511 - "Rpc Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 512 - "Resource Loader Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 513 - "Restore Sandbox Env Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 514 - "Theme Export Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 515 - "Theme Picker Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 516 - "Test Harness Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 517 - "Sdk Session Manager Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 518 - "Compaction Serialization Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 519 - "Export Html Skill Block Test"
Cohesion: 1.0
Nodes (0): 

### Community 520 - "Clipboard Native Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 521 - "User Message Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 522 - "Experimental Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 523 - "Settings Manager Bug Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 524 - "Truncate To Width Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 525 - "Rpc Jsonl Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 526 - "Custom Session Id Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 527 - "Save Entry Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 528 - "5303 Bash Output Truncation Test"
Cohesion: 1.0
Nodes (0): 

### Community 529 - "2791 Fswatch Error Crash Test"
Cohesion: 1.0
Nodes (0): 

### Community 530 - "3616 Settings Inmemory Reload Test"
Cohesion: 1.0
Nodes (0): 

### Community 531 - "File Trigger Ts"
Cohesion: 1.0
Nodes (0): 

### Community 532 - "Message Renderer Ts"
Cohesion: 1.0
Nodes (0): 

### Community 533 - "Model Status Ts"
Cohesion: 1.0
Nodes (0): 

### Community 534 - "Timed Confirm Ts"
Cohesion: 1.0
Nodes (0): 

### Community 535 - "Input Transform Ts"
Cohesion: 1.0
Nodes (0): 

### Community 536 - "Inline Bash Ts"
Cohesion: 1.0
Nodes (0): 

### Community 537 - "Working Message Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 538 - "Custom Compaction Ts"
Cohesion: 1.0
Nodes (0): 

### Community 539 - "System Prompt Header Ts"
Cohesion: 1.0
Nodes (0): 

### Community 540 - "Bookmark Ts"
Cohesion: 1.0
Nodes (0): 

### Community 541 - "Rpc Demo Ts"
Cohesion: 1.0
Nodes (0): 

### Community 542 - "Input Transform Streaming Ts"
Cohesion: 1.0
Nodes (0): 

### Community 543 - "Qna Ts"
Cohesion: 1.0
Nodes (0): 

### Community 544 - "Provider Payload Ts"
Cohesion: 1.0
Nodes (0): 

### Community 545 - "Send User Message Ts"
Cohesion: 1.0
Nodes (0): 

### Community 546 - "Protected Paths Ts"
Cohesion: 1.0
Nodes (0): 

### Community 547 - "Confirm Destructive Ts"
Cohesion: 1.0
Nodes (0): 

### Community 548 - "Permission Gate Ts"
Cohesion: 1.0
Nodes (0): 

### Community 549 - "Session Name Ts"
Cohesion: 1.0
Nodes (0): 

### Community 550 - "Git Checkpoint Ts"
Cohesion: 1.0
Nodes (0): 

### Community 551 - "Auto Commit On Exit Ts"
Cohesion: 1.0
Nodes (0): 

### Community 552 - "Structured Output Ts"
Cohesion: 1.0
Nodes (0): 

### Community 553 - "Status Line Ts"
Cohesion: 1.0
Nodes (0): 

### Community 554 - "Bash Spawn Hook Ts"
Cohesion: 1.0
Nodes (0): 

### Community 555 - "Hello Ts"
Cohesion: 1.0
Nodes (0): 

### Community 556 - "09 Api Keys And Oauth"
Cohesion: 1.0
Nodes (0): 

### Community 557 - "02 Custom Model Ts"
Cohesion: 1.0
Nodes (0): 

### Community 558 - "06 Extensions Ts"
Cohesion: 1.0
Nodes (0): 

### Community 559 - "05 Tools Ts"
Cohesion: 1.0
Nodes (0): 

### Community 560 - "10 Settings Ts"
Cohesion: 1.0
Nodes (0): 

### Community 561 - "11 Sessions Ts"
Cohesion: 1.0
Nodes (0): 

### Community 562 - "04 Skills Ts"
Cohesion: 1.0
Nodes (0): 

### Community 563 - "01 Minimal Ts"
Cohesion: 1.0
Nodes (0): 

### Community 564 - "07 Context Files Ts"
Cohesion: 1.0
Nodes (0): 

### Community 565 - "12 Full Control Ts"
Cohesion: 1.0
Nodes (0): 

### Community 566 - "08 Prompt Templates Ts"
Cohesion: 1.0
Nodes (0): 

### Community 567 - "03 Custom Prompt Ts"
Cohesion: 1.0
Nodes (0): 

### Community 568 - "Defaults Ts"
Cohesion: 1.0
Nodes (0): 

### Community 569 - "Slash Commands Ts"
Cohesion: 1.0
Nodes (0): 

### Community 570 - "Provider Display Names Ts"
Cohesion: 1.0
Nodes (0): 

### Community 571 - "Rpc Types Ts"
Cohesion: 1.0
Nodes (0): 

### Community 572 - "Image Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 573 - "Wrap Ansi Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 574 - "Regression Regional Indicator Width Test"
Cohesion: 1.0
Nodes (0): 

### Community 575 - "Chat Simple Ts"
Cohesion: 1.0
Nodes (0): 

### Community 576 - "Editor Component Ts"
Cohesion: 1.0
Nodes (0): 

### Community 577 - "Nodejs Env Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 578 - "Resource Formatting Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 579 - "Node Ts"
Cohesion: 1.0
Nodes (0): 

### Community 580 - "Bedrock Provider D Ts"
Cohesion: 1.0
Nodes (0): 

### Community 581 - "Together Models Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 582 - "Openai Responses Reasoning Replay E2e"
Cohesion: 1.0
Nodes (0): 

### Community 583 - "Zen Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 584 - "Bedrock Models Test Ts"
Cohesion: 1.0
Nodes (0): 

### Community 585 - "Openai Responses Message Id Test"
Cohesion: 1.0
Nodes (0): 

### Community 586 - "Openai Codex Cache Affinity E2e"
Cohesion: 1.0
Nodes (0): 

### Community 587 - "Anthropic Tool Name Normalization Test"
Cohesion: 1.0
Nodes (0): 

### Community 588 - "Openai Responses Foreign Toolcall Id"
Cohesion: 1.0
Nodes (0): 

### Community 589 - "Generate Test Image Ts"
Cohesion: 1.0
Nodes (0): 

### Community 590 - "Result Type (ok Err)"
Cohesion: 1.0
Nodes (1): Result type (ok/err)

### Community 591 - "PromptTemplate Interface"
Cohesion: 1.0
Nodes (1): PromptTemplate interface

### Community 592 - "AgentHarnessResources Interface"
Cohesion: 1.0
Nodes (1): AgentHarnessResources interface

### Community 593 - "CompactionError Class"
Cohesion: 1.0
Nodes (1): CompactionError class

### Community 594 - "BranchSummaryError Class"
Cohesion: 1.0
Nodes (1): BranchSummaryError class

### Community 595 - "FileError Class"
Cohesion: 1.0
Nodes (1): FileError class

### Community 596 - "agentLoop Tests"
Cohesion: 1.0
Nodes (1): agentLoop tests

### Community 597 - "StreamOptions Interface"
Cohesion: 1.0
Nodes (1): StreamOptions Interface

### Community 598 - "AssistantMessage"
Cohesion: 1.0
Nodes (1): AssistantMessage

### Community 599 - "createClient (Vertex ADC)"
Cohesion: 1.0
Nodes (1): createClient (Vertex ADC)

### Community 600 - "isCloudflareProvider"
Cohesion: 1.0
Nodes (1): isCloudflareProvider

### Community 601 - "combineAbortSignals"
Cohesion: 1.0
Nodes (1): combineAbortSignals

### Community 602 - "createAssistantMessageDiagnostic"
Cohesion: 1.0
Nodes (1): createAssistantMessageDiagnostic

### Community 603 - "OAuthLoginCallbacks"
Cohesion: 1.0
Nodes (1): OAuthLoginCallbacks

### Community 604 - "Together Models (Kimi K2 6,"
Cohesion: 1.0
Nodes (1): Together models (Kimi K2.6, gpt-oss) registration

### Community 605 - "Bedrock convertMessages Unknown Content Handling"
Cohesion: 1.0
Nodes (1): Bedrock convertMessages unknown-content handling

### Community 606 - "handleStreaming Text Helper"
Cohesion: 1.0
Nodes (1): handleStreaming text helper

### Community 607 - "Bash Spawn Hook Extension (createBashTool"
Cohesion: 1.0
Nodes (1): Bash Spawn Hook Extension (createBashTool spawnHook)

### Community 608 - "configureHttpDispatcher (undici Global Dispatcher +"
Cohesion: 1.0
Nodes (1): configureHttpDispatcher (undici global dispatcher + proxy)

### Community 609 - "parseSkillBlock"
Cohesion: 1.0
Nodes (1): parseSkillBlock

### Community 610 - "createToolDefinitionFromAgentTool"
Cohesion: 1.0
Nodes (1): createToolDefinitionFromAgentTool

### Community 611 - "stripJsonComments"
Cohesion: 1.0
Nodes (1): stripJsonComments

### Community 612 - "formatDimensionNote"
Cohesion: 1.0
Nodes (1): formatDimensionNote

### Community 613 - "killProcessTree"
Cohesion: 1.0
Nodes (1): killProcessTree

### Community 614 - "sanitizeBinaryOutput"
Cohesion: 1.0
Nodes (1): sanitizeBinaryOutput

### Community 615 - "warnDeprecation"
Cohesion: 1.0
Nodes (1): warnDeprecation

### Community 616 - "supportsLanguage"
Cohesion: 1.0
Nodes (1): supportsLanguage

### Community 617 - "AuthStorage (617)"
Cohesion: 1.0
Nodes (1): AuthStorage

### Community 618 - "initTheme"
Cohesion: 1.0
Nodes (1): initTheme

### Community 619 - "restoreSandboxEnv (bun Sandbox Env Restorer)"
Cohesion: 1.0
Nodes (1): restoreSandboxEnv (bun sandbox env restorer)

### Community 620 - "createWriteTool"
Cohesion: 1.0
Nodes (1): createWriteTool

### Community 621 - "createLsTool"
Cohesion: 1.0
Nodes (1): createLsTool

### Community 622 - "Disable Model Invocation Skill Fixture"
Cohesion: 1.0
Nodes (1): Disable Model Invocation Skill Fixture

### Community 623 - "Nested Child Skill Fixture"
Cohesion: 1.0
Nodes (1): Nested Child Skill Fixture

### Community 624 - "FuzzyMatch Interface"
Cohesion: 1.0
Nodes (1): FuzzyMatch interface

### Community 625 - "SelectList Test"
Cohesion: 1.0
Nodes (1): SelectList Test

## Ambiguous Edges - Review These
- `isContextOverflow (multi-provider patterns)` → `enableAllGitHubCopilotModels (policy acceptance)`  [AMBIGUOUS]
  pi/packages/ai/test/overflow.test.ts · relation: conceptually_related_to
- `OAuthCredentials` → `reasoning replay cross-provider handoff`  [AMBIGUOUS]
  pi/packages/ai/test/openai-responses-reasoning-replay-e2e.test.ts · relation: references
- `red-circle.png (vision test fixture)` → `Context overflow handling`  [AMBIGUOUS]
  pi/packages/ai/test/data/red-circle.png · relation: shares_data_with
- `Pi Terminal Coding Harness` → `Exy Pufferfish Illustration`  [AMBIGUOUS]
  pi/packages/coding-agent/docs/images/exy.png · relation: conceptually_related_to
- `GitHub Issue Autocomplete Extension` → `Provider Payload Logger Extension`  [AMBIGUOUS]
  pi/packages/coding-agent/examples/extensions/github-issue-autocomplete.ts · relation: conceptually_related_to
- `Shutdown Command Extension` → `Confirm Destructive Actions Extension`  [AMBIGUOUS]
  pi/packages/coding-agent/examples/extensions/shutdown-command.ts · relation: conceptually_related_to
- `buildSystemPrompt (tools/guidelines/context/skills assembly)` → `isInstallTelemetryEnabled (PI_TELEMETRY gate)`  [AMBIGUOUS]
  pi/packages/coding-agent/src/core/system-prompt.ts · relation: conceptually_related_to
- `Daxnuts Easter Egg Component` → `Extension Multi-line Editor`  [AMBIGUOUS]
  pi/packages/coding-agent/src/modes/interactive/components/daxnuts.ts · relation: conceptually_related_to
- `watchWithErrorHandler` → `resolvePath`  [AMBIGUOUS]
  pi/packages/coding-agent/src/utils/fs-watch.ts · relation: shares_data_with
- `runPrintMode Tests` → `Concept: Compaction Lifecycle (manual/threshold/overflow + before_compact/compact events)`  [AMBIGUOUS]
  pi/packages/coding-agent/test/print-mode.test.ts · relation: conceptually_related_to
- `Plan Mode Utils (isSafeCommand/extractTodoItems/extractDoneSteps/markCompletedSteps)` → `Extension Event System (input/tool_result/before_agent_start)`  [AMBIGUOUS]
  pi/packages/coding-agent/test/plan-mode-utils.test.ts · relation: conceptually_related_to
- `First Time Setup Tests` → `Project Trust Concept`  [AMBIGUOUS]
  pi/packages/coding-agent/test/first-time-setup.test.ts · relation: references
- `Box container component` → `Box container component`  [AMBIGUOUS]
  pi/packages/tui/src/components/box.ts · relation: references

## Knowledge Gaps
- **532 isolated node(s):** `ProcessExitError`, `ProcessExitError`, `BashResultRenderComponent`, `BedrockRuntimeServiceException`, `BedrockRuntimeServiceException` (+527 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Lockstep Monorepo Versioning Rationale`** (2 nodes): `lockstep monorepo versioning rationale`, `lockstep versioning sync logic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `inputTransformStreaming (git Diff Transform Extension)`** (2 nodes): `ExtensionAPI`, `inputTransformStreaming (git diff transform extension)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Google Shared Convert Tools Test`** (2 nodes): `google-shared-convert-tools.test.ts`, `makeTool()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Reasoning Replay Cross Provider Handoff`** (2 nodes): `reasoning replay cross-provider handoff`, `OAuthCredentials`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Skill Precedence: Project > User`** (2 nodes): `#2781 skill collision precedence`, `Skill precedence: project > user > package`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createPersistedSession()`** (2 nodes): `file-operations.test.ts`, `createPersistedSession()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `OSC 777 OSC 99 Windows`** (2 nodes): `OSC 777 / OSC 99 / Windows Toast Notification`, `Terminal Notify Extension`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Get Current Time Ts`** (2 nodes): `get-current-time.ts`, `getCurrentTime()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `execCommand()`** (2 nodes): `exec.ts`, `execCommand()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bedrock Provider Type Declarations`** (2 nodes): `Bedrock Provider Type Declarations`, `Bedrock Provider JS`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `migrateSessionEntries Function`** (2 nodes): `migrateSessionEntries function`, `migration.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Agent Session Runtime Events Test`** (2 nodes): `agent-session-runtime-events.test.ts`, `createRuntimeHost()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `#2791 Fswatch Error Crash`** (2 nodes): `#2791 fswatch error crash`, `#3217 scoped model order`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `stripJsonComments()`** (2 nodes): `json.ts`, `stripJsonComments()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Session Info Modified Timestamp Test`** (2 nodes): `session-info-modified-timestamp.test.ts`, `createSessionFile()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `widgetPlacementExtension()`** (2 nodes): `widget-placement.ts`, `widgetPlacementExtension()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `CLI Args (parseArgs)`** (2 nodes): `CLI Args (parseArgs)`, `args.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `HTTP Dispatcher (applyHttpProxySettings)`** (2 nodes): `HTTP Dispatcher (applyHttpProxySettings)`, `HTTP Dispatcher Proxy Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Assistant Message Test Ts`** (2 nodes): `assistant-message.test.ts`, `createAssistantMessage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Rpc Example Ts`** (2 nodes): `rpc-example.ts`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `processFileArguments()`** (2 nodes): `file-processor.ts`, `processFileArguments()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `5208 Late Bash Output Test`** (2 nodes): `5208-late-bash-output.test.ts`, `getTextOutput()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Tool Call Id Normalization Test`** (2 nodes): `tool-call-id-normalization.test.ts`, `buildPrefilledMessages()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Shutdown Command Ts`** (2 nodes): `shutdown-command.ts`, `execute()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Session Picker Ts`** (2 nodes): `session-picker.ts`, `selectSession()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Session Selector Search Test Ts`** (2 nodes): `session-selector-search.test.ts`, `makeSession()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `getPiUserAgent Tests`** (2 nodes): `getPiUserAgent Tests`, `getPiUserAgent util`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `InteractiveMode Startup Input Tests`** (2 nodes): `InteractiveMode`, `InteractiveMode Startup Input Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Dirty Repo Guard Ts`** (2 nodes): `dirty-repo-guard.ts`, `checkDirtyRepo()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bash Execution Width Test Ts`** (2 nodes): `bash-execution-width.test.ts`, `createTuiStub()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Find >Glob Mapping Anti Pattern`** (2 nodes): `CC canonical casing round-trip`, `find->Glob mapping anti-pattern rationale`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `executeBashWithOperations()`** (2 nodes): `bash-executor.ts`, `executeBashWithOperations()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `3303 Find Nested Gitignore Test`** (2 nodes): `3303-find-nested-gitignore.test.ts`, `runFind()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Mac System Theme Ts`** (2 nodes): `mac-system-theme.ts`, `isDarkMode()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `combineAbortSignals()`** (2 nodes): `abort-signals.ts`, `combineAbortSignals()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Clipboard Image Bmp Conversion Test`** (2 nodes): `clipboard-image-bmp-conversion.test.ts`, `createTinyBmp1x1Red24bpp()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Word Navigation Test Ts`** (2 nodes): `word-navigation.test.ts`, `isAtomic()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Rpc Client Process Exit Test`** (2 nodes): `rpc-client-process-exit.test.ts`, `writeChildScript()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Ctx Compact Context Compaction`** (2 nodes): `ctx.compact Context Compaction`, `Trigger Compaction Extension`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Edit Tool Legacy Input Test`** (2 nodes): `edit-tool-legacy-input.test.ts`, `createTempDir()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Skills Collision Second Calendar Skill`** (2 nodes): `Skills Collision First Calendar Skill`, `Skills Collision Second Calendar Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `3302 Find Path Glob Test`** (2 nodes): `3302-find-path-glob.test.ts`, `runFind()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Openai Responses Partial Json Cleanup`** (2 nodes): `openai-responses-partial-json-cleanup.test.ts`, `createOutput()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `IMAGE MODELS Data`** (2 nodes): `getImageModel`, `IMAGE_MODELS Data`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Open Browser Ts`** (2 nodes): `open-browser.ts`, `openBrowser()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Invalid YAML Frontmatter Skill Fixture`** (2 nodes): `Invalid YAML Frontmatter Skill Fixture`, `Missing Description Skill Fixture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Startup Session Name Test`** (2 nodes): `cli (core)`, `startup session name test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Clipboard BMP To PNG Conversion`** (2 nodes): `Clipboard BMP to PNG Conversion Tests`, `readClipboardImage util`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `mapKeyToDoom()`** (2 nodes): `doom-keys.ts`, `mapKeyToDoom()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `shortHash()`** (2 nodes): `hash.ts`, `shortHash()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `sanitizeSurrogates()`** (2 nodes): `sanitize-unicode.ts`, `sanitizeSurrogates()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Initial Message Test`** (2 nodes): `Build Initial Message`, `Build Initial Message Test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Openrouter Cache Write Repro Test`** (2 nodes): `openrouter-cache-write-repro.test.ts`, `createLongSystemPrompt()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `#5303 Bash Output Truncation`** (2 nodes): `#5208 late bash output`, `#5303 bash output truncation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `RpcClient Clone Tests`** (2 nodes): `RpcClient`, `RpcClient Clone Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `pirateExtension()`** (2 nodes): `pirate.ts`, `pirateExtension()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `getModelSearchText()`** (2 nodes): `model-search.ts`, `getModelSearchText()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Interactive Mode Startup Input Test`** (2 nodes): `interactive-mode-startup-input.test.ts`, `createSubmitContext()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Input Transform Streaming Example Test`** (2 nodes): `input-transform-streaming-example.test.ts`, `setup()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Interactive Mode Anthropic Warning Test`** (2 nodes): `interactive-mode-anthropic-warning.test.ts`, `createSettingsManager()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `2835 Tools Allowlist Filters Extension`** (2 nodes): `2835-tools-allowlist-filters-extension-tools.test.ts`, `createSession()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Anthropic 'no Low Surrogate' JSON`** (2 nodes): `Anthropic 'no low surrogate' JSON error`, `testUnpairedHighSurrogate 0xD83D`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Unique Fallback Message IDs (msg`** (2 nodes): `Unique fallback message IDs (msg_pi_1) for multi-block turns`, `OpenAI Responses Message ID Conversion Test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Interactive Mode Suspend Test Ts`** (2 nodes): `interactive-mode-suspend.test.ts`, `callHandleCtrlZ()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `2753 Reload Stale Resource Settings`** (2 nodes): `2753-reload-stale-resource-settings.test.ts`, `createRuntime()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bug Regression Isimageline Startswith Bug`** (2 nodes): `bug-regression-isimageline-startswith-bug.test.ts`, `oldIsImageLine()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Providers Openai Responses Shared Ts`** (2 nodes): `OpenAI Responses Foreign ToolCall ID`, `src/providers/openai-responses-shared.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `RPC JSONL Framing Test`** (2 nodes): `RPC JSONL Line Reader`, `RPC JSONL Framing Test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Question Ts`** (2 nodes): `question.ts`, `question()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Path Utils expandPath resolveReadPath Test`** (2 nodes): `path-utils (core)`, `path-utils expandPath/resolveReadPath test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `runPrintMode()`** (2 nodes): `print-mode.ts`, `runPrintMode()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Compaction Summary Reasoning Test Ts`** (2 nodes): `compaction-summary-reasoning.test.ts`, `createModel()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `isResizeImageWorkerRequest()`** (2 nodes): `image-resize-worker.ts`, `isResizeImageWorkerRequest()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Hidden Thinking Label Ts`** (2 nodes): `hidden-thinking-label.ts`, `applyLabel()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Vertex ADC Fallback For Placeholder`** (2 nodes): `Google Vertex API Key Resolution Test`, `Vertex ADC fallback for placeholder API keys`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `runRpcMode()`** (2 nodes): `rpc-mode.ts`, `runRpcMode()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Typebox Helpers Ts`** (2 nodes): `typebox-helpers.ts`, `StringEnum()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Image Convert Ts`** (2 nodes): `image-convert.ts`, `convertToPng()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createFindTool`** (2 nodes): `createFindTool`, `createGrepTool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Simple Ts`** (2 nodes): `simple.ts`, `source()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Anthropic Adaptive Thinking Models Test`** (2 nodes): `anthropic-adaptive-thinking-models.test.ts`, `getAllModels()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `areExperimentalFeaturesEnabled()`** (2 nodes): `experimental.ts`, `areExperimentalFeaturesEnabled()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `normalizeChangelogLinks Test`** (2 nodes): `changelog utils (core)`, `normalizeChangelogLinks test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `OpenRouter Cache Write Tokens Regression`** (2 nodes): `prompt_cache_key / session-affinity headers`, `OpenRouter cache_write_tokens regression E2E`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Extensions Input Event Test Ts`** (2 nodes): `extensions-input-event.test.ts`, `createRunner()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Prompt Template Argument Substitution Test`** (2 nodes): `Prompt Templates Module`, `Prompt Template Argument Substitution Test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `buildInitialMessage()`** (2 nodes): `initial-message.ts`, `buildInitialMessage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `headersToRecord()`** (2 nodes): `headers.ts`, `headersToRecord()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `FooterDataProvider Reftable Branch Detection Test`** (2 nodes): `FooterDataProvider (core)`, `FooterDataProvider reftable branch detection test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `toolsExtension()`** (2 nodes): `tools.ts`, `toolsExtension()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `GitHub Issue Autocomplete Extension`** (2 nodes): `GitHub Issue Autocomplete Extension`, `Provider Payload Logger Extension`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `commandsExtension()`** (2 nodes): `commands.ts`, `commandsExtension()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Multiline Description Skill Fixture`** (2 nodes): `Multiline Description Skill Fixture`, `Name Mismatch Skill Fixture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `clampOpenAIPromptCacheKey()`** (2 nodes): `openai-prompt-cache.ts`, `clampOpenAIPromptCacheKey()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `triggerCompaction()`** (2 nodes): `trigger-compact.ts`, `triggerCompaction()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Calculate Ts`** (2 nodes): `calculate.ts`, `calculate()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `#5661 Uppercase Header Values`** (2 nodes): `#5596 missing theme export`, `#5661 uppercase header values`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createToolCallWithPlainSchema()`** (2 nodes): `validation.test.ts`, `createToolCallWithPlainSchema()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Reload Runtime Ts`** (2 nodes): `reload-runtime.ts`, `execute()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Keybindings Migration Test Ts`** (2 nodes): `keybindings-migration.test.ts`, `createAgentDir()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Image Processing Test Ts`** (2 nodes): `image-processing.test.ts`, `imageBytes()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Regression Overlay Cjk Boundary Test`** (2 nodes): `regression-overlay-cjk-boundary.test.ts`, `compositeLineAt()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `truncateToVisualLines()`** (2 nodes): `visual-truncate.ts`, `truncateToVisualLines()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Initial Message Test Ts`** (2 nodes): `initial-message.test.ts`, `createArgs()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Root Skill Preferred Fixture`** (2 nodes): `Nested Child Skill Fixture`, `Root Skill Preferred Fixture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createEventBus()`** (2 nodes): `event-bus.ts`, `createEventBus()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `encodeSessionDir()`** (2 nodes): `cost.ts`, `encodeSessionDir()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Generate Test Image Script`** (2 nodes): `generate-test-image Script`, `Red Circle Test Image`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `loadClipboardNative()`** (2 nodes): `clipboard-native.ts`, `loadClipboardNative()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Pi User Agent Ts`** (2 nodes): `pi-user-agent.ts`, `getPiUserAgent()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Test Ts`** (2 nodes): `test.ts`, `main()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `3592 No Builtin Tools Keeps`** (2 nodes): `3592-no-builtin-tools-keeps-extension-tools.test.ts`, `createSession()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Box Container Component`** (1 nodes): `Box container component`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Pi Test Ps1`** (1 nodes): `pi-test.ps1`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Sync Versions Js`** (1 nodes): `sync-versions.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Browser Smoke Entry Ts`** (1 nodes): `browser-smoke-entry.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Manager Ssh Test Ts`** (1 nodes): `package-manager-ssh.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Path Utils Test Ts`** (1 nodes): `path-utils.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Theme Detection Test Ts`** (1 nodes): `theme-detection.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Changelog Test Ts`** (1 nodes): `changelog.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Interactive Mode Compaction Test Ts`** (1 nodes): `interactive-mode-compaction.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Agent Session Dynamic Tools Test`** (1 nodes): `agent-session-dynamic-tools.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Model Resolver Test Ts`** (1 nodes): `model-resolver.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Interactive Mode Import Command Test`** (1 nodes): `interactive-mode-import-command.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Export Html Whitespace Test Ts`** (1 nodes): `export-html-whitespace.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Settings Manager Test Ts`** (1 nodes): `settings-manager.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Pi User Agent Test Ts`** (1 nodes): `pi-user-agent.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Sdk Skills Test Ts`** (1 nodes): `sdk-skills.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Image Resize Callers Test Ts`** (1 nodes): `image-resize-callers.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Syntax Highlight Test Ts`** (1 nodes): `syntax-highlight.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Plan Mode Utils Test Ts`** (1 nodes): `plan-mode-utils.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Git Ssh Url Test Ts`** (1 nodes): `git-ssh-url.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Trust Selector Test Ts`** (1 nodes): `trust-selector.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Rpc Client Clone Test Ts`** (1 nodes): `rpc-client-clone.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Trust Manager Test Ts`** (1 nodes): `trust-manager.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Http Dispatcher Test Ts`** (1 nodes): `http-dispatcher.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `First Time Setup Test Ts`** (1 nodes): `first-time-setup.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Frontmatter Test Ts`** (1 nodes): `frontmatter.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Rpc Test Ts`** (1 nodes): `rpc.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Resource Loader Test Ts`** (1 nodes): `resource-loader.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Restore Sandbox Env Test Ts`** (1 nodes): `restore-sandbox-env.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Theme Export Test Ts`** (1 nodes): `theme-export.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Theme Picker Test Ts`** (1 nodes): `theme-picker.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Test Harness Test Ts`** (1 nodes): `test-harness.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Sdk Session Manager Test Ts`** (1 nodes): `sdk-session-manager.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Compaction Serialization Test Ts`** (1 nodes): `compaction-serialization.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Export Html Skill Block Test`** (1 nodes): `export-html-skill-block.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Clipboard Native Test Ts`** (1 nodes): `clipboard-native.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `User Message Test Ts`** (1 nodes): `user-message.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Experimental Test Ts`** (1 nodes): `experimental.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Settings Manager Bug Test Ts`** (1 nodes): `settings-manager-bug.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Truncate To Width Test Ts`** (1 nodes): `truncate-to-width.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Rpc Jsonl Test Ts`** (1 nodes): `rpc-jsonl.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Custom Session Id Test Ts`** (1 nodes): `custom-session-id.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Save Entry Test Ts`** (1 nodes): `save-entry.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `5303 Bash Output Truncation Test`** (1 nodes): `5303-bash-output-truncation.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `2791 Fswatch Error Crash Test`** (1 nodes): `2791-fswatch-error-crash.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `3616 Settings Inmemory Reload Test`** (1 nodes): `3616-settings-inmemory-reload.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `File Trigger Ts`** (1 nodes): `file-trigger.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Message Renderer Ts`** (1 nodes): `message-renderer.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Model Status Ts`** (1 nodes): `model-status.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Timed Confirm Ts`** (1 nodes): `timed-confirm.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Input Transform Ts`** (1 nodes): `input-transform.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Inline Bash Ts`** (1 nodes): `inline-bash.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Working Message Test Ts`** (1 nodes): `working-message-test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Custom Compaction Ts`** (1 nodes): `custom-compaction.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `System Prompt Header Ts`** (1 nodes): `system-prompt-header.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bookmark Ts`** (1 nodes): `bookmark.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Rpc Demo Ts`** (1 nodes): `rpc-demo.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Input Transform Streaming Ts`** (1 nodes): `input-transform-streaming.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Qna Ts`** (1 nodes): `qna.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Provider Payload Ts`** (1 nodes): `provider-payload.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Send User Message Ts`** (1 nodes): `send-user-message.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Protected Paths Ts`** (1 nodes): `protected-paths.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Confirm Destructive Ts`** (1 nodes): `confirm-destructive.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Permission Gate Ts`** (1 nodes): `permission-gate.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Session Name Ts`** (1 nodes): `session-name.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Git Checkpoint Ts`** (1 nodes): `git-checkpoint.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Auto Commit On Exit Ts`** (1 nodes): `auto-commit-on-exit.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Structured Output Ts`** (1 nodes): `structured-output.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Status Line Ts`** (1 nodes): `status-line.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bash Spawn Hook Ts`** (1 nodes): `bash-spawn-hook.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Hello Ts`** (1 nodes): `hello.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `09 Api Keys And Oauth`** (1 nodes): `09-api-keys-and-oauth.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `02 Custom Model Ts`** (1 nodes): `02-custom-model.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `06 Extensions Ts`** (1 nodes): `06-extensions.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `05 Tools Ts`** (1 nodes): `05-tools.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `10 Settings Ts`** (1 nodes): `10-settings.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `11 Sessions Ts`** (1 nodes): `11-sessions.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `04 Skills Ts`** (1 nodes): `04-skills.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `01 Minimal Ts`** (1 nodes): `01-minimal.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `07 Context Files Ts`** (1 nodes): `07-context-files.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `12 Full Control Ts`** (1 nodes): `12-full-control.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `08 Prompt Templates Ts`** (1 nodes): `08-prompt-templates.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `03 Custom Prompt Ts`** (1 nodes): `03-custom-prompt.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Defaults Ts`** (1 nodes): `defaults.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Slash Commands Ts`** (1 nodes): `slash-commands.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Provider Display Names Ts`** (1 nodes): `provider-display-names.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Rpc Types Ts`** (1 nodes): `rpc-types.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Image Test Ts`** (1 nodes): `image-test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Wrap Ansi Test Ts`** (1 nodes): `wrap-ansi.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Regression Regional Indicator Width Test`** (1 nodes): `regression-regional-indicator-width.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Chat Simple Ts`** (1 nodes): `chat-simple.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Editor Component Ts`** (1 nodes): `editor-component.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Nodejs Env Test Ts`** (1 nodes): `nodejs-env.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Resource Formatting Test Ts`** (1 nodes): `resource-formatting.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Node Ts`** (1 nodes): `node.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bedrock Provider D Ts`** (1 nodes): `bedrock-provider.d.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Together Models Test Ts`** (1 nodes): `together-models.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Openai Responses Reasoning Replay E2e`** (1 nodes): `openai-responses-reasoning-replay-e2e.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Zen Test Ts`** (1 nodes): `zen.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bedrock Models Test Ts`** (1 nodes): `bedrock-models.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Openai Responses Message Id Test`** (1 nodes): `openai-responses-message-id.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Openai Codex Cache Affinity E2e`** (1 nodes): `openai-codex-cache-affinity-e2e.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Anthropic Tool Name Normalization Test`** (1 nodes): `anthropic-tool-name-normalization.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Openai Responses Foreign Toolcall Id`** (1 nodes): `openai-responses-foreign-toolcall-id.test.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Generate Test Image Ts`** (1 nodes): `generate-test-image.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Result Type (ok Err)`** (1 nodes): `Result type (ok/err)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `PromptTemplate Interface`** (1 nodes): `PromptTemplate interface`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `AgentHarnessResources Interface`** (1 nodes): `AgentHarnessResources interface`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `CompactionError Class`** (1 nodes): `CompactionError class`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `BranchSummaryError Class`** (1 nodes): `BranchSummaryError class`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `FileError Class`** (1 nodes): `FileError class`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `agentLoop Tests`** (1 nodes): `agentLoop tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `StreamOptions Interface`** (1 nodes): `StreamOptions Interface`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `AssistantMessage`** (1 nodes): `AssistantMessage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createClient (Vertex ADC)`** (1 nodes): `createClient (Vertex ADC)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `isCloudflareProvider`** (1 nodes): `isCloudflareProvider`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `combineAbortSignals`** (1 nodes): `combineAbortSignals`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createAssistantMessageDiagnostic`** (1 nodes): `createAssistantMessageDiagnostic`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `OAuthLoginCallbacks`** (1 nodes): `OAuthLoginCallbacks`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Together Models (Kimi K2 6,`** (1 nodes): `Together models (Kimi K2.6, gpt-oss) registration`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bedrock convertMessages Unknown Content Handling`** (1 nodes): `Bedrock convertMessages unknown-content handling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `handleStreaming Text Helper`** (1 nodes): `handleStreaming text helper`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Bash Spawn Hook Extension (createBashTool`** (1 nodes): `Bash Spawn Hook Extension (createBashTool spawnHook)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `configureHttpDispatcher (undici Global Dispatcher +`** (1 nodes): `configureHttpDispatcher (undici global dispatcher + proxy)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `parseSkillBlock`** (1 nodes): `parseSkillBlock`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createToolDefinitionFromAgentTool`** (1 nodes): `createToolDefinitionFromAgentTool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `stripJsonComments`** (1 nodes): `stripJsonComments`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `formatDimensionNote`** (1 nodes): `formatDimensionNote`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `killProcessTree`** (1 nodes): `killProcessTree`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `sanitizeBinaryOutput`** (1 nodes): `sanitizeBinaryOutput`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `warnDeprecation`** (1 nodes): `warnDeprecation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `supportsLanguage`** (1 nodes): `supportsLanguage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `AuthStorage (617)`** (1 nodes): `AuthStorage`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `initTheme`** (1 nodes): `initTheme`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `restoreSandboxEnv (bun Sandbox Env Restorer)`** (1 nodes): `restoreSandboxEnv (bun sandbox env restorer)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createWriteTool`** (1 nodes): `createWriteTool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `createLsTool`** (1 nodes): `createLsTool`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Disable Model Invocation Skill Fixture`** (1 nodes): `Disable Model Invocation Skill Fixture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Nested Child Skill Fixture`** (1 nodes): `Nested Child Skill Fixture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `FuzzyMatch Interface`** (1 nodes): `FuzzyMatch interface`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `SelectList Test`** (1 nodes): `SelectList Test`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `isContextOverflow (multi-provider patterns)` and `enableAllGitHubCopilotModels (policy acceptance)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `OAuthCredentials` and `reasoning replay cross-provider handoff`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `red-circle.png (vision test fixture)` and `Context overflow handling`?**
  _Edge tagged AMBIGUOUS (relation: shares_data_with) - confidence is low._
- **What is the exact relationship between `Pi Terminal Coding Harness` and `Exy Pufferfish Illustration`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `GitHub Issue Autocomplete Extension` and `Provider Payload Logger Extension`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Shutdown Command Extension` and `Confirm Destructive Actions Extension`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `buildSystemPrompt (tools/guidelines/context/skills assembly)` and `isInstallTelemetryEnabled (PI_TELEMETRY gate)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._