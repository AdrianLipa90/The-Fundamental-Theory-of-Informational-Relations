#!/usr/bin/env python3
import json, pathlib, math, sys
here=pathlib.Path(__file__).resolve().parents[1]
res=here/'results'/'E_MU_RELEASE_REFINEMENT_GATE_v7_0.json'
data=json.loads(res.read_text())
assert data['technical_status']=='PASS'
assert data['canon_allowed'] is False
assert data['mass_spectrum_closure_claimed'] is False
ip=data['input_policy']
for k in ['electron_mass_as_input','muon_mass_as_input','tau_mass_as_input','PDG_table_as_input','exact_replay_table_as_input','v6_1_action_target_as_input']:
    assert ip[k] is False, k
assert ip['scoring_after_freeze_only'] is True
assert data['derived_e_mu_release_action'] > 0
assert abs(data['scoring_only']['energy_ratio_relative_error']) < 0.02
print('VALIDATION_MODULE70_v7_0: PASS')
