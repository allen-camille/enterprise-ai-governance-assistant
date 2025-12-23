# Enterprise AI Incident & Governance Assistant

A Python-based incident analysis assistant designed to support SOC analysts, security teams and governance functions with structured incident triage, root cause analysis and regulatory mapping.

The project simulates AI-assisted reasoning using deterministic logic and is built to be safely extended with LLMs (e.g. Azure OpenAI) in later stages.

---

## 🎯 Purpose

The assistant helps transform unstructured incident descriptions into:

- Clear incident classification  
- Severity assessment  
- Root Cause Hypothesis (RCA)  
- Evidence collection checklist  
- Time-based triage actions  
- Mapping to regulatory and governance frameworks  

This mirrors real-world workflows used in **incident response, SOC operations and public-sector security governance**.

---

## 🧠 What the Assistant Does

Given a free-text incident description, the assistant produces:

### ✔ Incident Analysis
- Category (e.g. Malware infection, Performance degradation)
- Severity (Low / Medium / High)
- Likely cause

### ✔ Root Cause Analysis (RCA)
- Hypothesis describing how the incident likely occurred

### ✔ Evidence Checklist
- Logs, artifacts and data needed to confirm or disprove the hypothesis

### ✔ Triage Timeline
- **0–30 minutes** (containment & preservation)
- **1–4 hours** (scoping & investigation)
- **24–72 hours** (eradication, recovery, lessons learned)

### ✔ Governance & Compliance Mapping
- **MSB** (Swedish information security incident classification)
- **NIS2** relevance assessment
- **ISO/IEC 27001:2022** control references

---
---

## 🔒 Application Scope & Guarantees

This application is a **human-in-the-loop analyst support tool** for structured incident analysis in regulated environments.

It is designed to support **information security, risk, compliance, and governance functions** by improving clarity, consistency, and documentation quality during early incident handling and assessment.

### ✅ What the tool DOES

- Structures free-text incident descriptions into a **standardized, repeatable analysis format**
- Supports **initial triage and documentation** of security incidents
- Maps incidents to **recognized governance and security frameworks**, such as:
  - MSB incident classification
  - ISO/IEC 27001 (incident handling & logging)
  - NIS2 relevance assessment
- Produces **deterministic and explainable output** based solely on provided input
- Helps analysts distinguish between:
  - facts
  - assumptions
  - uncertainties
  - open questions
- Supports **human decision-making**, documentation, and audit readiness

### 🚫 What the tool DOES NOT

- Perform automated detection, monitoring, or alerting
- Replace human judgement or decision-making
- Take response, containment, or remediation actions
- Execute commands or interact with endpoints
- Access live systems, logs, networks, or external data sources
- Perform autonomous or self-initiated actions

### 🧭 Governance & Control Principles

- The tool is **advisory only**
- All outputs are intended to be **reviewed, validated, and approved by a human analyst**
- No decisions are made or enforced by the application itself
- The design supports **auditability, traceability, and controlled use**

This scope is intentional and ensures that the application can be safely evaluated and used in **regulated and compliance-driven organizations**.


---

## Operational Boundaries & Assumptions

This application is designed to operate under the following assumptions and constraints:

### Operational Assumptions
- Input is provided manually by a human analyst
- Incident descriptions may be incomplete, uncertain, or evolving
- The output represents a point-in-time analytical snapshot
- The assistant is used within an established incident management process
- Final decisions are always taken by authorized personnel

### Operational Boundaries
- No persistence of incident data beyond the execution context
- No learning, adaptation, or memory across executions
- No automated escalation, notification, or enforcement actions
- No integration with SIEM, EDR, SOAR, or ticketing systems
- No guarantee of completeness or correctness beyond provided input

### Intended Usage Context
- Early-phase incident triage
- Structured documentation support
- Governance, audit, and compliance-oriented analysis
- Analyst decision support in regulated environments

This tool is **not** intended for real-time detection, autonomous response,
or unsupervised operational use.

---

## 📂 Project Structure

```text
enterprise-ai-governance-assistant/
│
├── main.py                # Single entrypoint
├── src/
│   ├── __init__.py
│   ├── incident_analysis.py   # Core analysis & governance logic
│   └── runner.py              # CLI workflow & output formatting
│
└── README.md
