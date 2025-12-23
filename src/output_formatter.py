from typing import List
from .incident_analysis import IncidentAnalysis


def print_section(title: str) -> None:
    print(f"\n--- {title} ---")


def print_list(items: List[str]) -> None:
    for item in items:
        print(f"- {item}")


def format_incident_output(analysis: IncidentAnalysis) -> None:
    """
    Responsible ONLY for presentation / formatting of the analysis output.
    No logic or decision-making lives here.
    """

    print("\n=== Incident Analysis Result ===")

    print(f"Category: {analysis.category}")
    print(f"Severity: {analysis.severity}")
    print(f"Likely cause: {analysis.likely_cause}")

    print_section("Root Cause Hypothesis (RCA)")
    print(analysis.root_cause_hypothesis)

    print_section("Framework Mapping")
    print(f"MSB classification: {analysis.msb_classification}")
    print(f"NIS2 relevance: {analysis.nis2_relevance}")
    print(f"ISO/IEC 27001 reference: {analysis.iso27001_reference}")


    print_section("Recommended Actions")
    print_list(analysis.recommended_actions)

    print_section("Evidence to Collect")
    print_list(analysis.evidence_to_collect)

    print_section("Triage Timeline")

    print("\n0–30 min:")
    print_list(analysis.triage_0_30m)

    print("\n1–4 h:")
    print_list(analysis.triage_1_4h)

    print("\n24–72 h:")
    print_list(analysis.triage_24_72h)
