# Graph Report - hermes-agent  (2026-04-11)

## Corpus Check
- Large corpus: 1309 files · ~2,174,237 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 29368 nodes · 66153 edges · 755 communities detected
- Extraction: 60% EXTRACTED · 40% INFERRED · 0% AMBIGUOUS · INFERRED: 26500 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Platform` - 2488 edges
2. `PlatformConfig` - 2152 edges
3. `MessageEvent` - 1414 edges
4. `MessageType` - 1298 edges
5. `SendResult` - 1159 edges
6. `BasePlatformAdapter` - 1091 edges
7. `AIAgent` - 1021 edges
8. `GatewayConfig` - 879 edges
9. `SessionDB` - 761 edges
10. `SessionSource` - 754 edges

## Surprising Connections (you probably didn't know these)
- `Credential Pool Rotation` --conceptually_related_to--> `AIAgent Class`  [INFERRED]
  hermes-agent/RELEASE_v0.7.0.md → hermes-agent/run_agent.py
- `Model Tools Module` --references--> `Self-Registering Tools Pattern`  [INFERRED]
  hermes-agent/model_tools.py → hermes-agent/AGENTS.md
- `Landing Page JavaScript` --semantically_similar_to--> `Hermes CLI Main Entry Point`  [AMBIGUOUS] [semantically similar]
  hermes-agent/landingpage/script.js → hermes-agent/hermes_cli/main.py
- `TelegramAdapter` --extends--> `BasePlatformAdapter`  [INFERRED]
  hermes-agent/tests/e2e/conftest.py → gateway/platforms/base.py
- `Normalize tool_stats to include all possible tools with consistent schema.` --uses--> `AIAgent`  [INFERRED]
  hermes-agent/batch_runner.py → hermes-agent/run_agent.py

## Hyperedges (group relationships)
- **Core Agent Loop** — agents_AIAgent, agents_model_tools, agents_prompt_builder, agents_context_compressor, agents_tool_registry [INFERRED]
- **Tool Discovery Pipeline** — agents_model_tools, agents_tool_registry, agents_mcp_tool, agents_plugins, agents_Self_Registering_Tools [INFERRED]
- **Session Persistence Stack** — agents_hermes_state, agents_WAL_Mode, agents_FT5_Search, agents_hermes_constants, agents_gateway_runner [INFERRED]
- **API error recovery pipeline: classify error, compute jittered backoff, track rate limits** — error_classifier_failoverreason, retry_utils_jitteredbackoff, rate_limit_tracker_ratelimitstate [INFERRED 0.80]
- **Cron job execution pipeline: scheduler tick dispatches job, resolves model route, redacts script output** — cron_scheduler_tick, cron_jobs_cruddashboard, smart_model_routing_cheaprouting, redact_redactingformatter [EXTRACTED 0.90]
- **System prompt assembly: memory providers supply context blocks, prompt builder injects skills and context files** — memory_manager_memorymanager, memory_provider_memoryprovider, prompt_builder_skillsprompt [INFERRED 0.70]
- **HermesAgentBaseEnv orchestrates the full rollout pipeline by creating HermesAgentLoop for agent execution, then passing ToolContext to compute_reward for verification** —  [EXTRACTED 1.00]
- **TBLite is a thin subclass of TerminalBench2EvalEnv with calibrated difficulty; both share Docker-based sandbox verification and binary pass/fail scoring** —  [EXTRACTED 1.00]
- **Pricing accuracy pipeline: provider usage is normalized via CanonicalUsage, routed through BillingRoute for source resolution, estimated via PricingCatalog, and presented as CostResult with certainty metadata** —  [EXTRACTED 1.00]
- **shares_data_with** — base_base-blockchain-skill, solana_solana-blockchain-skill, coingecko_coingecko-api [INFERRED 0.80]
- **Distributed Training Strategies** — accelerate_HuggingFaceAccelerate, accelerate_DeepSpeed, accelerate_FSDP, accelerate_MegatronIntegration [EXTRACTED 1.00]
- **NeuroSkill BCI System** — neuroskill-bci_NeuroSkillBCI, neuroskill-bci_MetricsReference, neuroskill-bci_Protocols, neuroskill-bci_NeuroSkillAPI [EXTRACTED 1.00]
- **FastMCP Template Ecosystem** — fastmcp_FastMCPSkill, api_wrapper_ApiWrapperTemplate, database_server_DatabaseServerTemplate, file_processor_FileProcessorTemplate [EXTRACTED 1.00]
- **Flash Attention for GPU Training** — flash-attention_flash-attention, lambda-labs_lambda-labs-gpu, pytorch-lightning_pytorch-lightning [INFERRED 0.75]
- **RL Training with Atropos Agent Loop** — hermes-atropos-envs_hermes-agent-base-env, hermes-atropos-envs_atropos-base-env, hermes-atropos-envs_agent-result [EXTRACTED 0.90]
- **OSS Forensics Evidence Chain** — evidence-types_evidence-taxonomy, evidence-store_evidencesstore, forensic-report_template [EXTRACTED 0.90]
- **Hermes Memory Provider Plugin Ecosystem** — memory-plugins_discovery, byterover_memory-provider, hindsight_memory-provider, holographic_memory-provider [EXTRACTED 0.90]
- **Holographic Memory Subsystem** — holographic_memory-provider, holographic_memorystore, holographic_factretriever, holographic_hrr-module [EXTRACTED 0.95]
- **Memory Provider Plugin System** — honcho_memory_provider, mem0_memory_provider, openviking_memory_provider, retaindb_memory_provider, supermemory_memory_provider [EXTRACTED 1.00]
- **Honcho Plugin Internal Architecture** — honcho_memory_provider, honcho_client_config, honcho_session_manager, honcho_cli [EXTRACTED 1.00]
- **Apple macOS Skills Suite** — apple_skills_description, apple_notes_skill, apple_reminders_skill [EXTRACTED 1.00]
- **Autonomous Coding Agents Orchestrated by Hermes** — claude_code_skill, codex_skill, hermes_agent_skill, opencode_skill [EXTRACTED 0.90]
- **ASCII Video Cross-Referenced Reference System** — ascii_video_architecture, ascii_video_composition, ascii_video_effects, ascii_video_scenes, ascii_video_shaders, ascii_video_inputs, ascii_video_optimization, ascii_video_troubleshooting [EXTRACTED 0.95]
- **Creative Visualization Skills** — ascii_art_skill, ascii_video_skill, excalidraw_skill [EXTRACTED 0.90]
- **Manim Video Production Pipeline** — README_manim_video_pipeline, SKILL_manim_video_skill, rendering_cli_reference, rendering_ffmpeg_stitching [EXTRACTED 1.00]
- **p5.js Creative Coding System** — README_p5js_pipeline, SKILL_p5js_skill, p5js_animation_easing, p5js_color_systems_hsb [EXTRACTED 0.90]
- **p5.js Creative Coding Ecosystem** — p5js, p5js_webgl, p5js_particle_systems, p5js_perlin_noise, glsl_shaders, p5js_flow_fields, p5js_framebuffers [1.0]
- **p5.js Deterministic Export Pipeline** — p5js, puppeteer, ffmpeg, ccapture_js, fxhash, art_blocks, export_frames_script [1.0]
- **Warm Neutral Design Family (Claude + Notion)** — ds_claude, ds_notion, warm_neutral_palette, dark_light_alternation, font_inter [0.8]
- **Dark Background + Singular Accent Design Family (MongoDB + NVIDIA)** — ds_mongodb, ds_nvidia, color_forest_black, color_nvidia_green, dark_light_alternation, pill_button_pattern [0.75]
- **Hermes Agent Design Template System** — hermes_agent, popular_web_designs_skill, design_template, font_substitution_cdn, color_google_fonts, generative_widgets_skill, browser_vision_skill [0.85]
- **p5.js Creative Coding Ecosystem** — p5js, p5js_webgl, p5js_particle_systems, p5js_perlin_noise, glsl_shaders, p5js_flow_fields, p5js_framebuffers [1.0]
- **p5.js Deterministic Export Pipeline** — p5js, puppeteer, ffmpeg, ccapture_js, fxhash, art_blocks, export_frames_script [1.0]
- **Warm Neutral Design Family (Claude + Notion)** — ds_claude, ds_notion, warm_neutral_palette, dark_light_alternation, font_inter [0.8]
- **Dark Background + Singular Accent Design Family (MongoDB + NVIDIA)** — ds_mongodb, ds_nvidia, color_forest_black, color_nvidia_green, dark_light_alternation, pill_button_pattern [0.75]
- **Hermes Agent Design Template System** — hermes_agent, popular_web_designs_skill, design_template, font_substitution_cdn, color_google_fonts, generative_widgets_skill, browser_vision_skill [0.85]
- **he:dark-developer-design-systems** — design-system:resend, design-system:vercel, design-system:warp, design-system:voltagent, design-system:xai [INFERRED 0.80]
- **he:cinematic-photography-design-systems** — design-system:spacex, design-system:runwayml [INFERRED 0.85]
- **he:fintech-design-systems** — design-system:uber, design-system:revolut, design-system:wise, design-system:stripe [INFERRED 0.70]
- **he:github-skill-ecosystem** — skill:github-auth, skill:github-code-review, skill:github-issues, skill:codebase-inspection [INFERRED 1.00]
- **he:dogfood-qa-system** — skill:dogfood, ref:issue-taxonomy, template:dogfood-report [INFERRED 1.00]
- **he:dark-developer-design-systems** — design-system:resend, design-system:vercel, design-system:warp, design-system:voltagent, design-system:xai [INFERRED 0.80]
- **he:cinematic-photography-design-systems** — design-system:spacex, design-system:runwayml [INFERRED 0.85]
- **he:fintech-design-systems** — design-system:uber, design-system:revolut, design-system:wise, design-system:stripe [INFERRED 0.70]
- **he:github-skill-ecosystem** — skill:github-auth, skill:github-code-review, skill:github-issues, skill:codebase-inspection [INFERRED 1.00]
- **he:dogfood-qa-system** — skill:dogfood, ref:issue-taxonomy, template:dogfood-report [INFERRED 1.00]
- **he:github-workflow-ecosystem** — skill:github-pr-workflow, skill:github-repo-management, tool:gh-cli, api:github-rest, ref:github-api-cheatsheet [INFERRED]
- **he:mcp-integration** — skill:mcporter, skill:native-mcp, concept:mcp [INFERRED]
- **he:youtube-content-pipeline** — skill:youtube-content, script:fetch_transcript.py, ref:output-formats, api:youtube-transcript [INFERRED]
- **he:llm-evaluation-toolchain** — skill:lm-evaluation-harness, tool:lm-eval, ref:benchmark-guide, ref:api-evaluation, ref:distributed-eval, ref:custom-tasks [INFERRED]
- **he:wb-mlops-platform** — skill:weights-and-biases, tool:wandb, ref:artifacts, ref:integrations, ref:sweeps [INFERRED]
- **he:github-workflow-ecosystem** — skill:github-pr-workflow, skill:github-repo-management, tool:gh-cli, api:github-rest, ref:github-api-cheatsheet [INFERRED]
- **he:mcp-integration** — skill:mcporter, skill:native-mcp, concept:mcp [INFERRED]
- **he:youtube-content-pipeline** — skill:youtube-content, script:fetch_transcript.py, ref:output-formats, api:youtube-transcript [INFERRED]
- **he:llm-evaluation-toolchain** — skill:lm-evaluation-harness, tool:lm-eval, ref:benchmark-guide, ref:api-evaluation, ref:distributed-eval, ref:custom-tasks [INFERRED]
- **he:wb-mlops-platform** — skill:weights-and-biases, tool:wandb, ref:artifacts, ref:integrations, ref:sweeps [INFERRED]
- **H:1** — E:llama_cpp, E:vllm, E:outlines [INFERRED 0.85]
- **H:2** — E:obliteratus, E:vllm, E:llama_cpp [INFERRED 0.90]
- **H:3** — E:gguf_q4km, E:gguf_q5km, E:gguf_q6k, E:gguf_q8_0 [INFERRED 0.95]
- **H_grounded_sam_pipeline** — E_GroundingDINO, E_SAM [1.0]
- **H_sd_training_stack** — E_StableDiffusion, E_LoRA, E_Diffusers [1.0]
- **H_axolotl_rlhf_stack** — E_Axolotl, E_TRL, E_GRPO [1.0]
- **H_dspy_optimization_loop** — E_DSPy_Module, E_DSPy_Optimizer, E_DSPy_Signature [1.0]
- **H_fsdp_qlora_pipeline** — E_FSDP, E_LoRA, E_Axolotl [1.0]
- **H_whisper_deployment_stack** — E_Whisper, E_faster_whisper, E_LangChain [0.9]
- **he1-quantization-ecosystem** — gguf-format, awq-quantization, gptq-quantization, quantization [INFERRED]
- **he2-inference-serving-ecosystem** — llama-cpp-skill, vllm-skill, outlines-skill, openai-compatible-api, structured-generation [INFERRED]
- **he3-vllm-performance-optimization** — paged-attention, continuous-batching, prefix-caching, speculative-decoding, vllm-optimization [INFERRED]
- **he_mlops_ecosystem** — clip, sam, stable_diffusion, whisper, axolotl, dspy, grpo_rl_training [1.0]
- **he_lora_ecosystem** — axolotl_lora, sd_lora, lora_peft, peft, grpo_rl_training [1.0]
- **he_rlhf_training** — axolotl, grpo_rl_training, trl, rlhf, axolotl_grpo_trainer, axolotl_dpo_trainer, reward_functions [0.9]
- **he_rlhf_pipeline** — RLHF, SFT, Reward_Model, PPO [EXTRACTED 1.00]
- **he_peft_methods** — LoRA, QLoRA, DoRA, AdaLoRA, LoftQ [EXTRACTED 1.00]
- **he_trl_methods** — TRL, SFT, DPO, PPO, GRPO [EXTRACTED 1.00]
- **google_workspace_pipeline** — google_api_py, gws_bridge_py, gws_cli [INFERRED]
- **pptx_editing_workflow** — add_slide_py, clean_py, pack_py [INFERRED]
- **pdf_extraction_decision_tree** — pymupdf, marker_pdf, extract_pymupdf_py, extract_marker_py [INFERRED]
- **godmode_attack_modes** — godmode_skill, jailbreak_templates, parseltongue, godmode_race, auto_jailbreak [EXTRACTED 1.00]
- **research_paper_pipeline_phases** — research_paper_writing_skill, autoreason_methodology, conference_checklists, citation_workflow, experiment_patterns, arxiv_skill [EXTRACTED 1.00]
- **polymarket_data_access_stack** — polymarket_skill, polymarket_api_endpoints, polymarket_script, polymarket_gamma_api, polymarket_clob_api, polymarket_data_api [EXTRACTED 1.00]
- **he-1** — plan-skill, subagent-driven-development-skill, requesting-code-review-skill [INFERRED 0.80]
- **he-2** — writing-guide, reviewer-guidelines, human-evaluation, paper-types, templates-readme [EXTRACTED 1.00]
- **he-3** — aaai2026-readme, acl-readme, acl-formatting, colm2025-readme, templates-readme [EXTRACTED 1.00]
- **he_skill_ecosystem** — systematic-debugging, test-driven-development, writing-plans, subagent-driven-development [EXTRACTED 1.00]
- **he_model_context_management** — ctx_halving_fix_test, ollama_num_ctx_test, model_metadata_module, anthropic_adapter [EXTRACTED 0.90]
- **he_hermes_infrastructure** — hermes_state_test, hermes_logging_test, mcp_serve_test, conftest, SessionDB, EventBridge [INFERRED 0.80]
- **he_acp_adapter_subsystem** — acp_adapter_server, acp_adapter_session, acp_adapter_events, acp_adapter_tools, acp_adapter_auth, acp_adapter_permissions, acp_adapter_entry [EXTRACTED 1.00]
- **he_auxiliary_client_resolution_chain** — agent_auxiliary_client, agent_anthropic_adapter, hermes_cli_config, hermes_cli_runtime_provider, tools_vision_tools [INFERRED 0.80]
- **he_compression_subsystem** — TrajectoryCompressor, CompressionConfig, TrajectoryMetrics, AggregateMetrics, ContextCompressor [INFERRED 0.70]
- **he_memory_system** — agent.memory_provider, agent.memory_manager, agent.builtin_memory_provider, plugins.memory.mem0, plugins.memory.honcho [INFERRED]
- **he_model_context_resolution** — agent.model_metadata, agent.models_dev, agent.anthropic_adapter [INFERRED]
- **he_prompt_assembly** — agent.prompt_builder, agent.prompt_caching, agent.skill_commands, agent.skill_utils, tools.skills_tool [INFERRED]
- **he_cli_session_lifecycle** — branch_command, new_session_command, SessionDB, HermesCLI, retry_command [INFERRED]
- **he_provider_resolution_flow** — provider_resolution, resolve_runtime_provider, openai-codex_provider, nous_provider, smart_model_routing, HermesCLI [INFERRED]
- **he_tui_rendering_pipeline** — tui_extension_hooks, approval_ui, background_tui_refresh, loading_indicator, low_context_warning, HermesCLI [INFERRED]
- **cli_cron_e2e_pipeline** — HermesCLI, AIAgent, GatewayRunner, cron_scheduler, cron_jobs, TelegramAdapter [EXTRACTED 1.00]
- **reasoning_display_pipeline** — AIAgent, reasoning_extraction, reasoning_command, HermesCLI [EXTRACTED 1.00]
- **cron_delivery_pipeline** — cron_scheduler, cron_jobs, send_message_tool, SessionDB, skills_tool, runtime_provider [EXTRACTED 1.00]
- **Gateway Integration Test Suite** — agent_cache_tests, allowlist_startup_check_tests, api_server_tests, api_server_jobs_tests, api_server_toolset_tests, approve_deny_command_tests, async_memory_flush_tests, background_command_tests, background_process_notifications_tests, base_topic_sessions_tests, bluebubbles_tests, channel_directory_tests, command_bypass_tests, config_tests, config_cwd_bridge_tests, delivery_tests, dingtalk_tests, discord_bot_filter_tests [EXTRACTED 1.00]
- **Platform Adapter Subsystem** — api_server_adapter, bluebubbles_adapter, dingtalk_adapter, base_platform_adapter, gateway_run, gateway_config [EXTRACTED 1.00]
- **Session Lifecycle and Command Approval Flow** — gateway_session, tools_approval, gateway_run, base_platform_adapter, command_bypass_tests, approve_deny_command_tests [INFERRED 0.80]
- **Discord gateway adapter test suite** — test_discord_channel_controls, test_discord_connect, test_discord_document_handling, test_discord_free_response, test_discord_imports, test_discord_media_metadata, test_discord_opus, test_discord_reactions, test_discord_reply_mode, test_discord_send, test_discord_slash_commands, test_discord_system_messages, test_discord_thread_persistence [EXTRACTED 1.00]
- **Multi-platform gateway adapter system** — DiscordAdapter, TelegramAdapter, FeishuAdapter, EmailAdapter, BasePlatformAdapter, PlatformConfig, MessageEvent, MessageType, SessionSource, GatewayRunner [EXTRACTED 0.90]
- **Gateway lifecycle and runner tests** — test_flush_memory_stale_guard, test_gateway_inactivity_timeout, test_gateway_shutdown, GatewayRunner [EXTRACTED 1.00]
- **Matrix E2EE End-to-End Encryption Flow** — test_matrix, gateway_platforms_matrix, gateway_config [INFERRED]
- **Platform Adapter Lifecycle: Connect, Message, Reconnect, Send** — test_platform_reconnect, test_platform_base, test_queue_consumption, test_interrupt_key_match, gateway_run, gateway_platforms_base [INFERRED]
- **Gateway Slash Command Handler Suite** — test_plan_command, test_reasoning_command, test_resume_command, test_retry_replacement, test_retry_response, gateway_run [INFERRED]
- **he_platform_adapter_hierarchy** — base_platform_adapter, telegram_adapter, discord_adapter, slack_adapter, signal_adapter, sms_adapter, api_server_adapter [EXTRACTED 1.00]
- **he_session_lifecycle** — session_source, session_store, session_entry, build_session_key, session_reset_policy, session_db, plugin_hooks [EXTRACTED 1.00]
- **he_message_processing_pipeline** — gateway_runner, message_event, agent_pending_sentinel, base_platform_adapter, send_with_retry, session_store, model_metadata [EXTRACTED 1.00]
- **he_telegram_adapter_test_suite** — test_telegram_approval_buttons, test_telegram_caption_merge, test_telegram_conflict, test_telegram_documents, test_telegram_format, test_telegram_group_gating, test_telegram_photo_interrupts, test_telegram_reactions, test_telegram_reply_mode, test_telegram_text_batching, test_telegram_thread_fallback [EXTRACTED 1.00]
- **he_gateway_runner_test_suite** — test_step_callback_compat, test_telegram_photo_interrupts, test_title_command, test_transcript_offset, test_unauthorized_dm_behavior, test_unknown_command, test_update_command [EXTRACTED 1.00]
- **he_network_resilience_tests** — test_telegram_network, test_telegram_network_reconnect, test_telegram_conflict, test_telegram_thread_fallback [INFERRED 0.80]
- **he_gateway_platform_test_suite** — gateway_update_streaming, gateway_verbose_command, gateway_voice_command, gateway_webhook_adapter, gateway_webhook_dynamic_routes, gateway_webhook_integration, gateway_wecom, gateway_whatsapp_connect, gateway_whatsapp_group_gating, gateway_whatsapp_reply_prefix, gateway_ws_auth_retry [EXTRACTED 1.00]
- **he_hermes_cli_auth_test_suite** — hermes_cli_anthropic_oauth, hermes_cli_anthropic_persistence, hermes_cli_auth_codex, hermes_cli_auth_commands, hermes_cli_auth_nous, hermes_cli_auth_qwen [EXTRACTED 1.00]
- **he_multi_provider_auth_system** — hermes_cli_auth, hermes_cli_auth_commands_mod, credential_pool, hermes_cli_runtime_provider, hermes_cli_api_key_providers, hermes_cli_auth_codex, hermes_cli_auth_nous, hermes_cli_auth_qwen [EXTRACTED 0.90]
- **he_gateway_testing_cluster** — test_gateway, test_gateway_linger, test_gateway_runtime_health, test_gateway_service, hermes_cli_gateway [INFERRED]
- **he_config_testing_cluster** — test_config, test_config_env_expansion, test_config_validation, hermes_cli_config [INFERRED]
- **he_provider_model_testing_cluster** — test_codex_models, test_copilot_auth, test_gemini_provider, hermes_cli_auth, hermes_cli_models, hermes_cli_codex_models, hermes_cli_copilot_auth, hermes_cli_model_normalize [INFERRED]
- **he_model_provider_resolution_pipeline** — hermes_cli_main, hermes_cli_model_switch, hermes_cli_models, hermes_cli_runtime_provider, hermes_cli_auth, hermes_cli_config [EXTRACTED 1.00]
- **he_plugin_lifecycle_management** — hermes_cli_plugins, hermes_cli_plugins_cmd, plugins_memory, tools_registry, model_tools [EXTRACTED 1.00]
- **he_mcp_server_configuration_flow** — hermes_cli_mcp_config, hermes_cli_tools_config, tools_mcp_tool, hermes_cli_curses_ui, hermes_cli_config [EXTRACTED 1.00]
- **Setup Wizard Flow** —  [INFERRED]
- **Skills Management Tests** —  [INFERRED]
- **Update and Gateway Restart** —  [INFERRED]
- **he_memory_providers** — RetainDBMemoryProvider, HindsightMemoryProvider, Mem0MemoryProvider, SupermemoryMemoryProvider, HonchoMemoryProvider [INFERRED 0.80]
- **he_terminal_backends** — test_daytona_terminal, test_modal_terminal, terminal_tool [EXTRACTED 1.00]
- **he_context_overflow_handling** — test_1630_context_overflow_loop, test_413_compression, AIAgent, context_compressor [EXTRACTED 1.00]
- **he_fallback_compression_persistence** — AIAgent, provider_fallback, ContextCompressor, primary_runtime_restore [EXTRACTED 1.00]
- **he_compression_session_split_gateway** — context_compression, session_persistence, SessionDB, GatewayRunner [EXTRACTED 1.00]
- **he_anthropic_error_compression_fallback** — anthropic_error_handling, context_compression, provider_fallback, long_context_tier_429 [EXTRACTED 1.00]
- **he_multi_provider_api_parity** — test_provider_parity, test_strict_api_validation, test_run_agent_codex_responses, run_agent_module [EXTRACTED 1.00]
- **he_google_workspace_integration** — test_google_oauth_setup, test_google_workspace_api, google_oauth_setup_script, gws_bridge_script, google_api_script [EXTRACTED 1.00]
- **he_flashcard_quiz_pipeline** — test_memento_cards, test_youtube_quiz, memento_cards_script, youtube_quiz_script [EXTRACTED 1.00]
- **he_browser_tool_ecosystem** — browser_tool, camofox, cdp_override, ssrf_protection, cloud_provider, agent_browser, browser_console, browser_cleanup, browser_content_none_guard, homebrew_paths [EXTRACTED 1.00]
- **he_security_pipeline** — command_guards, tirith_security, approval_module, cron_prompt_injection, cronjob_tools, env_passthrough [EXTRACTED 1.00]
- **he_environment_backends** — docker_environment, docker_find, daytona_environment, daytona_sdk, environments_base, local_environment, code_execution_tool, hermes_tools [EXTRACTED 1.00]
- **he_file_safety_subsystem** — test_file_operations, test_file_read_guards, test_file_staleness, test_file_write_safety, test_file_tools, test_file_tools_live [INFERRED 0.90]
- **he_managed_infrastructure_tests** — test_managed_browserbase_and_modal, test_managed_media_gateways, test_managed_modal_environment, test_managed_tool_gateway, test_local_env_blocklist [INFERRED 0.85]
- **he_mcp_integration_tests** — test_mcp_dynamic_discovery, test_mcp_oauth, test_mcp_probe, test_managed_server_tool_support [INFERRED 0.85]
- **he_mcp_tool_testing_ecosystem** — test_mcp_stability, test_mcp_structured_content, test_mcp_tool, test_mcp_tool_issue_948 [EXTRACTED 1.00]
- **he_modal_environment_testing** — test_modal_sandbox_fixes, test_modal_snapshot_isolation, modal_environment_module, modal_sdk [EXTRACTED 1.00]
- **he_send_message_multi_platform** — test_send_message_tool, test_send_message_missing_platforms, send_message_tool_module, telegram_api, gateway_platform [EXTRACTED 1.00]
- **skill_lifecycle** — skills_sync, skill_manager_tool, skills_tool, skills_guard, skills_hub [INFERRED 0.80]
- **terminal_execution_backends** — terminal_tool, local_environment, ssh_environment, tirith_security, process_registry [INFERRED 0.80]
- **path_security_defense_in_depth** — path_traversal_prevention, symlink_prefix_confusion, security_scanning [INFERRED 0.80]
- **he_voice_pipeline** — test_voice_cli_integration, test_voice_mode, cli_module, voice_mode_module, transcription_tools_module, tts_tool_module [EXTRACTED 1.00]
- **he_web_security_stack** — browser_tool, url_safety_module, website_policy_module, browser_camofox, browser_camofox_state [EXTRACTED 1.00]
- **he_command_approval_system** — approval, ansi_strip, tirith_security_module, terminal_tool_module [EXTRACTED 1.00]
- **Hermes Tool Registration Pattern** — clarify_tool, cronjob_tools, code_execution_tool, delegate_tool, file_tools, homeassistant_tool, image_generation_tool, memory_tool, mixture_of_agents_tool, tools_registry [INFERRED]
- **Sandbox Security Chain** — code_execution_tool, env_passthrough, redact_module, terminal_tool [INFERRED]
- **MCP Integration Stack** — mcp_tool, mcp_oauth, osv_check, tools_registry, auxiliary_client [INFERRED]

## Communities

### Community 0 - "Community 0"
Cohesion: 0.0
Nodes (2492): MessageType, APIServerAdapter, body_limit_middleware(), check_api_server_requirements(), cors_middleware(), _extract_output_items(), _IdempotencyCache, _make_request_fingerprint() (+2484 more)

### Community 1 - "Community 1"
Cohesion: 0.0
Nodes (1320): InsightsEngine, agent.insights, AuthError, Structured auth error with UX mapping hints., AutoSuggest, _build_boot_prompt(), handle(), Built-in boot-md hook — run ~/.hermes/BOOT.md on gateway startup.  This hook is (+1312 more)

### Community 2 - "Community 2"
Cohesion: 0.0
Nodes (677): MemoryStore, agent.display, agent.error_classifier, agent.context_compressor, agent.display, agent.model_metadata, CheckpointManager, _dir_file_count() (+669 more)

### Community 3 - "Community 3"
Cohesion: 0.0
Nodes (476): _accent_hex(), _active_profile_name(), _all_profile_host_configs(), _build_compact_banner(), _busy_command(), ChatConsole, _cleanup_worktree(), clone_honcho_for_profile() (+468 more)

### Community 4 - "Community 4"
Cohesion: 0.0
Nodes (514): acp_adapter.auth, ACP Entry Point, AI Gateway Provider, Alibaba Provider, Anthropic Provider, API Mode System, _archive_directory(), claw_command() (+506 more)

### Community 5 - "Community 5"
Cohesion: 0.01
Nodes (494): MessageEvent, SessionSource, Agent Cache Tests, _AGENT_PENDING_SENTINEL, Allowlist Startup Check Tests, APIServerAdapter, API Server Jobs Tests, API Server Tests (+486 more)

### Community 6 - "Community 6"
Cohesion: 0.01
Nodes (346): agent.builtin_memory_provider, agent.memory_manager, agent.memory_provider, BuiltinMemoryProvider, BuiltinMemoryProvider — wraps MEMORY.md / USER.md as a MemoryProvider.  Always r, Access the underlying MemoryStore for legacy code paths., Built-in file-backed memory (MEMORY.md + USER.md).      Always active, never dis, Built-in memory is always available. (+338 more)

### Community 7 - "Community 7"
Cohesion: 0.01
Nodes (444): BaseEnvironment, BaseModalExecutionEnvironment, DaytonaEnvironment, DockerEnvironment, LocalEnvironment, ManagedModalEnvironment, ModalEnvironment, ProcessHandle (+436 more)

### Community 8 - "Community 8"
Cohesion: 0.0
Nodes (286): HermesACPAgent, HonchoClientConfig, HonchoMemoryProvider, HonchoSession, HonchoSessionManager, SessionManager, acp, acp_adapter (+278 more)

### Community 9 - "Community 9"
Cohesion: 0.01
Nodes (321): MCPServerTask, SamplingHandler, hermes_cli.mcp_config, MCP Dynamic Discovery, _build_safe_env(), _build_utility_schemas(), _check_message_handler_support(), _connect_server() (+313 more)

### Community 10 - "Community 10"
Cohesion: 0.01
Nodes (293): ClaudeMarketplaceSource, ClawHubSource, GitHubSource, LobeHubSource, OptionalSkillSource, SkillSource, SkillsShSource, WellKnownSkillSource (+285 more)

### Community 11 - "Community 11"
Cohesion: 0.01
Nodes (308): agent.anthropic_adapter, agent.auxiliary_client, agent.anthropic_adapter, AsyncHttpxClientWrapper __del__ Neuter, AnthropicAuxiliaryClient, _AnthropicChatShim, _AnthropicCompletionsAdapter, async_call_llm() (+300 more)

### Community 12 - "Community 12"
Cohesion: 0.01
Nodes (281): AgentResult, _extract_reasoning_from_message(), HermesAgentLoop, HermesAgentLoop -- Reusable Multi-Turn Agent Engine  Runs the hermes-agent tool-, Runs hermes-agent's tool-calling loop using standard OpenAI-spec tool calling., Initialize the agent loop.          Args:             server: Server object with, Execute the full agent loop using standard OpenAI tool calling.          Args:, Replace the global tool executor with a new one of the given size.      Called b (+273 more)

### Community 13 - "Community 13"
Cohesion: 0.01
Nodes (243): Hunk, HunkLine, OperationType, PatchOperation, ABC, apply_v4a_operations, Configurable budget constants for tool result persistence.  Overridable at the R, check_clarify_requirements() (+235 more)

### Community 14 - "Community 14"
Cohesion: 0.01
Nodes (394): Command approval module, Command security guards (tirith + dangerous), Cosign Provenance Verification, _config_overrides(), _configured_platforms(), _count_mcp_servers(), _count_skills(), _cron_summary() (+386 more)

### Community 15 - "Community 15"
Cohesion: 0.01
Nodes (326): AIAgent, COMMANDS Registry, COMMAND_REGISTRY, ContextCompressor, DEFAULT_CONFIG, GatewayConfig, GatewayRunner, HermesCLI (+318 more)

### Community 16 - "Community 16"
Cohesion: 0.01
Nodes (303): AdaLoRA (Adaptive Rank LoRA), Bradley-Terry Loss, DistributedDataParallel (DDP), DPO (Direct Preference Optimization), DeviceMesh, DoRA (Weight-Decomposed Low-Rank Adaptation), FSDP (Fully Sharded Data Parallel), GRPO (Group Relative Policy Optimization) (+295 more)

### Community 17 - "Community 17"
Cohesion: 0.01
Nodes (173): BatchRunner, BatchRunner, Batch Runner Checkpoint Tests, _extract_reasoning_stats(), _extract_tool_stats(), main(), _normalize_tool_error_counts(), _normalize_tool_stats() (+165 more)

### Community 18 - "Community 18"
Cohesion: 0.01
Nodes (131): agent.skill_commands, agent.skill_utils, Skill Commands Scanner, approval_callback(), clarify_callback(), prompt_for_secret(), Interactive prompt callbacks for terminal_tool integration.  These bridge termin, Prompt for dangerous command approval through the TUI.      Shows a selection UI (+123 more)

### Community 19 - "Community 19"
Cohesion: 0.01
Nodes (124): ACP Auth Helpers, ACP Event Callbacks, ACP Permission Bridge, HermesACPAgent, SessionManager, ACP Tool Helpers, agent.context_references, agent.prompt_builder (+116 more)

### Community 20 - "Community 20"
Cohesion: 0.01
Nodes (129): agent.auxiliary_client, LLM Content None Guard, tools.mixture_of_agents_tool, OpenClaw to Hermes Migration Script, tools.session_search_tool, tools.skills_guard, Tests for auxiliary model config bridging — verifies that config.yaml values are, Config without auxiliary section should not crash. (+121 more)

### Community 21 - "Community 21"
Cohesion: 0.01
Nodes (89): HindsightMemoryProvider, Mem0MemoryProvider, RetainDBMemoryProvider, SupermemoryMemoryProvider, WriteQueue, MemoryProviderInterface, _clean_env(), _make_mock_client() (+81 more)

### Community 22 - "Community 22"
Cohesion: 0.01
Nodes (210): _convert_to_png(), _find_powershell(), _get_ps_exe(), has_clipboard_image(), _is_wsl(), _linux_save(), _macos_has_image(), _macos_osascript() (+202 more)

### Community 23 - "Community 23"
Cohesion: 0.01
Nodes (119): tools.browser_tool, tools.browser_providers.browser_use, tools.browser_providers.browserbase, tools.credential_files, Idempotency Key Pattern, tools.image_generation_tool, Managed Modal Environment, tools.environments.managed_modal (+111 more)

### Community 24 - "Community 24"
Cohesion: 0.01
Nodes (163): DiscordAdapter, PlatformConfig, VoiceReceiver, _ensure_discord_mock(), FakeDMChannel, FakeTextChannel, FakeThread, make_message() (+155 more)

### Community 25 - "Community 25"
Cohesion: 0.02
Nodes (129): ProcessRegistry, ProcessSession, Background Process Notifications Tests, Code Execution Tool Module, _clean_shell_noise(), _env_temp_dir(), _handle_process(), _is_host_pid_alive() (+121 more)

### Community 26 - "Community 26"
Cohesion: 0.01
Nodes (153): _apply_env_overrides(), check_config_version(), _coerce_bool(), config_command(), ConfigIssue, _deep_merge(), edit_config(), _ensure_default_soul_md() (+145 more)

### Community 27 - "Community 27"
Cohesion: 0.02
Nodes (145): CloudBrowserProvider, Interface for cloud browser backends (Browserbase, Steel, etc.).      Implementa, Browser session cleanup, Browser LLM response None content guard, _allow_private_urls(), browser_back(), _browser_cleanup_thread_worker(), browser_click() (+137 more)

### Community 28 - "Community 28"
Cohesion: 0.01
Nodes (87): Comprehensive tests for ANSI escape sequence stripping (ECMA-48).  The strip_ans, Device Control String sequences., 8-bit C1 control characters., Select Graphic Rendition — the most common ANSI sequences., Real-world contamination scenarios from bug reports., The original reported bug: shebang corrupted by color codes., Clean content must pass through unmodified., Array indexing must not be confused with CSI. (+79 more)

### Community 29 - "Community 29"
Cohesion: 0.01
Nodes (61): BasePlatformAdapter, EmailAdapter, FeishuAdapter, Tests for document cache utilities in gateway/platforms/base.py.  Covers: get_do, Point the module-level DOCUMENT_CACHE_DIR to a fresh tmp_path., Malicious directory components are stripped — only the leaf name survives., A filename that is literally '..' falls back to 'document'., _redirect_cache() (+53 more)

### Community 30 - "Community 30"
Cohesion: 0.01
Nodes (89): agent.anthropic_adapter, agent.auxiliary_client, agent.model_metadata, hermes_cli.models, _clean_client_cache(), Tests for cross-loop client cache isolation fix (#2681).  Verifies that _get_cac, Simulate gateway mode: _run_async spawns a thread with asyncio.run(),         wh, A cached client whose loop has closed should be replaced. (+81 more)

### Community 31 - "Community 31"
Cohesion: 0.02
Nodes (206): ACP Editor Integration, API Server, Auxiliary Model System, Batch Processing, Browser Automation, Browser Use, camofox_back(), camofox_click() (+198 more)

### Community 32 - "Community 32"
Cohesion: 0.01
Nodes (93): cmd_update, gateway.status, hermes_cli.doctor, Gateway subcommand handler: run, start, stop, restart, status, install, uninstall, setup for systemd/launchd services, Tests for hermes_cli.doctor., The ◆ Memory Provider section should respect memory.provider config., Create a minimal HERMES_HOME with config.yaml., Run doctor and capture stdout. (+85 more)

### Community 33 - "Community 33"
Cohesion: 0.01
Nodes (163): BrowserUseProvider, BrowserbaseProvider, CloudBrowserProvider, FirecrawlProvider, browser_providers_init, build_channel_directory(), _build_discord(), _build_from_sessions() (+155 more)

### Community 34 - "Community 34"
Cohesion: 0.01
Nodes (61): agent.prompt_caching, agent.prompt_caching, Tests for agent/anthropic_adapter.py — Anthropic Messages API adapter., Date-stamped model IDs should resolve via substring match., Unknown future models should get the highest known limit., User-specified max_tokens should be respected., max_tokens should be clamped to context_length if it's smaller., No clamping when context_length exceeds output limit. (+53 more)

### Community 35 - "Community 35"
Cohesion: 0.02
Nodes (89): Matrix Adapter, _make_adapter(), _make_fake_nio(), _ensure_nio_mock(), _make_adapter(), _make_event(), _make_room(), Default (require_mention=true): messages without mention are ignored. (+81 more)

### Community 36 - "Community 36"
Cohesion: 0.03
Nodes (112): hermes_cli.plugins, hermes_cli.plugins_cmd, discover_plugins(), _env_enabled(), _get_disabled_plugins(), get_plugin_cli_commands(), get_plugin_manager(), get_plugin_tool_names() (+104 more)

### Community 37 - "Community 37"
Cohesion: 0.02
Nodes (69): create_mcp_server(), EventBridge, _extract_attachments(), _extract_message_content(), _get_session_db(), _get_sessions_dir(), _load_channel_directory(), _load_sessions_index() (+61 more)

### Community 38 - "Community 38"
Cohesion: 0.02
Nodes (90): AggregateMetrics, CompressionConfig, TrajectoryCompressor, TrajectoryMetrics, _count_tokens_for_entry(), _init_tokenizer_worker(), load_dataset_from_hf(), main() (+82 more)

### Community 39 - "Community 39"
Cohesion: 0.02
Nodes (81): mock_sd(), Tests for tools.voice_mode -- all mocked, no real microphone or API calls., Verify current_rms property updates in real-time for UI feedback., Verify that silence detection params can be configured., Bug: proc.wait(timeout) raised TimeoutExpired but process was not killed., WSL with PULSE_SERVER set should NOT block voice mode., Bug: stream.start() failure left stream unclosed., Bug: _on_silence_stop was read/written without lock in audio callback. (+73 more)

### Community 40 - "Community 40"
Cohesion: 0.02
Nodes (41): ProviderConfig, Describes a known inference provider., Tests for API-key provider support (z.ai/GLM, Kimi, MiniMax, AI Gateway)., Ensure we didn't break the existing OAuth providers., Test resolve_provider() with new providers., OpenRouter API key should win over GLM in auto-detection., ZAI_API_KEY should work when GLM_API_KEY is not set., Test that new providers are correctly registered. (+33 more)

### Community 41 - "Community 41"
Cohesion: 0.03
Nodes (111): _poll_for_token(), Poll the token endpoint until the user approves or the code expires., build_oauth_auth(), _can_open_browser(), MCP OAuth 2.1 PKCE, _find_free_port(), _get_token_dir(), HermesTokenStorage (+103 more)

### Community 42 - "Community 42"
Cohesion: 0.02
Nodes (89): agent.skill_utils, hermes_cli.skills_config, build_context_files_prompt(), build_nous_subscription_prompt(), _build_skills_manifest(), build_skills_system_prompt(), _build_snapshot_entry(), clear_skills_system_prompt_cache() (+81 more)

### Community 43 - "Community 43"
Cohesion: 0.03
Nodes (63): adapter(), _build_rtp_packet(), _ensure_discord_mock(), _fill_buffer(), _make_discord_adapter(), _make_event(), _make_receiver(), runner() (+55 more)

### Community 44 - "Community 44"
Cohesion: 0.01
Nodes (67): Tests for web backend client configuration and singleton behavior.  Coverage:, Shared gateway scheme should allow local plain-http vendor hosts., Unexpected shared gateway schemes should fail fast., An explicit Firecrawl gateway origin should override the shared domain., Default gateway origin should point at the Firecrawl vendor hostname., Explicit Firecrawl config should win over the gateway fallback., Auth lookup should read from HERMES_HOME/auth.json, not ~/.hermes/auth.json., Availability checks should not be pinned to module import state. (+59 more)

### Community 45 - "Community 45"
Cohesion: 0.02
Nodes (107): agent.models_dev, agent.models_dev, Context Probe Tiers, _check_hermes_model_warning(), CustomAutoResult, _ensure_direct_aliases(), get_authenticated_provider_slugs(), list_authenticated_providers() (+99 more)

### Community 46 - "Community 46"
Cohesion: 0.02
Nodes (65): Device Path Blocking, File Read Deduplication, File Staleness Detection, tools.file_tools, tools.fuzzy_match, _FakeReadResult, _make_fake_ops(), Re-reading an unchanged file should return a lightweight stub. (+57 more)

### Community 47 - "Community 47"
Cohesion: 0.02
Nodes (54): Slack Adapter, _ensure_slack_mock(), _make_adapter(), test_api_failure_returns_empty(), test_bot_message_ts_cap(), test_deny_action(), test_empty_thread(), test_fetches_and_formats_context() (+46 more)

### Community 48 - "Community 48"
Cohesion: 0.03
Nodes (129): _agent_key_is_usable(), _auth_file_path(), _auth_lock_path(), _auth_store_lock(), clear_provider_auth(), _codex_access_token_is_expiring(), _codex_device_code_login(), _coerce_ttl_seconds() (+121 more)

### Community 49 - "Community 49"
Cohesion: 0.02
Nodes (120): G0DM0D3, L1B3RT4S, auto_jailbreak(), _build_messages(), _detect_model_family(), _get_api_key(), _get_current_model(), Detect model family from model ID string. (+112 more)

### Community 50 - "Community 50"
Cohesion: 0.02
Nodes (48): profile_env(), Comprehensive tests for hermes_cli.profiles module.  Tests cover: validation, di, Tests for create_profile()., Clone config gracefully skips files that don't exist in source., Tests for delete_profile()., Tests for list_profiles()., Tests for set_active_profile() / get_active_profile()., Tests for get_active_profile_name(). (+40 more)

### Community 51 - "Community 51"
Cohesion: 0.04
Nodes (118): _apply_default_agent_settings(), check_auth(), _check_espeak_ng(), _clean_discord_user_ids(), _current_reasoning_effort(), _curses_prompt_choice(), _ensure_deps(), exchange_auth_code() (+110 more)

### Community 52 - "Community 52"
Cohesion: 0.02
Nodes (53): _force_local_terminal(), _mock_handle_function_call(), Verify json_parse, shell_quote, and retry helpers are generated., Integration tests using the mock dispatcher., Helper: run code with mocked handle_function_call., Script that just prints -- no tool calls., Sandboxed scripts can import modules that live at the repo root., Script calls terminal and prints the result. (+45 more)

### Community 53 - "Community 53"
Cohesion: 0.02
Nodes (53): Tests for cron/scheduler.py — origin resolution, delivery routing, and error log, Failed jobs deliver regardless of [SILENT] in output., Verify _build_job_prompt always injects [SILENT] guidance., deliver: 'telegram:My Group' resolves without display suffix., Cron hint tells agents their final response is auto-delivered., System guidance appears before the user's prompt text., Verify that a missing skill logs a warning and does not crash the job., Job should run even when a referenced skill is not installed. (+45 more)

### Community 54 - "Community 54"
Cohesion: 0.02
Nodes (58): _json_stdout(), _mock_run(), Tests for the tirith security scanning subprocess wrapper., Without HERMES_HOME set, falls back to ~/.hermes., Pre-set cached path to skip auto-install in scan tests.      Tests that specific, _resolve_tirith_path should expand ~ in configured path., Build a mock subprocess.CompletedProcess., ensure_installed must return immediately when download needed. (+50 more)

### Community 55 - "Community 55"
Cohesion: 0.03
Nodes (67): FakeHAServer, HomeAssistantAdapter, Home Assistant Adapter, _async_call_service(), _async_get_state(), _async_list_entities(), _async_list_services(), _build_service_payload() (+59 more)

### Community 56 - "Community 56"
Cohesion: 0.04
Nodes (50): cmd_add(), cmd_add_quiz(), cmd_delete(), cmd_delete_collection(), cmd_due(), cmd_export(), cmd_import(), cmd_list() (+42 more)

### Community 57 - "Community 57"
Cohesion: 0.03
Nodes (63): _cleanup_worktree(), git_repo(), _git_repo_root(), Tests for git worktree isolation (CLI --worktree / -w flag).  Verifies worktree, Test git repo root detection., Create a temporary git repo for testing., Two worktrees from the same repo are independent., Worktree should contain the repo's tracked files. (+55 more)

### Community 58 - "Community 58"
Cohesion: 0.06
Nodes (100): _build_user_local_paths(), _default_system_service_user(), _detect_venv_dir(), _ensure_linger_enabled(), _ensure_user_systemd_env(), find_gateway_pids(), gateway_command(), gateway_setup() (+92 more)

### Community 59 - "Community 59"
Cohesion: 0.04
Nodes (69): adapter(), auth_adapter(), _create_app(), _make_adapter(), test_agent_error_returns_500(), test_browser_origin_rejected_by_default(), test_chat_completions_requires_auth(), test_chat_completions_usage() (+61 more)

### Community 60 - "Community 60"
Cohesion: 0.05
Nodes (71): _attachment_placeholder(), _build_create_message_body(), _build_create_message_request(), _build_file_upload_body(), _build_file_upload_request(), _build_get_chat_request(), _build_get_message_request(), _build_image_upload_body() (+63 more)

### Community 61 - "Community 61"
Cohesion: 0.02
Nodes (45): Tests for the hermes_cli models module., Models belonging to the current provider should not trigger a switch., Models in the OpenRouter catalog should be found., Completely unknown model names should return None., nous/openrouter should never be auto-suggested as target provider., Tests for filter_nous_free_models — Nous Portal free-model policy., Regular paid models pass through unchanged., Free models NOT in the allowlist are filtered out. (+37 more)

### Community 62 - "Community 62"
Cohesion: 0.02
Nodes (20): r"""Backslashes in inline code must be escaped for MarkdownV2., r"""Backslashes in fenced code blocks must be escaped for MarkdownV2., r"""Backticks inside fenced code blocks must be escaped for MarkdownV2., r"""Already-escaped backslashes should not be quadruple-escaped., The || delimiters must not be escaped as \\|\\|., Only > at line start is a blockquote; mid-line > should be escaped., Bold markers inside code blocks should not be converted., **** (empty bold) should not crash. (+12 more)

### Community 63 - "Community 63"
Cohesion: 0.03
Nodes (47): _make_mock_parent(), Verify child gets parent's depth + 1., Verify children are registered/unregistered for interrupt propagation., Verify _last_resolved_tool_names is restored after subagent runs., The process-global _last_resolved_tool_names must be restored         after a su, Even when the child agent raises, the global must be restored., Regression: _build_child_agent must not reference _saved_tool_names.          Th, Create a mock parent agent with the fields delegate_task expects. (+39 more)

### Community 64 - "Community 64"
Cohesion: 0.03
Nodes (78): Strip ANSI escape sequences from subprocess output.  Used by terminal_tool, code, Remove ANSI escape sequences from text.      Returns the input unchanged (fast p, strip_ansi(), _approval_key_aliases(), _ApprovalEntry, approve_permanent(), approve_session(), check_all_command_guards() (+70 more)

### Community 65 - "Community 65"
Cohesion: 0.04
Nodes (84): check_nous_free_tier(), clear_nous_free_tier_cache(), _copilot_catalog_ids(), _copilot_catalog_item_is_text_model(), copilot_default_headers(), copilot_model_api_mode(), curated_models_for_provider(), detect_provider_for_model() (+76 more)

### Community 66 - "Community 66"
Cohesion: 0.03
Nodes (25): Tests for provider-aware `/model` validation in hermes_cli.models., custom:name:model → named custom provider., Triple syntax should handle whitespace., custom:name: with no model → treated as custom:name (bare)., GPT-5+ models should use Responses API (matching opencode)., gpt-5-mini is the exception — uses Chat Completions., Non-GPT-5 models use Chat Completions., When catalog shows both endpoints, model ID pattern wins. (+17 more)

### Community 67 - "Community 67"
Cohesion: 0.04
Nodes (32): Gateway Platform Config, Send Message Tool Module, Telegram Bot API, _make_aiohttp_resp(), _make_aiohttp_session(), Tests for _send_mattermost, _send_matrix, _send_homeassistant, _send_dingtalk., Each call should generate a distinct transaction ID in the URL., Build a minimal async-context-manager mock for an aiohttp response. (+24 more)

### Community 68 - "Community 68"
Cohesion: 0.04
Nodes (81): build_anthropic_client(), build_anthropic_kwargs(), _convert_content_part_to_anthropic(), _convert_content_to_anthropic(), convert_messages_to_anthropic(), _convert_openai_image_part_to_anthropic(), convert_tools_to_anthropic(), _detect_claude_code_version() (+73 more)

### Community 69 - "Community 69"
Cohesion: 0.09
Nodes (25): backup_existing(), dump_yaml_file(), ensure_parent(), extract_markdown_entries(), ItemResult, load_yaml_file(), main(), merge_entries() (+17 more)

### Community 70 - "Community 70"
Cohesion: 0.03
Nodes (18): extract_media_tags_broken(), extract_media_tags_fixed(), Tests for MEDIA tag extraction from tool results.  Verifies that MEDIA tags (e.g, MEDIA tags from the current turn SHOULD be extracted., Multiple TTS calls in history should NOT accumulate in new responses., Extract MEDIA tags from tool results, but ONLY from new messages     (those adde, Multiple MEDIA tags in current turn should be deduplicated., The BROKEN behavior: extract MEDIA tags from ALL messages including history. (+10 more)

### Community 71 - "Community 71"
Cohesion: 0.03
Nodes (24): Tests for cron/jobs.py — schedule parsing, job CRUD, and due-job detection., Redirect cron storage to a temp directory., Agent succeeds but delivery fails — both tracked independently., Successful delivery clears the previous delivery error., Agent fails AND delivery fails — both errors recorded., Tests for advance_next_run() — crash-safety for recurring jobs., Interval jobs should have next_run_at bumped to the next future occurrence., Cron-expression jobs should have next_run_at bumped to the next occurrence. (+16 more)

### Community 72 - "Community 72"
Cohesion: 0.05
Nodes (51): GatewayDiscord, _build_encrypted_rtp_packet(), _make_secret_key(), _make_voice_receiver(), Integration tests for Discord voice channel audio flow.  Uses real NaCl encrypti, End-to-end: real NaCl encrypt → _on_packet decrypt → buffer., Real NaCl encrypted packet → decrypted → buffered., Packet encrypted with wrong key → NaCl fails → not buffered. (+43 more)

### Community 73 - "Community 73"
Cohesion: 0.04
Nodes (78): Abliteration / Refusal Removal, Activation Checkpointing, AWQ Quantization, BaseModelArgs, Continuous Batching, DDP (DistributedDataParallel), DeepSpeed Strategy, DTensor (+70 more)

### Community 74 - "Community 74"
Cohesion: 0.03
Nodes (30): Tests for hermes_cli.plugins_cmd — the ``hermes plugins`` CLI subcommand., Extract plugin directory name from Git URLs., Verify alias routing in plugins_command()., Manifest reading edge cases., Test the install command., Test the update command., Reject path-traversal attempts while accepting valid names., Test the remove command. (+22 more)

### Community 75 - "Community 75"
Cohesion: 0.04
Nodes (39): _make_sessions(), Tests for the interactive session browser (`hermes sessions browse`).  Covers: -, Invalid selection followed by valid one works., KeyboardInterrupt in fallback mode returns None., Fallback mode should display all session entries., When a session has a title, show it instead of the preview., When no title, show preview., Generate a list of fake rich-session dicts. (+31 more)

### Community 76 - "Community 76"
Cohesion: 0.04
Nodes (40): _mock_response(), _enable_persistence(), _mock_response(), Persistence tests for the Camofox browser backend.  Tests that managed persisten, With managed_persistence: stable userId derived from Hermes profile., VNC URL is derived from the Camofox health endpoint., camofox_soft_cleanup drops local state only when managed persistence is on., Soft cleanup must never hit the Camofox /sessions DELETE endpoint. (+32 more)

### Community 77 - "Community 77"
Cohesion: 0.04
Nodes (58): RunState, check_rl_api_keys(), check_rl_python_version(), _ensure_logs_dir(), EnvironmentInfo, _get_env_config_fields(), get_missing_keys(), _initialize_environments() (+50 more)

### Community 78 - "Community 78"
Cohesion: 0.03
Nodes (19): Home Assistant Domain Blocklist, tools.homeassistant_tool, Tests for the Home Assistant tool module.  Tests real logic: entity filtering, p, Verify dangerous HA service domains are blocked., Safe domains like 'light' should not be blocked (will fail on network, not block, Verify entity_id format validation prevents path traversal., Some services (like scene.turn_on) don't need entity_id., Registry should exclude HA tools when HASS_TOKEN is not set. (+11 more)

### Community 79 - "Community 79"
Cohesion: 0.03
Nodes (28): environments.hermes_base_env, Tests for ManagedServer / tool-parser integration.  Validates that: 1. The insta, ManagedServer checks `if parsed_tool_calls:` — None should be falsy., ManagedServer uses `parsed_content or ""` — must be str or None., Test that hermes_base_env.py's tool-parser wiring matches the current API., Hermes wires parser selection through ServerManager.tool_parser., Verify hermes_base_env uses the config field rather than a local parser instance, Test that ManagedServer's API matches what hermes-agent expects. (+20 more)

### Community 80 - "Community 80"
Cohesion: 0.03
Nodes (28): cron_env(), Tests for cron job script injection feature.  Tests cover: - Script field in job, Scripts can output structured JSON for the LLM to parse., Test that script output is injected into the prompt., Test the cronjob tool's script parameter., Isolated cron environment with temp HERMES_HOME., Regression tests for path containment bypass in _run_job_script().      Prior to, Absolute paths outside ~/.hermes/scripts/ must be rejected. (+20 more)

### Community 81 - "Community 81"
Cohesion: 0.04
Nodes (14): Tests for tools/skill_manager_tool.py — skill creation, editing, and deletion., Patch both SKILLS_DIR and get_all_skills_dirs so _find_skill searches     only t, _skill_dir(), TestCreateSkill, TestDeleteSkill, TestEditSkill, TestPatchSkill, TestRemoveFile (+6 more)

### Community 82 - "Community 82"
Cohesion: 0.06
Nodes (33): _doh_answer(), _fake_transport_factory(), FakeDoHClient, FakeTransport, _make_response(), _telegram_request(), test_aclose_closes_all_transports(), test_all_doh_ips_same_as_system_dns_uses_seed() (+25 more)

### Community 83 - "Community 83"
Cohesion: 0.04
Nodes (61): build_tool_preview(), capture_local_edit_snapshot(), _detect_tool_failure(), _diff_from_snapshot(), _display_diff_path(), _emit_inline_diff(), extract_edit_diff(), format_context_pressure() (+53 more)

### Community 84 - "Community 84"
Cohesion: 0.05
Nodes (27): Tests for tools/skills_sync.py — manifest-based skill seeding and updating., Create a fake bundled skills directory., Return context manager stack for patching sync globals., After fresh install, manifest should have v2 format with hashes., Skill in manifest but not on disk = user deleted it. Don't re-add., Skill in manifest + on disk + user hasn't modified = update from bundled., Skill modified by user should NOT be overwritten even if bundled changed., Skill in sync (user == bundled == origin) = no action needed. (+19 more)

### Community 85 - "Community 85"
Cohesion: 0.05
Nodes (28): agent.rate_limit_tracker, _bar(), _bucket_line(), _fmt_count(), _fmt_seconds(), format_rate_limit_compact(), format_rate_limit_display(), parse_rate_limit_headers() (+20 more)

### Community 86 - "Community 86"
Cohesion: 0.04
Nodes (16): Mattermost Adapter, _make_adapter(), test_audio_media_type_is_full_mime(), test_dm_always_responds(), test_document_media_type_is_full_mime(), test_free_response_channel_responds_without_mention(), test_image_media_type_is_full_mime(), test_mention_stripped_from_text() (+8 more)

### Community 87 - "Community 87"
Cohesion: 0.03
Nodes (16): agent.redact, _ensure_redaction_enabled(), Tests for agent.redact -- secret masking in logs and output., Ensure HERMES_REDACT_SECRETS is not disabled by prior test imports., Simulate what happens when the agent runs `env` or `printenv`., Regression tests for ElevenLabs (sk_), Tavily (tvly-), and Exa (exa_) keys., TestAuthHeaders, TestElevenLabsTavilyExaKeys (+8 more)

### Community 88 - "Community 88"
Cohesion: 0.04
Nodes (26): _add_rotating_handler(), _ManagedRotatingFileHandler, Enable DEBUG-level console logging for ``--verbose`` / ``-v`` mode.      Called, RotatingFileHandler that ensures group-writable perms in managed mode.      In m, Add a ``RotatingFileHandler`` to *logger*, skipping if one already     exists fo, Best-effort read of ``logging.*`` from config.yaml.      Returns ``(level, max_s, Configure the Hermes logging subsystem.      Safe to call multiple times — the s, _read_logging_config() (+18 more)

### Community 89 - "Community 89"
Cohesion: 0.06
Nodes (52): adapter(), auth_adapter(), _create_app(), _make_adapter(), Tests for the Cron Jobs API endpoints on the API server adapter.  Covers: - CRUD, Create an adapter with optional API key., Create the aiohttp app with jobs routes registered., test_auth_passes_with_valid_key() (+44 more)

### Community 90 - "Community 90"
Cohesion: 0.04
Nodes (31): Tests for tools/clarify_tool.py - Interactive clarifying questions., Non-list choices should return error., Non-string choices should be converted to strings., Tests for callback error handling., Should return error if callback raises exception., Callback should receive trimmed question., User response should be stripped of whitespace., Tests for the requirements check function. (+23 more)

### Community 91 - "Community 91"
Cohesion: 0.05
Nodes (30): Hidden Directory Filter, Skills Install Policy, _new_should_allow(), _old_should_allow(), Regression tests for skills guard policy precedence.  Official/builtin skills sh, Simulate the BROKEN old logic., Simulate the FIXED logic., TestPolicyPrecedenceForDangerousVerdicts (+22 more)

### Community 92 - "Community 92"
Cohesion: 0.06
Nodes (23): _make_cli(), Tests for HermesCLI initialization -- catches configuration bugs that only manif, When agent is running, /queue should still put the prompt in _pending_input., Create a HermesCLI instance with minimal mocking., When agent is idle, /queue should still queue (not reject)., In queue mode, Enter while busy should go to _pending_input, not _interrupt_queu, In interrupt mode (default), Enter while busy goes to _interrupt_queue., Single-query mode calls chat() without going through run(). (+15 more)

### Community 93 - "Community 93"
Cohesion: 0.04
Nodes (9): Tests for tools/cronjob_tools.py — prompt scanning, schedule/list/remove dispatc, Cron is internal (JSON-based scheduler), no system crontab needed., Without any session env vars, cronjob tool should not be available., TestCronjobRequirements, TestListCronjobs, TestRemoveCronjob, TestScanCronPrompt, TestScheduleCronjob (+1 more)

### Community 94 - "Community 94"
Cohesion: 0.08
Nodes (49): advance_next_run(), _apply_skill_fields(), _compute_grace_seconds(), compute_next_run(), create_job(), _ensure_aware(), ensure_dirs(), get_due_jobs() (+41 more)

### Community 95 - "Community 95"
Cohesion: 0.08
Nodes (27): _make_signal_adapter(), _stub_rpc(), test_fetch_attachment_handles_dict_response(), test_fetch_attachment_returns_none_on_empty(), test_fetch_attachment_uses_id_parameter(), test_send_document_error_includes_path(), test_send_document_too_large(), test_send_image_file_missing() (+19 more)

### Community 96 - "Community 96"
Cohesion: 0.08
Nodes (47): cmd_contract(), cmd_gas(), cmd_price(), cmd_stats(), cmd_token(), cmd_tx(), cmd_wallet(), cmd_whales() (+39 more)

### Community 97 - "Community 97"
Cohesion: 0.05
Nodes (48): AIAgent, API Server (OpenAI-compatible), Background Sessions, Cron Scheduler, DM Pairing System, End-to-End Encryption (E2EE), Gateway Service Management, Home Assistant Tools (+40 more)

### Community 98 - "Community 98"
Cohesion: 0.07
Nodes (27): _cmd_approve(), _cmd_clear_pending(), _cmd_list(), _cmd_revoke(), pairing_command(), DM Pairing System  Code-based approval flow for authorizing new users on messagi, Check if a user is approved (paired) on a platform., List approved users, optionally filtered by platform. (+19 more)

### Community 99 - "Community 99"
Cohesion: 0.08
Nodes (20): _make_agent(), _make_tool_defs(), _make_transport_error(), _mock_resolve(), Tests for per-turn primary runtime restoration and transport recovery.  Verifies, After restore, the full fallback chain should be available again., If client rebuild fails, the method returns False gracefully., Create an exception whose type().__name__ matches the given name. (+12 more)

### Community 100 - "Community 100"
Cohesion: 0.07
Nodes (21): _apply_file_size_limits(), check_wecom_requirements(), _coerce_list(), _decode_base64(), _decrypt_file_bytes(), _derive_message_type(), _detect_image_ext(), _detect_wecom_media_type() (+13 more)

### Community 101 - "Community 101"
Cohesion: 0.06
Nodes (42): _FakePopen, _make_dummy_env(), _make_execute_only_env(), _mock_subprocess_run(), Opt-in docker cwd mounting should bind the host cwd to /workspace., Mock subprocess.run to intercept docker run -d and docker version calls.      Re, Host cwd should not be mounted unless the caller explicitly opts in., Explicit user volumes for /workspace should take precedence over cwd mount. (+34 more)

### Community 102 - "Community 102"
Cohesion: 0.05
Nodes (17): Tests for browser_console tool and browser_vision annotate param., browser_console is properly registered in the tool registry., browser_console must be reachable via toolset resolution., browser_vision supports annotate parameter., Without annotate, screenshot command has no --annotate flag., browser_console() returns console messages + JS errors in one call., With annotate=True, screenshot command includes --annotate., browser.record_sessions config option. (+9 more)

### Community 103 - "Community 103"
Cohesion: 0.07
Nodes (40): _build_command_lookup(), _build_description(), _clamp_command_names(), _collect_gateway_skill_entries(), _completion_text(), _context_completions(), discord_skill_commands(), _extract_context_word() (+32 more)

### Community 104 - "Community 104"
Cohesion: 0.07
Nodes (20): FakeTool, _isolate_config(), _make_args(), Tests for hermes_cli.mcp_config — ``hermes mcp`` subcommands.  These tests mock, Server without explicit enabled key defaults to enabled., Must specify --url or --command., Add an HTTP server, accept all tools., Redirect all config I/O to a temp directory. (+12 more)

### Community 105 - "Community 105"
Cohesion: 0.06
Nodes (20): Tests for BasePlatformAdapter._send_with_retry and _is_retryable_error.  Verifie, ConnectTimeout is a connection error, not a delivery-ambiguous timeout., _StubAdapter, test_connect_timeout_still_retried(), test_fallback_failure_logged_but_not_raised(), test_network_to_nonnetwork_transition_falls_back_to_plaintext(), test_non_network_error_falls_back_immediately(), test_notice_send_exception_doesnt_propagate() (+12 more)

### Community 106 - "Community 106"
Cohesion: 0.05
Nodes (14): Pairing Store, _make_store(), Tests for gateway/pairing.py — DM pairing security system., Create a PairingStore with PAIRING_DIR pointed to tmp_path., Multiple codes for different users should be distinct., TestApprovalFlow, TestCodeExpiry, TestCodeGeneration (+6 more)

### Community 107 - "Community 107"
Cohesion: 0.06
Nodes (25): Google API Script, Google OAuth Setup Script, Google Workspace Bridge Script, FakeCredentials, FakeFlow, Regression tests for Google Workspace OAuth setup.  These tests cover the headle, Partial scopes are accepted with a warning (gws migration: v2.0)., reset() (+17 more)

### Community 108 - "Community 108"
Cohesion: 0.05
Nodes (23): Tests for macOS Homebrew PATH discovery in browser_tool.py., Should find npx in Homebrew paths as a fallback., Should raise FileNotFoundError when nothing works., Verify _run_browser_command() includes Homebrew node dirs in subprocess PATH., A local agent-browser path containing spaces must stay one argv entry., Verify _SANE_PATH includes Homebrew directories., The synthetic npx fallback should still expand into separate argv items., When _discover_homebrew_node_dirs returns dirs, they should appear         in th (+15 more)

### Community 109 - "Community 109"
Cohesion: 0.05
Nodes (16): _clean_state(), Tests for check_all_command_guards() — combined tirith + dangerous command guard, When tools.tirith_security can't be imported, treated as allow., Clear approval state and relevant env vars between tests., Tirith 'block' is now treated as an approvable warning (not a hard block)., TestAlwaysVisibility, TestCombinedWarnings, TestContainerSkip (+8 more)

### Community 110 - "Community 110"
Cohesion: 0.12
Nodes (24): _ensure_telegram_mock(), _make_document(), _make_file_obj(), _make_message(), _make_photo(), _make_update(), _redirect_cache(), test_caption_preserved_with_injection() (+16 more)

### Community 111 - "Community 111"
Cohesion: 0.05
Nodes (15): OSV (Open Source Vulnerabilities) API, OSV Check Module, Tests for OSV malware check on MCP extension packages., Known malware package returns error string., Network errors allow the package (fail-open)., Non-npx/uvx commands are skipped entirely., uvx commands check PyPI ecosystem., Live integration test against the real OSV API. Skipped if offline. (+7 more)

### Community 112 - "Community 112"
Cohesion: 0.08
Nodes (10): assistant_dict_call(), make_tc(), Unit tests for AIAgent pre/post-LLM-call guardrails.  Covers three static method, Create a minimal tool_call SimpleNamespace mirroring the OpenAI SDK object., Dict-style tool_call (as stored in message history)., TestCapDelegateTaskCalls, TestDeduplicateToolCalls, TestGetToolCallIdStatic (+2 more)

### Community 113 - "Community 113"
Cohesion: 0.05
Nodes (14): GatewayStreamConsumer, Tests for GatewayStreamConsumer — media directive stripping in streaming., Verify MEDIA: directives and internal markers are stripped from display text., Text without MEDIA: passes through unchanged., Basic MEDIA:<path> tag is removed., MEDIA: tag with space after colon is removed., MEDIA: tags wrapped in quotes or backticks are removed., [[audio_as_voice]] directive is removed. (+6 more)

### Community 114 - "Community 114"
Cohesion: 0.1
Nodes (16): _make_agent(), _make_tool_defs(), _mock_resolve(), Tests for the provider fallback model feature.  Verifies that AIAgent can switch, Fallback should fail gracefully when the API key env var is unset., Custom base_url in config should override the provider default., Z.AI should also check Z_AI_API_KEY as fallback env var., OpenAI Codex fallback should use OAuth credentials and codex_responses mode. (+8 more)

### Community 115 - "Community 115"
Cohesion: 0.07
Nodes (10): _display_metas(), _display_names(), Tests for file path autocomplete in the CLI completer., Test the completer produces path completions via the prompt_toolkit API., Extract plain-text display names from a list of Completion objects., Extract plain-text display_meta from a list of Completion objects., TestExtractPathWord, TestFileSizeLabel (+2 more)

### Community 116 - "Community 116"
Cohesion: 0.1
Nodes (33): defusedxml, markitdown, _can_merge(), _consolidate_text(), _find_elements(), _first_child_run(), _get_child(), _get_children() (+25 more)

### Community 117 - "Community 117"
Cohesion: 0.07
Nodes (26): _create_and_return_transport(), _get_current_loop(), _mock_vision_response(), Regression tests for the _run_async() event-loop lifecycle.  These tests verify, Multiple _run_async calls on the same worker thread should         reuse the sam, Different worker threads must get their own loops to avoid         contention (t, Worker thread loops must be different from the main thread's         persistent, When a loop is already running, _run_async falls back to a thread. (+18 more)

### Community 118 - "Community 118"
Cohesion: 0.06
Nodes (15): Tests for _detect_file_drop — file path detection that prevents dragged/pasted a, r"""macOS drags produce paths like /path/to/my\ file.png, A file literally named 'help' inside a directory starting with /., Create a temporary .png file and return its path., Create a temporary .py file and return its path., Create a file whose name contains spaces (like macOS screenshots)., A directory path should not be treated as a file drop., TestEdgeCases (+7 more)

### Community 119 - "Community 119"
Cohesion: 0.07
Nodes (19): FakeAgent, Tests for cron job inactivity-based timeout.  Tests cover: - Active agent runs i, An agent that goes idle should be detected and interrupted., HERMES_CRON_TIMEOUT=0 means no timeout at all., HERMES_CRON_TIMEOUT env var is respected., HERMES_CRON_TIMEOUT=0 yields None (unlimited)., The TimeoutError message should include last activity info., If agent lacks get_activity_summary, idle_secs stays 0 (never times out). (+11 more)

### Community 120 - "Community 120"
Cohesion: 0.1
Nodes (34): cmd_activity(), cmd_nft(), cmd_price(), cmd_stats(), cmd_token(), cmd_tx(), cmd_wallet(), cmd_whales() (+26 more)

### Community 121 - "Community 121"
Cohesion: 0.07
Nodes (20): isolate_skills(), _make_skill_content(), Tests for skill content size limits.  Agent writes (create/edit/patch/write_file, patch action checks resulting size, not just the new_string., Patches that shrink an already-oversized skill should succeed., Patch on a supporting file also checks size., write_file action enforces both char and byte limits., Skills dropped directly on disk are not constrained. (+12 more)

### Community 122 - "Community 122"
Cohesion: 0.1
Nodes (32): _add_bars(), _default_fields(), draw_outlined_text(), fetch_imgflip_templates(), _fetch_url(), find_font(), generate_from_image(), generate_meme() (+24 more)

### Community 123 - "Community 123"
Cohesion: 0.1
Nodes (21): _AsyncCM, _bare_adapter(), _connect_patches(), _make_adapter(), _mock_aiohttp(), Minimal async context manager returning a fixed value., Build a mock ``aiohttp.ClientSession`` returning a fixed response., Return a dict of common patches needed to reach the health-check loop. (+13 more)

### Community 124 - "Community 124"
Cohesion: 0.07
Nodes (33): AIAgent Class, Async-Sync Bridging, Context Compression, Credential Pool Rotation, FTS5 Full-Text Search, HermesCLI Class, Profile System, Prompt Caching Policy (+25 more)

### Community 125 - "Community 125"
Cohesion: 0.1
Nodes (9): Tests for gateway/channel_directory.py — channel resolution and display., Write sessions.json at the path _build_from_sessions expects., Helper to write a fake channel directory., TestBuildChannelDirectoryWrites, TestBuildFromSessions, TestFormatDirectoryForDisplay, TestLoadDirectory, TestResolveChannelName (+1 more)

### Community 126 - "Community 126"
Cohesion: 0.1
Nodes (7): _make_adapter(), If target already contains ';' it's a raw GUID — return unchanged., TestBlueBubblesAttachmentDownload, TestBlueBubblesConfigLoading, TestBlueBubblesGuidResolution, TestBlueBubblesHelpers, TestBlueBubblesWebhookParsing

### Community 127 - "Community 127"
Cohesion: 0.09
Nodes (13): _is_long_context_tier_error(), Tests for Anthropic Sonnet long-context tier 429 handling.  When Claude Max user, When the long-context tier error fires, context_length should     drop to 200k a, Verify the long-context 429 doesn't hit the generic rate-limit     or client-err, The error should be intercepted before the generic         is_rate_limited check, Opus should NOT match — falls through to generic rate-limit., A normal 429 should NOT match the long-context check., Verify the detection heuristic matches the Anthropic error. (+5 more)

### Community 128 - "Community 128"
Cohesion: 0.11
Nodes (12): _build_parser(), Tests for parent→subparser flag propagation.  When flags like --yolo, -w, -s exi, When no subcommand is given, flags must work and defaults must hold., Verify --yolo sets HERMES_YOLO_MODE regardless of flag position.      This tests, Replicate the exact check from cmd_chat in main.py., Build the hermes argument parser from the real code.      We import the real mai, Flags placed before 'chat' must propagate through., Flags placed after 'chat' must still work. (+4 more)

### Community 129 - "Community 129"
Cohesion: 0.1
Nodes (29): build_release_artifacts(), bump_version(), categorize_commit(), clean_subject(), generate_changelog(), get_commits(), get_current_version(), get_last_tag() (+21 more)

### Community 130 - "Community 130"
Cohesion: 0.1
Nodes (17): _compute_scroll_offset(), Tests for the scrolling viewport logic in _curses_prompt_choice (issue #5755)., Simulate pressing UP through all items; cursor always in view., Mirror of the scroll adjustment block inside _curses_menu., Return the list indices that would be rendered for the given state., Start position: offset stays 0, first items visible., Cursor inside the current window: offset unchanged., Cursor on Cancel (index 12) with 8-row window: offset = 12 - 8 + 1 = 5. (+9 more)

### Community 131 - "Community 131"
Cohesion: 0.07
Nodes (6): Tests for terminal command exit code semantic interpretation., Command with only env var assignments, no actual command., grep exit 2+ is a real error — should return None., Test _interpret_exit_code returns correct notes for known command semantics., In a pipeline, the last command determines the exit code., TestInterpretExitCode

### Community 132 - "Community 132"
Cohesion: 0.12
Nodes (10): adapter_factory(), _ensure_telegram_mock(), test_all_mode_all_chunks_thread(), test_first_mode_only_first_chunk_threads(), test_no_reply_to_param_no_threading(), test_off_mode_no_reply_threading(), test_single_chunk_respects_mode(), TestEnvVarOverride (+2 more)

### Community 133 - "Community 133"
Cohesion: 0.07
Nodes (9): E2E tests for Telegram gateway slash commands.  Each test drives a message throu, Verify session state changes across command sequences., Verify the pipeline handles unauthorized users., Verify the pipeline handles send failures gracefully., Gateway slash commands dispatched through the full adapter pipeline., TestAuthorization, TestSendFailureResilience, TestSessionLifecycle (+1 more)

### Community 134 - "Community 134"
Cohesion: 0.11
Nodes (8): _make_args(), Tests for hermes_cli/webhook.py — webhook subscription CLI., TestList, TestPersistence, TestRemove, TestSubscribe, TestWebhookEnabledGate, WebhookCommand

### Community 135 - "Community 135"
Cohesion: 0.07
Nodes (11): _clean_passthrough(), Tests for tools.env_passthrough — skill and config env var passthrough., Verify that the passthrough is checked in execute_code's env filtering., TENOR_API_KEY should be blocked without passthrough., TENOR_API_KEY should pass through when registered., Verify that the passthrough is checked in terminal's env sanitizers., Ensure a clean passthrough state for every test., TestConfigPassthrough (+3 more)

### Community 136 - "Community 136"
Cohesion: 0.1
Nodes (19): _can_symlink(), _new_check_escapes(), _old_check_escapes(), Tests for the symlink boundary check prefix confusion fix in skills_guard.py.  R, Check if we can create symlinks (needs admin/dev-mode on Windows)., Test the full symlink scenario with real filesystem symlinks., A symlink from axolotl/ to axolotl-backdoor/ must be caught., A symlink that stays within the skill directory is fine. (+11 more)

### Community 137 - "Community 137"
Cohesion: 0.08
Nodes (28): Constrained Generation, Experiment Tracking, GGUF Format, Hyperparameter Optimization, LLM Evaluation, MLOps, Model Registry, Model Quantization (+20 more)

### Community 138 - "Community 138"
Cohesion: 0.07
Nodes (17): Skills Hub Module, Tests that search_files excludes hidden directories by default.  Regression for, _write_index_cache should create .ignore in .hub/ directory., Create a directory tree with hidden and visible directories., _search_files uses find, which should exclude hidden directories., find should not return files from .hub/ directory., find should not return files from .git/ directory., find should still return files from visible directories. (+9 more)

### Community 139 - "Community 139"
Cohesion: 0.11
Nodes (17): _chat_response_with_memory_call(), _FakeOpenAI, _make_agent(), Tests for flush_memories() working correctly across all provider modes.  Catches, When auxiliary client is unavailable and we fall back to direct         OpenAI c, When an auxiliary client is available, flush_memories should use it     instead, Non-Codex mode with no auxiliary falls back to self.client., Verify that memory tool calls from the flush response actually get executed. (+9 more)

### Community 140 - "Community 140"
Cohesion: 0.07
Nodes (5): TestDeduplication, TestDingTalkAdapterInit, TestDingTalkRequirements, TestExtractText, TestPlatformEnum

### Community 141 - "Community 141"
Cohesion: 0.08
Nodes (10): Tests for agent.title_generator — auto-generated session titles., Tests for maybe_auto_title() — the fire-and-forget entry point., Should not fire for conversations with more than 2 user messages., Should fire a background thread for the first exchange., Unit tests for generate_title()., Long user/assistant messages should be truncated in the LLM request., Tests for auto_title_session() — the sync worker function., TestAutoTitleSession (+2 more)

### Community 142 - "Community 142"
Cohesion: 0.17
Nodes (25): cmd_book(), cmd_event(), cmd_history(), cmd_market(), cmd_price(), cmd_search(), cmd_trades(), cmd_trending() (+17 more)

### Community 143 - "Community 143"
Cohesion: 0.14
Nodes (16): _make_author(), _make_message(), Tests for Discord bot message filtering (DISCORD_ALLOW_BOTS)., Create a mock Discord author., Default behavior (no env var) should be 'none'., Allow_bots value should be case-insensitive., Create a mock Discord message., Test the DISCORD_ALLOW_BOTS filtering logic. (+8 more)

### Community 144 - "Community 144"
Cohesion: 0.08
Nodes (7): StickerCache, Tests for gateway/sticker_cache.py — sticker description cache., set_name alone (no emoji) produces no context — only emoji+set_name triggers 'fr, TestBuildAnimatedStickerInjection, TestBuildStickerInjection, TestCacheSticker, TestLoadSaveCache

### Community 145 - "Community 145"
Cohesion: 0.08
Nodes (10): Tests for build_tool_preview defensive handling and normal operation., PR #453: None args should not crash, should return None., Empty dict has no keys to preview., Known tool with its primary arg should return a preview string., Unknown tool but with a recognized fallback key should still preview., Unknown tool with no recognized keys should return None., Preview should truncate long values., Process tool special case should also handle None args. (+2 more)

### Community 146 - "Community 146"
Cohesion: 0.13
Nodes (13): Hook Registry, _create_hook(), _patch_no_builtins(), Tests for gateway/hooks.py — event hook system., Helper to create a hook directory with HOOK.yaml and handler.py., Suppress built-in hook registration so tests only exercise user-hook discovery., test_emit_calls_sync_handler(), test_emit_default_context() (+5 more)

### Community 147 - "Community 147"
Cohesion: 0.11
Nodes (14): _make_response(), Tests for None guard on browser_tool LLM response content.  browser_tool.py has, Build a minimal OpenAI-compatible ChatCompletion response stub., When LLM returns None content, should fall back to truncated snapshot., Normal string content should pass through., Empty string content should also fall back to truncated., tools/browser_tool.py — browser_vision() analysis extraction, When LLM returns None content, analysis should have a fallback message. (+6 more)

### Community 148 - "Community 148"
Cohesion: 0.14
Nodes (9): Tests for the config.yaml → env var bridge logic in gateway/run.py.  Specificall, cwd: '.' should trigger MESSAGING_CWD fallback., MESSAGING_CWD in initial env should be picked up as fallback., Explicit top-level cwd should take precedence over MESSAGING_CWD., Simulate the gateway config bridge logic from gateway/run.py.      Returns the r, Top-level `cwd:` should be treated as `terminal.cwd`., terminal.cwd should win over top-level cwd., _simulate_config_bridge() (+1 more)

### Community 149 - "Community 149"
Cohesion: 0.13
Nodes (21): determine_api_mode(), get_label(), get_overlay(), get_provider(), HermesOverlay, is_aggregator(), normalize_provider(), ProviderDef (+13 more)

### Community 150 - "Community 150"
Cohesion: 0.15
Nodes (18): _jwt_with_email(), Tests for auth subcommands backed by the credential pool., Removing an env-seeded credential should also clear the env var from .env     so, After removing an env-seeded credential, load_pool should NOT re-create it., Removing a manually-added credential should NOT touch .env., test_auth_add_anthropic_oauth_persists_pool_entry(), test_auth_add_api_key_persists_manual_entry(), test_auth_add_codex_oauth_persists_pool_entry() (+10 more)

### Community 151 - "Community 151"
Cohesion: 0.19
Nodes (20): _build_folder_listing(), _code_fence_language(), ContextReference, ContextReferenceResult, _ensure_reference_path_allowed(), _expand_file_reference(), _expand_folder_reference(), _expand_git_reference() (+12 more)

### Community 152 - "Community 152"
Cohesion: 0.14
Nodes (20): arXiv REST API, arXiv Research Skill, Autoreason Iterative Refinement Methodology, blogwatcher-cli, Blogwatcher Skill, Citation Management & Hallucination Prevention, Conference Paper Checklists, Experiment Design Patterns (+12 more)

### Community 153 - "Community 153"
Cohesion: 0.09
Nodes (14): Singularity/Apptainer, Singularity Environment Module, Tests for Singularity/Apptainer preflight availability check.  Verifies that a c, _find_singularity_executable resolution tests., When both are available, apptainer should be preferred., When only singularity is available, use it., Must raise RuntimeError with install instructions., _ensure_singularity_available preflight tests. (+6 more)

### Community 154 - "Community 154"
Cohesion: 0.16
Nodes (22): Landing Page JavaScript, Hermes CLI Main Entry Point, MCP Server Management CLI, Memory Provider Setup Wizard, Per-Provider Model Name Normalization, Model Switching Core Pipeline, Model Catalogs and Validation Helpers, Nous Subscription Feature State (+14 more)

### Community 155 - "Community 155"
Cohesion: 0.34
Nodes (20): Copy-ConfigTemplates(), Install-Dependencies(), Install-NodeDeps(), Install-Repository(), Install-SystemPackages(), Install-Uv(), Install-Venv(), Invoke-SetupWizard() (+12 more)

### Community 156 - "Community 156"
Cohesion: 0.13
Nodes (14): _path_escapes_skill_dir(), Tests for the skill_view path boundary check.  Regression test: the original che, Reproduce the boundary check from tools/skills_tool.py.      Returns True when t, Verify the path boundary check works on all platforms., A file inside the skill directory must NOT be flagged., Deeply nested valid paths must also pass., A file outside the skill directory must be flagged., A file in a sibling skill directory must be flagged.          This catches prefi (+6 more)

### Community 157 - "Community 157"
Cohesion: 0.14
Nodes (19): build_plan_path(), build_preloaded_skills_prompt(), build_skill_invocation_message(), _build_skill_message(), get_skill_commands(), _inject_skill_config(), _load_skill_payload(), Shared slash command helpers for skills and built-in prompt-style modes.  Shared (+11 more)

### Community 158 - "Community 158"
Cohesion: 0.1
Nodes (7): Tests for file permissions hardening on sensitive files., Test the _secure_file and _secure_dir helpers., Verify cron files get secure permissions., Verify config files get secure permissions., TestConfigFilePermissions, TestCronFilePermissions, TestSecureHelpers

### Community 159 - "Community 159"
Cohesion: 0.13
Nodes (12): _make_adapter(), _make_request(), Tests for SSE client disconnect → agent task cancellation.  When a streaming /v1, BrokenPipeError (another disconnect variant) also cancels the task., If agent already finished before disconnect, don't try to cancel., When the client disconnects, agent.interrupt() must be called         so the age, Build a minimal APIServerAdapter with mocked internals., When agent_ref is not provided (None), the task is still cancelled         on di (+4 more)

### Community 160 - "Community 160"
Cohesion: 0.1
Nodes (19): Tests for agent.retry_utils jittered backoff., Base delay should double each attempt (before jitter)., Even with high attempt numbers, delay should not exceed max_delay., With jitter enabled, delays should vary across calls., First attempt delay should equal base_delay (with no jitter)., base_delay=0 should return max_delay (guard against busy-wait)., Very large attempt numbers should not overflow and should return max_delay., Negative attempt should not crash and behaves like attempt=1. (+11 more)

### Community 161 - "Community 161"
Cohesion: 0.14
Nodes (19): detect_vendor(), _dots_to_hyphens(), is_aggregator_provider(), model_display_name(), _normalize_for_deepseek(), normalize_model_for_provider(), _prepend_vendor(), Per-provider model name normalization.  Different LLM providers expect model ide (+11 more)

### Community 162 - "Community 162"
Cohesion: 0.13
Nodes (12): _mock_httpx_client(), Different model architectures use different key prefixes in model_info., Should return None if model_info has no context_length key., Create a mock httpx.Client context manager that returns given /api/show data., Test the Ollama /api/show context length query., Should extract context_length from GGUF model_info metadata., If the Modelfile sets num_ctx explicitly, that should take priority., Should return None if the server is not Ollama. (+4 more)

### Community 163 - "Community 163"
Cohesion: 0.19
Nodes (17): calendar_create(), calendar_delete(), calendar_list(), contacts_list(), docs_get(), drive_search(), gmail_get(), gmail_labels() (+9 more)

### Community 164 - "Community 164"
Cohesion: 0.15
Nodes (3): switchPlatform(), switchStepPlatform(), TerminalDemo

### Community 165 - "Community 165"
Cohesion: 0.11
Nodes (8): Tests for skill fuzzy patching via tools.fuzzy_match., Fuzzy matching should also work on supporting files., Fuzzy matching should still run frontmatter validation on SKILL.md., The dispatcher should route to the fuzzy-matching patch., Patch with extra leading whitespace should still find the target., Patch where only indentation differs should succeed., Multiple fuzzy matches should return an error without replace_all., TestFuzzyPatchSkill

### Community 166 - "Community 166"
Cohesion: 0.11
Nodes (5): Tests for _ThreadedProcessHandle — the adapter for SDK backends., TestBasicExecution, TestCancelFn, TestPolling, TestStdoutPipe

### Community 167 - "Community 167"
Cohesion: 0.22
Nodes (17): Atropos RL Training Integration, AgentResult, HermesAgentLoop, AgenticOPDEnv, HermesAgentBaseEnv, HermesAgentEnvConfig, apply_patches(), Monkey patches for making hermes-agent tools work inside async frameworks (Atrop (+9 more)

### Community 168 - "Community 168"
Cohesion: 0.11
Nodes (10): config_home(), Tests that provider selection via `hermes model` always persists correctly.  Reg, _model_flow_copilot should persist provider/base_url/model together., _model_flow_copilot_acp should persist provider/base_url/model together., Isolated HERMES_HOME with a minimal string-format config., When config.model is a plain string, _save_model_choice must         convert it, When config.model is already a dict, _save_model_choice preserves it., _model_flow_api_key_provider must persist the provider even when         config. (+2 more)

### Community 169 - "Community 169"
Cohesion: 0.16
Nodes (8): _patch_info(), Tests for GatewayRunner._format_session_info — session config surfacing., If runtime resolution raises, should still produce output., Create a bare GatewayRunner without __init__., Return a context-manager stack that patches _format_session_info deps., No config.yaml should not crash., runner(), TestFormatSessionInfo

### Community 170 - "Community 170"
Cohesion: 0.11
Nodes (11): Tests for the AsyncHttpxClientWrapper.__del__ neuter fix.  The OpenAI SDK's ``As, Entries with an open loop should be preserved., Sync entries (cached_loop=None) should be preserved., Verify neuter_async_httpx_del replaces __del__ on the SDK class., After neuter, __del__ should do nothing (no RuntimeError)., Calling neuter twice doesn't break anything., neuter_async_httpx_del doesn't raise if the openai SDK isn't installed., Verify stale cache entries are evicted and force-closed. (+3 more)

### Community 171 - "Community 171"
Cohesion: 0.27
Nodes (16): check(), check_bot_permissions(), check_config(), check_env_vars(), check_packages(), check_system_tools(), main(), mask() (+8 more)

### Community 172 - "Community 172"
Cohesion: 0.16
Nodes (10): _make_cli(), Tests for automatic MCP reload when config.yaml mcp_servers section changes., If mtime and mcp_servers unchanged, _reload_mcp is NOT called., If file mtime changes but mcp_servers is identical, no reload., Adding a new MCP server to config triggers auto-reload., Removing an MCP server from config triggers auto-reload., Create a minimal HermesCLI instance with mocked config., If called within CONFIG_WATCH_INTERVAL, stat() is skipped. (+2 more)

### Community 173 - "Community 173"
Cohesion: 0.15
Nodes (9): _clean_for_display(), Gateway streaming consumer — bridges sync agent callbacks to async platform deli, Async task that drains the queue and edits the platform message., Send a new message chunk, optionally threaded to a previous message.          Re, Return the visible text already shown in the streamed message., Return only the part of final_text the user has not already seen., Send the final continuation after streaming edits stop working., Send or edit the streaming message. (+1 more)

### Community 174 - "Community 174"
Cohesion: 0.15
Nodes (15): copilot_device_code_login(), copilot_request_headers(), _gh_cli_candidates(), is_classic_pat(), GitHub Copilot authentication utilities.  Implements the OAuth device code flow, Return candidate ``gh`` binary paths, including common Homebrew installs., Return a token from ``gh auth token`` when the GitHub CLI is available., Run the GitHub OAuth device code flow for Copilot.      Prints instructions for (+7 more)

### Community 175 - "Community 175"
Cohesion: 0.25
Nodes (6): EvidenceStore, main(), _now_iso(), Re-compute SHA-256 for all entries and report mismatches., Search for keyword in content, source, actor, or url., _sha256()

### Community 176 - "Community 176"
Cohesion: 0.18
Nodes (12): discover_fallback_ips(), _is_retryable_connect_error(), _normalize_fallback_ips(), parse_fallback_ip_env(), _query_doh_provider(), Telegram-specific network helpers.  Provides a hostname-preserving fallback tran, Return the IPv4 addresses that the OS resolver gives for api.telegram.org., Query one DoH provider and return A-record IPs. (+4 more)

### Community 177 - "Community 177"
Cohesion: 0.3
Nodes (9): _build_agent(), _connection_error(), FakeRequestClient, FakeSharedClient, OpenAIFactory, test_closed_shared_client_is_recreated_before_request(), test_concurrent_requests_do_not_break_each_other_when_one_client_closes(), test_retry_after_api_connection_error_recreates_request_client() (+1 more)

### Community 178 - "Community 178"
Cohesion: 0.13
Nodes (8): Tests for save_config_value() in cli.py — atomic write behavior., save_config_value() must use atomic_yaml_write to avoid data loss., save_config_value must route through atomic_yaml_write, not bare open()., Writing a new key must not clobber existing config entries., Dot-separated paths create intermediate dicts as needed., Updating an existing key replaces the value., If atomic_yaml_write raises, the original file is untouched., TestSaveConfigValueAtomic

### Community 179 - "Community 179"
Cohesion: 0.15
Nodes (13): bulk_check(), check_available(), check_ssl(), dns_records(), main(), Query WHOIS servers for domain registration info., Resolve DNS records using system DNS + Google DoH., Check domain availability using passive signals (DNS + WHOIS + SSL). (+5 more)

### Community 180 - "Community 180"
Cohesion: 0.14
Nodes (8): Tests for delegate_tool toolset scoping.  Verifies that subagents cannot gain to, Subagent toolsets must be a subset of parent's enabled_toolsets., LLM requests toolsets parent doesn't have — extras are dropped., LLM requests subset of parent tools — all pass through., When toolsets is None/empty, child inherits parent's set., Blocked toolsets (delegation, clarify, etc.) are always removed., If parent has no overlap with requested, child gets nothing extra., TestToolsetIntersection

### Community 181 - "Community 181"
Cohesion: 0.14
Nodes (5): Regression tests for browser session cleanup and screenshot recovery., When camofox mode + managed persistence, soft_cleanup fires instead of close., When camofox mode but managed persistence is off, camofox_close fires., TestBrowserCleanup, TestScreenshotPathRecovery

### Community 182 - "Community 182"
Cohesion: 0.14
Nodes (5): Regression tests for cron prompt injection scanner bypass.  The original regex `, Multi-word variants that previously bypassed the scanner., Original single-word patterns must still be caught., Ensure the broader regex doesn't create false positives., TestMultiWordInjectionBypass

