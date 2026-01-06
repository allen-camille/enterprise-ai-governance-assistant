\# Node Contracts – Prompt Flows v1.0

Enterprise AI Governance Assistant  

Status: Implementation-ready baseline  



📄 Node Contracts – Prompt Flows v1.0

Enterprise AI Governance Assistant

Scope: Incident Analysis \& Gap Analysis

Status: Baseline – implementation-ready

Version: 1.0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1\. Purpose of this document

This document defines the node-level contracts for the governance-first AI assistant.

It specifies:

•	flow structure

•	node responsibilities

•	required inputs and outputs

•	risk and flag semantics

•	governance enforcement rules

The purpose is to ensure that all implementations of these prompt flows are:

•	deterministic

•	auditable

•	governance-aligned

•	safe for regulated environments

This is a design and control artifact, not source code.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2\. Shared principles for all flows

All nodes and flows must adhere to:

•	Governance before functionality

•	AI as analytical support, never decision-maker

•	Mandatory human-in-the-loop

•	Deterministic and methodical behavior

•	Explicit uncertainty handling (“Oklart”)

•	Risk-based reasoning

•	Traceability and versioning

No node may override these principles.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3\. Shared technical baseline

All flows must implement:

3.1 Metadata injection

Every run must produce:

•	flow\_name

•	flow\_version

•	timestamp

•	analysis\_type

Future-ready fields (optional):

•	user\_role

•	tenant\_context

3.2 Governance layers

Every flow must contain:

1\.	Input node

2\.	Validation / sanitization node

3\.	LLM analysis node

4\.	Policy \& structure enforcement node

5\.	Output node

No direct “input → LLM → output” chains are allowed.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

🟥 4. Prompt Flow: Incident Analysis (incident\_analysis\_v1)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.1 Node A1 — incident\_input

Type: Input

Purpose: Controlled incident intake.

Inputs

•	incident\_description (string, required)

•	affected\_asset (string, required)

•	detected\_by (enum: user | soc | monitoring | other)

•	initial\_impact (enum: low | medium | high)

•	logs\_available (enum: yes | no | unknown)

•	personal\_data\_involved (enum: yes | no | unknown)

•	regulatory\_context (string, optional)

Output

•	incident\_input\_payload (object)

Governance rules

•	Mandatory fields enforced

•	No free-text conversation

•	All input treated as potentially sensitive

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.2 Node A2 — sanitize\_and\_validate\_input

Type: Tool / Python

Purpose: Sanitation, validation, metadata generation.

Outputs

•	clean\_incident\_description

•	clean\_affected\_asset

•	context\_summary

•	validation\_status (ok | warn)

•	flags (array)

•	run\_metadata (object)

Standard flags

•	possible\_pii

•	missing\_logs

•	low\_information

•	high\_initial\_impact

•	potential\_regulatory

Governance rules

•	No blocking in v1, only flagging

•	Metadata always generated

•	Missing or weak input must be visible downstream

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.3 Node A3 — incident\_analysis\_prompt

Type: LLM

Purpose: Deterministic incident analysis.

Mandatory output structure

1\.	Incident overview

2\.	Proposed classification (non-decision)

3\.	Impacted areas

4\.	Risk assessment

5\.	Possible response categories

6\.	Escalation indicators

7\.	Uncertainties and assumptions

8\.	Human review required

Locked analysis rules

•	No decisions

•	No imperatives

•	“Oklart” used when data is insufficient

•	Risk must include:

o	likelihood

o	impact

o	risk level

o	justification

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.4 Node A4 — enforce\_structure\_and\_policy

Type: Tool / Python

Purpose: Governance enforcement layer.

Outputs

•	incident\_analysis\_final

•	policy\_flags

•	quality\_checks

Mandatory checks

•	all\_sections\_present

•	risk\_block\_present

•	human\_review\_present

•	tone\_ok

Governance actions

•	Inject missing sections

•	Weaken overconfident language

•	Enforce responsibility statement

•	Flag structural repairs

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.5 Node A5 — incident\_output

Type: Output

Purpose: Controlled delivery.

Outputs

•	final\_report

•	policy\_flags

•	trace\_metadata

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5\. Incident flow – locked operational semantics

5.1 Risk model

Every analysis must include:

•	Likelihood: low | medium | high

•	Impact: low | medium | high

•	Risk level: low | medium | high

•	Justification

Risk level must follow a defined matrix logic.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5.2 Escalation logic (minimum)

escalation\_candidate must be set if any of the following are true:

•	risk level = high

•	possible\_pii = true

•	high\_initial\_impact = true

•	low\_information = true

Escalation indicates senior human review, not technical action.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5.3 “Oklart” handling

“Oklart” must always include:

•	what is missing

•	which role typically owns that information

Uncertainty is treated as a risk signal.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

🟦 6. Prompt Flow: Gap Analysis (gap\_analysis\_v1)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6.1 Node B1 — gap\_input

Type: Input

Purpose: Structured requirement and current-state intake.

Inputs

•	requirement\_text (required)

•	current\_state (required)

•	scope (required)

•	assessment\_context (enum)

•	regulatory\_reference (optional)

•	risk\_tolerance (optional)

•	documentation\_available (optional)

Output

•	gap\_input\_payload

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6.2 Node B2 — sanitize\_and\_validate\_gap\_input

Type: Tool / Python

Purpose: Normalization, evidence assessment, metadata.

Outputs

•	clean\_requirement\_text

•	clean\_current\_state

•	flags

•	run\_metadata

Standard flags

•	vague\_requirement

•	insufficient\_current\_state

•	evidence\_missing

•	governance\_gap

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6.3 Node B3 — gap\_analysis\_prompt

Type: LLM

Purpose: Methodical gap analysis.

Mandatory structure

1\.	Summary

2\.	Identified requirements and sub-requirements

3\.	Assessment per sub-requirement

4\.	Identified gaps

5\.	Risk assessment per gap

6\.	Prioritization overview

7\.	Uncertainties and assumptions

8\.	Human review required

Locked logic

•	All requirements decomposed

•	Only outcomes allowed:

o	fulfilled

o	partially fulfilled

o	not fulfilled

o	unclear

•	“Unclear” is risk-relevant

•	No compliance declarations

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6.4 Node B4 — enforce\_gap\_policy

Type: Tool / Python

Outputs

•	gap\_analysis\_final

•	policy\_flags

•	quality\_checks

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6.5 Node B5 — gap\_output

Type: Output

Outputs

•	final\_report

•	policy\_flags

•	trace\_metadata

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7\. Gap flow – locked operational semantics

7.1 Gap risk model

Each gap must include:

•	likelihood

•	impact

•	risk level

•	justification

Same matrix principle as incident flow.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7.2 Prioritization logic

Priorities must be expressed as:

•	Critical gaps

•	Significant gaps

•	Minor gaps

•	Observations

Driven by:

•	risk level

•	dependencies

•	uncertainty

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7.3 Escalation logic (gap)

Escalation candidate if:

•	any high-risk gap

•	multiple “unclear” outcomes

•	systemic governance weaknesses

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

8\. Human-in-the-loop enforcement

All flows must end with a mandatory block stating:

•	this is analytical support

•	not a compliance determination

•	not a decision system

•	requiring human assessment

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9\. Versioning and change control

This document defines Node Contracts v1.0.

•	Baselines must not be modified

•	Changes require:

o	new version

o	documented rationale

o	governance review

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

10\. Status

Node Contracts v1.0 – Implementation-ready

Supports Prompt Baseline v1.0.





