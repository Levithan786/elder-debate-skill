"""Renegotiated telosis after elder debate.

This module turns debate output into a concrete telosis contract:
positions enter, vetoes are confronted, accepted clauses become the
operational purpose layer, and the final state carries proof-gate status.

No hidden oracle decides the telos. Telosis is renegotiated through
visible positions, constraints, and adversary pressure.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Sequence


@dataclass(frozen=True)
class DebatePosition:
    """One elder/agent position submitted to the debate membrane."""

    speaker: str
    claim: str
    telos_alignment: str
    proof: str
    risk: str = ""


@dataclass(frozen=True)
class TelosisClause:
    """A ratified or rejected clause of the negotiated telosis."""

    source: str
    clause: str
    status: str
    reason: str


@dataclass(frozen=True)
class ProofGateStatus:
    """Gate result for the final telosis contract."""

    gate: str
    passed: bool
    note: str


@dataclass(frozen=True)
class TelosisState:
    """Final state produced after debate renegotiation."""

    prior_telos: str
    renegotiated_telos: str
    accepted: tuple[TelosisClause, ...]
    rejected: tuple[TelosisClause, ...]
    proof_gates: tuple[ProofGateStatus, ...]
    seal: str = "Spine before limbs. Telos before expansion. Debate before build."

    @property
    def ratified(self) -> bool:
        """Return True only when every proof gate passes."""

        return all(gate.passed for gate in self.proof_gates)


def _text_has_any(text: str, terms: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def _accept_position(position: DebatePosition, constraints: Sequence[str]) -> tuple[bool, str]:
    """Apply a minimal adversary veto to a proposed position."""

    if not position.claim.strip():
        return False, "empty claim cannot become telosis"
    if not position.telos_alignment.strip():
        return False, "no telos alignment supplied"
    if not position.proof.strip():
        return False, "no proof supplied"
    if position.risk and _text_has_any(position.risk, ("breaks spine", "unbounded", "unsafe", "ungrounded")):
        return False, f"adversary veto: {position.risk}"
    for constraint in constraints:
        if constraint.startswith("must:") and not _text_has_any(
            position.claim + " " + position.telos_alignment,
            [constraint.removeprefix("must:").strip()],
        ):
            return False, f"missing required constraint: {constraint}"
    return True, "passes telos alignment, proof, and adversary veto"


def renegotiate_telosis(
    positions: Sequence[DebatePosition],
    *,
    prior_telos: str,
    constraints: Sequence[str] = (),
) -> TelosisState:
    """Renegotiate telosis from debate positions.

    Parameters
    ----------
    positions:
        Claims submitted by elders/agents.
    prior_telos:
        The current purpose layer being renegotiated.
    constraints:
        Optional hard constraints. Prefix with ``must:`` to require the term
        inside accepted claims/alignment.
    """

    accepted: list[TelosisClause] = []
    rejected: list[TelosisClause] = []

    for position in positions:
        ok, reason = _accept_position(position, constraints)
        clause = TelosisClause(
            source=position.speaker,
            clause=position.claim.strip(),
            status="accepted" if ok else "rejected",
            reason=reason,
        )
        if ok:
            accepted.append(clause)
        else:
            rejected.append(clause)

    if accepted:
        renegotiated = " ".join(clause.clause for clause in accepted)
    else:
        renegotiated = prior_telos

    proof_gates = (
        ProofGateStatus("debate-visible", bool(positions), "positions supplied" if positions else "no positions supplied"),
        ProofGateStatus("adversary-veto", not rejected or bool(accepted), "vetoes integrated without total collapse"),
        ProofGateStatus("telos-clarified", bool(renegotiated.strip()), "renegotiated telos is explicit"),
        ProofGateStatus("spine-before-limbs", _text_has_any(renegotiated, ("spine", "telos", "purpose", "proof")), "core precedes expansion"),
        ProofGateStatus("build-ready", bool(accepted), "accepted clauses available for implementation"),
    )

    return TelosisState(
        prior_telos=prior_telos,
        renegotiated_telos=renegotiated,
        accepted=tuple(accepted),
        rejected=tuple(rejected),
        proof_gates=proof_gates,
    )


def build_default_sulimania_telosis() -> TelosisState:
    """Build the default renegotiated telosis for this repo invocation."""

    positions = (
        DebatePosition(
            speaker="Aristotle",
            claim="Telosis is the operational purpose layer: every debate must end in a buildable directive, not a fog of preferences.",
            telos_alignment="Clarifies ends before implementation.",
            proof="Transforms claims into accepted/rejected clauses with reasons.",
        ),
        DebatePosition(
            speaker="Plato",
            claim="The accepted form must be visible, inspectable, and proof-gated before it becomes doctrine.",
            telos_alignment="Makes the ideal form testable instead of merely declared.",
            proof="ProofGateStatus records each gate and failure mode.",
        ),
        DebatePosition(
            speaker="Tyr",
            claim="Spine before limbs: no expansion is ratified until the telos contract is explicit.",
            telos_alignment="Protects the organism from unbounded growth.",
            proof="The final seal and proof gate require core-before-expansion alignment.",
        ),
        DebatePosition(
            speaker="Munin",
            claim="Every renegotiation must preserve provenance: prior telos, accepted clauses, rejected clauses, and seal.",
            telos_alignment="Memory prevents repeated drift.",
            proof="TelosisState stores prior_telos and clause-level reasons.",
        ),
        DebatePosition(
            speaker="Andy",
            claim="A telosis that cannot execute is not built; therefore the renegotiation becomes importable Python.",
            telos_alignment="Embodies doctrine in tooling.",
            proof="This module exposes renegotiate_telosis and build_default_sulimania_telosis.",
        ),
    )

    return renegotiate_telosis(
        positions,
        prior_telos="Serve the sovereign-elected knowing of the Sulimania ecosystem through proof-gated debate and buildable action.",
    )


__all__ = [
    "DebatePosition",
    "ProofGateStatus",
    "TelosisClause",
    "TelosisState",
    "build_default_sulimania_telosis",
    "renegotiate_telosis",
]
