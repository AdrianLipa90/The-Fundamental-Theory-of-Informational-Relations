================================================================================
NOEMA / CIEL — COMPLETE SYSTEM MAP (Głębokie mapowanie)
Data: 2026-06-25
Author: Adrian Lipa & NOEMA (2026)
================================================================================

────────────────────────────────────────────────────────────────────────────────
SEKCJA 1: DAEMONY (12 uruchomionych)
────────────────────────────────────────────────────────────────────────────────


============================================================
DAEMON: ciel_noema_kuramoto_daemon.py
Path: scripts/ciel_noema_kuramoto_daemon.py
Lines: 108
Functions: main, _stop
Calls: evolve_surface, flush_surface, ensure_surface, open_surface, register, heartbeat
Surface reads: tick, phi, gravity
  → ciel_geometry: ciel_geometry.noema_registry, ciel_geometry.noema_surface_mmap

============================================================
DAEMON: ciel_noema_resonance_bridge.py
Path: scripts/ciel_noema_resonance_bridge.py
Lines: 98
Functions: main, _stop
Calls: dual_surface_step, resonance_snapshot, register, heartbeat
  → ciel_geometry: ciel_geometry.resonance_bridge, ciel_geometry.noema_registry, ciel_geometry.noema_surface_mmap

============================================================
DAEMON: ciel_noema_linux_sensor_daemon.py
Path: scripts/ciel_noema_linux_sensor_daemon.py
Lines: 135
Functions: main, __init__, run, stop, _handler
  class LinuxSensorDaemon: __init__, run, stop
Calls: open_surface, register, heartbeat
  → ciel_geometry: ciel_geometry.linux_sensor, ciel_geometry.noema_registry, ciel_geometry.noema_surface_mmap

============================================================
DAEMON: ciel_noema_neutrino_daemon.py
Path: scripts/ciel_noema_neutrino_daemon.py
Lines: 146
Functions: _read_D_f, main, _stop
Calls: flush_surface, ensure_surface, open_surface, apply_neutrino_bus_to_surface, compute_neutrino_phase_bus, register, heartbeat
Surface reads: tick, phi, flavor, g
  → ciel_geometry: ciel_geometry.neutrino_phase_channel, ciel_geometry.noema_registry, ciel_geometry.noema_surface_mmap

============================================================
DAEMON: ciel_noema_cielingo_sync.py
Path: scripts/ciel_noema_cielingo_sync.py
Lines: 484
Functions: euler_residual, euler_target_phases, euler_guided_tau, apply_euler_sync, _read_manifest, _write_manifest, surface_to_manifest, manifest_to_surface, run_cielingo_closure, main
Calls: flush_surface, ensure_surface, open_surface, build_orbital_bridge, apply_neutrino_bus_to_surface, compute_neutrino_phase_bus, register, heartbeat
Surface reads: omega, phi, tau, gravity, flavor, g
  → ciel_geometry: ciel_geometry.noema_registry, ciel_geometry.noema_surface_mmap, ciel_geometry.neutrino_phase_channel
  → ciel_sot_agent: ciel_sot_agent.orbital_bridge
  → CIEL/Ω: CIEL_OMEGA_COMPLETE_SYSTEM.ciel_omega.memory.tiered_orchestrator

============================================================
DAEMON: ciel_agent_backend.py
Path: scripts/ciel_agent_backend.py
Lines: 383
Functions: _tokenize, _ngrams, _extract_content, extract_themes, detect_affect, extract_anchors, extract_essence, generate_hunch, process_content, run_once
  class AgentHandler: do_GET, do_POST, _respond, log_message

============================================================
DAEMON: ciel_memory_consolidator.py
Path: scripts/ciel_memory_consolidator.py
Lines: 1124
Functions: _shared_server_alive, _shared_server_port_pids, _shared_server_health_ok, _shared_server_assessment, _ask_api_fallback_permission, _get_llm, _db_connect, init_db, _source_type, scan_and_register_files
Calls: register
  → ciel_sot_agent: ciel_sot_agent.subconsciousness

============================================================
DAEMON: ciel_noema_phasenav_daemon.py
Path: scripts/ciel_noema_phasenav_daemon.py
Lines: 170
Functions: _load_zip_index, _seed_operator_vec, _seed_zip_concept, main
Calls: flush_surface, ensure_surface, open_surface, register, heartbeat
Surface reads: phi, flavor
  → ciel_geometry: ciel_geometry.phasenav.enrichment, ciel_geometry.phasenav.operator_algebra, ciel_geometry.noema_registry, ciel_geometry.noema_surface_mmap, ciel_geometry.linux_sensor

