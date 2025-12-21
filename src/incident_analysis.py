from dataclasses import dataclass


@dataclass
class IncidentAnalysis:
    category: str
    severity: str
    likely_cause: str
    recommended_actions: list[str]


def analyze_incident(description: str) -> IncidentAnalysis:
    """
    Simple rule-based incident analysis.
    This simulates AI reasoning before we plug in a real LLM.
    """

    text = description.lower()

    if "malware" in text or "virus" in text or "botnet" in text:
        return IncidentAnalysis(
            category="Malware infection",
            severity="High",
            likely_cause="Suspicious process or external communication detected",
            recommended_actions=[
                "Isolate affected system",
                "Run antivirus / EDR scan",
                "Collect logs for forensic analysis",
                "Notify security team",
            ],
        )

    if "slow" in text or "cpu" in text:
        return IncidentAnalysis(
            category="Performance degradation",
            severity="Medium",
            likely_cause="High resource usage or misbehaving process",
            recommended_actions=[
                "Inspect running processes",
                "Check recent changes",
                "Monitor system performance",
            ],
        )

    return IncidentAnalysis(
        category="Unclassified incident",
        severity="Low",
        likely_cause="Insufficient information",
        recommended_actions=[
            "Collect more details from user",
            "Review logs",
        ],
    )
