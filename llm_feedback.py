import requests
from utils import format_prompt

# API_KEY = "gsk_SKlVA8PNEJJtptaymq9pWGdyb3FYsMrvaPp7Oy0B2rU8ZcfD463"   # <-- replace again carefully
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def get_feedback(resume_text: str, job_role: str = "", job_desc: str = "") -> str:
    if job_role or job_desc:
        prompt = f"""
You are an expert ATS system. Compare the resume to the job role and description.

Job Role: {job_role}
Job Description: {job_desc}

Resume:
{resume_text}

Give:
1. Match percentage
2. Strengths
3. Missing keywords
4. Improvement tips
"""
    else:
        prompt = format_prompt(resume_text)

    try:
        response = requests.post(
            API_URL,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.1-8b-instant",
                "messages": [
                    {"role": "system", "content": "You are an expert ATS & career advisor."},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 700,
                "temperature": 0.7
            }
        )

        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text}"

        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"Error getting feedback: {str(e)}"