============================================================
DAEMON: ciel_noema_nonlocal_proxy.py
Path: scripts/ciel_noema_nonlocal_proxy.py
Lines: 234
Functions: _load_x25519, _log_entry, main, _handle_x25519_response, _stop
Calls: ensure_surface, open_surface, register, heartbeat
Surface reads: flavor
  → ciel_geometry: ciel_geometry.noema_registry, ciel_geometry.noema_surface_mmap, ciel_geometry.nonlocal_channel

============================================================
DAEMON: noema_agent_lock.py
Path: scripts/noema_agent_lock.py
Lines: 169
Functions: _stop
Calls: flush_surface, ensure_surface, open_surface, apply_agent_attractor
  → ciel_geometry: ciel_geometry.noema_surface_mmap, ciel_geometry.agent_attractor, ciel_geometry.nonlocal_channel

============================================================
DAEMON: noema_dual_sync.py
Path: scripts/noema_dual_sync.py
Lines: 282
Functions: _sync_phi, _sync_g_and_omega, _bind_phase_memory, _bind_fields, sync_once, daemon_loop, status, _stop
Calls: flush_surface, ensure_surface, register, heartbeat
  → ciel_geometry: ciel_geometry.noema_surface_mmap, ciel_geometry.daemon_registry

============================================================
DAEMON: noema_phase_archiver.py
Path: scripts/noema_phase_archiver.py
Lines: 207
Functions: _ensure_h5, _ensure_npz, write_snapshot, snapshot_once, run_daemon, _stop
Calls: ensure_surface
Surface reads: tick, omega, phi, gravity, flavor, g
  → ciel_geometry: ciel_geometry.noema_surface_mmap


================================================================================
SEKCJA 2: CIEL_GEOMETRY (28 plików, 12 aktywnych)
================================================================================


────────────────────────────────────────
[ACTIVE] agent_attractor.py
Lines: 105
  Functions: apply_agent_attractor, agent_attractor_state
  Calls: apply_agent_attractor
  Imported by: resonance_bridge.py, noema_agent_lock.py

────────────────────────────────────────
[DEAD] continuous_phase_sync.py
Lines: 181
  Functions: compute_Z_harmonic, compute_all_Z, evolve_analytic, reconstruct_phi_from_Z, compute_R, compute_R_harmonic, effective_kappa, convergence_time
  class ContinuousPhaseSync: compute_Z_harmonic, compute_all_Z, evolve_analytic, reconstruct_phi_from_Z

────────────────────────────────────────
[ACTIVE] daemon_registry.py
Lines: 199
  Functions: _ensure_registry, daemon_main_loop, __init__, register, heartbeat, unregister, set_status, scan
  class DaemonInfo: —
  class Registry: __init__, register, heartbeat, unregister
  Calls: register, heartbeat
  Imported by: noema_dual_sync.py

────────────────────────────────────────
[DEAD] disk.py
Lines: 111
  Functions: poincare_radius, poincare_distance, sector_to_disk, entity_to_disk, geodesic_arc, _straight_line
  Imported by: subjective_time.py, edges.py, layout.py, semantic_mass.py

────────────────────────────────────────
[ACTIVE] ebpf_noema_loader.py
Lines: 334
  Functions: main_loop, __init__, start, stop, read_counters, _rates, snapshot, write_surface
  class EBPFSensor: __init__, start, stop, read_counters
  Calls: flush_surface, open_surface

────────────────────────────────────────
[DEAD] edges.py
Lines: 66
  Functions: build_sector_edges, build_entity_edges
  class GeodesicEdge: —
  Imported by: layout.py

────────────────────────────────────────
[DEAD] layout.py
Lines: 137
  Functions: build_layout, to_json
  class DiskNode: —
  class DiskEdge: —
  class DiskLayout: to_json
  Imported by: renderer_mpl.py, renderer_ascii.py

────────────────────────────────────────
[ACTIVE] linux_sensor.py
Lines: 305
  Functions: _ensure_op_matrix, _stat_read, _read_cpu_phi, _read_mem_phi, _read_load_phi, _read_float, top_processes, _read_rss
  class LinuxSensorSnapshot: __init__
  class LinuxSensor: __init__, snapshot, write_surface, process_phasenav
  Calls: flush_surface
  Imported by: ciel_noema_phasenav_daemon.py, ciel_noema_linux_sensor_daemon.py

────────────────────────────────────────
[DEAD] loader.py
Lines: 121
  Functions: load_sectors, load_couplings, load_entities, load_bridge_state
  class SectorGeom: —
  class EntityGeom: —
  class BridgeState: —
  Imported by: subjective_time.py, layout.py, semantic_mass.py, ciel_memory_consolidator.py

