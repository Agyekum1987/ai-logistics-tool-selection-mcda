# ai-logistics-tool-selection-mcda

## Executive Summary
Business analysis and data analysis case study focused on AI logistics tool selection for Canada–Africa trade. Built a decision-support model by cleaning a 65-tool dataset and applying MCDA (Weighted Sum Model) to score and rank tools across six criteria. Deliverables include a ranked table, per-criterion score breakdown, and visuals (Top-10 ranking + heatmap).
Client: Africa Trade Desk (ATD) | Timeline: 13 weeks | Methods: PRISMA-ScR + MCDA | Tools: Python (pandas, matplotlib), ChatGPT, Perplexity, Kimi AI, Microsoft Excel

## Data Analysis & Python Implementation
### Data pipeline (what I did)
- Built a structured dataset of 65 AI logistics tools and standardized fields for reliable comparison (tool name, category, evidence links, and scoring inputs).
- Cleaned and normalized the dataset in Python (pandas): removed duplicates, fixed inconsistent labels, and handled missing values so scoring was consistent across tools.
- Engineered scoring features by mapping tool capabilities and evidence into 1–5 scores across six criteria:
  Ease of Use, Cost Efficiency, Integration Readiness, Scalability, Paperwork & Reports Automation, Real-Time Visibility.

### Scoring + ranking model (how the analysis works)
  - Implemented an MCDA Weighted Sum Model:
  - normalized scores where needed,
  - applied criterion weights,
  - calculated total scores,
  - generated a full ranking and Top-10 shortlist.
  - Produced decision-ready outputs:
  - ranked results table (overall + per-criterion breakdown),
  - Top-10 comparison heatmap for quick pattern spotting,
  - visuals to support the final recommendations.

## The Business Problem
ATD supports Canada–Africa trade but lacked a repeatable way to evaluate AI logistics tools:
- Too many options (65+ tools) with inconsistent information
- No structured scoring method to match tool capabilities to needs
- High risk of selecting tools that don’t fit small teams or trade corridor constraints

## My Role as Business Analyst

### Phase 1: Stakeholder Engagement & Requirements
Stakeholder interviews with ATD trade enablement and operations leads to confirm priorities and constraints.
- **Susan Namulindwa** (Trade Enablement Lead): Defined "AI-First" mandate, small-team constraint
- **Victoria Schorr** (Operations): Identified customs automation as priority pain point

Techniques used:
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
## MCDA Scoring Model
Tools were scored (1–5) and ranked using an MCDA Weighted Sum Model across six weighted criteria:
- Ease of Use (20%)
- Integration Readiness (20%)
- Cost Efficiency (15%)
- Scalability (15%)
- Paperwork & Reports Automation (15%)
- Real-Time Visibility (15%)

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
- Automated scoring and ranking across 65 tools to reduce manual comparison effort
- Reduced decision friction by converting tool selection into a transparent scoring model.
- Produced a reusable evaluation matrix and visuals (rankings + heatmaps) to support repeatable tool selection.

## Technical Implementation
- **Language:** Python (Pandas, Matplotlib, Seaborn)
- **Method:** Multi-Criteria Decision Analysis (Weighted Sum Model)
- **Data:** PRISMA-ScR compliant review of 27 sources (2023-2025)

## Repository Contents
- `mcda_analysis.py` - Python evaluation engine
- `stakeholder_meetings.md` - Elicitation notes from Susan & Victoria
- `requirements.txt` - Python dependencies
- `assets/` - Project presentation and full report
