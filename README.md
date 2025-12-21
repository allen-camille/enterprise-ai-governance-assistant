# Enterprise AI Incident & Governance Assistant

A Python-based incident analysis assistant designed to support **SOC analysts, security teams and governance functions** with structured incident triage, root cause analysis and regulatory mapping.

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

## 🏗 Project Structure