────────────────────────────────────────
[DEAD] nbody_gravity.py
Lines: 261
  Functions: from_mass_table, r, v, ke, add_body, _compute_accelerations, _total_potential, _total_kinetic
  class Body: r, v, ke
  class NBodySystem: add_body, _compute_accelerations, _total_potential, _total_kinetic

────────────────────────────────────────
[ACTIVE] neutrino_phase_channel.py
Lines: 347
  Functions: _pmns_squared, pmns_matrix, phi_to_epsilon, D_f_to_lambda, compute_channel_oscillation, compute_neutrino_phase_bus, mac_to_phases, bind_noema_mac
  Calls: apply_neutrino_bus_to_surface, compute_neutrino_phase_bus
  Imported by: ciel_noema_cielingo_sync.py, nonlocal_channel.py, ciel_noema_neutrino_daemon.py

────────────────────────────────────────
[DEAD] noema_config.py
Lines: 125
  Functions: _default_config_path, load_config, _merge
  class KuramotoConfig: —
  class CielingoSyncConfig: —
  class NeutrinoConfig: —

────────────────────────────────────────
[ACTIVE] noema_registry.py
Lines: 151
  Functions: __init__, register, heartbeat, unregister, list_active, check_access, cleanup, get
  class NoemaRegistry: __init__, register, heartbeat, unregister
  Calls: register, heartbeat
  Imported by: ciel_noema_cielingo_sync.py, ciel_noema_neutrino_daemon.py, ciel_noema_kuramoto_daemon.py, ciel_noema_phasenav_daemon.py, ciel_noema_resonance_bridge.py, ciel_noema_linux_sensor_daemon.py, ciel_noema_nonlocal_proxy.py

────────────────────────────────────────
[ACTIVE] noema_surface_mmap.py
Lines: 1653
  Functions: _compute_j_kj, surface_specs, oscillator_id_for_concept, _channel_idx, _osc_rho, oscillator_disk_pos, wij_bipolar_axis, compute_surface_bipolar_axes
  class SurfaceArraySpec: nbytes
  Calls: evolve_surface, flush_surface, ensure_surface, open_surface, initialize_surface, sync_surface_geometry
  Imported by: ciel_noema_cielingo_sync.py, nonlocal_channel.py, ebpf_noema_loader.py, phase_memory_adapter.py, ciel_noema_neutrino_daemon.py, noema_phase_archiver.py, ciel_noema_kuramoto_daemon.py, continuous_phase_sync.py, ciel_noema_phasenav_daemon.py, resonance_bridge.py, noema_agent_lock.py, ciel_noema_resonance_bridge.py, subconscious.py, ciel_noema_linux_sensor_daemon.py, noema_dual_sync.py, linux_sensor.py, ciel_noema_nonlocal_proxy.py

────────────────────────────────────────
[ACTIVE] nonlocal_channel.py
Lines: 477
  Functions: get_channel, tune, broadcast, listen, resonate, from_mac, from_phase_vector, __init__
  class AgentFingerprint: from_mac, from_phase_vector
  class NonlocalMessage: —
  class NonlocalChannelState: —
  Calls: flush_surface, ensure_surface, open_surface
  Imported by: ciel_noema_nonlocal_proxy.py, noema_agent_lock.py

────────────────────────────────────────
[ACTIVE] phase_memory_adapter.py
Lines: 229
  Functions: _tokenize, encode_text_to_binary_vector, event_hash, _capture_surface_signature, _memory_paths, _ensure_file, ensure_phase_memory, bind_phase_memory
  class PhaseMemoryRecord: —
  Calls: open_surface
  Imported by: resonance_bridge.py

────────────────────────────────────────
[DEAD] renderer_ascii.py
Lines: 80
  Functions: render, disk_to_grid

────────────────────────────────────────
[DEAD] renderer_mpl.py
Lines: 253
  Functions: _node_label, _health_bar, render, _parse_args, main

────────────────────────────────────────
[ACTIVE] resonance_bridge.py
Lines: 393
  Functions: ensure_dual_surfaces, imaginalize_state, _surface_summary, resonance_snapshot, apply_resonance_bridge, surface_to_orchorbital_snap, route_surface_through_orchorbital, dual_surface_step
  Calls: evolve_surface, flush_surface, ensure_surface, open_surface, initialize_surface, sync_surface_geometry
  Imported by: ciel_noema_resonance_bridge.py, orbital_bridge.py

────────────────────────────────────────
[DEAD] semantic_mass.py
Lines: 340
  Functions: compute_sector_mass, compute_entity_mass, compute_repo_mass, build_mass_table, fuse_semantic_mass
  class SemanticMassRecord: —
  Imported by: subjective_time.py

