from src.incident_analysis import analyze_incident


def run() -> None:
    print("=== Incident Analysis Assistant ===\n")

    description = input("Describe the incident:\n> ")

    analysis = analyze_incident(description)

    print("\n--- Analysis Result ---")
    print(f"Category: {analysis.category}")
    print(f"Severity: {analysis.severity}")
    print(f"Likely cause: {analysis.likely_cause}")

    print("\n--- Root Cause Hypothesis (RCA) ---")
    print(analysis.root_cause_hypothesis)

    print("\n--- Framework Mapping ---")
    print(f"MSB classification: {analysis.msb_classification}")
    print(f"NIS2 relevance: {analysis.nis2_relevance}")
    print(f"ISO/IEC 27001 reference: {analysis.iso27001_reference}")

    print("\nRecommended actions:")
    for action in analysis.recommended_actions:
        print(f"- {action}")

    print("\n--- Evidence to Collect ---")
    for item in analysis.evidence_to_collect:
        print(f"- {item}")

    print("\n--- Triage Timeline ---")

    print("\n0–30 min:")
    for item in analysis.triage_0_30m:
        print(f"- {item}")

    print("\n1–4 h:")
    for item in analysis.triage_1_4h:
        print(f"- {item}")

    print("\n24–72 h:")
    for item in analysis.triage_24_72h:
        print(f"- {item}")
