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

## 🧪 Demonstration & Use-cases (A9)

This section demonstrates how regulated organizations can use the assistant in real workflows.
The goal is not automation — it is **structured, auditable decision support**.

---

### 🧩 Use-case 1: SOC Analyst – Early Incident Triage (A9.1)

**Scenario**  
A SOC analyst receives an early alert or user report indicating suspicious behavior
(e.g. slow workstation, unknown processes, potential malware indicators).

**How the assistant is used**

1. The analyst runs the tool locally:
   ```bash
   python -m src

### 🔍 Use-case 1: SOC / Incident Response Team

#### Scenario
A SOC analyst receives an early incident report from a user or monitoring function, for example:

- “A workstation is behaving unusually slow”
- “Unknown background processes observed”
- “Possible malware or unauthorized activity suspected”

At this stage:
- information is incomplete
- impact is unclear
- no confirmed indicators exist yet

#### How the Assistant Is Used

1. The analyst runs the assistant locally:

   ```bash
   python -m src

  
### 🏛️ Use-case 3: Myndighet / offentlig sektor – styrning & tillsyn


**Scenario:**  
En kommun eller statlig myndighet mottar information om en misstänkt informationssäkerhetsincident.  
Informationen är fragmenterad och kommer från verksamheten, IT eller extern part.

Organisationen måste snabbt:
- skapa en korrekt nulägesbild
- avgöra allvarlighetsgrad
- avgöra om incidenten är rapporteringspliktig
- dokumentera beslutsunderlag för ledning och tillsyn

---

**Hur assistenten används:**

1. En informationssäkerhetssamordnare eller handläggare matar in tillgänglig incidentinformation.
2. Assistenten strukturerar informationen till:
   - incidentkategori
   - preliminär påverkan
   - sannolik orsak
   - identifierade osäkerheter
3. Assistenten pekar ut:
   - vilka uppgifter som saknas
   - vilken dokumentation som krävs
   - vilka roller som behöver involveras
4. Resultatet används som:
   - underlag för intern rapportering
   - beslutsstöd till ledning
   - spårbar dokumentation vid eventuell extern granskning

---

**Värde för organisationen:**

- Förbättrad kvalitet i tidig incidentbedömning
- Minskad risk för felaktig eller sen rapportering
- Tydligare ansvarsfördelning
- Stärkt spårbarhet och revisionsbarhet
- Enhetligt arbetssätt oavsett erfarenhetsnivå hos handläggare

---

**Relevanta regelverk & krav:**

- NIS2 (incidentbedömning och rapportering)
- ISO/IEC 27001 – A.16 (incidenthantering)
- Offentlighets- och arkivkrav
- MSB:s riktlinjer för informationssäkerhet

---

**Sammanfattning:**  
Assistenten fungerar som ett **strukturerande stöd** mellan verksamhet, IT, säkerhet och ledning.  
Den stärker beslutsfattande utan att ersätta mänskligt ansvar eller juridisk bedömning.

## Use-case 4: Public-sector / Regulated Organization (Governance & Audit Readiness)

### Scenario
A municipality/agency receives an incident report from a business unit:
> “A shared file server is behaving strangely. Some users report missing access and unusual activity. We are unsure if this is malware or a misconfiguration.”

The organization operates under:
- ISO/IEC 27001 requirements (structured incident handling)
- NIS2 expectations (risk-based management and reporting readiness)
- Public-sector governance expectations (traceability, documentation)

### How the Assistant Is Used
The analyst enters the free-text description into the tool.

The assistant produces a governance-aligned output that:
- Creates a **repeatable incident record** from uncertain input
- Separates **facts vs assumptions vs unknowns**
- Lists **evidence needed** to reduce uncertainty
- Defines **time-bound next steps** (triage timeline)
- Provides **framework mapping** to support compliance reporting

### Output Value (What Improves)
- **Higher documentation quality** early in the incident (before details are lost)
- **Clear decision-support snapshot** for managers and stakeholders
- **Audit-ready structure** (what was known, what was done, what remains)
- **Reduced ambiguity** in communication across IT, security, and business units
- **Faster alignment** on scope, severity, and escalation

### Governance Benefit
This use-case demonstrates governance-first value:
- Consistent structure across incidents (even when input is messy)
- Traceability for post-incident review and audits
- A safe, human-controlled way to introduce AI-style reasoning into regulated work

### Example “Stakeholder-ready Summary” (what the analyst can forward)
- **Current status:** Preliminary incident classification completed (pending evidence)
- **Impact:** Potential availability/integrity impact for shared resources
- **Next actions (0–30 min):** isolate affected scope, preserve logs, confirm user impact
- **Evidence needed:** authentication logs, file access logs, endpoint telemetry, change history
- **Compliance mapping:** ISO/IEC 27001 incident handling controls + NIS2 relevance check

> The assistant does not decide or act — it supports consistent, auditable human decision-making.


### 🏛 Use-case 4: Public Sector / Municipality Incident Assessment

**Context:**  
A municipality or public-sector organization experiences a potential information security incident involving citizen data, internal systems, or critical services.

**Typical challenges:**
- Fragmented or incomplete initial information
- High regulatory pressure (GDPR, NIS2, MSB)
- Need for clear documentation early in the process
- Limited technical security resources

**How the assistant is used:**
1. An analyst or information security coordinator inputs the initial incident description.
2. The assistant structures the information into:
   - Incident classification
   - Severity assessment
   - Root Cause Analysis hypothesis
   - Evidence checklist
   - Time-based triage actions
3. The output is mapped to:
   - MSB incident categories
   - NIS2 relevance
   - ISO/IEC 27001 incident handling controls

**Organizational value:**
- Improves consistency in how incidents are assessed across departments
- Reduces ambiguity in early incident documentation
- Supports non-technical staff with structured analytical reasoning
- Strengthens compliance, audit readiness, and reporting quality
- Enables faster escalation to management with a clear situation picture

**Why this matters:**  
Public-sector organizations often lack deep in-house security expertise.  
This assistant provides **structured, governance-aligned support** without introducing operational or compliance risk.


### 🧑‍💼 Use-case 5: CISO / Management Decision Support

**Context:**  
Senior management or a CISO needs a clear, reliable overview of an ongoing or suspected incident to decide on escalation, communication, and resource allocation.

**Typical challenges:**
- Technical reports are often inconsistent or overly detailed
- Management needs clarity, not raw logs
- Decisions must be defensible during audits or external review
- High risk of miscommunication during early incident stages

**How the assistant is used:**
1. Analysts run the assistant during early incident handling.
2. The structured output is shared with management, showing:
   - What is known
   - What is uncertain
   - What evidence is missing
   - What actions are recommended in defined time windows
3. Governance mappings provide immediate context for:
   - Regulatory impact
   - Compliance relevance
   - Reporting obligations

**Organizational value:**
- Translates technical uncertainty into management-friendly structure
- Supports defensible, traceable decision-making
- Improves communication between analysts and leadership
- Reduces risk of overreaction or delayed response
- Strengthens trust between security teams and executives

**Why this matters:**  
This positions the assistant as a **decision-support companion**, not a technical tool —  
exactly what leadership roles need in regulated environments.


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