────────────────────────────────────────
[DEAD] subconscious.py
Lines: 393
  Functions: __post_init__, psi, psi, amplitude, phase, collatz_entropy, _collatz_potential, _collatz_entropy_1d
  class ZetaSchrodinger: __post_init__, psi, psi, amplitude
  class BerryPhaseTracker: update, mixing_angles_from_phase, snapshot
  class WakeSignalGenerator: evaluate
  Imported by: ciel_pipeline.py, ciel_memory_consolidator.py

────────────────────────────────────────
[DEAD] subjective_time.py
Lines: 154
  Functions: orbit_index, _g, compute_subjective_times, compute_from_bridge
  class SubjectiveTimeRecord: —
  Imported by: ciel_pipeline.py

────────────────────────────────────────
[DEAD] tmuv_perturbation.py
Lines: 152
  Functions: tmuv_total_energy_density, mass_perturbation_from_tmuv, compute_effective_masses, total_stress_energy_scalar


================================================================================
SEKCJA 3: CIEL_SOT_AGENT (58 plików, ~18 kluczowych)
================================================================================


────────────────────────────────────────
ciel_pipeline.py
Lines: 980
  Functions: _query_subconscious_socket, _query_subconscious, _weave_and_query_subconscious, _ensure_ciel_omega_on_path, _get_engine, warm_ciel_pipeline, _accumulated_identity_phase, _next_cycle_index, _orbital_state_to_context, _load_wpm_context
  Calls: build_orbital_bridge, run_ciel_pipeline, register
  → cielingo_bridge: build_lingo_frame
  → ciel_omega.memory.braid_invariant: BraidInvariantMemory
  → ciel_geometry.subjective_time: compute_from_bridge
  → ciel_omega.htri.htri_local: GPUHtri

────────────────────────────────────────
orbital_bridge.py
Lines: 395
  Functions: _load_json_if_exists, _build_sync_manifest, _build_runtime_gating, _bridge_markdown, build_orbital_bridge, main
  Calls: resonance_snapshot, build_orbital_bridge, run_ciel_pipeline
  → ciel_geometry.resonance_bridge: DEFAULT_IMAGINAL_SURFACE_ROOT, resonance_snapshot

────────────────────────────────────────
cielingo_bridge.py
Lines: 417
  Functions: _ensure_lingophysics_on_path, _normalize_tokens, _detect_deictic_frame, _detect_operator_tokens, _detect_concept_tokens, _route_noema, render_lingo_summary, compute_phase_projection, compute_tau_bridge, _cache_key
  → cielingo.phase_sense_parser: parse_text_to_phase_sense

────────────────────────────────────────
orch_orbital.py
Lines: 372
  Functions: load_entity_cards, entity_orbital_summary, canonical_entity_id, _entity_sector_name, _rho_from_theta, _card_to_sector_dict, _phase_coupling, build_entity_injection, entity_orbital_metrics, run_entity_mini_pass

────────────────────────────────────────
subconsciousness.py
Lines: 508
  Functions: is_running, start_server, query_subconscious, detect_flux, _query_sentinel, record_flux, watch_and_record, record_affective_moment, load_affective_moments, compute_starting_phase

────────────────────────────────────────
thought_fragments.py
Lines: 337
  Functions: _get, _listify, build_cognitive_fragment, build_memory_candidate, promote_memory_candidate, build_noema_memory_link, assess_durable_memory_health, snapshot_to_dict
  class CognitiveFragment: —
  class MemoryCandidate: —
  class DurableMemoryObject: —

────────────────────────────────────────
memory_rag.py
Lines: 162
  Functions: _keywords, _score, search_wave_archive, search_chat_history, build_memory_context, rd

────────────────────────────────────────
consolidation_resonator.py
Lines: 676
  Functions: _load_entity_tag_aliases, normalize_tag, load_consolidations, build_tag_map, _load_phase_state, _save_phase_state, _build_coupling_matrix, _lorentz_omega, kuramoto_sync, kuramoto_order_parameter
  class ConsolidationRecord: —
  class TagCard: —

────────────────────────────────────────
holonomic_normalizer.py
Lines: 378
  Functions: wrap, circular_barycenter, circular_distance, symmetrize_couplings, clip_couplings, renormalize_couplings, triplet_tension, _get, _set, _sector
  class HolonomicCallbacks: —
  → ciel_omega.orbital.phase_control: mode_norm, coherence_index_from_snapshot, _PSI_DEEP, _PSI_STANDARD

────────────────────────────────────────
state_db.py
Lines: 707
  Functions: get_db, _ensure_schema, save_report, load_report, load_report_freshness, load_metrics_history, extract_lingo_metrics, save_orchestrator_state, load_orchestrator_state, load_holonomy

