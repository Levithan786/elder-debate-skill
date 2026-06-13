"""Algorithm substrate for the elder debate skill."""

from .feather_truth_modes import (
    Feather,
    FeatherGateStatus,
    FeatherRegistry,
    FeatherStatus,
    FeatherVerification,
    TeliosisMode,
    TruthMode,
    build_default_feather_registry,
    build_feather_registry,
    default_feathers,
    route_claim_to_feathers,
    verify_feather,
)
from .telosis_after_debate import (
    DebatePosition,
    ProofGateStatus,
    TelosisClause,
    TelosisState,
    build_default_sulimania_telosis,
    renegotiate_telosis,
)

__all__ = [
    "DebatePosition",
    "Feather",
    "FeatherGateStatus",
    "FeatherRegistry",
    "FeatherStatus",
    "FeatherVerification",
    "ProofGateStatus",
    "TeliosisClause",
    "TeliosisMode",
    "TelosisState",
    "TruthMode",
    "build_default_feather_registry",
    "build_default_sulimania_telosis",
    "build_feather_registry",
    "default_feathers",
    "renegotiate_telosis",
    "route_claim_to_feathers",
    "verify_feather",
]