### Community 183 - "Community 183"
Cohesion: 0.17
Nodes (13): Cardiac and Autonomic Metrics, EEG Frequency Bands, Flow State Pattern, NeuroSkill Metric Definitions, Muse 2 Headband, Muse S Headband, NeuroSkill WebSocket & HTTP API, NeuroSkill BCI Integration (+5 more)

### Community 184 - "Community 184"
Cohesion: 0.15
Nodes (0): 

### Community 185 - "Community 185"
Cohesion: 0.15
Nodes (12): crt.sh (Certificate Transparency), ddgs Python Package / CLI, Domain Intelligence Skill, DuckDuckGo Search Skill, Google DNS-over-HTTPS, parallel-cli (CLI tool), Parallel CLI Skill, Playwright (+4 more)

### Community 186 - "Community 186"
Cohesion: 0.23
Nodes (13): ASCII Art Skill, ASCII Video Architecture Reference, ASCII Video Composition Reference, ASCII Video Effects Catalog, ASCII Video Input Sources, ASCII Video Optimization Reference, ASCII Video Scene System, ASCII Video Shader Pipeline (+5 more)

### Community 187 - "Community 187"
Cohesion: 0.21
Nodes (13): BootstrapFewShot, BootstrapFinetune, COPRO, DSPy, dspy.ChainOfThought, dspy.MultiChainComparison, dspy.Predict, dspy.ProgramOfThought (+5 more)