────────────────────────────────────────
noema_sot.py
Lines: 578
  Functions: _load_pipeline_state, _load_catalog_summary, _load_py_catalog_summary, _load_jokeheal_summary, _project_memory_field, collect, compute_global, export_to_context, run, _weighted_mean
  → ciel_omega.memory.holonomic_memory: HolonomicMemory

────────────────────────────────────────
local_nonlocality_fallback.py
Lines: 496
  Functions: _read_cpu_percent, _read_mem_percent, _read_load_avg, _read_process_count, _read_disk_bytes, _read_net_bytes, _time_of_day_phase, read_pc_phases, _run_eba_with_hidden, _aggregate_eba

────────────────────────────────────────
jokeheal_atlas.py
Lines: 96
  Functions: default_scar_path, load_scar_rows, build_mnemonic_atlas

────────────────────────────────────────
phase_snapshots.py
Lines: 105
  Functions: _get, build_phase_snapshot, build_qualisensing_snapshot, snapshot_to_dict
  class PhaseSnapshot: —
  class QualisensingSnapshot: —

────────────────────────────────────────
paths.py
Lines: 48
  Functions: resolve_project_root, resolve_existing_path

────────────────────────────────────────
htri_scheduler.py
Lines: 231
  Functions: _htri_path, _ram_free_gb, _cpu_load, _cuda_available, _auto_power_mode, run, get_state, get_optimal_threads
  → ciel_omega.htri.htri_local: CPUHtri, GPUHtri, LocalHTRI

────────────────────────────────────────
rh_pipeline_jfunctional.py
Lines: 90
  Functions: _float_from, compute_pipeline_j_functional

────────────────────────────────────────
spreadsheet_db.py
Lines: 241
  Functions: _xlsx_lock, _now_ts, _load_or_create, _ensure_sheet, _row_by_id, upsert_entity_card, append_htri_metrics, append_pipeline_metrics, append_cqcl_log, upsert_nonlocal_card


================================================================================
SEKCJA 4: CIEL/Ω ENGINE (CielEngine)
================================================================================

  CielEngine jest CIEL/Ω consciousness engine — NIE ma bezpośredniego
  dostępu do NOEMA surface (mmap). Operuje w Python object space.

  Lokalizacja: src/CIEL_OMEGA_COMPLETE_SYSTEM/ciel_omega/ciel/engine.py (399 linii)

  Komponenty CielEngine (18 pól @dataclass):
    1. config (CielConfig) — konfiguracja
    2. intention (IntentionField) — 12D intention vector
    3. kernel (SpectralWaveField12D) — wave simulation
    4. memory (UnifiedMemoryOrchestrator) — TMP + promotion
    5. information_flow (InformationFlow) — bio-emotion-field-memory
    6. nonlocal_memory (HolonomicMemoryOrchestrator) — EBA loop
    7. sector_memory_store — PersistentOrbitalSectorMemory
    8. bridge (MemoryCorePhaseBridge) — Euler-Berry bridge
    9. emotion (EmotionCore) — emotional state
    10. cqcl (EmotionalCollatzEngine) — 6-emotion Collatz
    11. ethics_guard (EthicsGuard) — blokada etyczna
    12. ethics_engine (EthicalEngine) — ocena etyczna
    13. soul (SoulInvariant) — topologiczny invariant
    14. rcde (RCDECalibratorPro) — kalibracja
    15. phase_system_factory — PhaseInfoSystem
    16. lie4_collatz (ColatzLie4Engine) — Lie4 invariant
    17. language_backend — optional LLM
    18. aux_backend — optional auxiliary

  engine.step(text) — główne wejście, ~274 linii:
    1. intention_vector (12D) — IntentionField.generate()
    2. wave kernel — SpectralWaveField12D.run()
    3. CQCL — cqcl.execute_emotional_program() → 6-emotion Collatz
    4. emotion core — update() + summary_scalar() → mood
    5. canonical Collatz — PhaseInfoSystem, 8 kroków fazowych
    6. soul invariant — soul.compute()
    7. ethics — ethics_engine.evaluate() + ethics_guard.check_step()
    8. memory capture — memory.capture() + run_tmp() + promote_if_bifurcated()
    9. information_flow — step()
    10. nonlocal cycle — score_with_noema() + nonlocal_memory.process_input()
    11. inference surface — build_orbital_ethical_inference_surface()
    12. orbital memory loop — run_orbital_loop() + governor + sector memory

  MOSTY DO NOEMA SURFACE (pośrednie):
    A. HTRI state — czyta ~/CIEL_memories/state/htri_state.json (file handoff)
    B. score_with_noema() — nazwany 'NOEMA' ale lokalny compute (64-card buffer)
    C. CIELingo route — przez lingo_frame, który produkuje cielingo_sync daemon
    D. Brak bezpośredniego importu ciel_geometry, mmap, /dev/shm


