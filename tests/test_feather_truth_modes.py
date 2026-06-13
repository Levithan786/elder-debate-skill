from algorithms.feather_truth_modes import (
    Feather,
    FeatherStatus,
    TeliosisMode,
    TruthMode,
    build_default_feather_registry,
    route_claim_to_feathers,
    verify_feather,
)


def test_default_feather_registry_is_ratified():
    registry = build_default_feather_registry()

    assert registry.ratified
    assert len(registry.feathers) == 8
    assert {feather.truth_mode for feather in registry.feathers} == set(TruthMode)


def test_feather_without_evidence_is_not_ratified():
    feather = Feather(
        name="Unproven Feather",
        truth_mode=TruthMode.WITNESS,
        teliosis_mode=TeliosisMode.RECORD,
        truth_question="What was seen?",
        teliosis="Record the seen.",
        evidence_required=(),
        output_contract="Observation note.",
    )

    verification = verify_feather(feather)

    assert verification.status == FeatherStatus.NEEDS_EVIDENCE
    assert not verification.ratified


def test_route_claim_to_ratified_feathers():
    routed = route_claim_to_feathers("Build the next debate artifact.")

    assert "witness_feather" in routed
    assert "ledger_feather" in routed
    assert routed["craft_feather"].startswith("operational:build")


def test_empty_claim_is_blocked():
    routed = route_claim_to_feathers("   ")

    assert routed == {"blocked": "empty claim cannot be routed through feathers"}