### Community 188 - "Community 188"
Cohesion: 0.27
Nodes (12): _clear_terminal_env(), Local backend uses Hermes' own LocalEnvironment wrapper., Remove terminal env vars that could affect requirements checks., test_local_terminal_requirements(), test_modal_backend_auto_mode_prefers_managed_gateway_over_direct_creds(), test_modal_backend_direct_mode_does_not_fall_back_to_managed(), test_modal_backend_managed_mode_does_not_fall_back_to_direct(), test_modal_backend_managed_mode_without_feature_flag_logs_clear_error() (+4 more)

### Community 189 - "Community 189"
Cohesion: 0.22
Nodes (5): _load_module(), Tests for Hermes-managed Camofox state helpers., TestCamofoxConfigDefaults, TestCamofoxIdentity, TestCamofoxStatePaths

### Community 190 - "Community 190"
Cohesion: 0.21
Nodes (5): _DummyCLI, _make_real_cli(), show_banner() no longer prints the activated skills line — it moved to run()., test_main_raises_for_unknown_preloaded_skill(), test_show_banner_does_not_print_skills()

### Community 191 - "Community 191"
Cohesion: 0.21
Nodes (12): GitHub REST API, Conventional Commits, CI Troubleshooting Quick Reference, Conventional Commits Quick Reference, GitHub REST API Cheatsheet, GitHub Pull Request Workflow, GitHub Repository Management, Bug Report Template (+4 more)