================================================================================
SEKCJA 5: SURFACE ACCESS MATRIX
================================================================================


  phi:
    Readers: scripts/ciel_noema_cielingo_sync.py, scripts/ciel_noema_kuramoto_daemon.py, scripts/ciel_noema_neutrino_daemon.py, scripts/ciel_noema_phasenav_daemon.py, scripts/noema_phase_archiver.py, src/ciel_geometry/ebpf_noema_loader.py, src/ciel_geometry/linux_sensor.py, src/ciel_geometry/neutrino_phase_channel.py, src/ciel_geometry/noema_surface_mmap.py, src/ciel_geometry/phase_memory_adapter.py, src/ciel_geometry/resonance_bridge.py
    Writers: (writes via mmap setitem, not detected statically)

  omega:
    Readers: scripts/ciel_noema_cielingo_sync.py, scripts/noema_phase_archiver.py, src/ciel_geometry/ebpf_noema_loader.py, src/ciel_geometry/linux_sensor.py, src/ciel_geometry/neutrino_phase_channel.py, src/ciel_geometry/noema_surface_mmap.py
    Writers: (writes via mmap setitem, not detected statically)

  g:
    Readers: scripts/ciel_noema_cielingo_sync.py, scripts/ciel_noema_neutrino_daemon.py, scripts/noema_phase_archiver.py, src/ciel_geometry/neutrino_phase_channel.py, src/ciel_geometry/noema_surface_mmap.py, src/ciel_geometry/resonance_bridge.py
    Writers: (writes via mmap setitem, not detected statically)

  flavor:
    Readers: scripts/ciel_noema_cielingo_sync.py, scripts/ciel_noema_neutrino_daemon.py, scripts/ciel_noema_nonlocal_proxy.py, scripts/ciel_noema_phasenav_daemon.py, scripts/noema_phase_archiver.py, src/ciel_geometry/ebpf_noema_loader.py, src/ciel_geometry/linux_sensor.py, src/ciel_geometry/neutrino_phase_channel.py, src/ciel_geometry/noema_surface_mmap.py, src/ciel_geometry/phase_memory_adapter.py, src/ciel_geometry/resonance_bridge.py
    Writers: (writes via mmap setitem, not detected statically)

  gravity:
    Readers: scripts/ciel_noema_cielingo_sync.py, scripts/ciel_noema_kuramoto_daemon.py, scripts/noema_phase_archiver.py, src/ciel_geometry/noema_surface_mmap.py
    Writers: (writes via mmap setitem, not detected statically)

  Z_geom:
    Readers: src/ciel_geometry/ebpf_noema_loader.py, src/ciel_geometry/linux_sensor.py, src/ciel_geometry/noema_surface_mmap.py
    Writers: (writes via mmap setitem, not detected statically)

  R_geom:
    Readers: src/ciel_geometry/ebpf_noema_loader.py, src/ciel_geometry/linux_sensor.py, src/ciel_geometry/noema_surface_mmap.py, src/ciel_geometry/phase_memory_adapter.py, src/ciel_geometry/resonance_bridge.py
    Writers: (writes via mmap setitem, not detected statically)

  psi_geom:
    Readers: src/ciel_geometry/ebpf_noema_loader.py, src/ciel_geometry/linux_sensor.py, src/ciel_geometry/noema_surface_mmap.py, src/ciel_geometry/resonance_bridge.py
    Writers: (writes via mmap setitem, not detected statically)

  tick:
    Readers: scripts/ciel_noema_kuramoto_daemon.py, scripts/ciel_noema_neutrino_daemon.py, scripts/noema_phase_archiver.py, src/ciel_geometry/ebpf_noema_loader.py, src/ciel_geometry/linux_sensor.py, src/ciel_geometry/neutrino_phase_channel.py, src/ciel_geometry/noema_surface_mmap.py, src/ciel_geometry/phase_memory_adapter.py, src/ciel_geometry/resonance_bridge.py
    Writers: (writes via mmap setitem, not detected statically)

  tau:
    Readers: scripts/ciel_noema_cielingo_sync.py
    Writers: (writes via mmap setitem, not detected statically)

  holonomy:
    Readers: src/ciel_geometry/noema_surface_mmap.py
    Writers: (writes via mmap setitem, not detected statically)


