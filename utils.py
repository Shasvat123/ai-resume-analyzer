def format_prompt(resume_text: str) -> str:
    return f"""
You are an AI career coach. Analyze the following resume and provide:
1. Strengths
2. Weaknesses
3. Suggestions for improvement
4. How well it fits common job roles

Resume:
{resume_text}
"""
