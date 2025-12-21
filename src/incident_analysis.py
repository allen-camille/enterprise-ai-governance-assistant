from dataclasses import dataclass


@dataclass
class IncidentAnalysis:
    category: str
    severity: str
    likely_cause: str
    root_cause_hypothesis: str
    recommended_actions: list[str]
    evidence_to_collect: list[str]

    triage_0_30m: list[str]
    triage_1_4h: list[str]
    triage_24_72h: list[str]

    msb_classification: str
    nis2_relevance: str
    iso27001_reference: str


def analyze_incident(description: str) -> IncidentAnalysis:
    """
    Rule-based incident analysis with RCA and evidence collection.
    Simulates structured analyst reasoning before LLM integration.
    """

    text = description.lower()

    if "malware" in text or "virus" in text or "botnet" in text:
        return IncidentAnalysis(
            category="Malware infection",
            severity="High",
            likely_cause="Suspicious process or external communication detected",
            root_cause_hypothesis=(
                "Initial infection likely caused by phishing, malicious download "
                "or exploitation of an unpatched vulnerability, followed by "
                "command-and-control communication."
            ),
            recommended_actions=[
                "Isolate affected system",
                "Run antivirus / EDR scan",
                "Collect logs for forensic analysis",
                "Notify security team",
            ],
            evidence_to_collect=[
                "Process list and running services",
                "EDR alerts and scan results",
                "DNS, proxy and firewall logs",
                "Suspicious files and hashes",
                "User activity and email logs",
            ],
            triage_0_30m=[
                "Isolate the host from the network",
                "Preserve volatile evidence (process list, network connections)",
                "Notify SOC / incident handler",
            ],
            triage_1_4h=[
                "Collect endpoint + DNS/proxy logs",
                "Run EDR scan and identify persistence mechanisms",
                "Scope: check if other hosts show similar indicators",
            ],
            triage_24_72h=[
                "Validate containment and monitor for recurrence",
                "Plan eradication + recovery steps",
                "Document incident and lessons learned",
            ],
            msb_classification="Informationssäkerhetsincident – Skadlig kod / Botnet / Intrångsförsök",
            nis2_relevance=(
                "Potentiellt NIS2-relevant om incidenten påverkar "
                "tillgänglighet, konfidentialitet eller integritet i viktiga system."
            ),
            iso27001_reference=(
                "ISO/IEC 27001:2022 – Incidenthantering, "
                "loggning/övervakning och hantering av säkerhetshändelser."
            ),
        )

    if "slow" in text or "cpu" in text:
        return IncidentAnalysis(
            category="Performance degradation",
            severity="Medium",
            likely_cause="High resource usage or misbehaving process",
            root_cause_hypothesis=(
                "Performance degradation likely caused by misbehaving application, "
                "resource leak, scheduled task or early-stage malware activity."
            ),
            recommended_actions=[
                "Inspect running processes",
                "Check recent changes",
                "Monitor system performance",
            ],
            evidence_to_collect=[
                "CPU and memory usage metrics",
                "Running processes and services",
                "Recent software changes",
                "System and application event logs",
            ],
            triage_0_30m=[
                "Identify top CPU/memory processes",
                "Check if the device is business-critical",
                "Capture quick snapshot of system state",
            ],
            triage_1_4h=[
                "Review recent installs/updates and scheduled tasks",
                "Analyze event logs for anomalies",
                "Run targeted malware scan if suspicious behavior appears",
            ],
            triage_24_72h=[
                "Apply fixes or configuration changes",
                "Improve monitoring thresholds",
                "Document root cause and preventive actions",
            ],
            msb_classification="Informationssäkerhetsincident – Driftstörning / Avvikande systembeteende",
            nis2_relevance=(
                "Kan bli NIS2-relevant om tillgänglighet eller "
                "driftsäkerhet för viktiga tjänster påverkas."
            ),
            iso27001_reference=(
                "ISO/IEC 27001:2022 – Driftövervakning, "
                "ändringshantering och incidenthantering."
            ),
        )

    return IncidentAnalysis(
        category="Unclassified incident",
        severity="Low",
        likely_cause="Insufficient information",
        root_cause_hypothesis=(
            "Root cause cannot be determined with current information. "
            "Additional data is required."
        ),
        recommended_actions=[
            "Collect more details from user",
            "Review logs",
        ],
        evidence_to_collect=[
            "User-reported symptoms and timeline",
            "System and application logs",
            "Network traffic overview",
        ],
        triage_0_30m=[
            "Clarify incident details and scope",
            "Determine if the incident is ongoing",
        ],
        triage_1_4h=[
            "Collect relevant logs",
            "Assess potential business impact",
        ],
        triage_24_72h=[
            "Finalize classification",
            "Document findings and close incident",
        ],
        msb_classification="Oklar – kräver mer information",
        nis2_relevance="Bedöms när påverkan och omfattning är fastställd.",
        iso27001_reference="ISO/IEC 27001:2022 – Rapportering och hantering av säkerhetshändelser.",
    )
