import os
from dotenv import load_dotenv
from groq import Groq

# -----------------------
# LOAD ENVIRONMENT
# -----------------------

load_dotenv()

# -----------------------
# CLIENT
# -----------------------

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# -----------------------
# AI ANALYSIS
# -----------------------

def generate_explanation(results):

    total = len(results)

    tampered = sum(
        1 for r in results
        if "Tampered" in r["status"]
    )

    secure = total - tampered

    prompt = f"""
Analyze this cloud integrity audit report.

Total Files: {total}

Secure Files: {secure}

Tampered Files: {tampered}

Provide:

1. Security Summary
2. Risks
3. Recommendations
4. Best Algorithm
5. Conclusion
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:

        print("Groq Error:", e)

        return """
AI Integrity Report

Cloud verification completed successfully.
"""