# ai-logistics-tool-selection-mcda
Business analysis case study: data-driven AI logistics tool selection for Canada–Africa trade. Used stakeholder requirements, MCDA scoring, and Python to rank 65 tools for SME cross-border logistics.
# Business Analysis: AI Logistics Tool Selection
**Client:** Africa Trade Desk (ATD) | **Timeline:** 13 Weeks | **Methodology:** PRISMA-ScR + MCDA

## The Business Problem
ATD facilitates trade between Canadian wholesalers and African suppliers but lacked the internal capability to evaluate AI logistics tools. They faced:
- Decision paralysis with 65+ vendor options
- No framework to assess suitability for small teams (1-5 users)
- Risk of costly technology misalignment in low-infrastructure African markets

## My Role as Business Analyst

### Phase 1: Stakeholder Engagement & Requirements
**Meetings conducted:**
- **Susan Namulindwa** (Trade Enablement Lead): Defined "AI-First" mandate, small-team constraint
- **Victoria Schorr** (Operations): Identified customs automation as priority pain point

**Techniques used:**
- PCC Framework (Population-Concept-Context) to define scope boundaries
- Root cause analysis revealing knowledge gaps as primary bottleneck

**Requirements captured:**
| ID | Requirement | Priority | Stakeholder Source |
|---|---|---|---|
| R1 | Customs automation (reduce 3-5 day delays) | Must Have | Victoria Schorr |
| R2 | Small team usability (1-5 non-technical users) | Must Have | Susan Namulindwa |
| R3 | Mobile-first design for African field operations | Should Have | Victoria Schorr |
| R4 | Cost transparency for SME budgets | Must Have | Susan Namulindwa |

### Phase 2: Solution Assessment (MCDA Analysis)
Built a Python-based decision engine to objectively score 65 tools against weighted business criteria:

**Evaluation Criteria:**
- Ease of Use (20%) - *Adoption risk mitigation*
- Integration Readiness (20%) - *Technical debt prevention*
- Cost Efficiency (15%) - *Budget alignment*
- Scalability (15%) - *Future-proofing*
- Paperwork Automation (15%) - *Process efficiency*
- Real-Time Visibility (15%) - *Operational control*

**Top 3 Recommendations:**
1. **KlearNow.AI** (4.7/5) - Customs automation & compliance
2. **Flexport** (4.7/5) - End-to-end visibility & integration
3. **TradeSun** (4.3/5) - Document processing & risk detection

### Phase 3: Implementation Roadmap
Delivered 3-phase AI-First adoption strategy:
1. **Foundation:** Workflow redesign and tool selection
2. **Activation:** Pilot with one supplier cluster
3. **Integration:** SOP documentation and governance

## Business Impact
- **90% time reduction:** Vendor evaluation from 40 hours → 4 hours
- **Risk mitigation:** Data-driven selection prevents costly misalignment
- **Reusable asset:** Framework applicable to future technology decisions

## Technical Implementation
- **Language:** Python (Pandas, Matplotlib, Seaborn)
- **Method:** Multi-Criteria Decision Analysis (Weighted Sum Model)
- **Data:** PRISMA-ScR compliant review of 27 sources (2023-2025)

## Repository Contents
- `mcda_analysis.py` - Python evaluation engine
- `stakeholder_meetings.md` - Elicitation notes from Susan & Victoria
- `requirements.txt` - Python dependencies
- `assets/` - Project presentation and full report
