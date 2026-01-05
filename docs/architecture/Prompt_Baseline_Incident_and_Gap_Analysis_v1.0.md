\# Prompt Baseline – Incident \& Gap Analysis

\*\*Governance-First AI-assistent\*\*  

\*\*Version:\*\* 1.0  

\*\*Status:\*\* Frozen baseline  



---



📄 Prompt Baseline – Incident \& Gap Analysis

Governance-First AI-assistent

Version 1.0 (fryst baseline)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1\. Syfte och användningsområde

Detta dokument beskriver den fastställda Prompt Baseline v1.0 för en governance-first AI-assistent avsedd för arbete inom:

•	informationssäkerhet

•	cybersäkerhet

•	GRC (Governance, Risk \& Compliance)

•	offentlig sektor och andra reglerade miljöer

Syftet är att visa hur AI kan användas som strukturerat analysstöd, utan att fatta beslut eller överta ansvar från människan.

Dokumentet utgör en design- och styrartefakt, inte teknisk kod.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2\. Grundläggande designprinciper

Samtliga prompt flows i denna baseline bygger på följande principer:

•	Governance före funktionalitet

•	AI som analysstöd – aldrig beslutsfattare

•	Human-in-the-loop som obligatoriskt krav

•	Deterministiskt och metodiskt beteende

•	Spårbarhet och revisionsbarhet

•	Riskbaserat arbetssätt

•	Tydlig ansvarsfördelning mellan verktyg och organisation

Dessa principer betraktas som icke-förhandlingsbara.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3\. Vad som menas med deterministiskt beteende

I detta sammanhang innebär deterministiskt beteende att:

•	AI-assistenten alltid följer samma analysmetod

•	Samma typer av input behandlas med samma struktur

•	Risk bedöms konsekvent (sannolikhet, konsekvens, risknivå)

•	Osäkerhet uttrycks tydligt genom “Oklart” när underlag saknas

Determinism syftar till förutsägbarhet och jämförbarhet, inte till perfekta eller identiska svar.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4\. Prompt Flow v1 – Incidentanalys

4.1 Syfte

Att ge strukturerat analysstöd vid incidenter genom att:

•	skapa en gemensam analysram

•	identifiera påverkan och risk

•	stödja eskalering och prioritering

Assistenten initierar inga åtgärder och fattar inga beslut.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.2 Input (styrd)

Obligatoriska fält

•	Incidentbeskrivning

•	Påverkad tillgång/system

•	Hur incidenten upptäcktes

•	Initial upplevd påverkan

Valfria fält

•	Tillgång till loggar

•	Personuppgifter involverade

•	Regulatorisk kontext (ex. GDPR, NIS2)

All input förutsätts vara sanerad från onödig personuppgiftsdata.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.3 Analyssteg (fast ordning)

1\.	Incidentöversikt

2\.	Föreslagen klassificering (ej beslut)

3\.	Påverkansområden (CIA + regelefterlevnad)

4\.	Riskbedömning

5\.	Möjliga åtgärdskategorier

6\.	Eskaleringsindikatorer

7\.	Osäkerheter och antaganden

8\.	Human review required

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.4 Output-krav

•	Samma struktur vid varje körning

•	Rekommendationer formuleras som “bör övervägas”

•	Risk anges som låg/medel/hög med motivering

•	“Oklart” används när information saknas

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5\. Prompt Flow v1 – Gap-analys (krav ↔ nuläge)

5.1 Syfte

Att stödja systematisk jämförelse mellan krav och nuläge för att:

•	identifiera faktiska gap

•	synliggöra risk

•	ge underlag för prioritering

Flödet är avsett för informationssäkerhet, revision och styrning.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5.2 Input (styrd)

Obligatoriska fält

•	Kravtext

•	Beskrivning av nuläge

•	Scope (system/process/organisation)

•	Bedömningskontext

Valfria fält

•	Regulatorisk referens

•	Riskaptit

•	Tillgänglig dokumentation

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5.3 Analyssteg (fast ordning)

1\.	Identifiering av delkrav

2\.	Bedömning per delkrav

o	uppfyllt

o	delvis uppfyllt

o	ej uppfyllt

o	oklart

3\.	Identifierade gap

4\.	Riskbedömning per gap

5\.	Prioriteringsöversikt

6\.	Osäkerheter och antaganden

7\.	Human review required

“Oklart” betraktas som ett riskrelevant utfall, inte som ett fel.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6\. Human-in-the-loop och ansvar

Alla analyser avslutas med följande ansvarstext:

Detta är ett analysstöd.

Bedömning, prioritering och beslut kräver mänsklig granskning.

Organisationen ansvarar alltid för hur resultatet används.

AI-assistenten kan inte godkänna efterlevnad eller initiera åtgärder.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7\. Spårbarhet och styrning (baseline)

För varje körning ska metadata kunna spåras, exempelvis:

•	vilket prompt flow och version som använts

•	tidsstämpel

•	användarroll (konceptuellt)

•	typ av analys

Inga råa personuppgifter eller fullständiga styrdokument lagras i loggar.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

8\. Samlad bedömning

Denna Prompt Baseline visar hur AI kan användas på ett:

•	kontrollerat

•	revisionsbart

•	riskmedvetet

•	ansvarssäkert

sätt i organisationer med höga krav på governance och regelefterlevnad.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9\. Status

Prompt Baseline v1.0 – fryst

Ändringar ska ske kontrollerat och versionssättas.





