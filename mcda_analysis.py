"""
ATD Logistics Tool Evaluation Engine
Business Analysis Tool using Multi-Criteria Decision Analysis (MCDA)
Author: Breck Onwona Agyekum
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Business Criteria Weights (from stakeholder requirements)
# Derived from meetings with Susan Namulindwa and Victoria Schorr
CRITERIA_WEIGHTS = {
    'ease_of_use': 0.20,           # Susan's priority: Non-technical staff
    'integration_readiness': 0.20, # Victoria's priority: System compatibility
    'cost_efficiency': 0.15,       # Budget constraint for SMEs
    'scalability': 0.15,           # Future growth capability
    'paperwork_automation': 0.15,  # Customs automation requirement
    'real_time_visibility': 0.15   # Tracking requirement
}

def calculate_weighted_score(tool_scores):
    """
    Calculate business fit score using Weighted Sum Model
    Args: tool_scores (dict) - raw scores 1-5 for each criterion
    Returns: float - weighted composite score (1-5 scale)
    """
    total_score = 0
    for criterion, weight in CRITERIA_WEIGHTS.items():
        if criterion in tool_scores:
            total_score += tool_scores[criterion] * weight
    return round(total_score, 2)

def evaluate_tools(dataframe):
    """
    Rank all tools by business fit
    Args: dataframe with columns matching CRITERIA_WEIGHTS keys
    Returns: DataFrame with 'business_score' and 'rank' columns added
    """
    df = dataframe.copy()
    
    # Calculate weighted score for each tool
    df['business_score'] = df.apply(
        lambda row: calculate_weighted_score(row.to_dict()), 
        axis=1
    )
    
    # Rank tools (1 = best)
    df['rank'] = df['business_score'].rank(ascending=False, method='dense').astype(int)
    
    return df.sort_values('rank')

def generate_executive_chart(df, top_n=10):
    """
    Create bar chart for stakeholder presentations
    """
    top_tools = df.head(top_n).sort_values('business_score')
    
    plt.figure(figsize=(12, 6))
    chart = sns.barplot(
        data=top_tools,
        x='business_score',
        y='tool_name',
        palette='viridis'
    )
    
    plt.title('AI Logistics Solutions: Business Fit Ranking\n(ATD Canada-Africa Trade Corridor)', 
              fontsize=14, pad=20)
    plt.xlabel('Weighted Business Fit Score (1-5)', fontsize=12)
    plt.ylabel('Vendor Solution', fontsize=12)
    
    # Add score labels on bars
    for i, v in enumerate(top_tools['business_score']):
        chart.text(v + 0.05, i, str(v), color='black', va='center')
    
    plt.tight_layout()
    plt.savefig('evaluation_results.png', dpi=300, bbox_inches='tight')
    print("Chart saved as 'evaluation_results.png'")

# Example usage with sample data structure
if __name__ == "__main__":
    print("ATD Business Analysis Engine Loaded")
    print(f"Evaluation Criteria: {list(CRITERIA_WEIGHTS.keys())}")
    print("Ready to evaluate logistics tools...")
