from src.incident_analysis import analyze_incident


def run() -> None:
    print("=== Incident Analysis Assistant ===\n")

    description = input("Describe the incident:\n> ")

    analysis = analyze_incident(description)

    print("\n--- Analysis Result ---")
    print(f"Category: {analysis.category}")
    print(f"Severity: {analysis.severity}")
    print(f"Likely cause: {analysis.likely_cause}")
    print("Recommended actions:")
    for action in analysis.recommended_actions:
        print(f"- {action}")