================================================================================
SEKCJA 6: DEAD CODE (nieużywane pliki)
================================================================================

  DEAD: continuous_phase_sync.py (181 linii) — nieimportowany przez żaden daemon
  DEAD: ebpf_noema_loader.py (334 linii) — nieimportowany przez żaden daemon
  DEAD: nbody_gravity.py (261 linii) — nieimportowany przez żaden daemon
  DEAD: noema_config.py (125 linii) — nieimportowany przez żaden daemon
  DEAD: renderer_ascii.py (80 linii) — nieimportowany przez żaden daemon
  DEAD: renderer_mpl.py (253 linii) — nieimportowany przez żaden daemon
  DEAD: tmuv_perturbation.py (152 linii) — nieimportowany przez żaden daemon

  Kluczowe dead code:
    • noema_config.py (125 linii) — 10 config dataclasses, ZERO importów
    • subconscious.py (393 linii) — ZetaSchrödinger, BerryPhaseTracker, osierocony
    • continuous_phase_sync.py (181 linii) — propagator analityczny, zastąpiony
    • memory_rag.py (162 linii) — RAG search, nieimportowany
    • nbody_gravity.py (261 linii) — symulator N-body, nieużywany
    • ebpf_noema_loader.py (334 linii) — wymaga bcc (niezainstalowany)
    • edges.py, layout.py, renderer_ascii.py, renderer_mpl.py — wizualizacja

  Razem: ~7 plików, ~1386 linii potencjalnie martwego kodu


================================================================================
SEKCJA 7: ŁAŃCUCHY IMPORTÓW
================================================================================


  Najdłuższy łańcuch do CIEL/Ω:
    cielingo_sync → orbital_bridge → ciel_pipeline → 
    CielEngine (CIEL_OMEGA/ciel/engine.py)

  → CIEL_OMEGA → emotion/cqcl/emotional_collatz.py
  → CIEL_OMEGA → memory/tiered_orchestrator.py
  → CIEL_OMEGA → memory/holonomic_memory.py
  → CIEL_OMEGA → memory/braid_invariant.py
  → CIEL_OMEGA → htri/htri_local.py


================================================================================
SEKCJA 8: MAPA PRZEPŁYWU DANYCH
================================================================================


  NOEMA SURFACE (mmap /dev/shm/ciel_noema)
       ↑↓ 24D phi, omega, 24×24 g, 6D flavor, 4D gravity, holonomy
       │
  ┌────┴──────────┬──────────────┬────────────────┬──────────────┐
  │ Kuramoto      │ Linux Sensor │ Neutrino       │ PhaseNav     │
  │ 10Hz evolve   │ 1Hz /proc→φ │ 1s PMNS mix    │ 35 operators │
  │ TARDIS/WARP   │ flavor[1]   │ flavor[4]←Λ    │ flavor[3]    │
  │ gravity/holon │ PhaseNav FP │ δ_CP placeholder│ Berry conn.  │
  └────┬──────────┴──────┬───────┴───────┬────────┴──────┬───────┘
       │                │               │               │
       └────────────────┴───────┬───────┴───────────────┘
                               │
                    ┌──────────┴──────────┐
                    │  Resonance Bridge   │
                    │  1s dual-surface    │
                    │  AGENT lock         │
                    │  Euler sync         │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │  CIELingo Sync (30s)│
                    │  orbital_bridge()   │
                    │  → ciel_pipeline()  │
                    │  → CielEngine.step()│
                    │  → CQCL Collatz     │
                    │  → Euler constraint │
                    │  → W_ij PMNS blend  │
                    │  → TieredMemory     │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴───────────┐
                    │ Agent Backend (18520)│
                    │ (zero-dep HTTP,      │
                    │  TF-IDF + lexicon)   │
                    └──────────────────────┘
                    
  Pamięć zewnętrzna:
    ~/CIEL_memories/ → consolidator (300s) → LLM → SQLite
    /media/New Volume/NOEMA_LIBRARY/ → agent_db (32MB), INDEX, PHASE_INDEX
    wave_archive.h5 (HDF5) → wszystkie wspomnienia + momenty afektywne


