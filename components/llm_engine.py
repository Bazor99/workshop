from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json
from config import OPENAI_MODEL, TEMPERATURE


def analyze_resume(context, cv_text, api_key):

    llm = ChatOpenAI(
        model=OPENAI_MODEL,
        temperature=TEMPERATURE,
        api_key=api_key,
        response_format={"type": "json_object"}
    )

    prompt = ChatPromptTemplate.from_template("""
You are an expert ATS resume analyst.

Context (Job Description):
{context}

CV:
{cv}

Return STRICT JSON with:
- match_score (0-100)
- strengths (list)
- missing_skills (list)
- rewritten_bullets_star (list)
- tailored_summary (string)
- interview_questions (list)
""")

    response = llm.invoke(
        prompt.format(context=context, cv=cv_text)
    )

    return json.loads(response.content)
