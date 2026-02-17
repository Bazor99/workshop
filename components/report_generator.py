def generate_markdown_report(analysis):

    match_score = analysis.get("match_score", 0)

    report = f"""
# Resume Analysis Report

## Match Score: {match_score}/100

## Tailored Summary
{analysis.get("tailored_summary", "")}

## Strengths
{chr(10).join(['- ' + s for s in analysis.get("strengths", [])])}

## Missing Skills
{chr(10).join(['- ' + m for m in analysis.get("missing_skills", [])])}

## Suggestions for improvement
{chr(10).join(['- ' + b for b in analysis.get("Suggestions for improvement", [])])}

## Interview Questions
{chr(10).join(['- ' + q for q in analysis.get("interview_questions", [])])}
"""
    return report