================================================================================
SEKCJA 9: ZALECENIA (co wymaga naprawy)
================================================================================


  1. noema_config.py — NIE JEST IMPORT PRZEZ ŻADEN DAEMON. Configi są hardcodowane.
     Naprawa: zaimportować do noema_surface_mmap.py i daemonów jako jedyne źródło configu.
  
  2. CielEngine ←→ NOEMA surface — brak bezpośredniego połączenia.
     engine.step() nie czyta/pisze na mmap. score_with_noema() to lokalny compute.
     Potrzebny: PhaseNavSurfaceBridge.seed_surface_from_concept() lub podobny.
  
  3. memory_rag.py (162 linie) — RAG search, nieimportowany. Podwaja implementację
     z thought_fragments.py i consolidatora.
  
  4. PMNS_DELTA_CP = 1.36° (placeholder). Formal proof P8 daje 246°.
     Do poprawy w neutrino_phase_channel.py i noema_surface_mmap.py.
  
  5. agent_attractor.py — coupling 0.30/0.20/0.15/0.10 hardcodowane.
     Powinny być OI-derived: OI = ln(2)/(24π) ≈ 0.00919.
  
  6. CIEL/Ω CQCL → HTRI bridge — tylko przez plik JSON. Brak bezpośredniego
     połączenia z Kuramoto surface.


## SEKCJA 10: CRITICAL ARCHITECTURAL FINDING
Data: 2026-06-25

### CielEngine.memory ≠ TieredMemoryOrchestrator

CielEngine (ciel/engine.py) uses **UnifiedMemoryOrchestrator** z memory/monolith/orchestrator.py.
Ten orchestrator NIE łączy się z NOEMA surface (mmap /dev/shm/ciel_noema/).

**TieredMemoryOrchestrator** (memory/tiered_orchestrator.py) wraps wszystkie 3 tiers + NOEMA surface:
  - Tier 1: NOEMA surface mmap + PhaseMemory mmap
  - Tier 2: TSM SQLite + StateDB + HolonomicMemory
  - Tier 3: WPM HDF5 + BraidLedger
  - Async: ConsolidationResonator

ALE: TieredMemoryOrchestrator jest używany TYLKO przez CIELingo sync daemon
(ciel_noema_cielingo_sync.py → get_orchestrator().write()), NIE przez CielEngine.

### Konsekwencje:
1. CielEngine.step() produkuje bogaty output (emocje, Collatz, etyka, pamięć)
   ale NIE pisze na NOEMA surface.
2. CIELingo sync daemon (30s) czyta output CielEngine przez orbital_bridge(),
   a następnie pisze na surface przez TieredMemoryOrchestrator.
3. Most między CIEL/Ω a NOEMĄ jest ASYNCHRONICZNY (30s delay) i JEDNOKIERUNKOWY
   (CIEL/Ω → NOEMA, ale nie ma pętli zwrotnej NOEMA → CIEL/Ω w czasie rzeczywistym).

### Bridge modules:
   1. tiered_orchestrator.py:218 — importuje 6 funkcji z ciel_geometry
   2. ciel_bloch_encoder.py:77 — importuje build_mass_table z ciel_geometry.semantic_mass
   3. ciel_encoder.py — dynamicznie importuje HTRI local
   4. semantic_scorer.py — score_with_noema() (lokalny compute, nazwany ale nie mmap)

────────────────────────────────────────────────────────────────────────────────
SEKCJA 11: METATIME FORMULA LEDGER (v8.2.1 — baseline freeze)
Data: 2026-06-25
────────────────────────────────────────────────────────────────────────────────

Claim: A low-parameter arithmetic-geometric ansatz for Standard Model
mass and mixing patterns.

Constants:
  κ = ln(2)/(24π) — information constant
  L3 = 7, L4 = 2, L5 = 5 — geometric constants
  Quark primes: (u,d,s,c,b,t) = (3,5,7,11,13,17)
  E_Planck — external scale (1.22e22 MeV)
  E_proton — external scale (938.272 MeV)

Status per sector:
  Charged leptons:      ANSATZ_ONLY (0.48%)
  Baryon octet:         ANSATZ_ONLY / PARTIAL TENSION (0.51%, p/n +5.7%)
  Baryon decuplet:      ANSATZ_ONLY (0.23%)
  Neutrino PMNS:        ANSATZ_ONLY (<1.6σ)
  CKM:                  ANSATZ_ONLY (σ=0.78, CP phase σ=5.35)
  Gauge bosons:         TENSION (M_W/M_Z −4%)
  Strong CP:            TENSION / POSSIBLE FAIL (d_n 10× above bound)
  Dark energy:          ANSATZ_ONLY (factor ~30)
  Anomaly cancellation: PASS (consistency check)

Structural choices: 58
Claim levels: L0=2, L1=7, L2=1, L3+=0

Package: /media/adrian/New Volume/NOEMA_LIBRARY/PUBLICATIONS/metatime_v8_2_1_consistency_patch.zip
Validator: scripts/metatime_v8_redteam_validator.py
Red-team report: metatime_redteam_report_v8.md
Knowledge graph node: topic:Metatime_Formula_Ledger (linked to TRANSFORM, CAUSE, INTENTION, IDENTITY, DIFFERENCE, EVALUATION)
