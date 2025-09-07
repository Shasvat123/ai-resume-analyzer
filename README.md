📄 AI Resume Analyzer

AI Resume Analyzer is a Streamlit web app that analyzes your resume, provides AI-powered feedback, gives interactive coaching, and suggests ways to improve your resume based on a specific job role or description. Users can also store their resumes and feedback securely in a local database.

Features

Resume Extraction

Upload your resume as a PDF.

Extracts text using resume_parser.

AI Feedback

Uses a Large Language Model (LLM) to analyze your resume.

Compares resume content with the job role and job description (optional) to provide:

Match percentage

Strengths

Missing keywords

Improvement tips

Interactive Coaching

Highlights missing keywords in the resume.

Suggests how to rewrite bullet points in context.

Gamified ATS score progression shows how adding improvements boosts your resume score.

Career Roadmap Suggestions

Suggests courses, certifications, or projects to close skill gaps.

Example: “Since NLP is missing, consider the Coursera NLP specialization.”

Database Storage

Stores uploaded resumes, AI feedback, and job roles in an SQLite database.

Allows reviewing previously analyzed resumes.

Frontend

Built with Streamlit.

Simple, interactive UI with expanders, text areas, and progress bars.

Setup Instructions
1. Clone the Repository
git clone https://github.com/Shasvat123/ai-resume-analyzer.git
cd ai-resume-analyzer

2. Create & Activate Virtual Environment
python -m venv venv
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# macOS / Linux
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure API Key

Open llm_feedback.py.

Find the line with the API key:

API_KEY = "# YOUR_API_KEY_HERE"


Remove the # and replace it with your API key.

Important: Do NOT push your API key to GitHub; use .env or local environment variables for security.

import os
API_KEY = os.getenv("OPENAI_API_KEY")  # Recommended approach

5. Run the App
streamlit run app.py


Open in browser: http://localhost:8501

Project Structure
ai-resume-analyzer/
│
├── app.py              # Main Streamlit app
├── llm_feedback.py     # Module to get AI feedback from LLM
├── resume_parser.py    # Parses PDF resumes
├── db.py               # Handles SQLite database operations
├── utils.py            # Utility functions like prompt formatting
├── resumes.db          # SQLite database (created automatically)
├── requirements.txt    # List of Python dependencies
└── README.md           # Project documentation

Workflow Diagram
+-----------------+
| Upload Resume   | --> PDF uploaded via Streamlit
+-----------------+
          |
          v
+-----------------+
| Extract Text    | --> resume_parser extracts text from PDF
+-----------------+
          |
          v
+-----------------+
| AI Feedback     | --> get_feedback compares resume with job role/desc
| & Suggestions   | --> Provides strengths, missing keywords, tips
+-----------------+
          |
          v
+-----------------+
| Interactive     | --> Shows coaching tips, ATS score, roadmap
| Coaching        |
+-----------------+
          |
          v
+-----------------+
| Store in DB     | --> Saves resume, feedback, job role
+-----------------+
          |
          v
+-----------------+
| View History    | --> User can see previous analyses
+-----------------+