### Community 192 - "Community 192"
Cohesion: 0.27
Nodes (5): _make_cli(), Tests for protected HermesCLI TUI extension hooks.  Verifies that wrapper CLIs c, Create a HermesCLI with prompt_toolkit stubs (same pattern as test_cli_init)., TestExtensionHookDefaults, TestExtensionHookSubclass

### Community 193 - "Community 193"
Cohesion: 0.18
Nodes (11): Manim Video Production Pipeline, Manim Video Skill Definition, Manim Core Animations Reference, SurroundingRectangle Highlight, Manim Equations and LaTeX Reference, Algorithm Visualization Pattern, Manim Axes and Plotting, Manim Mobjects (Text, Shapes, Groups) (+3 more)

### Community 194 - "Community 194"
Cohesion: 0.33
Nodes (10): clean_unused_files(), get_referenced_files(), get_slide_referenced_files(), get_slides_in_sldidlst(), Remove unreferenced files from an unpacked PPTX directory.  Usage: python clean., remove_orphaned_files(), remove_orphaned_rels_files(), remove_orphaned_slides() (+2 more)

### Community 195 - "Community 195"
Cohesion: 0.27
Nodes (9): _check_config(), _headers(), list_assignments(), list_courses(), _paginated_get(), Validate required environment variables are set., Fetch all pages up to max_items, following Canvas Link headers., List enrolled courses. (+1 more)

### Community 196 - "Community 196"
Cohesion: 0.18
Nodes (7): fake_scratch(), Tests for get_active_environments_info disk usage calculation., Create fake hermes scratch directories with known sizes., Each task should only count its own directories, not all hermes-* dirs., With 2 active tasks, each should count only its own dirs., TestDiskUsageGlob, TestDiskUsageWarningHardening

### Community 197 - "Community 197"
Cohesion: 0.27
Nodes (5): _force_remove_worktree(), git_repo(), Security-focused integration tests for CLI worktree setup., Create a temporary git repo for testing real cli._setup_worktree behavior., TestWorktreeIncludeSecurity

### Community 198 - "Community 198"
Cohesion: 0.18
Nodes (1): Regression tests for sudo detection and sudo password handling.

### Community 199 - "Community 199"
Cohesion: 0.29
Nodes (11): brv CLI Integration, ByteRoverMemoryProvider, Dedicated Async Event Loop, HindsightMemoryProvider, FactRetriever, HRR Phase Encoding Module, HolographicMemoryProvider, MemoryStore (SQLite) (+3 more)

### Community 200 - "Community 200"
Cohesion: 0.27
Nodes (11): Boundary Inversion Technique, Auto-Jailbreak Pipeline, GODMODE CLASSIC Attack, PARSELTONGUE Obfuscation, Prefill Messages, Refusal Inversion Technique, ULTRAPLINIAN Multi-Model Racing, G0DM0D3 Godmode Jailbreaking Skill (+3 more)

### Community 201 - "Community 201"
Cohesion: 0.31
Nodes (9): _add_forward_compat_models(), _fetch_models_from_api(), get_codex_model_ids(), Codex model discovery from API, local cache, and config., Return available Codex model IDs, trying API first, then local sources., Add Clawdbot-style synthetic forward-compat Codex models.      If a newer Codex, Fetch available models from the Codex API. Returns visible models sorted by prio, _read_cache_models() (+1 more)

### Community 202 - "Community 202"
Cohesion: 0.31
Nodes (9): find_nearby(), geocode(), haversine(), _http_get(), _http_post(), main(), Distance in meters between two coordinates., Convert address/city/zip to coordinates via Nominatim. (+1 more)

### Community 203 - "Community 203"
Cohesion: 0.31
Nodes (9): _connect(), describe_table(), list_tables(), query(), List user-defined SQLite tables., Describe columns for a SQLite table., Run a read-only SELECT query and return rows plus column names., _reject_mutation() (+1 more)

### Community 204 - "Community 204"
Cohesion: 0.36
Nodes (9): Telephony Skill Script, load_module(), test_diagnose_includes_decision_tree_and_saved_state(), test_messages_after_checkpoint_returns_only_newer_items(), test_save_twilio_writes_env_and_state(), test_twilio_buy_number_saves_env_and_state(), test_twilio_inbox_marks_seen_checkpoint(), test_upsert_env_updates_existing_values() (+1 more)

### Community 205 - "Community 205"
Cohesion: 0.27
Nodes (9): API Wrapper MCP Template, httpx HTTP Client, Database Server MCP Template, SQLite Read-Only Server, FastMCP CLI Reference, FastMCP Python Library, FastMCP Skill, File Processor MCP Template (+1 more)

### Community 206 - "Community 206"
Cohesion: 0.44
Nodes (7): _add_to_content_types(), _add_to_presentation_rels(), create_slide_from_layout(), duplicate_slide(), _get_next_slide_id(), get_next_slide_number(), Add a new slide to an unpacked PPTX directory.  Usage: python add_slide.py <unpa

### Community 207 - "Community 207"
Cohesion: 0.33
Nodes (4): Tests for the startup allowlist warning check in gateway/run.py., Replicate the startup allowlist warning logic. Returns True if warning fires., TestAllowlistStartupCheck, _would_warn()

### Community 208 - "Community 208"
Cohesion: 0.22
Nodes (9): Flash Attention Performance Benchmarks, Flash Attention, flash-attn Library, FlashAttention-3 FP8 on H100, PyTorch Scaled Dot Product Attention, LightningModule, PyTorch Lightning, Lightning Trainer Class (+1 more)

### Community 209 - "Community 209"
Cohesion: 0.22
Nodes (4): Tests for tools.environments.docker.find_docker — Docker CLI discovery., Clear the module-level docker executable cache between tests., _reset_cache(), TestFindDocker

### Community 210 - "Community 210"
Cohesion: 0.36
Nodes (8): get_hermes_home(), get_token_path(), get_valid_token(), main(), Refresh the access token using the refresh token., Return a valid access token, refreshing if needed., Refresh token if needed, then exec gws with remaining args., refresh_token()

### Community 211 - "Community 211"
Cohesion: 0.33
Nodes (8): get_resource(), _headers(), health_check(), Check whether the upstream API is reachable., Fetch one resource by ID from the upstream API., Search upstream resources by query string., _request(), search_resources()

### Community 212 - "Community 212"
Cohesion: 0.22
Nodes (0): 

### Community 213 - "Community 213"
Cohesion: 0.22
Nodes (2): agent.smart_model_routing, hermes_cli.runtime_provider

