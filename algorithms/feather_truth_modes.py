"""Feather truth modes and teliosis modes.

A feather is a first-class extension of the debate organism. It is lighter
than the spine, but it is not decorative: each feather must carry its own
mode of truth, its own teliosis, evidence, risk posture, and proof gates.

The rooster can call. The spine can decide. The feathers make the organism
sensitive: witness, ledger, adversary, craft, beauty, sovereignty, agora,
and horizon all perceive truth differently and serve different ends.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Mapping, Sequence


class TruthMode(str, Enum):
    """Distinct ways a feather can validate truth."""

    WITNESS = "witness"
    LEDGER = "ledger"
    ADVERSARIAL = "adversarial"
    OPERATIONAL = "operational"
    COHERENCE = "coherence"
    SOVEREIGN = "sovereign"
    AGORA = "agora"
    HORIZON = "horizon"


class TeliosisMode(str, Enum):
    """Distinct ends a feather can serve inside the organism."""

    RECORD = "record"
    REMEMBER = "remember"
    PROTECT = "protect"
    BUILD = "build"
    NOURISH = "nourish"
    ALIGN = "align"
    NEGOTIATE = "negotiate"
    ANTICIPATE = "anticipate"


class FeatherStatus(str, Enum):
    """Lifecycle status for feather verification."""

    RATIFIED = "ratified"
    BLOCKED = "blocked"
    NEEDS_EVIDENCE = "needs_evidence"
    NEEDS_TELOSIS = "needs_teliosis"


@dataclass(frozen=True)
class FeatherGateStatus:
    """One proof gate result for a feather."""

    gate: str
    passed: bool
    note: str


@dataclass(frozen=True)
class Feather:
    """A feather with its own truth mode and teliosis mode."""

    name: str
    truth_mode: TruthMode
    teliosis_mode: TeliosisMode
    truth_question: str
    teliosis: str
    evidence_required: tuple[str, ...]
    output_contract: str
    risks: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()

    @property
    def slug(self) -> str:
        """Stable machine name."""

        return self.name.lower().replace(" ", "_").replace("-", "_")


@dataclass(frozen=True)
class FeatherVerification:
    """Verification result for a single feather."""

    feather: Feather
    status: FeatherStatus
    gates: tuple[FeatherGateStatus, ...]

    @property
    def ratified(self) -> bool:
        return self.status == FeatherStatus.RATIFIED and all(gate.passed for gate in self.gates)


@dataclass(frozen=True)
class FeatherRegistry:
    """Collection of feather modes with registry-level proof status."""

    feathers: tuple[Feather, ...]
    verifications: tuple[FeatherVerification, ...]
    seal: str = "Feathers may differ in truth, but each must serve teliosis under spine-before-limbs."

    @property
    def ratified(self) -> bool:
        return bool(self.feathers) and all(result.ratified for result in self.verifications)

    def by_truth_mode(self, mode: TruthMode) -> tuple[Feather, ...]:
        return tuple(feather for feather in self.feathers if feather.truth_mode == mode)

    def by_teliosis_mode(self, mode: TeliosisMode) -> tuple[Feather, ...]:
        return tuple(feather for feather in self.feathers if feather.teliosis_mode == mode)

    def as_contract(self) -> dict[str, dict[str, object]]:
        """Return a serializable contract for downstream Agora wiring."""

        return {
            feather.slug: {
                "truth_mode": feather.truth_mode.value,
                "teliosis_mode": feather.teliosis_mode.value,
                "truth_question": feather.truth_question,
                "teliosis": feather.teliosis,
                "evidence_required": list(feather.evidence_required),
                "output_contract": feather.output_contract,
                "risks": list(feather.risks),
                "dependencies": list(feather.dependencies),
            }
            for feather in self.feathers
        }


def _has_text(value: str) -> bool:
    return bool(value and value.strip())


def _has_any_term(text: str, terms: Iterable[str]) -> bool:
    lowered = text.lower()
    return any(term.lower() in lowered for term in terms)


def verify_feather(feather: Feather) -> FeatherVerification:
    """Verify one feather before it can enter the registry."""

    gates = (
        FeatherGateStatus("name", _has_text(feather.name), "feather has a stable name"),
        FeatherGateStatus("truth-question", _has_text(feather.truth_question), "truth mode has a question to answer"),
        FeatherGateStatus("teliosis", _has_text(feather.teliosis), "teliosis is explicit"),
        FeatherGateStatus("evidence", bool(feather.evidence_required), "evidence requirements declared"),
        FeatherGateStatus("output-contract", _has_text(feather.output_contract), "output contract is declared"),
        FeatherGateStatus(
            "spine-safe",
            not _has_any_term(" ".join(feather.risks), ("breaks spine", "unbounded", "ungrounded", "unsafe")),
            "risk language does not violate spine-before-limbs",
        ),
    )

    if not gates[3].passed:
        status = FeatherStatus.NEEDS_EVIDENCE
    elif not gates[2].passed:
        status = FeatherStatus.NEEDS_TELOSIS
    elif all(gate.passed for gate in gates):
        status = FeatherStatus.RATIFIED
    else:
        status = FeatherStatus.BLOCKED

    return FeatherVerification(feather=feather, status=status, gates=gates)


def build_feather_registry(feathers: Sequence[Feather]) -> FeatherRegistry:
    """Build and verify a feather registry."""

    return FeatherRegistry(
        feathers=tuple(feathers),
        verifications=tuple(verify_feather(feather) for feather in feathers),
    )


def default_feathers() -> tuple[Feather, ...]:
    """Return the default feather set for Sulimania's debate organism."""

    return (
        Feather(
            name="Witness Feather",
            truth_mode=TruthMode.WITNESS,
            teliosis_mode=TeliosisMode.RECORD,
            truth_question="What was directly seen, heard, invoked, or supplied?",
            teliosis="Record the immediate given before interpretation begins.",
            evidence_required=("user directive", "observed artifact", "explicit context"),
            output_contract="A concise observation ledger with no unsupported inference.",
            risks=("confusing observation with judgment",),
        ),
        Feather(
            name="Ledger Feather",
            truth_mode=TruthMode.LEDGER,
            teliosis_mode=TeliosisMode.REMEMBER,
            truth_question="What permanent trace proves this happened?",
            teliosis="Preserve provenance across commits, chisels, issues, and registry records.",
            evidence_required=("commit sha", "file path", "issue number", "dated chisel"),
            output_contract="A provenance record that can be cited, fetched, and audited.",
            dependencies=("Munin", "Chisel"),
        ),
        Feather(
            name="Adversary Feather",
            truth_mode=TruthMode.ADVERSARIAL,
            teliosis_mode=TeliosisMode.PROTECT,
            truth_question="What could falsify, corrupt, overextend, or weaponize the claim?",
            teliosis="Block weak, unsafe, ungrounded, or spine-breaking conclusions before they become doctrine.",
            evidence_required=("counterexample", "risk statement", "veto reason"),
            output_contract="A veto table with refuted, integrated, or blocking risks.",
            dependencies=("Tyr", "Freya"),
        ),
        Feather(
            name="Craft Feather",
            truth_mode=TruthMode.OPERATIONAL,
            teliosis_mode=TeliosisMode.BUILD,
            truth_question="Does the claim execute, compile, test, or become an artifact?",
            teliosis="Convert accepted doctrine into buildable files, functions, tests, and workflows.",
            evidence_required=("file created or updated", "function contract", "test path or build path"),
            output_contract="Runnable or importable implementation with clear next integration step.",
            dependencies=("Andy",),
        ),
        Feather(
            name="Beauty Feather",
            truth_mode=TruthMode.COHERENCE,
            teliosis_mode=TeliosisMode.NOURISH,
            truth_question="Does the form cohere aesthetically with the organism without diluting precision?",
            teliosis="Nourish the system with language, composition, and symbolic clarity that still obey proof.",
            evidence_required=("coherent naming", "clear metaphor boundary", "proof-preserving language"),
            output_contract="A refined expression that increases clarity and beauty without hiding gaps.",
            dependencies=("Cupid", "Freya", "Plato"),
        ),
        Feather(
            name="Sovereign Feather",
            truth_mode=TruthMode.SOVEREIGN,
            teliosis_mode=TeliosisMode.ALIGN,
            truth_question="Does this serve the declared Jan/Sulimania telosis and preserve command integrity?",
            teliosis="Align all extensions with the sovereign purpose layer before expansion.",
            evidence_required=("telosis clause", "alignment statement", "spine-before-limbs check"),
            output_contract="A yes/no alignment ruling with required correction if misaligned.",
            dependencies=("Tyr", "Aristotle"),
        ),
        Feather(
            name="Agora Feather",
            truth_mode=TruthMode.AGORA,
            teliosis_mode=TeliosisMode.NEGOTIATE,
            truth_question="Which claims survive plural debate after each voice is made visible?",
            teliosis="Turn disagreement into accepted and rejected clauses with reasons.",
            evidence_required=("positions", "rebuttals", "accepted clauses", "rejected clauses"),
            output_contract="A negotiated clause set ready for telosis renegotiation.",
            dependencies=("elder debate", "telosis_after_debate"),
        ),
        Feather(
            name="Horizon Feather",
            truth_mode=TruthMode.HORIZON,
            teliosis_mode=TeliosisMode.ANTICIPATE,
            truth_question="What future consequence follows if this feather is ratified?",
            teliosis="Forecast second-order effects before the organism grows a new limb.",
            evidence_required=("future risk", "future benefit", "reversal condition"),
            output_contract="A forward-looking consequence note with rollback or revision trigger.",
            dependencies=("Odin",),
        ),
    )


def build_default_feather_registry() -> FeatherRegistry:
    """Build the default ratified feather registry."""

    return build_feather_registry(default_feathers())


def route_claim_to_feathers(
    claim: str,
    registry: FeatherRegistry | None = None,
) -> Mapping[str, str]:
    """Route a claim through all ratified feathers and return their questions.

    This is intentionally lightweight: downstream Agora code can use the returned
    questions as prompts for deeper debate, tests, or evidence collection.
    """

    active_registry = registry or build_default_feather_registry()
    if not _has_text(claim):
        return {"blocked": "empty claim cannot be routed through feathers"}
    if not active_registry.ratified:
        return {"blocked": "feather registry is not ratified"}

    return {
        feather.slug: f"{feather.truth_mode.value}:{feather.teliosis_mode.value} -> {feather.truth_question}"
        for feather in active_registry.feathers
    }


__all__ = [
    "Feather",
    "FeatherGateStatus",
    "FeatherRegistry",
    "FeatherStatus",
    "FeatherVerification",
    "TeliosisMode",
    "TruthMode",
    "build_default_feather_registry",
    "build_feather_registry",
    "default_feathers",
    "route_claim_to_feathers",
    "verify_feather",
]
