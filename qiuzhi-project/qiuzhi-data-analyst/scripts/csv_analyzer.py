#!/usr/bin/env python3
"""
CSV Analyzer for Qiuzhi Data Analyst Skill
"""

import pandas as pd
import sys
import os
from typing import Dict, Any

def analyze_csv(file_path: str) -> Dict[str, Any]:
    """
    Analyze a CSV file and return insights
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Basic information
        info = {
            "shape": df.shape,
            "columns": df.columns.tolist(),
            "dtypes": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "numerical_summary": df.describe().to_dict() if not df.empty else {},
            "head": df.head().to_dict() if not df.empty else {}
        }
        
        return info
    except Exception as e:
        return {"error": str(e)}

def generate_summary_report(file_path: str) -> str:
    """
    Generate a human-readable summary of the CSV analysis
    """
    analysis = analyze_csv(file_path)
    
    if "error" in analysis:
        return f"Error analyzing file: {analysis['error']}"
    
    report = f"# CSV Analysis Report\n\n"
    report += f"## File: {os.path.basename(file_path)}\n\n"
    report += f"- **Rows**: {analysis['shape'][0]}\n"
    report += f"- **Columns**: {analysis['shape'][1]}\n\n"
    
    report += "## Columns:\n"
    for col in analysis['columns']:
        report += f"- {col}\n"
    report += "\n"
    
    if analysis['missing_values']:
        report += "## Missing Values:\n"
        for col, count in analysis['missing_values'].items():
            if count > 0:
                report += f"- {col}: {count}\n"
        report += "\n"
    
    if analysis['numerical_summary']:
        report += "## Numerical Summary:\n"
        for stat, values in analysis['numerical_summary'].items():
            report += f"- {stat}: {dict(list(values.items())[:5])}\n"  # Limit output
    
    return report

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python csv_analyzer.py <path_to_csv_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist")
        sys.exit(1)
    
    report = generate_summary_report(file_path)
    print(report)
    
    # Save report to a file
    output_path = file_path.replace('.csv', '_analysis_report.md')
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"\nAnalysis report saved to: {output_path}")