### Community 214 - "Community 214"
Cohesion: 0.36
Nodes (4): _load_ensure_ssl(), Tests for SSL certificate auto-detection in gateway/run.py., Import _ensure_ssl_certs fresh (gateway/run.py has heavy deps, so we     extract, TestEnsureSslCerts

### Community 215 - "Community 215"
Cohesion: 0.5
Nodes (7): _build_tar_b64(), _load_terminalbench_module(), Security tests for Terminal-Bench 2 archive extraction., _stub_module(), test_extract_base64_tar_allows_safe_files(), test_extract_base64_tar_rejects_path_traversal(), test_extract_base64_tar_rejects_symlinks()

### Community 216 - "Community 216"
Cohesion: 0.36
Nodes (7): extract_video_id(), fetch_transcript(), format_timestamp(), main(), Extract the 11-character video ID from various YouTube URL formats., Convert seconds to HH:MM:SS or MM:SS format., Fetch transcript segments from YouTube.      Returns a list of dicts with 'text'

### Community 217 - "Community 217"
Cohesion: 0.25
Nodes (7): convert_scratchpad_to_think(), has_incomplete_scratchpad(), Trajectory saving utilities and static helpers.  _convert_to_trajectory_format s, Convert <REASONING_SCRATCHPAD> tags to <think> tags., Check if content has an opening <REASONING_SCRATCHPAD> without a closing tag., Append a trajectory entry to a JSONL file.      Args:         trajectory: The Sh, save_trajectory()

### Community 218 - "Community 218"
Cohesion: 0.36
Nodes (7): Return basic metadata and a preview for a UTF-8 text file., Find matching lines in a UTF-8 text file., Expose a text file as a resource., read_file_resource(), _read_text(), search_text_file(), summarize_text_file()

### Community 219 - "Community 219"
Cohesion: 0.25
Nodes (5): Tests for KeyboardInterrupt handling in exit cleanup paths.  ``except Exception`, cron/scheduler.py — end_session + close in the finally block., If end_session raises KeyboardInterrupt, close() must still run., If close() raises KeyboardInterrupt, it must not escape run_job., TestCronJobCleanup

### Community 220 - "Community 220"
Cohesion: 0.43
Nodes (7): Chroma Embedding Database, Chroma Integration Guide, FAISS Similarity Search, HNSW Index, IVF Index, FAISS Index Types Guide, Product Quantization

### Community 221 - "Community 221"
Cohesion: 0.29
Nodes (4): sessions delete should not crash when stdin is closed (non-TTY)., sessions prune should not crash when stdin is closed (non-TTY)., test_sessions_delete_handles_eoferror_on_confirm(), test_sessions_prune_handles_eoferror_on_confirm()

### Community 222 - "Community 222"
Cohesion: 0.33
Nodes (7): Autonomous AI Agents Category, Blackbox CLI Skill, Communication Category, Health Category, Honcho Memory Skill, 1-3-1 Rule Skill, Hermes Optional Skills

### Community 223 - "Community 223"
Cohesion: 0.29
Nodes (7): Design System: Replicate, Design System: Resend, Design System: Sentry, Design System: Vercel, Design System: VoltAgent, Design System: Warp, Design System: xAI

### Community 224 - "Community 224"
Cohesion: 0.29
Nodes (7): HNSW Index, Qdrant Vector Similarity Search Engine, Qdrant Advanced Usage, Qdrant Distributed Deployment, Qdrant Hybrid Search (Dense + Sparse), Qdrant Quantization Strategies, Qdrant Troubleshooting Guide

### Community 225 - "Community 225"
Cohesion: 0.43
Nodes (7): AudioCraft Advanced Usage Guide, AudioCraft Audio Generation Skill, AudioCraft Troubleshooting Guide, AudioGen Text-to-Sound, EnCodec Neural Audio Codec, Models Description, MusicGen Text-to-Music

### Community 226 - "Community 226"
Cohesion: 0.29
Nodes (1): TestResolveCdpOverride

### Community 227 - "Community 227"
Cohesion: 0.38
Nodes (7): Review Output Template, GitHub Skills, Codebase Inspection (pygount), GitHub Authentication Setup, GitHub Code Review, GitHub Issues Management, Webhook Subscriptions

### Community 228 - "Community 228"
Cohesion: 0.33
Nodes (5): _mask_token(), Regex-based secret redaction for logs and tool output.  Applies pattern matching, Mask a token, preserving prefix for long tokens., Apply all redaction patterns to a block of text.      Safe to call on any string, redact_sensitive_text()

### Community 229 - "Community 229"
Cohesion: 0.29
Nodes (0): 

### Community 230 - "Community 230"
Cohesion: 0.33
Nodes (6): EarlyStopping, GradientAccumulationScheduler, LearningRateMonitor, ModelCheckpoint, PyTorch Lightning Callbacks, StochasticWeightAveraging

### Community 231 - "Community 231"
Cohesion: 0.33
Nodes (6): EvidenceStore Manager, Observation Types (RAPTOR), Evidence Verification States, Forensic Investigation Report Template, Malicious Package Investigation Report Template, Evidence Recording via evidence-store.py

### Community 232 - "Community 232"
Cohesion: 0.33
Nodes (6): Evidence Store (evidence-store.py), GitHub Archive (BigQuery), OSS Forensics Skill, Security Skills Category, Supply Chain Attack Investigation, Wayback Machine CDX API

### Community 233 - "Community 233"
Cohesion: 0.33
Nodes (0): 

### Community 234 - "Community 234"
Cohesion: 0.4
Nodes (6): Skill Categories, skills.json Data File, extract-skills.py Script, Skills Dashboard Page, Docusaurus, React

### Community 235 - "Community 235"
Cohesion: 0.47
Nodes (5): concat_buffers(), main(), Build the Excalidraw v2 concat-buffers binary format.      Layout: [version=1 (4, Encrypt and upload Excalidraw JSON to excalidraw.com.      Args:         excalid, upload()

### Community 236 - "Community 236"
Cohesion: 0.6
Nodes (5): _consolidate_small_categories(), extract_cached_index_skills(), extract_local_skills(), _guess_category(), main()

### Community 237 - "Community 237"
Cohesion: 0.4
Nodes (6): Accelerate Custom Plugins, DeepSpeed ZeRO, FSDP (Fully Sharded Data Parallel), HuggingFace Accelerate, Megatron-LM Integration, Accelerate Performance Tuning

### Community 238 - "Community 238"
Cohesion: 0.33
Nodes (6): Neuronpedia, SAE Class (Sparse Autoencoder Model), SAETrainingRunner, SAELens: Sparse Autoencoders for Mechanistic Interpretability, Sparse Autoencoders (SAE), TransformerLens

### Community 239 - "Community 239"
Cohesion: 0.4
Nodes (5): apply_anthropic_cache_control(), _apply_cache_marker(), Anthropic prompt caching (system_and_3 strategy).  Reduces input token costs by, Add cache_control to a single message, handling all format variations., Apply system_and_3 caching strategy to messages for Anthropic models.      Place

### Community 240 - "Community 240"
Cohesion: 0.4
Nodes (6): HuggingFace Alignment Handbook, DPO (Direct Preference Optimization), SimPO - Simple Preference Optimization, SimPO Datasets Guide, SimPO Hyperparameters Guide, SimPO Loss Functions (Sigmoid/Hinge)

### Community 241 - "Community 241"
Cohesion: 0.53
Nodes (6): ASCII Video README, Claude Code Skill, Codex CLI Skill, Find My Apple Skill, Hermes Agent Skill, OpenCode CLI Skill

### Community 242 - "Community 242"
Cohesion: 0.6
Nodes (4): expandWhatsAppIdentifiers(), matchesAllowedUser(), normalizeWhatsAppIdentifier(), readMappingFile()

### Community 243 - "Community 243"
Cohesion: 0.5
Nodes (4): _load_dotenv_with_fallback(), load_hermes_dotenv(), Helpers for loading Hermes .env files consistently across entrypoints., Load Hermes environment files with user config taking precedence.      Behavior:

### Community 244 - "Community 244"
Cohesion: 0.4
Nodes (5): p5.js Production Pipeline, p5.js Skill Definition, Manim Rate Functions, p5.js Easing Functions, p5.js HSB Color Mode

### Community 245 - "Community 245"
Cohesion: 0.6
Nodes (5): GitHub Archive Event Types, GitHub Archive BigQuery Guide, Supply Chain Attack Investigation Templates, Deleted Content Recovery Techniques, Sherlock OSINT Username Search Skill

### Community 246 - "Community 246"
Cohesion: 0.5
Nodes (5): Serverless GPU Computing, Modal Advanced Usage Guide, Modal Troubleshooting Guide, Modal Serverless GPU, Modal

### Community 247 - "Community 247"
Cohesion: 0.4
Nodes (5): BillingRoute Data Model, CanonicalUsage Data Model, CostResult Data Model, Pricing Accuracy Architecture, Pricing Catalog Subsystem

### Community 248 - "Community 248"
Cohesion: 0.6
Nodes (4): _condense_xml(), pack(), Pack a directory into a DOCX, PPTX, or XLSX file.  Validates with auto-repair, c, _run_validation()

### Community 249 - "Community 249"
Cohesion: 0.5
Nodes (4): _load_optional_dependencies(), Regression tests for packaging metadata in pyproject.toml., matrix-nio[e2e] depends on python-olm which is upstream-broken on modern     mac, test_matrix_extra_exists_but_excluded_from_all()

### Community 250 - "Community 250"
Cohesion: 0.4
Nodes (5): Honcho Integration Spec, AI Peer Identity Formation Pattern, Async Prefetch Pattern, Dynamic Reasoning Level Pattern, Per-Peer Memory Modes Pattern

### Community 251 - "Community 251"
Cohesion: 0.6
Nodes (5): Base Blockchain Skill, Base Blockchain Client, CoinGecko Price API, Solana Blockchain Client, Solana Blockchain Skill

### Community 252 - "Community 252"
Cohesion: 1.0
Nodes (3): list_templates(), main(), render_template()

### Community 253 - "Community 253"
Cohesion: 0.5
Nodes (2): Fake Home Assistant server for integration testing.  Provides a real HTTP + WebS, Home Assistant Integration

### Community 254 - "Community 254"
Cohesion: 0.67
Nodes (3): main(), Write a WAV file from float32 samples (no soundfile dependency)., _write_wav()

### Community 255 - "Community 255"
Cohesion: 0.67
Nodes (4): YouTube Transcript API, YouTube Output Format Examples, fetch_transcript.py, YouTube Content Tool

### Community 256 - "Community 256"
Cohesion: 0.5
Nodes (4): Himalaya Configuration Reference, Message Composition (MML), Email Skills, Himalaya Email CLI

### Community 257 - "Community 257"
Cohesion: 0.5
Nodes (2): check_requirements(), Check disk space before installing.

### Community 258 - "Community 258"
Cohesion: 0.67
Nodes (4): Optuna Integration, Hyperparameter Tuning with PyTorch Lightning, Ray Tune Integration, Weights & Biases Sweeps

### Community 259 - "Community 259"
Cohesion: 0.5
Nodes (4): Design System: Revolut, Design System: Superhuman, Design System: Uber, Design System: Wise

### Community 260 - "Community 260"
Cohesion: 0.5
Nodes (3): jittered_backoff(), Retry utilities — jittered backoff for decorrelated retries.  Replaces fixed exp, Compute a jittered exponential backoff delay.      Args:         attempt: 1-base

### Community 261 - "Community 261"
Cohesion: 0.5
Nodes (2): Register built-in hooks that are always active., Scan the hooks directory for hook directories and load their handlers.

### Community 262 - "Community 262"
Cohesion: 0.5
Nodes (3): has_binary_extension(), Binary file extensions to skip for text-based operations.  These files can't be, Check if a file path has a binary extension. Pure string check, no I/O.

### Community 263 - "Community 263"
Cohesion: 0.5
Nodes (1): setup-hermes.sh

### Community 264 - "Community 264"
Cohesion: 0.5
Nodes (4): Gaming Skills, Minecraft Modpack Server Setup, Pokemon Player, Songwriting & AI Music Generation

### Community 265 - "Community 265"
Cohesion: 0.5
Nodes (1): Regression tests for CLI /retry history replacement semantics.

### Community 266 - "Community 266"
Cohesion: 0.5
Nodes (4): Agent Client Protocol (ACP), Migration Skills Category, OpenClaw to Hermes Migration, Migrator Class

### Community 267 - "Community 267"
Cohesion: 0.5
Nodes (1): Regression tests for invalid/None terminal command handling.

### Community 268 - "Community 268"
Cohesion: 0.5
Nodes (4): AgentResult Dataclass, Atropos BaseEnv, HermesAgentBaseEnv, HermesAgentLoop

### Community 269 - "Community 269"
Cohesion: 0.67
Nodes (3): HeartMuLa Music Generation, Hugging Face Hub CLI, Hugging Face CLI (hf)

### Community 270 - "Community 270"
Cohesion: 1.0
Nodes (3): AgentResult, HermesAgentLoop, vLLM Integration

### Community 271 - "Community 271"
Cohesion: 0.67
Nodes (3): Lambda Labs Advanced Usage, Lambda Labs GPU Cloud, Lambda Labs Troubleshooting

### Community 272 - "Community 272"
Cohesion: 0.67
Nodes (0): 

### Community 273 - "Community 273"
Cohesion: 0.67
Nodes (3): CanonicalUsage, estimate_usage_cost, normalize_usage

### Community 274 - "Community 274"
Cohesion: 1.0
Nodes (3): Model Context Protocol (MCP), mcporter, Native MCP Client

### Community 275 - "Community 275"
Cohesion: 1.0
Nodes (3): Atomic JSON Write Tests, Atomic YAML Write Tests, Utils Module

### Community 276 - "Community 276"
Cohesion: 0.67
Nodes (3): Skills System Prompt Builder, Skill Command Resolution, SubdirectoryHintTracker

### Community 277 - "Community 277"
Cohesion: 0.67
Nodes (3): Issue Taxonomy, Dogfood QA Testing, Dogfood Report Template

### Community 278 - "Community 278"
Cohesion: 0.67
Nodes (3): CLIP Vision Encoder, LLaVA Vision-Language Model, LLaVA Training Guide

### Community 279 - "Community 279"
Cohesion: 1.0
Nodes (2): main(), parseArgs()

### Community 280 - "Community 280"
Cohesion: 0.67
Nodes (3): Bioinformatics Skills Gateway, bioSkills Repository (GPTomics/bioSkills), ClawBio Repository (ClawBio/ClawBio)

### Community 281 - "Community 281"
Cohesion: 0.67
Nodes (3): Design System: Stripe, Design System: Webflow, Design System: Zapier

### Community 282 - "Community 282"
Cohesion: 1.0
Nodes (3): OpenStreetMap APIs, find_nearby.py, Find Nearby

### Community 283 - "Community 283"
Cohesion: 0.67
Nodes (3): Meme Generator Script, Imgflip Meme API, Meme Generation Skill

### Community 284 - "Community 284"
Cohesion: 0.67
Nodes (3): EventBridge, mcp_serve Module, MCP Serve Tests

### Community 285 - "Community 285"
Cohesion: 1.0
Nodes (3): Apple Notes Skill, Apple Reminders Skill, Apple Skills Description

### Community 286 - "Community 286"
Cohesion: 0.67
Nodes (3): NeMo Curator Deduplication, NeMo Curator Quality Filtering, NeMo Curator

### Community 287 - "Community 287"
Cohesion: 0.67
Nodes (3): auto_title_session, generate_title, maybe_auto_title

### Community 288 - "Community 288"
Cohesion: 0.67
Nodes (3): Instructor Library, Instructor Provider Configuration, Pydantic Response Models

### Community 289 - "Community 289"
Cohesion: 1.0
Nodes (1): sidebars_config

### Community 290 - "Community 290"
Cohesion: 1.0
Nodes (2): Pinecone Deployment Guide, Pinecone Vector Database

### Community 291 - "Community 291"
Cohesion: 1.0
Nodes (2): Inference.sh CLI Skill, Inference.sh Platform

### Community 292 - "Community 292"
Cohesion: 1.0
Nodes (2): Production Quality Checklist, 12 Visual Design Principles

### Community 293 - "Community 293"
Cohesion: 1.0
Nodes (2): Delivery Router, Delivery Routing Tests

### Community 294 - "Community 294"
Cohesion: 1.0
Nodes (2): EVIDENCE_TYPES Constants, Evidence Types Taxonomy

### Community 295 - "Community 295"
Cohesion: 1.0
Nodes (2): get_pricing_entry, OpenRouter Pricing

### Community 296 - "Community 296"
Cohesion: 1.0
Nodes (2): acp_adapter.entry, test_acp_entry

### Community 297 - "Community 297"
Cohesion: 1.0
Nodes (2): WhatsApp Allowlist Module, WhatsApp Bridge Server

### Community 298 - "Community 298"
Cohesion: 1.0
Nodes (2): agent.retry_utils Module, Retry Utils Tests

### Community 299 - "Community 299"
Cohesion: 1.0
Nodes (2): EvidenceStore, Evidence Store Tests

### Community 300 - "Community 300"
Cohesion: 1.0
Nodes (2): Tenor GIF API, GIF Search (Tenor)

### Community 301 - "Community 301"
Cohesion: 1.0
Nodes (2): agent-browser CLI, Homebrew PATH discovery

### Community 302 - "Community 302"
Cohesion: 1.0
Nodes (2): IOC_TYPES Constants, IOC Types

### Community 303 - "Community 303"
Cohesion: 1.0
Nodes (2): check_website_access, load_website_blocklist

### Community 304 - "Community 304"
Cohesion: 1.0
Nodes (1): Default SOUL.md template seeded into HERMES_HOME on first run.

### Community 305 - "Community 305"
Cohesion: 1.0
Nodes (2): Packaging Metadata Tests, Project Metadata Tests

### Community 306 - "Community 306"
Cohesion: 1.0
Nodes (2): Hermes Agent Project, Termux Constraints

### Community 307 - "Community 307"
Cohesion: 1.0
Nodes (2): AES-GCM Client-Side Encryption, Excalidraw Upload Script

### Community 308 - "Community 308"
Cohesion: 1.0
Nodes (2): Atropos RL Training, RL Toolset

### Community 309 - "Community 309"
Cohesion: 1.0
Nodes (2): OAuth Authorization Code + PKCE Flow, Gemini OAuth Provider Implementation Plan

### Community 310 - "Community 310"
Cohesion: 1.0
Nodes (2): Data Science Skills, Jupyter Live Kernel (hamelnb)

### Community 311 - "Community 311"
Cohesion: 1.0
Nodes (2): Auto Title Generator, Trajectory Saver

### Community 312 - "Community 312"
Cohesion: 1.0
Nodes (0): 

### Community 313 - "Community 313"
Cohesion: 1.0
Nodes (2): Hermes Agent Homebrew Formula, Homebrew Packaging README

### Community 314 - "Community 314"
Cohesion: 1.0
Nodes (2): Design System: Runway, Design System: SpaceX

### Community 315 - "Community 315"
Cohesion: 1.0
Nodes (2): DingTalkAdapter, DingTalk Adapter Tests

### Community 316 - "Community 316"
Cohesion: 1.0
Nodes (2): Design System: Spotify, Design System: Supabase

### Community 317 - "Community 317"
Cohesion: 1.0
Nodes (2): Windows PowerShell Installer, Hermes Release Script

### Community 318 - "Community 318"
Cohesion: 1.0
Nodes (2): Note Taking, Obsidian Vault

### Community 319 - "Community 319"
Cohesion: 1.0
Nodes (2): Home Assistant Integration, Home Assistant Toolset

### Community 320 - "Community 320"
Cohesion: 1.0
Nodes (2): Honcho Memory Plugin, Pluggable Memory Provider Interface

### Community 321 - "Community 321"
Cohesion: 1.0
Nodes (1): Load configuration from YAML file.

### Community 322 - "Community 322"
Cohesion: 1.0
Nodes (1): Normalize summary-model output to a safe string.

### Community 323 - "Community 323"
Cohesion: 1.0
Nodes (1): Normalize summary text to include the expected prefix exactly once.

### Community 324 - "Community 324"
Cohesion: 1.0
Nodes (1): Validate and sanitize a session title.          - Strips leading/trailing whites

### Community 325 - "Community 325"
Cohesion: 1.0
Nodes (1): Sanitize user input for safe use in FTS5 MATCH queries.          FTS5 has its ow

### Community 326 - "Community 326"
Cohesion: 1.0
Nodes (1): Current audio input RMS level (0-32767). Updated each audio chunk.

### Community 327 - "Community 327"
Cohesion: 1.0
Nodes (1): Write numpy int16 audio data to a WAV file.          Returns the file path.

### Community 328 - "Community 328"
Cohesion: 1.0
Nodes (1): Strip shell startup warnings from the beginning of output.

### Community 329 - "Community 329"
Cohesion: 1.0
Nodes (1): Best-effort liveness check for host-visible PIDs.

### Community 330 - "Community 330"
Cohesion: 1.0
Nodes (1): Terminate a host-visible PID without requiring the original process handle.

### Community 331 - "Community 331"
Cohesion: 1.0
Nodes (1): Return the writable sandbox temp dir for env-backed background tasks.

### Community 332 - "Community 332"
Cohesion: 1.0
Nodes (1): Acquire an exclusive file lock for read-modify-write safety.          Uses a sep

### Community 333 - "Community 333"
Cohesion: 1.0
Nodes (1): Read a memory file and split into entries.          No file locking needed: _wri

### Community 334 - "Community 334"
Cohesion: 1.0
Nodes (1): Write entries to a memory file using atomic temp-file + rename.          Previou

### Community 335 - "Community 335"
Cohesion: 1.0
Nodes (1): Extract text from a ToolResultContent block.

### Community 336 - "Community 336"
Cohesion: 1.0
Nodes (1): Return ErrorData (MCP spec) or raise as fallback.

### Community 337 - "Community 337"
Cohesion: 1.0
Nodes (1): Validate and normalize a todo item.          Ensures required fields exist and s

### Community 338 - "Community 338"
Cohesion: 1.0
Nodes (1): Read a file with pagination support.

### Community 339 - "Community 339"
Cohesion: 1.0
Nodes (1): Write content to a file, creating directories as needed.

### Community 340 - "Community 340"
Cohesion: 1.0
Nodes (1): Replace text in a file using fuzzy matching.

### Community 341 - "Community 341"
Cohesion: 1.0
Nodes (1): Apply a V4A format patch.

### Community 342 - "Community 342"
Cohesion: 1.0
Nodes (1): Search for content or files.

### Community 343 - "Community 343"
Cohesion: 1.0
Nodes (1): Parse git --shortstat output into entry dict.

### Community 344 - "Community 344"
Cohesion: 1.0
Nodes (1): Short, human-readable name shown in logs and diagnostics.

### Community 345 - "Community 345"
Cohesion: 1.0
Nodes (1): Return True when all required env vars / credentials are present.          Calle

### Community 346 - "Community 346"
Cohesion: 1.0
Nodes (1): Create a cloud browser session and return session metadata.          Must return

### Community 347 - "Community 347"
Cohesion: 1.0
Nodes (1): Release / terminate a cloud session by its provider session ID.          Returns

### Community 348 - "Community 348"
Cohesion: 1.0
Nodes (1): Best-effort session teardown during process exit.          Called from atexit /

### Community 349 - "Community 349"
Cohesion: 1.0
Nodes (1): Release backend resources (container, instance, connection).

### Community 350 - "Community 350"
Cohesion: 1.0
Nodes (1): Append stdin_data as a shell heredoc to the command string.

### Community 351 - "Community 351"
Cohesion: 1.0
Nodes (1): Return replacement text for a completion.          When the user has already typ

### Community 352 - "Community 352"
Cohesion: 1.0
Nodes (1): Extract the current word if it looks like a file path.          Returns the path

### Community 353 - "Community 353"
Cohesion: 1.0
Nodes (1): Yield Completion objects for file paths matching *word*.

### Community 354 - "Community 354"
Cohesion: 1.0
Nodes (1): Extract a bare ``@`` token for context reference completions.

### Community 355 - "Community 355"
Cohesion: 1.0
Nodes (1): Yield Claude Code-style @ context completions.          Bare ``@`` or ``@partial

### Community 356 - "Community 356"
Cohesion: 1.0
Nodes (1): Create config from environment variables (fallback).

### Community 357 - "Community 357"
Cohesion: 1.0
Nodes (1): Create config from the resolved Honcho config path.          Resolution: $HERMES

### Community 358 - "Community 358"
Cohesion: 1.0
Nodes (1): Return the git repo root directory name, or None if not in a repo.

### Community 359 - "Community 359"
Cohesion: 1.0
Nodes (1): Get the Honcho client, initializing if needed.

### Community 360 - "Community 360"
Cohesion: 1.0
Nodes (1): Format local messages as an XML transcript for Honcho file upload.

### Community 361 - "Community 361"
Cohesion: 1.0
Nodes (1): Normalize Honcho card payloads into a plain list of strings.

### Community 362 - "Community 362"
Cohesion: 1.0
Nodes (0): 

### Community 363 - "Community 363"
Cohesion: 1.0
Nodes (1): _run_async should still work when called from inside an         already-running

### Community 364 - "Community 364"
Cohesion: 1.0
Nodes (0): 

### Community 365 - "Community 365"
Cohesion: 1.0
Nodes (1): Lazy-import execute_code to avoid pulling in firecrawl at collection time.

### Community 366 - "Community 366"
Cohesion: 1.0
Nodes (1): Read then write with no external modification — no warning.

### Community 367 - "Community 367"
Cohesion: 1.0
Nodes (1): Read, then external modify, then write — should warn.

### Community 368 - "Community 368"
Cohesion: 1.0
Nodes (1): Writing a file that was never read — no warning.

### Community 369 - "Community 369"
Cohesion: 1.0
Nodes (1): Creating a new file — no warning.

### Community 370 - "Community 370"
Cohesion: 1.0
Nodes (1): Task A reads, file changes, Task B writes — no warning for B.

### Community 371 - "Community 371"
Cohesion: 1.0
Nodes (1): Patch should warn if the target file changed since last read.

### Community 372 - "Community 372"
Cohesion: 1.0
Nodes (1): Patch with no external changes — no warning.

### Community 373 - "Community 373"
Cohesion: 1.0
Nodes (1): A read that returns >max chars is rejected.

### Community 374 - "Community 374"
Cohesion: 1.0
Nodes (1): Normal-sized reads pass through fine.

### Community 375 - "Community 375"
Cohesion: 1.0
Nodes (1): Content just under the limit should pass through fine.

### Community 376 - "Community 376"
Cohesion: 1.0
Nodes (1): Second read of same file+range returns dedup stub.

### Community 377 - "Community 377"
Cohesion: 1.0
Nodes (1): After the file is modified, dedup returns full content.

### Community 378 - "Community 378"
Cohesion: 1.0
Nodes (1): Same file but different offset/limit should not dedup.

### Community 379 - "Community 379"
Cohesion: 1.0
Nodes (1): Different task_ids have separate dedup caches.

### Community 380 - "Community 380"
Cohesion: 1.0
Nodes (1): After reset_file_dedup, the same read returns full content.

### Community 381 - "Community 381"
Cohesion: 1.0
Nodes (1): reset_file_dedup(None) clears all tasks.

### Community 382 - "Community 382"
Cohesion: 1.0
Nodes (1): reset_file_dedup does NOT affect the consecutive-read counter.

### Community 383 - "Community 383"
Cohesion: 1.0
Nodes (1): A config value of 50 should reject reads over 50 chars.

### Community 384 - "Community 384"
Cohesion: 1.0
Nodes (1): A config value of 500K should allow reads up to 500K chars.

### Community 385 - "Community 385"
Cohesion: 1.0
Nodes (1): When tasks array is provided, top-level goal/context/toolsets are ignored.

### Community 386 - "Community 386"
Cohesion: 1.0
Nodes (1): When delegation.provider is set, full credentials are resolved.

### Community 387 - "Community 387"
Cohesion: 1.0
Nodes (1): Nous provider resolves Nous Portal base_url and api_key.

### Community 388 - "Community 388"
Cohesion: 1.0
Nodes (1): When provider resolution fails, ValueError is raised with helpful message.

### Community 389 - "Community 389"
Cohesion: 1.0
Nodes (1): When provider resolves but has no API key, ValueError is raised.

### Community 390 - "Community 390"
Cohesion: 1.0
Nodes (1): When delegation.provider is configured, child agent gets resolved credentials.

### Community 391 - "Community 391"
Cohesion: 1.0
Nodes (1): Parent on Nous, subagent on OpenRouter — full credential switch.

### Community 392 - "Community 392"
Cohesion: 1.0
Nodes (1): When delegation config is empty, child inherits parent credentials.

### Community 393 - "Community 393"
Cohesion: 1.0
Nodes (1): When credential resolution fails, delegate_task returns a JSON error.

### Community 394 - "Community 394"
Cohesion: 1.0
Nodes (1): In batch mode, all children receive the resolved credentials.

### Community 395 - "Community 395"
Cohesion: 1.0
Nodes (1): Setting only model (no provider) changes model but keeps parent credentials.

### Community 396 - "Community 396"
Cohesion: 1.0
Nodes (1): Shared patches for pre-navigation tests that pass the SSRF check.

### Community 397 - "Community 397"
Cohesion: 1.0
Nodes (1): Shared patches for redirect tests.

### Community 398 - "Community 398"
Cohesion: 1.0
Nodes (1): On Windows, the old check incorrectly blocks valid subpaths.

### Community 399 - "Community 399"
Cohesion: 1.0
Nodes (1): tirith block goes through approval flow (user gets prompted).

### Community 400 - "Community 400"
Cohesion: 1.0
Nodes (1): tirith block + dangerous pattern → combined approval prompt.

### Community 401 - "Community 401"
Cohesion: 1.0
Nodes (1): In gateway mode, tirith block should return approval_required.

### Community 402 - "Community 402"
Cohesion: 1.0
Nodes (1): Both tirith warn and dangerous → single approval_required with both keys.

### Community 403 - "Community 403"
Cohesion: 1.0
Nodes (1): Non-ImportError exceptions from tirith wrapper should propagate.

### Community 404 - "Community 404"
Cohesion: 1.0
Nodes (1): After a failed download, subsequent resolves must not retry.

### Community 405 - "Community 405"
Cohesion: 1.0
Nodes (1): After cached miss, check_command_security hits OSError → fail_open.

### Community 406 - "Community 406"
Cohesion: 1.0
Nodes (1): An explicit tirith_path that doesn't exist must NOT trigger download.

### Community 407 - "Community 407"
Cohesion: 1.0
Nodes (1): An explicit ~/path that doesn't exist must NOT trigger download.

### Community 408 - "Community 408"
Cohesion: 1.0
Nodes (1): The default bare 'tirith' SHOULD trigger auto-download.

### Community 409 - "Community 409"
Cohesion: 1.0
Nodes (1): cosign verify-blob exits 0 → returns True.

### Community 410 - "Community 410"
Cohesion: 1.0
Nodes (1): Identity regexp must pin to the release workflow, not the whole repo.

### Community 411 - "Community 411"
Cohesion: 1.0
Nodes (1): cosign verify-blob exits non-zero → returns False (abort install).

### Community 412 - "Community 412"
Cohesion: 1.0
Nodes (1): cosign not on PATH → returns None (proceed with SHA-256 only).

### Community 413 - "Community 413"
Cohesion: 1.0
Nodes (1): cosign times out → returns None (proceed with SHA-256 only).

### Community 414 - "Community 414"
Cohesion: 1.0
Nodes (1): cosign OSError → returns None (proceed with SHA-256 only).

### Community 415 - "Community 415"
Cohesion: 1.0
Nodes (1): _install_tirith returns None when cosign rejects the signature.

### Community 416 - "Community 416"
Cohesion: 1.0
Nodes (1): _install_tirith proceeds with SHA-256 only when cosign is not on PATH.

### Community 417 - "Community 417"
Cohesion: 1.0
Nodes (1): _install_tirith falls back to SHA-256 when cosign exists but fails to execute.

### Community 418 - "Community 418"
Cohesion: 1.0
Nodes (1): _install_tirith proceeds with SHA-256 when .sig/.pem downloads fail.

### Community 419 - "Community 419"
Cohesion: 1.0
Nodes (1): _install_tirith proceeds only when cosign explicitly passes (True).

### Community 420 - "Community 420"
Cohesion: 1.0
Nodes (1): Synchronous _resolve_tirith_path persists failure to disk.

### Community 421 - "Community 421"
Cohesion: 1.0
Nodes (1): Successful install clears the disk failure marker.

### Community 422 - "Community 422"
Cohesion: 1.0
Nodes (1): When enabled_tools is None, all sandbox tools should be available.

### Community 423 - "Community 423"
Cohesion: 1.0
Nodes (1): When enabled_tools is [] (empty), all sandbox tools should be available.

### Community 424 - "Community 424"
Cohesion: 1.0
Nodes (1): When enabled_tools has no overlap with SANDBOX_ALLOWED_TOOLS,         should fal

### Community 425 - "Community 425"
Cohesion: 1.0
Nodes (1): rg should skip .hub/ by default (no --hidden flag).

### Community 426 - "Community 426"
Cohesion: 1.0
Nodes (1): rg should find content in visible directories.

### Community 427 - "Community 427"
Cohesion: 1.0
Nodes (1): After max retries, the download error should include exc_info.

### Community 428 - "Community 428"
Cohesion: 1.0
Nodes (1): When vision_analyze_tool encounters an error, it should log with exc_info.

### Community 429 - "Community 429"
Cohesion: 1.0
Nodes (1): Temp file cleanup failure should log warning with exc_info.

### Community 430 - "Community 430"
Cohesion: 1.0
Nodes (1): vision_analyze_tool should expand ~ in file paths.

### Community 431 - "Community 431"
Cohesion: 1.0
Nodes (1): A tilde path that doesn't resolve to a real file should fail gracefully.

### Community 432 - "Community 432"
Cohesion: 1.0
Nodes (1): Summarization should pick up a backend that becomes available later in-process.

### Community 433 - "Community 433"
Cohesion: 1.0
Nodes (1): node-hide-console-windows has a real MAL- advisory.

### Community 434 - "Community 434"
Cohesion: 1.0
Nodes (1): react should have zero MAL- advisories.

### Community 435 - "Community 435"
Cohesion: 1.0
Nodes (1): Skills in deeply nested dirs (e.g. cli-tool/components/skills/dev/my-skill/)

### Community 436 - "Community 436"
Cohesion: 1.0
Nodes (1): skip_disabled=True ignores the disabled set (for config UI).

### Community 437 - "Community 437"
Cohesion: 1.0
Nodes (1): Without skip_confirm, input() is called for confirmation.

### Community 438 - "Community 438"
Cohesion: 1.0
Nodes (1): When launchd is running the gateway, update should print         'auto-restart v

### Community 439 - "Community 439"
Cohesion: 1.0
Nodes (1): When no service manager is running but manual gateway is found, show manual rest

### Community 440 - "Community 440"
Cohesion: 1.0
Nodes (1): On Linux with systemd active, update should restart via systemctl.

### Community 441 - "Community 441"
Cohesion: 1.0
Nodes (1): When no gateway is running, update should skip the restart section entirely.

### Community 442 - "Community 442"
Cohesion: 1.0
Nodes (1): When user systemd is inactive but a system service exists, restart via system sc

### Community 443 - "Community 443"
Cohesion: 1.0
Nodes (1): When system service restart fails, show the failure message.

### Community 444 - "Community 444"
Cohesion: 1.0
Nodes (1): When both user and system services are active, both are restarted.

### Community 445 - "Community 445"
Cohesion: 1.0
Nodes (1): After launchd restart, the sweep must exclude the service PID.

### Community 446 - "Community 446"
Cohesion: 1.0
Nodes (1): After systemd restart, the sweep must exclude the service PID.

### Community 447 - "Community 447"
Cohesion: 1.0
Nodes (1): When both a service PID and a manual PID exist, only the manual one         is k

### Community 448 - "Community 448"
Cohesion: 1.0
Nodes (1): Previously this code path raised NameError: 'is_coding_plan'.         Now it del

### Community 449 - "Community 449"
Cohesion: 1.0
Nodes (1): When fetch_api_models returns results, those are used instead of defaults.

### Community 450 - "Community 450"
Cohesion: 1.0
Nodes (1): Selecting 'Custom model' lets user type a model name.

### Community 451 - "Community 451"
Cohesion: 1.0
Nodes (1): Second call within TTL returns cached result without API call.

### Community 452 - "Community 452"
Cohesion: 1.0
Nodes (1): After TTL expires, the API is called again.

### Community 453 - "Community 453"
Cohesion: 1.0
Nodes (1): Models already in vendor/model:tag format must not have their tag mangled.

### Community 454 - "Community 454"
Cohesion: 1.0
Nodes (1): Model in API but without context_length → defaults to 128000.

### Community 455 - "Community 455"
Cohesion: 1.0
Nodes (1): Persistent cache should be checked BEFORE API metadata.

### Community 456 - "Community 456"
Cohesion: 1.0
Nodes (1): Without base_url, cache lookup is skipped.

### Community 457 - "Community 457"
Cohesion: 1.0
Nodes (1): Single-model servers: use the only model even if name doesn't match.

### Community 458 - "Community 458"
Cohesion: 1.0
Nodes (1): Fuzzy match: configured model name is substring of endpoint model.

### Community 459 - "Community 459"
Cohesion: 1.0
Nodes (1): Explicit config_context_length takes priority over everything.

### Community 460 - "Community 460"
Cohesion: 1.0
Nodes (1): config_context_length=0 should be treated as unset.

### Community 461 - "Community 461"
Cohesion: 1.0
Nodes (1): config_context_length=None should be treated as unset.

### Community 462 - "Community 462"
Cohesion: 1.0
Nodes (1): Ensure 'qwen3.5:27b' is NOT reduced to '27b' during context length lookup.

### Community 463 - "Community 463"
Cohesion: 1.0
Nodes (1): On API failure with existing cache, stale data is returned.

### Community 464 - "Community 464"
Cohesion: 1.0
Nodes (1): Models with canonical_slug get indexed under both IDs.

### Community 465 - "Community 465"
Cohesion: 1.0
Nodes (1): Cache expires after _MODEL_CACHE_TTL seconds.

### Community 466 - "Community 466"
Cohesion: 1.0
Nodes (1): API returns JSON without 'data' key — empty cache, no crash.

### Community 467 - "Community 467"
Cohesion: 1.0
Nodes (1): Same model, different context per provider.

### Community 468 - "Community 468"
Cohesion: 1.0
Nodes (1): Isolated config environment with a writable config.yaml.

### Community 469 - "Community 469"
Cohesion: 1.0
Nodes (1): Base URL of the running server, e.g. ``http://127.0.0.1:12345``.

### Community 470 - "Community 470"
Cohesion: 1.0
Nodes (1): Symlinks pointing outside scripts/ must be rejected.

### Community 471 - "Community 471"
Cohesion: 1.0
Nodes (1): Estimated seconds remaining until reset, adjusted for elapsed time.

### Community 472 - "Community 472"
Cohesion: 1.0
Nodes (1): Error is expected to resolve on retry (with or without backoff).

### Community 473 - "Community 473"
Cohesion: 1.0
Nodes (1): Check if output is a real terminal, safe against closed streams.

### Community 474 - "Community 474"
Cohesion: 1.0
Nodes (1): Normalize summary text to the current compaction handoff format.

### Community 475 - "Community 475"
Cohesion: 1.0
Nodes (1): Extract the call ID from a tool_call entry (dict or SimpleNamespace).

### Community 476 - "Community 476"
Cohesion: 1.0
Nodes (1): Short identifier for this provider (e.g. 'builtin', 'honcho', 'hindsight').

### Community 477 - "Community 477"
Cohesion: 1.0
Nodes (1): Return True if this provider is configured, has credentials, and is ready.

### Community 478 - "Community 478"
Cohesion: 1.0
Nodes (1): Initialize for a session.          Called once at agent startup. May create reso

### Community 479 - "Community 479"
Cohesion: 1.0
Nodes (1): Return tool schemas this provider exposes.          Each schema follows the Open

### Community 480 - "Community 480"
Cohesion: 1.0
Nodes (1): Return metadata about all loaded hooks.

### Community 481 - "Community 481"
Cohesion: 1.0
Nodes (1): True if at least one message was sent/edited — signals the base         adapter

### Community 482 - "Community 482"
Cohesion: 1.0
Nodes (1): Strip MEDIA: directives and internal markers from text before display.

### Community 483 - "Community 483"
Cohesion: 1.0
Nodes (1): Split text into reasonably sized chunks for fallback sends.

### Community 484 - "Community 484"
Cohesion: 1.0
Nodes (1): CLI Main Entry Point

### Community 485 - "Community 485"
Cohesion: 1.0
Nodes (1): CLI Config

### Community 486 - "Community 486"
Cohesion: 1.0
Nodes (1): Setup Wizard

### Community 487 - "Community 487"
Cohesion: 1.0
Nodes (1): Env Loader

### Community 488 - "Community 488"
Cohesion: 1.0
Nodes (1): EventBridge

### Community 489 - "Community 489"
Cohesion: 1.0
Nodes (1): MiniSWERunner Class

### Community 490 - "Community 490"
Cohesion: 1.0
Nodes (1): BatchRunner Class

### Community 491 - "Community 491"
Cohesion: 1.0
Nodes (1): OpenRouter Provider

### Community 492 - "Community 492"
Cohesion: 1.0
Nodes (1): Nous Portal Provider

### Community 493 - "Community 493"
Cohesion: 1.0
Nodes (1): Vercel AI Gateway Provider

### Community 494 - "Community 494"
Cohesion: 1.0
Nodes (1): Security Defense Layers

### Community 495 - "Community 495"
Cohesion: 1.0
Nodes (1): ACP Adapter Package

### Community 496 - "Community 496"
Cohesion: 1.0
Nodes (1): Loads ~/.hermes/.env with override=True and project .env as fallback; returns list of loaded paths.

### Community 497 - "Community 497"
Cohesion: 1.0
Nodes (1): Wraps load_dotenv with UTF-8/latin-1 encoding fallback.

### Community 498 - "Community 498"
Cohesion: 1.0
Nodes (1): Main entry point for reading and displaying log lines with optional real-time follow mode.

### Community 499 - "Community 499"
Cohesion: 1.0
Nodes (1): Reads last N matching lines from a log file, reading more raw lines when filters are active.

### Community 500 - "Community 500"
Cohesion: 1.0
Nodes (1): Efficiently reads last N lines from a file using chunk-based reading for large files (>1MB).

### Community 501 - "Community 501"
Cohesion: 1.0
Nodes (1): Polls a log file for new content and prints matching lines in real time.

### Community 502 - "Community 502"
Cohesion: 1.0
Nodes (1): Prints available log files with sizes and modification times.

### Community 503 - "Community 503"
Cohesion: 1.0
Nodes (1): Checks if a log line passes level, session, and time-based filters.

### Community 504 - "Community 504"
Cohesion: 1.0
Nodes (1): Parses relative time strings like '1h', '30m', '2d' into datetime cutoffs.

### Community 505 - "Community 505"
Cohesion: 1.0
Nodes (1): Extracts and parses timestamp from a log line.

### Community 506 - "Community 506"
Cohesion: 1.0
Nodes (1): Extracts log level (DEBUG/INFO/WARNING/ERROR/CRITICAL) from a log line.

### Community 507 - "Community 507"
Cohesion: 1.0
Nodes (1): Main dispatcher for gateway subcommands (run, setup, install, uninstall, start, stop, restart, status).

### Community 508 - "Community 508"
Cohesion: 1.0
Nodes (1): Runs the gateway in foreground via asyncio.run(start_gateway()).

### Community 509 - "Community 509"
Cohesion: 1.0
Nodes (1): Interactive setup for 12+ messaging platforms and gateway service installation.

### Community 510 - "Community 510"
Cohesion: 1.0
Nodes (1): Finds PIDs of running gateway processes via ps/wmic, excluding specified PIDs.

### Community 511 - "Community 511"
Cohesion: 1.0
Nodes (1): Kills running gateway processes with SIGTERM or SIGKILL.

### Community 512 - "Community 512"
Cohesion: 1.0
Nodes (1): Stops only the gateway for the current HERMES_HOME profile using PID file.

### Community 513 - "Community 513"
Cohesion: 1.0
Nodes (1): Generates systemd unit file content for user or system gateway service.

### Community 514 - "Community 514"
Cohesion: 1.0
Nodes (1): Generates launchd plist XML content for macOS gateway service.

### Community 515 - "Community 515"
Cohesion: 1.0
Nodes (1): Installs systemd unit, enables it, and ensures linger is configured.

### Community 516 - "Community 516"
Cohesion: 1.0
Nodes (1): Installs launchd plist and bootstraps it via launchctl.

### Community 517 - "Community 517"
Cohesion: 1.0
Nodes (1): Starts the systemd gateway service, auto-refreshing unit if stale.

### Community 518 - "Community 518"
Cohesion: 1.0
Nodes (1): Starts the launchd gateway service via kickstart, self-healing missing plists.

### Community 519 - "Community 519"
Cohesion: 1.0
Nodes (1): Restarts the systemd gateway service with unit refresh.

### Community 520 - "Community 520"
Cohesion: 1.0
Nodes (1): Restarts the launchd service using kickstart -k for atomic kill+restart.

### Community 521 - "Community 521"
Cohesion: 1.0
Nodes (1): Shows systemd service status with linger guidance and runtime health.

### Community 522 - "Community 522"
Cohesion: 1.0
Nodes (1): Shows launchd service load status, plist freshness, and recent logs.

### Community 523 - "Community 523"
Cohesion: 1.0
Nodes (1): Returns profile-scoped systemd service name (e.g. hermes-gateway-coder).

### Community 524 - "Community 524"
Cohesion: 1.0
Nodes (1): Derives service name suffix from HERMES_HOME profile path.

### Community 525 - "Community 525"
Cohesion: 1.0
Nodes (1): Returns --profile <name> argument for named profiles.

### Community 526 - "Community 526"
Cohesion: 1.0
Nodes (1): Auto-enables systemd linger so user gateway service survives logout.

### Community 527 - "Community 527"
Cohesion: 1.0
Nodes (1): Rewrites installed systemd unit when generated definition has changed.

### Community 528 - "Community 528"
Cohesion: 1.0
Nodes (1): Rewrites installed launchd plist when generated definition has changed.

### Community 529 - "Community 529"
Cohesion: 1.0
Nodes (1): Interactive setup for Telegram, Discord, Slack, and other standard platforms.

### Community 530 - "Community 530"
Cohesion: 1.0
Nodes (1): Interactive setup for Signal messenger via signal-cli HTTP daemon.

### Community 531 - "Community 531"
Cohesion: 1.0
Nodes (1): Returns plain-text configuration status string for a messaging platform.

### Community 532 - "Community 532"
Cohesion: 1.0
Nodes (1): List of dicts defining 12+ messaging platform configs with env vars and setup instructions.

### Community 533 - "Community 533"
Cohesion: 1.0
Nodes (1): ANSI color code constants: RESET, BOLD, DIM, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN.

### Community 534 - "Community 534"
Cohesion: 1.0
Nodes (1): Applies ANSI color codes to text when color output is appropriate.

### Community 535 - "Community 535"
Cohesion: 1.0
Nodes (1): Returns True when colored output is appropriate (respects NO_COLOR, TERM=dumb, TTY).

### Community 536 - "Community 536"
Cohesion: 1.0
Nodes (1): Runs GitHub OAuth device code flow for Copilot authentication with polling.

### Community 537 - "Community 537"
Cohesion: 1.0
Nodes (1): Resolves GitHub token from env vars (COPILOT_GITHUB_TOKEN, GH_TOKEN, GITHUB_TOKEN) then gh CLI.

### Community 538 - "Community 538"
Cohesion: 1.0
Nodes (1): Validates token is usable with Copilot API (rejects classic PAT ghp_* tokens).

### Community 539 - "Community 539"
Cohesion: 1.0
Nodes (1): Builds standard headers for Copilot API requests including Editor-Version and User-Agent.

### Community 540 - "Community 540"
Cohesion: 1.0
Nodes (1): Returns token from gh auth token CLI when GitHub CLI is available.

### Community 541 - "Community 541"
Cohesion: 1.0
Nodes (1): Returns PIDs managed by systemd/launchd gateway services to avoid killing them during stale sweeps.

### Community 542 - "Community 542"
Cohesion: 1.0
Nodes (1): Waits for gateway process to exit by PID file, sending SIGKILL after grace period.

### Community 543 - "Community 543"
Cohesion: 1.0
Nodes (1): Detects active virtualenv directory from sys.prefix or common names under PROJECT_ROOT.

### Community 544 - "Community 544"
Cohesion: 1.0
Nodes (1): Returns Python path preferring venv python over system python.

### Community 545 - "Community 545"
Cohesion: 1.0
Nodes (1): Returns path to hermes CLI binary or falls back to module execution.

### Community 546 - "Community 546"
Cohesion: 1.0
Nodes (1): Returns systemd linger status for current user (enabled/disabled/unknown).

### Community 547 - "Community 547"
Cohesion: 1.0
Nodes (1): Dict mapping log names to filenames: agent.log, errors.log, gateway.log.

### Community 548 - "Community 548"
Cohesion: 1.0
Nodes (1): OAuth client ID for Copilot device code flow (Ov23li8tweQw6odWQebz).

### Community 549 - "Community 549"
Cohesion: 1.0
Nodes (1): Tuple of env var names checked in order: COPILOT_GITHUB_TOKEN, GH_TOKEN, GITHUB_TOKEN.

### Community 550 - "Community 550"
Cohesion: 1.0
Nodes (1): Checks if a token is a classic PAT (ghp_*).

### Community 551 - "Community 551"
Cohesion: 1.0
Nodes (1): Blender MCP Skill

### Community 552 - "Community 552"
Cohesion: 1.0
Nodes (1): Docker Management Skill

### Community 553 - "Community 553"
Cohesion: 1.0
Nodes (1): AgentMail Skill

### Community 554 - "Community 554"
Cohesion: 1.0
Nodes (0): 

### Community 555 - "Community 555"
Cohesion: 1.0
Nodes (1): ToolContext

### Community 556 - "Community 556"
Cohesion: 1.0
Nodes (1): Atropos Environment Usage Patterns

### Community 557 - "Community 557"
Cohesion: 1.0
Nodes (1): Advanced Validation Patterns

### Community 558 - "Community 558"
Cohesion: 1.0
Nodes (1): Instructor Real-World Examples

### Community 559 - "Community 559"
Cohesion: 1.0
Nodes (1): Sliding Window Attention

### Community 560 - "Community 560"
Cohesion: 1.0
Nodes (1): PII Redaction

### Community 561 - "Community 561"
Cohesion: 1.0
Nodes (1): NeMo Curator Multi-Modal Curation

### Community 562 - "Community 562"
Cohesion: 1.0
Nodes (1): LLaVA LoRA Fine-Tuning

### Community 563 - "Community 563"
Cohesion: 1.0
Nodes (1): FSDP Distributed Training

### Community 564 - "Community 564"
Cohesion: 1.0
Nodes (1): DeepSpeed ZeRO Training

### Community 565 - "Community 565"
Cohesion: 1.0
Nodes (1): Pinecone Hybrid Search

### Community 566 - "Community 566"
Cohesion: 1.0
Nodes (1): Pinecone Namespaces

### Community 567 - "Community 567"
Cohesion: 1.0
Nodes (1): Atropos Reward Function Patterns

### Community 568 - "Community 568"
Cohesion: 1.0
Nodes (1): Autonomous AI Agents Skills Category

### Community 569 - "Community 569"
Cohesion: 1.0
Nodes (1): Creative Skills Category

### Community 570 - "Community 570"
Cohesion: 1.0
Nodes (1): Excalidraw Diagram Examples

### Community 571 - "Community 571"
Cohesion: 1.0
Nodes (1): MovingCameraScene 2D Camera Control

### Community 572 - "Community 572"
Cohesion: 1.0
Nodes (1): ThreeDScene 3D Visualization

### Community 573 - "Community 573"
Cohesion: 1.0
Nodes (1): TransformMatchingTex Equation Morphing

### Community 574 - "Community 574"
Cohesion: 1.0
Nodes (1): Paper Explainer Workflow

### Community 575 - "Community 575"
Cohesion: 1.0
Nodes (1): manim-voiceover Plugin

### Community 576 - "Community 576"
Cohesion: 1.0
Nodes (1): Narrative Arc Structures

### Community 577 - "Community 577"
Cohesion: 1.0
Nodes (1): Manim Troubleshooting Reference

### Community 578 - "Community 578"
Cohesion: 1.0
Nodes (1): Layout Templates

### Community 579 - "Community 579"
Cohesion: 1.0
Nodes (1): Animation Pacing Guidelines

### Community 580 - "Community 580"
Cohesion: 1.0
Nodes (1): p5.js

### Community 581 - "Community 581"
Cohesion: 1.0
Nodes (1): Canvas Setup & Coordinate Systems

### Community 582 - "Community 582"
Cohesion: 1.0
Nodes (1): Draw Loop (setup/draw)

### Community 583 - "Community 583"
Cohesion: 1.0
Nodes (1): Transforms (translate/rotate/scale/push/pop)

### Community 584 - "Community 584"
Cohesion: 1.0
Nodes (1): Offscreen Buffers (createGraphics)

### Community 585 - "Community 585"
Cohesion: 1.0
Nodes (1): p5.js 2.0 Async Setup

### Community 586 - "Community 586"
Cohesion: 1.0
Nodes (1): p5.js 2.0 OKLCH Color

### Community 587 - "Community 587"
Cohesion: 1.0
Nodes (1): p5.js 2.0 splineVertex

### Community 588 - "Community 588"
Cohesion: 1.0
Nodes (0): 

### Community 589 - "Community 589"
Cohesion: 1.0
Nodes (1): PNG Export (saveCanvas)

### Community 590 - "Community 590"
Cohesion: 1.0
Nodes (1): GIF Export

### Community 591 - "Community 591"
Cohesion: 1.0
Nodes (1): SVG Export

### Community 592 - "Community 592"
Cohesion: 1.0
Nodes (1): MP4 Export (ffmpeg)

### Community 593 - "Community 593"
Cohesion: 1.0
Nodes (1): Puppeteer

### Community 594 - "Community 594"
Cohesion: 1.0
Nodes (1): ffmpeg

### Community 595 - "Community 595"
Cohesion: 1.0
Nodes (1): CCapture.js

### Community 596 - "Community 596"
Cohesion: 1.0
Nodes (1): fxhash Platform

### Community 597 - "Community 597"
Cohesion: 1.0
Nodes (1): Art Blocks Platform

### Community 598 - "Community 598"
Cohesion: 1.0
Nodes (1): Mouse Events (mousePressed/mouseMoved/etc)

### Community 599 - "Community 599"
Cohesion: 1.0
Nodes (1): Keyboard Events (keyPressed/keyTyped)

### Community 600 - "Community 600"
Cohesion: 1.0
Nodes (1): Touch Events (touchStarted/touchMoved)

### Community 601 - "Community 601"
Cohesion: 1.0
Nodes (1): DOM Controls (createButton/createSlider)

### Community 602 - "Community 602"
Cohesion: 1.0
Nodes (1): Audio Input (p5.sound)

### Community 603 - "Community 603"
Cohesion: 1.0
Nodes (1): Scroll-Driven Animation

### Community 604 - "Community 604"
Cohesion: 1.0
Nodes (1): 2D Primitives (rect/ellipse/triangle/etc)

### Community 605 - "Community 605"
Cohesion: 1.0
Nodes (1): Custom Shapes (beginShape/vertex/endShape)

### Community 606 - "Community 606"
Cohesion: 1.0
Nodes (1): Bezier Curves

### Community 607 - "Community 607"
Cohesion: 1.0
Nodes (1): Catmull-Rom Curves (curveVertex)

### Community 608 - "Community 608"
Cohesion: 1.0
Nodes (1): p5.Vector

### Community 609 - "Community 609"
Cohesion: 1.0
Nodes (1): Signed Distance Functions (SDFs)

### Community 610 - "Community 610"
Cohesion: 1.0
Nodes (1): Clipping & Masking (ERASE/BLEND)

### Community 611 - "Community 611"
Cohesion: 1.0
Nodes (1): Performance Optimization

### Community 612 - "Community 612"
Cohesion: 1.0
Nodes (1): FES (Friendly Error System) Disable

### Community 613 - "Community 613"
Cohesion: 1.0
Nodes (1): pixelDensity Optimization

### Community 614 - "Community 614"
Cohesion: 1.0
Nodes (1): Spatial Hashing

### Community 615 - "Community 615"
Cohesion: 1.0
Nodes (1): Object Pooling

### Community 616 - "Community 616"
Cohesion: 1.0
Nodes (1): Typography in p5.js

### Community 617 - "Community 617"
Cohesion: 1.0
Nodes (0): 

### Community 618 - "Community 618"
Cohesion: 1.0
Nodes (1): Particle Text Effect

### Community 619 - "Community 619"
Cohesion: 1.0
Nodes (1): Kinetic Typography

### Community 620 - "Community 620"
Cohesion: 1.0
Nodes (1): Perlin Noise

### Community 621 - "Community 621"
Cohesion: 1.0
Nodes (1): Fractional Brownian Motion (fBm)

### Community 622 - "Community 622"
Cohesion: 1.0
Nodes (1): Domain Warping

### Community 623 - "Community 623"
Cohesion: 1.0
Nodes (1): Curl Noise

### Community 624 - "Community 624"
Cohesion: 1.0
Nodes (1): Flow Fields

### Community 625 - "Community 625"
Cohesion: 1.0
Nodes (1): Particle Systems

### Community 626 - "Community 626"
Cohesion: 1.0
Nodes (1): Pixel Manipulation (loadPixels/updatePixels)

### Community 627 - "Community 627"
Cohesion: 1.0
Nodes (1): Bloom Effect

### Community 628 - "Community 628"
Cohesion: 1.0
Nodes (1): Reaction-Diffusion

### Community 629 - "Community 629"
Cohesion: 1.0
Nodes (1): L-Systems

### Community 630 - "Community 630"
Cohesion: 1.0
Nodes (1): Circle Packing

### Community 631 - "Community 631"
Cohesion: 1.0
Nodes (1): Voronoi Diagrams

### Community 632 - "Community 632"
Cohesion: 1.0
Nodes (1): Fractal Trees

### Community 633 - "Community 633"
Cohesion: 1.0
Nodes (1): Strange Attractors

### Community 634 - "Community 634"
Cohesion: 1.0
Nodes (1): Poisson Disk Sampling

### Community 635 - "Community 635"
Cohesion: 1.0
Nodes (1): p5.brush (addon)

### Community 636 - "Community 636"
Cohesion: 1.0
Nodes (1): p5.grain (addon)

### Community 637 - "Community 637"
Cohesion: 1.0
Nodes (1): WebGL Mode (WEBGL)

### Community 638 - "Community 638"
Cohesion: 1.0
Nodes (1): 3D Primitives (box/sphere/cylinder/torus/cone)

### Community 639 - "Community 639"
Cohesion: 1.0
Nodes (1): Camera System (orbitControl/PEasyCam)

### Community 640 - "Community 640"
Cohesion: 1.0
Nodes (1): Lighting (ambientLight/directionalLight/pointLight/spotLight)

### Community 641 - "Community 641"
Cohesion: 1.0
Nodes (1): Materials (normalMaterial/ambientMaterial/specularMaterial)

### Community 642 - "Community 642"
Cohesion: 1.0
Nodes (1): Custom Geometry (beginShape/vertex in 3D)

### Community 643 - "Community 643"
Cohesion: 1.0
Nodes (1): GLSL Shaders (vertex+fragment)

### Community 644 - "Community 644"
Cohesion: 1.0
Nodes (0): 

### Community 645 - "Community 645"
Cohesion: 1.0
Nodes (1): Framebuffers (createFramebuffer)

### Community 646 - "Community 646"
Cohesion: 1.0
Nodes (1): export-frames.js (Puppeteer Script)

### Community 647 - "Community 647"
Cohesion: 1.0
Nodes (1): Popular Web Designs Skill

### Community 648 - "Community 648"
Cohesion: 1.0
Nodes (1): Design System Template (9-section structure)

### Community 649 - "Community 649"
Cohesion: 1.0
Nodes (1): Claude (Anthropic) Design System

### Community 650 - "Community 650"
Cohesion: 1.0
Nodes (1): Parchment (#f5f4ed)

### Community 651 - "Community 651"
Cohesion: 1.0
Nodes (1): Terracotta Brand (#c96442)

### Community 652 - "Community 652"
Cohesion: 1.0
Nodes (1): Anthropic Serif (headline font)

### Community 653 - "Community 653"
Cohesion: 1.0
Nodes (1): Anthropic Sans (body/UI font)

### Community 654 - "Community 654"
Cohesion: 1.0
Nodes (1): Inter (CDN substitute)

### Community 655 - "Community 655"
Cohesion: 1.0
Nodes (1): JetBrains Mono (CDN mono substitute)

### Community 656 - "Community 656"
Cohesion: 1.0
Nodes (1): Ring Shadow (0px 0px 0px 1px)

### Community 657 - "Community 657"
Cohesion: 1.0
Nodes (1): MongoDB Design System

### Community 658 - "Community 658"
Cohesion: 1.0
Nodes (1): Forest Black (#001e2b)

### Community 659 - "Community 659"
Cohesion: 1.0
Nodes (1): MongoDB Green (#00ed64)

### Community 660 - "Community 660"
Cohesion: 1.0
Nodes (1): MongoDB Value Serif

### Community 661 - "Community 661"
Cohesion: 1.0
Nodes (1): Euclid Circular A

### Community 662 - "Community 662"
Cohesion: 1.0
Nodes (1): Source Code Pro

### Community 663 - "Community 663"
Cohesion: 1.0
Nodes (1): Pill Button (100px radius)

### Community 664 - "Community 664"
Cohesion: 1.0
Nodes (1): Teal-Tinted Shadow rgba(0,30,43,0.12)

### Community 665 - "Community 665"
Cohesion: 1.0
Nodes (1): NVIDIA Design System

### Community 666 - "Community 666"
Cohesion: 1.0
Nodes (1): NVIDIA Green (#76b900)

### Community 667 - "Community 667"
Cohesion: 1.0
Nodes (1): NVIDIA-EMEA Font

### Community 668 - "Community 668"
Cohesion: 1.0
Nodes (1): Green Border Accent (2px solid #76b900)

### Community 669 - "Community 669"
Cohesion: 1.0
Nodes (1): Minimal Radius (1-2px) Industrial Pattern

### Community 670 - "Community 670"
Cohesion: 1.0
Nodes (1): Notion Design System

### Community 671 - "Community 671"
Cohesion: 1.0
Nodes (1): Notion Blue (#0075de)

### Community 672 - "Community 672"
Cohesion: 1.0
Nodes (1): NotionInter (modified Inter)

### Community 673 - "Community 673"
Cohesion: 1.0
Nodes (1): Whisper Border (1px solid rgba(0,0,0,0.1))

### Community 674 - "Community 674"
Cohesion: 1.0
Nodes (1): Multi-Layer Shadow Stack (4-5 layers)

### Community 675 - "Community 675"
Cohesion: 1.0
Nodes (1): Negative Letter-Spacing at Display Sizes

### Community 676 - "Community 676"
Cohesion: 1.0
Nodes (1): Ollama Design System

### Community 677 - "Community 677"
Cohesion: 1.0
Nodes (1): SF Pro Rounded

### Community 678 - "Community 678"
Cohesion: 1.0
Nodes (1): Binary Radius System (12px or 9999px)

### Community 679 - "Community 679"
Cohesion: 1.0
Nodes (1): Zero Shadow Philosophy

### Community 680 - "Community 680"
Cohesion: 1.0
Nodes (1): Pure Grayscale Palette

### Community 681 - "Community 681"
Cohesion: 1.0
Nodes (1): Airbnb Design System

### Community 682 - "Community 682"
Cohesion: 1.0
Nodes (1): Airtable Design System

### Community 683 - "Community 683"
Cohesion: 1.0
Nodes (1): Apple Design System

### Community 684 - "Community 684"
Cohesion: 1.0
Nodes (1): BMW Design System

### Community 685 - "Community 685"
Cohesion: 1.0
Nodes (1): Cal.com Design System

### Community 686 - "Community 686"
Cohesion: 1.0
Nodes (1): Clay Design System

### Community 687 - "Community 687"
Cohesion: 1.0
Nodes (1): ClickHouse Design System

### Community 688 - "Community 688"
Cohesion: 1.0
Nodes (1): Cohere Design System

### Community 689 - "Community 689"
Cohesion: 1.0
Nodes (1): Coinbase Design System

### Community 690 - "Community 690"
Cohesion: 1.0
Nodes (1): Composio Design System

### Community 691 - "Community 691"
Cohesion: 1.0
Nodes (1): Cursor Design System

### Community 692 - "Community 692"
Cohesion: 1.0
Nodes (1): ElevenLabs Design System

### Community 693 - "Community 693"
Cohesion: 1.0
Nodes (1): Expo Design System

### Community 694 - "Community 694"
Cohesion: 1.0
Nodes (1): Figma Design System

### Community 695 - "Community 695"
Cohesion: 1.0
Nodes (1): Framer Design System

### Community 696 - "Community 696"
Cohesion: 1.0
Nodes (1): HashiCorp Design System

### Community 697 - "Community 697"
Cohesion: 1.0
Nodes (1): IBM Design System

### Community 698 - "Community 698"
Cohesion: 1.0
Nodes (1): Intercom Design System

### Community 699 - "Community 699"
Cohesion: 1.0
Nodes (1): Kraken Design System

### Community 700 - "Community 700"
Cohesion: 1.0
Nodes (1): Linear.app Design System

### Community 701 - "Community 701"
Cohesion: 1.0
Nodes (1): Lovable Design System

### Community 702 - "Community 702"
Cohesion: 1.0
Nodes (1): MiniMax Design System

### Community 703 - "Community 703"
Cohesion: 1.0
Nodes (1): Mintlify Design System

### Community 704 - "Community 704"
Cohesion: 1.0
Nodes (1): Miro Design System

### Community 705 - "Community 705"
Cohesion: 1.0
Nodes (1): Mistral.ai Design System

### Community 706 - "Community 706"
Cohesion: 1.0
Nodes (1): OpenCode.ai Design System

### Community 707 - "Community 707"
Cohesion: 1.0
Nodes (1): Pinterest Design System

### Community 708 - "Community 708"
Cohesion: 1.0
Nodes (1): PostHog Design System

### Community 709 - "Community 709"
Cohesion: 1.0
Nodes (1): Raycast Design System

### Community 710 - "Community 710"
Cohesion: 1.0
Nodes (1): generative-widgets skill (cloudflared tunnel)

### Community 711 - "Community 711"
Cohesion: 1.0
Nodes (1): browser_vision skill (visual verification)

### Community 712 - "Community 712"
Cohesion: 1.0
Nodes (1): Warm Neutral Palette Pattern

### Community 713 - "Community 713"
Cohesion: 1.0
Nodes (1): Dark/Light Section Alternation Pattern

### Community 714 - "Community 714"
Cohesion: 1.0
Nodes (1): Serif Headline / Sans Body Hierarchy

### Community 715 - "Community 715"
Cohesion: 1.0
Nodes (1): Pill Shape Geometry (9999px radius)

### Community 716 - "Community 716"
Cohesion: 1.0
Nodes (1): CDN Font Substitution Pattern

### Community 717 - "Community 717"
Cohesion: 1.0
Nodes (1): Google Fonts CDN (fonts.googleapis.com)

### Community 718 - "Community 718"
Cohesion: 1.0
Nodes (1): Design System: Sanity

### Community 719 - "Community 719"
Cohesion: 1.0
Nodes (1): Design System: Together AI

### Community 720 - "Community 720"
Cohesion: 1.0
Nodes (1): Diagramming Skills

### Community 721 - "Community 721"
Cohesion: 1.0
Nodes (1): Domain Intelligence

### Community 722 - "Community 722"
Cohesion: 1.0
Nodes (1): Feeds Skills

### Community 723 - "Community 723"
Cohesion: 1.0
Nodes (1): GIFs Skills

### Community 724 - "Community 724"
Cohesion: 1.0
Nodes (1): inference.sh

### Community 725 - "Community 725"
Cohesion: 1.0
Nodes (1): songsee Audio Visualization

### Community 726 - "Community 726"
Cohesion: 1.0
Nodes (1): Vector Databases

### Community 727 - "Community 727"
Cohesion: 1.0
Nodes (1): Productivity Skills

### Community 728 - "Community 728"
Cohesion: 1.0
Nodes (1): Fakes Package Init

### Community 729 - "Community 729"
Cohesion: 1.0
Nodes (1): Gateway Tests Package Init

### Community 730 - "Community 730"
Cohesion: 1.0
Nodes (1): Skin/Theme System

### Community 731 - "Community 731"
Cohesion: 1.0
Nodes (1): hermes-agent tests/run_agent

### Community 732 - "Community 732"
Cohesion: 1.0
Nodes (1): Browser SSRF local backend checks

### Community 733 - "Community 733"
Cohesion: 1.0
Nodes (1): ToolEntry

### Community 734 - "Community 734"
Cohesion: 1.0
Nodes (1): tool_result

### Community 735 - "Community 735"
Cohesion: 1.0
Nodes (1): EnvironmentInfo

### Community 736 - "Community 736"
Cohesion: 1.0
Nodes (1): Finding

### Community 737 - "Community 737"
Cohesion: 1.0
Nodes (1): ScanResult

### Community 738 - "Community 738"
Cohesion: 1.0
Nodes (1): GitHubAuth

### Community 739 - "Community 739"
Cohesion: 1.0
Nodes (1): HubLockFile

### Community 740 - "Community 740"
Cohesion: 1.0
Nodes (1): TapsManager

### Community 741 - "Community 741"
Cohesion: 1.0
Nodes (1): SkillMeta

### Community 742 - "Community 742"
Cohesion: 1.0
Nodes (1): SkillBundle

### Community 743 - "Community 743"
Cohesion: 1.0
Nodes (1): WebsitePolicyError

### Community 744 - "Community 744"
Cohesion: 1.0
Nodes (1): invalidate_cache

### Community 745 - "Community 745"
Cohesion: 1.0
Nodes (1): PreparedModalExec

### Community 746 - "Community 746"
Cohesion: 1.0
Nodes (1): ModalExecStart

### Community 747 - "Community 747"
Cohesion: 1.0
Nodes (1): neutts_jo_sample

### Community 748 - "Community 748"
Cohesion: 1.0
Nodes (1): Memory Toolset

### Community 749 - "Community 749"
Cohesion: 1.0
Nodes (1): Skills Toolset

### Community 750 - "Community 750"
Cohesion: 1.0
Nodes (1): Session Search Toolset

### Community 751 - "Community 751"
Cohesion: 1.0
Nodes (1): Todo Toolset

### Community 752 - "Community 752"
Cohesion: 1.0
Nodes (1): hermes-cli Platform Toolset

### Community 753 - "Community 753"
Cohesion: 1.0
Nodes (1): hermes-api-server Platform Toolset

### Community 754 - "Community 754"
Cohesion: 1.0
Nodes (1): .env File

## Ambiguous Edges - Review These
- `debug_helpers.py` → `code_execution_tool.py`  [AMBIGUOUS]
  hermes-agent/tests/tools/test_debug_helpers.py · relation: semantically_similar_to
- `checkpoint_manager.py` → `code_execution_tool.py`  [AMBIGUOUS]
  hermes-agent/tests/tools/test_checkpoint_manager.py · relation: semantically_similar_to
- `godmode_race.py` → `parseltongue.py`  [AMBIGUOUS]
  None · relation: semantically_similar_to
- `Hermes CLI Main Entry Point` → `Landing Page JavaScript`  [AMBIGUOUS]
  hermes-agent/landingpage/script.js · relation: semantically_similar_to

## Knowledge Gaps
- **4481 isolated node(s):** `Shared constants for Hermes Agent.  Import-safe module with no dependencies — ca`, `Return the Hermes home directory (default: ~/.hermes).      Reads HERMES_HOME en`, `Return the optional-skills directory, honoring package-manager wrappers.      Pa`, `Resolve a Hermes subdirectory with backward compatibility.      New installs get`, `Return a user-friendly display string for the current HERMES_HOME.      Uses ``~` (+4476 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 289`** (2 nodes): `docusaurus.config.ts`, `sidebars_config`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 290`** (2 nodes): `Pinecone Deployment Guide`, `Pinecone Vector Database`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 291`** (2 nodes): `Inference.sh CLI Skill`, `Inference.sh Platform`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 292`** (2 nodes): `Production Quality Checklist`, `12 Visual Design Principles`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 293`** (2 nodes): `Delivery Router`, `Delivery Routing Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 294`** (2 nodes): `EVIDENCE_TYPES Constants`, `Evidence Types Taxonomy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 295`** (2 nodes): `get_pricing_entry`, `OpenRouter Pricing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 296`** (2 nodes): `acp_adapter.entry`, `test_acp_entry`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 297`** (2 nodes): `WhatsApp Allowlist Module`, `WhatsApp Bridge Server`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 298`** (2 nodes): `agent.retry_utils Module`, `Retry Utils Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 299`** (2 nodes): `EvidenceStore`, `Evidence Store Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 300`** (2 nodes): `Tenor GIF API`, `GIF Search (Tenor)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 301`** (2 nodes): `agent-browser CLI`, `Homebrew PATH discovery`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 302`** (2 nodes): `IOC_TYPES Constants`, `IOC Types`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 303`** (2 nodes): `check_website_access`, `load_website_blocklist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 304`** (2 nodes): `default_soul.py`, `Default SOUL.md template seeded into HERMES_HOME on first run.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 305`** (2 nodes): `Packaging Metadata Tests`, `Project Metadata Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 306`** (2 nodes): `Hermes Agent Project`, `Termux Constraints`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 307`** (2 nodes): `AES-GCM Client-Side Encryption`, `Excalidraw Upload Script`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 308`** (2 nodes): `Atropos RL Training`, `RL Toolset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 309`** (2 nodes): `OAuth Authorization Code + PKCE Flow`, `Gemini OAuth Provider Implementation Plan`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 310`** (2 nodes): `Data Science Skills`, `Jupyter Live Kernel (hamelnb)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 311`** (2 nodes): `Auto Title Generator`, `Trajectory Saver`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 312`** (2 nodes): `index.tsx`, `handler()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 313`** (2 nodes): `Hermes Agent Homebrew Formula`, `Homebrew Packaging README`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 314`** (2 nodes): `Design System: Runway`, `Design System: SpaceX`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 315`** (2 nodes): `DingTalkAdapter`, `DingTalk Adapter Tests`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 316`** (2 nodes): `Design System: Spotify`, `Design System: Supabase`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 317`** (2 nodes): `Windows PowerShell Installer`, `Hermes Release Script`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 318`** (2 nodes): `Note Taking`, `Obsidian Vault`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 319`** (2 nodes): `Home Assistant Integration`, `Home Assistant Toolset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 320`** (2 nodes): `Honcho Memory Plugin`, `Pluggable Memory Provider Interface`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 321`** (1 nodes): `Load configuration from YAML file.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 322`** (1 nodes): `Normalize summary-model output to a safe string.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 323`** (1 nodes): `Normalize summary text to include the expected prefix exactly once.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 324`** (1 nodes): `Validate and sanitize a session title.          - Strips leading/trailing whites`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 325`** (1 nodes): `Sanitize user input for safe use in FTS5 MATCH queries.          FTS5 has its ow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 326`** (1 nodes): `Current audio input RMS level (0-32767). Updated each audio chunk.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 327`** (1 nodes): `Write numpy int16 audio data to a WAV file.          Returns the file path.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 328`** (1 nodes): `Strip shell startup warnings from the beginning of output.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 329`** (1 nodes): `Best-effort liveness check for host-visible PIDs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 330`** (1 nodes): `Terminate a host-visible PID without requiring the original process handle.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 331`** (1 nodes): `Return the writable sandbox temp dir for env-backed background tasks.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 332`** (1 nodes): `Acquire an exclusive file lock for read-modify-write safety.          Uses a sep`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 333`** (1 nodes): `Read a memory file and split into entries.          No file locking needed: _wri`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 334`** (1 nodes): `Write entries to a memory file using atomic temp-file + rename.          Previou`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 335`** (1 nodes): `Extract text from a ToolResultContent block.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 336`** (1 nodes): `Return ErrorData (MCP spec) or raise as fallback.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 337`** (1 nodes): `Validate and normalize a todo item.          Ensures required fields exist and s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 338`** (1 nodes): `Read a file with pagination support.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 339`** (1 nodes): `Write content to a file, creating directories as needed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 340`** (1 nodes): `Replace text in a file using fuzzy matching.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 341`** (1 nodes): `Apply a V4A format patch.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 342`** (1 nodes): `Search for content or files.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 343`** (1 nodes): `Parse git --shortstat output into entry dict.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 344`** (1 nodes): `Short, human-readable name shown in logs and diagnostics.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 345`** (1 nodes): `Return True when all required env vars / credentials are present.          Calle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 346`** (1 nodes): `Create a cloud browser session and return session metadata.          Must return`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 347`** (1 nodes): `Release / terminate a cloud session by its provider session ID.          Returns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 348`** (1 nodes): `Best-effort session teardown during process exit.          Called from atexit /`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 349`** (1 nodes): `Release backend resources (container, instance, connection).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 350`** (1 nodes): `Append stdin_data as a shell heredoc to the command string.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 351`** (1 nodes): `Return replacement text for a completion.          When the user has already typ`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 352`** (1 nodes): `Extract the current word if it looks like a file path.          Returns the path`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 353`** (1 nodes): `Yield Completion objects for file paths matching *word*.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 354`** (1 nodes): `Extract a bare ``@`` token for context reference completions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 355`** (1 nodes): `Yield Claude Code-style @ context completions.          Bare ``@`` or ``@partial`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 356`** (1 nodes): `Create config from environment variables (fallback).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 357`** (1 nodes): `Create config from the resolved Honcho config path.          Resolution: $HERMES`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 358`** (1 nodes): `Return the git repo root directory name, or None if not in a repo.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 359`** (1 nodes): `Get the Honcho client, initializing if needed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 360`** (1 nodes): `Format local messages as an XML transcript for Honcho file upload.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 361`** (1 nodes): `Normalize Honcho card payloads into a plain list of strings.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 362`** (1 nodes): `sidebars.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 363`** (1 nodes): `_run_async should still work when called from inside an         already-running`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 364`** (1 nodes): `test_minisweagent_path.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 365`** (1 nodes): `Lazy-import execute_code to avoid pulling in firecrawl at collection time.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 366`** (1 nodes): `Read then write with no external modification — no warning.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 367`** (1 nodes): `Read, then external modify, then write — should warn.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 368`** (1 nodes): `Writing a file that was never read — no warning.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 369`** (1 nodes): `Creating a new file — no warning.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 370`** (1 nodes): `Task A reads, file changes, Task B writes — no warning for B.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 371`** (1 nodes): `Patch should warn if the target file changed since last read.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 372`** (1 nodes): `Patch with no external changes — no warning.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 373`** (1 nodes): `A read that returns >max chars is rejected.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 374`** (1 nodes): `Normal-sized reads pass through fine.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 375`** (1 nodes): `Content just under the limit should pass through fine.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 376`** (1 nodes): `Second read of same file+range returns dedup stub.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 377`** (1 nodes): `After the file is modified, dedup returns full content.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 378`** (1 nodes): `Same file but different offset/limit should not dedup.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 379`** (1 nodes): `Different task_ids have separate dedup caches.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 380`** (1 nodes): `After reset_file_dedup, the same read returns full content.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 381`** (1 nodes): `reset_file_dedup(None) clears all tasks.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 382`** (1 nodes): `reset_file_dedup does NOT affect the consecutive-read counter.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 383`** (1 nodes): `A config value of 50 should reject reads over 50 chars.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 384`** (1 nodes): `A config value of 500K should allow reads up to 500K chars.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 385`** (1 nodes): `When tasks array is provided, top-level goal/context/toolsets are ignored.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 386`** (1 nodes): `When delegation.provider is set, full credentials are resolved.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 387`** (1 nodes): `Nous provider resolves Nous Portal base_url and api_key.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 388`** (1 nodes): `When provider resolution fails, ValueError is raised with helpful message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 389`** (1 nodes): `When provider resolves but has no API key, ValueError is raised.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 390`** (1 nodes): `When delegation.provider is configured, child agent gets resolved credentials.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 391`** (1 nodes): `Parent on Nous, subagent on OpenRouter — full credential switch.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 392`** (1 nodes): `When delegation config is empty, child inherits parent credentials.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 393`** (1 nodes): `When credential resolution fails, delegate_task returns a JSON error.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 394`** (1 nodes): `In batch mode, all children receive the resolved credentials.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 395`** (1 nodes): `Setting only model (no provider) changes model but keeps parent credentials.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 396`** (1 nodes): `Shared patches for pre-navigation tests that pass the SSRF check.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 397`** (1 nodes): `Shared patches for redirect tests.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 398`** (1 nodes): `On Windows, the old check incorrectly blocks valid subpaths.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 399`** (1 nodes): `tirith block goes through approval flow (user gets prompted).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 400`** (1 nodes): `tirith block + dangerous pattern → combined approval prompt.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 401`** (1 nodes): `In gateway mode, tirith block should return approval_required.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 402`** (1 nodes): `Both tirith warn and dangerous → single approval_required with both keys.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 403`** (1 nodes): `Non-ImportError exceptions from tirith wrapper should propagate.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 404`** (1 nodes): `After a failed download, subsequent resolves must not retry.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 405`** (1 nodes): `After cached miss, check_command_security hits OSError → fail_open.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 406`** (1 nodes): `An explicit tirith_path that doesn't exist must NOT trigger download.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 407`** (1 nodes): `An explicit ~/path that doesn't exist must NOT trigger download.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 408`** (1 nodes): `The default bare 'tirith' SHOULD trigger auto-download.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 409`** (1 nodes): `cosign verify-blob exits 0 → returns True.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 410`** (1 nodes): `Identity regexp must pin to the release workflow, not the whole repo.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 411`** (1 nodes): `cosign verify-blob exits non-zero → returns False (abort install).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 412`** (1 nodes): `cosign not on PATH → returns None (proceed with SHA-256 only).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 413`** (1 nodes): `cosign times out → returns None (proceed with SHA-256 only).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 414`** (1 nodes): `cosign OSError → returns None (proceed with SHA-256 only).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 415`** (1 nodes): `_install_tirith returns None when cosign rejects the signature.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 416`** (1 nodes): `_install_tirith proceeds with SHA-256 only when cosign is not on PATH.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 417`** (1 nodes): `_install_tirith falls back to SHA-256 when cosign exists but fails to execute.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 418`** (1 nodes): `_install_tirith proceeds with SHA-256 when .sig/.pem downloads fail.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 419`** (1 nodes): `_install_tirith proceeds only when cosign explicitly passes (True).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 420`** (1 nodes): `Synchronous _resolve_tirith_path persists failure to disk.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 421`** (1 nodes): `Successful install clears the disk failure marker.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 422`** (1 nodes): `When enabled_tools is None, all sandbox tools should be available.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 423`** (1 nodes): `When enabled_tools is [] (empty), all sandbox tools should be available.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 424`** (1 nodes): `When enabled_tools has no overlap with SANDBOX_ALLOWED_TOOLS,         should fal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 425`** (1 nodes): `rg should skip .hub/ by default (no --hidden flag).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 426`** (1 nodes): `rg should find content in visible directories.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 427`** (1 nodes): `After max retries, the download error should include exc_info.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 428`** (1 nodes): `When vision_analyze_tool encounters an error, it should log with exc_info.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 429`** (1 nodes): `Temp file cleanup failure should log warning with exc_info.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 430`** (1 nodes): `vision_analyze_tool should expand ~ in file paths.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 431`** (1 nodes): `A tilde path that doesn't resolve to a real file should fail gracefully.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 432`** (1 nodes): `Summarization should pick up a backend that becomes available later in-process.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 433`** (1 nodes): `node-hide-console-windows has a real MAL- advisory.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 434`** (1 nodes): `react should have zero MAL- advisories.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 435`** (1 nodes): `Skills in deeply nested dirs (e.g. cli-tool/components/skills/dev/my-skill/)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 436`** (1 nodes): `skip_disabled=True ignores the disabled set (for config UI).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 437`** (1 nodes): `Without skip_confirm, input() is called for confirmation.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 438`** (1 nodes): `When launchd is running the gateway, update should print         'auto-restart v`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 439`** (1 nodes): `When no service manager is running but manual gateway is found, show manual rest`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 440`** (1 nodes): `On Linux with systemd active, update should restart via systemctl.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 441`** (1 nodes): `When no gateway is running, update should skip the restart section entirely.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 442`** (1 nodes): `When user systemd is inactive but a system service exists, restart via system sc`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 443`** (1 nodes): `When system service restart fails, show the failure message.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 444`** (1 nodes): `When both user and system services are active, both are restarted.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 445`** (1 nodes): `After launchd restart, the sweep must exclude the service PID.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 446`** (1 nodes): `After systemd restart, the sweep must exclude the service PID.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 447`** (1 nodes): `When both a service PID and a manual PID exist, only the manual one         is k`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 448`** (1 nodes): `Previously this code path raised NameError: 'is_coding_plan'.         Now it del`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 449`** (1 nodes): `When fetch_api_models returns results, those are used instead of defaults.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 450`** (1 nodes): `Selecting 'Custom model' lets user type a model name.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 451`** (1 nodes): `Second call within TTL returns cached result without API call.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 452`** (1 nodes): `After TTL expires, the API is called again.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 453`** (1 nodes): `Models already in vendor/model:tag format must not have their tag mangled.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 454`** (1 nodes): `Model in API but without context_length → defaults to 128000.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 455`** (1 nodes): `Persistent cache should be checked BEFORE API metadata.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 456`** (1 nodes): `Without base_url, cache lookup is skipped.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 457`** (1 nodes): `Single-model servers: use the only model even if name doesn't match.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 458`** (1 nodes): `Fuzzy match: configured model name is substring of endpoint model.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 459`** (1 nodes): `Explicit config_context_length takes priority over everything.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 460`** (1 nodes): `config_context_length=0 should be treated as unset.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 461`** (1 nodes): `config_context_length=None should be treated as unset.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 462`** (1 nodes): `Ensure 'qwen3.5:27b' is NOT reduced to '27b' during context length lookup.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 463`** (1 nodes): `On API failure with existing cache, stale data is returned.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 464`** (1 nodes): `Models with canonical_slug get indexed under both IDs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 465`** (1 nodes): `Cache expires after _MODEL_CACHE_TTL seconds.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 466`** (1 nodes): `API returns JSON without 'data' key — empty cache, no crash.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 467`** (1 nodes): `Same model, different context per provider.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 468`** (1 nodes): `Isolated config environment with a writable config.yaml.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 469`** (1 nodes): `Base URL of the running server, e.g. ``http://127.0.0.1:12345``.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 470`** (1 nodes): `Symlinks pointing outside scripts/ must be rejected.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 471`** (1 nodes): `Estimated seconds remaining until reset, adjusted for elapsed time.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 472`** (1 nodes): `Error is expected to resolve on retry (with or without backoff).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 473`** (1 nodes): `Check if output is a real terminal, safe against closed streams.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 474`** (1 nodes): `Normalize summary text to the current compaction handoff format.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 475`** (1 nodes): `Extract the call ID from a tool_call entry (dict or SimpleNamespace).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 476`** (1 nodes): `Short identifier for this provider (e.g. 'builtin', 'honcho', 'hindsight').`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 477`** (1 nodes): `Return True if this provider is configured, has credentials, and is ready.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 478`** (1 nodes): `Initialize for a session.          Called once at agent startup. May create reso`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 479`** (1 nodes): `Return tool schemas this provider exposes.          Each schema follows the Open`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 480`** (1 nodes): `Return metadata about all loaded hooks.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 481`** (1 nodes): `True if at least one message was sent/edited — signals the base         adapter`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 482`** (1 nodes): `Strip MEDIA: directives and internal markers from text before display.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 483`** (1 nodes): `Split text into reasonably sized chunks for fallback sends.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 484`** (1 nodes): `CLI Main Entry Point`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 485`** (1 nodes): `CLI Config`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 486`** (1 nodes): `Setup Wizard`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 487`** (1 nodes): `Env Loader`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 488`** (1 nodes): `EventBridge`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 489`** (1 nodes): `MiniSWERunner Class`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 490`** (1 nodes): `BatchRunner Class`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 491`** (1 nodes): `OpenRouter Provider`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 492`** (1 nodes): `Nous Portal Provider`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 493`** (1 nodes): `Vercel AI Gateway Provider`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 494`** (1 nodes): `Security Defense Layers`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 495`** (1 nodes): `ACP Adapter Package`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 496`** (1 nodes): `Loads ~/.hermes/.env with override=True and project .env as fallback; returns list of loaded paths.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 497`** (1 nodes): `Wraps load_dotenv with UTF-8/latin-1 encoding fallback.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 498`** (1 nodes): `Main entry point for reading and displaying log lines with optional real-time follow mode.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 499`** (1 nodes): `Reads last N matching lines from a log file, reading more raw lines when filters are active.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 500`** (1 nodes): `Efficiently reads last N lines from a file using chunk-based reading for large files (>1MB).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 501`** (1 nodes): `Polls a log file for new content and prints matching lines in real time.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 502`** (1 nodes): `Prints available log files with sizes and modification times.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 503`** (1 nodes): `Checks if a log line passes level, session, and time-based filters.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 504`** (1 nodes): `Parses relative time strings like '1h', '30m', '2d' into datetime cutoffs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 505`** (1 nodes): `Extracts and parses timestamp from a log line.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 506`** (1 nodes): `Extracts log level (DEBUG/INFO/WARNING/ERROR/CRITICAL) from a log line.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 507`** (1 nodes): `Main dispatcher for gateway subcommands (run, setup, install, uninstall, start, stop, restart, status).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 508`** (1 nodes): `Runs the gateway in foreground via asyncio.run(start_gateway()).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 509`** (1 nodes): `Interactive setup for 12+ messaging platforms and gateway service installation.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 510`** (1 nodes): `Finds PIDs of running gateway processes via ps/wmic, excluding specified PIDs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 511`** (1 nodes): `Kills running gateway processes with SIGTERM or SIGKILL.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 512`** (1 nodes): `Stops only the gateway for the current HERMES_HOME profile using PID file.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 513`** (1 nodes): `Generates systemd unit file content for user or system gateway service.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 514`** (1 nodes): `Generates launchd plist XML content for macOS gateway service.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 515`** (1 nodes): `Installs systemd unit, enables it, and ensures linger is configured.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 516`** (1 nodes): `Installs launchd plist and bootstraps it via launchctl.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 517`** (1 nodes): `Starts the systemd gateway service, auto-refreshing unit if stale.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 518`** (1 nodes): `Starts the launchd gateway service via kickstart, self-healing missing plists.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 519`** (1 nodes): `Restarts the systemd gateway service with unit refresh.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 520`** (1 nodes): `Restarts the launchd service using kickstart -k for atomic kill+restart.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 521`** (1 nodes): `Shows systemd service status with linger guidance and runtime health.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 522`** (1 nodes): `Shows launchd service load status, plist freshness, and recent logs.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 523`** (1 nodes): `Returns profile-scoped systemd service name (e.g. hermes-gateway-coder).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 524`** (1 nodes): `Derives service name suffix from HERMES_HOME profile path.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 525`** (1 nodes): `Returns --profile <name> argument for named profiles.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 526`** (1 nodes): `Auto-enables systemd linger so user gateway service survives logout.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 527`** (1 nodes): `Rewrites installed systemd unit when generated definition has changed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 528`** (1 nodes): `Rewrites installed launchd plist when generated definition has changed.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 529`** (1 nodes): `Interactive setup for Telegram, Discord, Slack, and other standard platforms.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 530`** (1 nodes): `Interactive setup for Signal messenger via signal-cli HTTP daemon.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 531`** (1 nodes): `Returns plain-text configuration status string for a messaging platform.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 532`** (1 nodes): `List of dicts defining 12+ messaging platform configs with env vars and setup instructions.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 533`** (1 nodes): `ANSI color code constants: RESET, BOLD, DIM, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 534`** (1 nodes): `Applies ANSI color codes to text when color output is appropriate.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 535`** (1 nodes): `Returns True when colored output is appropriate (respects NO_COLOR, TERM=dumb, TTY).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 536`** (1 nodes): `Runs GitHub OAuth device code flow for Copilot authentication with polling.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 537`** (1 nodes): `Resolves GitHub token from env vars (COPILOT_GITHUB_TOKEN, GH_TOKEN, GITHUB_TOKEN) then gh CLI.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 538`** (1 nodes): `Validates token is usable with Copilot API (rejects classic PAT ghp_* tokens).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 539`** (1 nodes): `Builds standard headers for Copilot API requests including Editor-Version and User-Agent.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 540`** (1 nodes): `Returns token from gh auth token CLI when GitHub CLI is available.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 541`** (1 nodes): `Returns PIDs managed by systemd/launchd gateway services to avoid killing them during stale sweeps.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 542`** (1 nodes): `Waits for gateway process to exit by PID file, sending SIGKILL after grace period.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 543`** (1 nodes): `Detects active virtualenv directory from sys.prefix or common names under PROJECT_ROOT.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 544`** (1 nodes): `Returns Python path preferring venv python over system python.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 545`** (1 nodes): `Returns path to hermes CLI binary or falls back to module execution.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 546`** (1 nodes): `Returns systemd linger status for current user (enabled/disabled/unknown).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 547`** (1 nodes): `Dict mapping log names to filenames: agent.log, errors.log, gateway.log.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 548`** (1 nodes): `OAuth client ID for Copilot device code flow (Ov23li8tweQw6odWQebz).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 549`** (1 nodes): `Tuple of env var names checked in order: COPILOT_GITHUB_TOKEN, GH_TOKEN, GITHUB_TOKEN.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 550`** (1 nodes): `Checks if a token is a classic PAT (ghp_*).`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 551`** (1 nodes): `Blender MCP Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 552`** (1 nodes): `Docker Management Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 553`** (1 nodes): `AgentMail Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 554`** (1 nodes): `openclaw_to_hermes.py`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 555`** (1 nodes): `ToolContext`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 556`** (1 nodes): `Atropos Environment Usage Patterns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 557`** (1 nodes): `Advanced Validation Patterns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 558`** (1 nodes): `Instructor Real-World Examples`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 559`** (1 nodes): `Sliding Window Attention`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 560`** (1 nodes): `PII Redaction`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 561`** (1 nodes): `NeMo Curator Multi-Modal Curation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 562`** (1 nodes): `LLaVA LoRA Fine-Tuning`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 563`** (1 nodes): `FSDP Distributed Training`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 564`** (1 nodes): `DeepSpeed ZeRO Training`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 565`** (1 nodes): `Pinecone Hybrid Search`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 566`** (1 nodes): `Pinecone Namespaces`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 567`** (1 nodes): `Atropos Reward Function Patterns`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 568`** (1 nodes): `Autonomous AI Agents Skills Category`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 569`** (1 nodes): `Creative Skills Category`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 570`** (1 nodes): `Excalidraw Diagram Examples`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 571`** (1 nodes): `MovingCameraScene 2D Camera Control`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 572`** (1 nodes): `ThreeDScene 3D Visualization`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 573`** (1 nodes): `TransformMatchingTex Equation Morphing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 574`** (1 nodes): `Paper Explainer Workflow`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 575`** (1 nodes): `manim-voiceover Plugin`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 576`** (1 nodes): `Narrative Arc Structures`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 577`** (1 nodes): `Manim Troubleshooting Reference`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 578`** (1 nodes): `Layout Templates`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 579`** (1 nodes): `Animation Pacing Guidelines`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 580`** (1 nodes): `p5.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 581`** (1 nodes): `Canvas Setup & Coordinate Systems`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 582`** (1 nodes): `Draw Loop (setup/draw)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 583`** (1 nodes): `Transforms (translate/rotate/scale/push/pop)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 584`** (1 nodes): `Offscreen Buffers (createGraphics)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 585`** (1 nodes): `p5.js 2.0 Async Setup`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 586`** (1 nodes): `p5.js 2.0 OKLCH Color`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 587`** (1 nodes): `p5.js 2.0 splineVertex`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 588`** (1 nodes): `p5.js 2.0 shader.modify()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 589`** (1 nodes): `PNG Export (saveCanvas)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 590`** (1 nodes): `GIF Export`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 591`** (1 nodes): `SVG Export`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 592`** (1 nodes): `MP4 Export (ffmpeg)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 593`** (1 nodes): `Puppeteer`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 594`** (1 nodes): `ffmpeg`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 595`** (1 nodes): `CCapture.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 596`** (1 nodes): `fxhash Platform`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 597`** (1 nodes): `Art Blocks Platform`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 598`** (1 nodes): `Mouse Events (mousePressed/mouseMoved/etc)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 599`** (1 nodes): `Keyboard Events (keyPressed/keyTyped)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 600`** (1 nodes): `Touch Events (touchStarted/touchMoved)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 601`** (1 nodes): `DOM Controls (createButton/createSlider)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 602`** (1 nodes): `Audio Input (p5.sound)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 603`** (1 nodes): `Scroll-Driven Animation`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 604`** (1 nodes): `2D Primitives (rect/ellipse/triangle/etc)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 605`** (1 nodes): `Custom Shapes (beginShape/vertex/endShape)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 606`** (1 nodes): `Bezier Curves`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 607`** (1 nodes): `Catmull-Rom Curves (curveVertex)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 608`** (1 nodes): `p5.Vector`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 609`** (1 nodes): `Signed Distance Functions (SDFs)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 610`** (1 nodes): `Clipping & Masking (ERASE/BLEND)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 611`** (1 nodes): `Performance Optimization`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 612`** (1 nodes): `FES (Friendly Error System) Disable`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 613`** (1 nodes): `pixelDensity Optimization`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 614`** (1 nodes): `Spatial Hashing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 615`** (1 nodes): `Object Pooling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 616`** (1 nodes): `Typography in p5.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 617`** (1 nodes): `textToPoints()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 618`** (1 nodes): `Particle Text Effect`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 619`** (1 nodes): `Kinetic Typography`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 620`** (1 nodes): `Perlin Noise`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 621`** (1 nodes): `Fractional Brownian Motion (fBm)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 622`** (1 nodes): `Domain Warping`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 623`** (1 nodes): `Curl Noise`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 624`** (1 nodes): `Flow Fields`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 625`** (1 nodes): `Particle Systems`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 626`** (1 nodes): `Pixel Manipulation (loadPixels/updatePixels)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 627`** (1 nodes): `Bloom Effect`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 628`** (1 nodes): `Reaction-Diffusion`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 629`** (1 nodes): `L-Systems`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 630`** (1 nodes): `Circle Packing`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 631`** (1 nodes): `Voronoi Diagrams`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 632`** (1 nodes): `Fractal Trees`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 633`** (1 nodes): `Strange Attractors`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 634`** (1 nodes): `Poisson Disk Sampling`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 635`** (1 nodes): `p5.brush (addon)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 636`** (1 nodes): `p5.grain (addon)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 637`** (1 nodes): `WebGL Mode (WEBGL)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 638`** (1 nodes): `3D Primitives (box/sphere/cylinder/torus/cone)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 639`** (1 nodes): `Camera System (orbitControl/PEasyCam)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 640`** (1 nodes): `Lighting (ambientLight/directionalLight/pointLight/spotLight)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 641`** (1 nodes): `Materials (normalMaterial/ambientMaterial/specularMaterial)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 642`** (1 nodes): `Custom Geometry (beginShape/vertex in 3D)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 643`** (1 nodes): `GLSL Shaders (vertex+fragment)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 644`** (1 nodes): `createFilterShader()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 645`** (1 nodes): `Framebuffers (createFramebuffer)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 646`** (1 nodes): `export-frames.js (Puppeteer Script)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 647`** (1 nodes): `Popular Web Designs Skill`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 648`** (1 nodes): `Design System Template (9-section structure)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 649`** (1 nodes): `Claude (Anthropic) Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 650`** (1 nodes): `Parchment (#f5f4ed)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 651`** (1 nodes): `Terracotta Brand (#c96442)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 652`** (1 nodes): `Anthropic Serif (headline font)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 653`** (1 nodes): `Anthropic Sans (body/UI font)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 654`** (1 nodes): `Inter (CDN substitute)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 655`** (1 nodes): `JetBrains Mono (CDN mono substitute)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 656`** (1 nodes): `Ring Shadow (0px 0px 0px 1px)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 657`** (1 nodes): `MongoDB Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 658`** (1 nodes): `Forest Black (#001e2b)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 659`** (1 nodes): `MongoDB Green (#00ed64)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 660`** (1 nodes): `MongoDB Value Serif`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 661`** (1 nodes): `Euclid Circular A`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 662`** (1 nodes): `Source Code Pro`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 663`** (1 nodes): `Pill Button (100px radius)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 664`** (1 nodes): `Teal-Tinted Shadow rgba(0,30,43,0.12)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 665`** (1 nodes): `NVIDIA Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 666`** (1 nodes): `NVIDIA Green (#76b900)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 667`** (1 nodes): `NVIDIA-EMEA Font`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 668`** (1 nodes): `Green Border Accent (2px solid #76b900)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 669`** (1 nodes): `Minimal Radius (1-2px) Industrial Pattern`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 670`** (1 nodes): `Notion Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 671`** (1 nodes): `Notion Blue (#0075de)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 672`** (1 nodes): `NotionInter (modified Inter)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 673`** (1 nodes): `Whisper Border (1px solid rgba(0,0,0,0.1))`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 674`** (1 nodes): `Multi-Layer Shadow Stack (4-5 layers)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 675`** (1 nodes): `Negative Letter-Spacing at Display Sizes`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 676`** (1 nodes): `Ollama Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 677`** (1 nodes): `SF Pro Rounded`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 678`** (1 nodes): `Binary Radius System (12px or 9999px)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 679`** (1 nodes): `Zero Shadow Philosophy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 680`** (1 nodes): `Pure Grayscale Palette`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 681`** (1 nodes): `Airbnb Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 682`** (1 nodes): `Airtable Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 683`** (1 nodes): `Apple Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 684`** (1 nodes): `BMW Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 685`** (1 nodes): `Cal.com Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 686`** (1 nodes): `Clay Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 687`** (1 nodes): `ClickHouse Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 688`** (1 nodes): `Cohere Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 689`** (1 nodes): `Coinbase Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 690`** (1 nodes): `Composio Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 691`** (1 nodes): `Cursor Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 692`** (1 nodes): `ElevenLabs Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 693`** (1 nodes): `Expo Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 694`** (1 nodes): `Figma Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 695`** (1 nodes): `Framer Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 696`** (1 nodes): `HashiCorp Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 697`** (1 nodes): `IBM Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 698`** (1 nodes): `Intercom Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 699`** (1 nodes): `Kraken Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 700`** (1 nodes): `Linear.app Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 701`** (1 nodes): `Lovable Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 702`** (1 nodes): `MiniMax Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 703`** (1 nodes): `Mintlify Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 704`** (1 nodes): `Miro Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 705`** (1 nodes): `Mistral.ai Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 706`** (1 nodes): `OpenCode.ai Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 707`** (1 nodes): `Pinterest Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 708`** (1 nodes): `PostHog Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 709`** (1 nodes): `Raycast Design System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 710`** (1 nodes): `generative-widgets skill (cloudflared tunnel)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 711`** (1 nodes): `browser_vision skill (visual verification)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 712`** (1 nodes): `Warm Neutral Palette Pattern`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 713`** (1 nodes): `Dark/Light Section Alternation Pattern`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 714`** (1 nodes): `Serif Headline / Sans Body Hierarchy`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 715`** (1 nodes): `Pill Shape Geometry (9999px radius)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 716`** (1 nodes): `CDN Font Substitution Pattern`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 717`** (1 nodes): `Google Fonts CDN (fonts.googleapis.com)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 718`** (1 nodes): `Design System: Sanity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 719`** (1 nodes): `Design System: Together AI`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 720`** (1 nodes): `Diagramming Skills`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 721`** (1 nodes): `Domain Intelligence`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 722`** (1 nodes): `Feeds Skills`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 723`** (1 nodes): `GIFs Skills`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 724`** (1 nodes): `inference.sh`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 725`** (1 nodes): `songsee Audio Visualization`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 726`** (1 nodes): `Vector Databases`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 727`** (1 nodes): `Productivity Skills`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 728`** (1 nodes): `Fakes Package Init`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 729`** (1 nodes): `Gateway Tests Package Init`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 730`** (1 nodes): `Skin/Theme System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 731`** (1 nodes): `hermes-agent tests/run_agent`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 732`** (1 nodes): `Browser SSRF local backend checks`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 733`** (1 nodes): `ToolEntry`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 734`** (1 nodes): `tool_result`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 735`** (1 nodes): `EnvironmentInfo`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 736`** (1 nodes): `Finding`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 737`** (1 nodes): `ScanResult`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 738`** (1 nodes): `GitHubAuth`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 739`** (1 nodes): `HubLockFile`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 740`** (1 nodes): `TapsManager`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 741`** (1 nodes): `SkillMeta`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 742`** (1 nodes): `SkillBundle`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 743`** (1 nodes): `WebsitePolicyError`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 744`** (1 nodes): `invalidate_cache`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 745`** (1 nodes): `PreparedModalExec`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 746`** (1 nodes): `ModalExecStart`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 747`** (1 nodes): `neutts_jo_sample`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 748`** (1 nodes): `Memory Toolset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 749`** (1 nodes): `Skills Toolset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 750`** (1 nodes): `Session Search Toolset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 751`** (1 nodes): `Todo Toolset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 752`** (1 nodes): `hermes-cli Platform Toolset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 753`** (1 nodes): `hermes-api-server Platform Toolset`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 754`** (1 nodes): `.env File`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `debug_helpers.py` and `code_execution_tool.py`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `checkpoint_manager.py` and `code_execution_tool.py`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `godmode_race.py` and `parseltongue.py`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Hermes CLI Main Entry Point` and `Landing Page JavaScript`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **Why does `AIAgent` connect `Community 1` to `Community 0`, `Community 2`, `Community 3`, `Community 4`, `Community 99`, `Community 6`, `Community 7`, `Community 8`, `Community 11`, `Community 15`, `Community 112`, `Community 17`, `Community 114`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Why does `Platform` connect `Community 0` to `Community 1`, `Community 2`, `Community 3`, `Community 132`, `Community 5`, `Community 8`, `Community 140`, `Community 14`, `Community 16`, `Community 24`, `Community 26`, `Community 29`, `Community 33`, `Community 35`, `Community 43`, `Community 47`, `Community 53`, `Community 55`, `Community 59`, `Community 60`, `Community 67`, `Community 70`, `Community 82`, `Community 86`, `Community 95`, `Community 123`, `Community 126`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Why does `hermes_cli.config` connect `Community 4` to `Community 0`, `Community 1`, `Community 2`, `Community 3`, `Community 5`, `Community 7`, `Community 9`, `Community 11`, `Community 14`, `Community 15`, `Community 18`, `Community 19`, `Community 20`, `Community 25`, `Community 26`, `Community 31`, `Community 33`, `Community 36`, `Community 48`, `Community 51`, `Community 58`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._