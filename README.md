# Enterprise AI Incident & Governance Assistant

A Python-based incident analysis assistant designed to support **SOC analysts, security teams, and governance functions** with structured incident triage, root cause analysis, and regulatory mapping.

The project simulates **AI-assisted analytical reasoning** using deterministic, explainable logic and is intentionally designed to be **safely extendable with LLMs** (e.g. Azure OpenAI) in later phases.

This repository demonstrates how AI can be introduced responsibly into **regulated and compliance-driven environments**.

---

## 🎯 Purpose

The purpose of this application is to transform **unstructured incident descriptions** into a **clear, repeatable, and governance-aligned analysis** that supports:

- Early-phase incident triage  
- Consistent documentation  
- Risk and impact assessment  
- Compliance and audit readiness  
- Human decision-making in complex environments  

The assistant mirrors real-world workflows used in:

- SOC operations  
- Incident response teams  
- Information security governance  
- Public-sector and regulated organizations  

---

## 🧠 What the Assistant Does

Given a free-text incident description, the assistant produces a **structured analytical output** consisting of:

### ✔ Incident Classification
- Incident category (e.g. Malware infection, Performance degradation)
- Severity assessment (Low / Medium / High)
- Initial impact considerations

### ✔ Root Cause Analysis (RCA)
- A reasoned hypothesis describing how the incident likely occurred
- Explicit distinction between:
  - known facts
  - assumptions
  - uncertainties

### ✔ Evidence & Data Checklist
- Logs, artifacts, and technical evidence required to:
  - validate hypotheses
  - reduce uncertainty
  - support forensic or follow-up investigation

### ✔ Time-Based Triage Actions
- **0–30 minutes**: containment, preservation, immediate safeguards
- **1–4 hours**: scoping, investigation, coordination
- **24–72 hours**: eradication, recovery, lessons learned

### ✔ Governance & Compliance Mapping
- **MSB** (Swedish information security incident classification)
- **NIS2** relevance assessment
- **ISO/IEC 27001:2022** control references (incident handling, logging, governance)

---

## 🔒 Application Scope & Guarantees

This application is a **human-in-the-loop analyst support tool**.

It is intentionally designed to **assist**, not automate, security decision-making in regulated environments.

### ✅ What the Tool DOES

- Structures free-text incident descriptions into a **standardized, repeatable format**
- Supports **initial triage, analysis, and documentation**
- Aligns incident analysis with recognized **governance and security frameworks**
- Produces **deterministic, explainable output**
- Improves clarity, consistency, and auditability
- Helps analysts reason about:
  - impact
  - uncertainty
  - evidence gaps
  - next investigative steps

### 🚫 What the Tool DOES NOT

- Perform automated detection or monitoring
- Replace human judgement or accountability
- Take containment, remediation, or response actions
- Interact with live systems, networks, or logs
- Execute commands or access external data sources
- Learn, adapt, or retain memory across executions
- Operate autonomously or initiate actions

---

## 🧭 Governance & Control Principles

The design explicitly follows governance-first principles:

- The tool is **advisory only**
- All outputs must be **reviewed and validated by a human analyst**
- No decisions are enforced by the application
- No actions are taken without human approval
- The system supports:
  - traceability
  - explainability
  - controlled usage
  - audit readiness

This makes the application suitable for **evaluation, demonstration, and controlled use** in organizations with high regulatory demands.

---

## ⚙ Operational Boundaries & Assumptions

### Operational Assumptions
- Input is provided manually by a human analyst
- Incident descriptions may be incomplete or evolving
- Output represents a **point-in-time analytical snapshot**
- The assistant is used within an established incident management process
- Final decisions are always taken by authorized personnel

### Operational Boundaries
- No persistence of incident data beyond execution
- No integration with SIEM, EDR, SOAR, or ticketing systems
- No automated escalation or notification
- No real-time or continuous monitoring
- No guarantee of correctness beyond provided input

### Intended Usage Context
- Early-phase incident triage
- Structured documentation support
- Governance, risk, and compliance analysis
- Analyst decision support in regulated environments

---

## 🏢 Organizational Value

This application provides **tangible value** to organizations by:

- Improving consistency in early incident handling
- Reducing ambiguity in incident documentation
- Supporting both junior and senior analysts with structured reasoning
- Enhancing audit readiness and compliance documentation
- Acting as a **decision-support companion**, not a decision-maker
- Providing a **safe foundation for future AI-assisted security tooling**

It is especially relevant for organizations operating under:

- **ISO/IEC 27001**
- **NIS2**
- Public-sector governance requirements
- Critical infrastructure or other regulated industries

---

## 🧱 Architectural Philosophy

The project is intentionally built using:

- **Deterministic logic** instead of black-box AI
- Clear separation of concerns (analysis, formatting, orchestration)
- Explicit governance boundaries
- Safe defaults suitable for regulated organizations

This approach demonstrates how AI-assisted tools can be introduced
**incrementally, transparently, and responsibly**.

---

## 📂 Project Structure

```text
enterprise-ai-governance-assistant/
│
├── main.py                     # Single entrypoint
├── src/
│   ├── __init__.py
│   ├── incident_analysis.py    # Core analysis & governance logic
│   ├── output_formatter.py     # Centralized output formatting
│   └── runner.py               # CLI workflow orchestration
│
├── .env.example                # Environment variable template
├── .gitignore
└── README.md
