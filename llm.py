import os
import json
from dotenv import load_dotenv
from google import genai

# Load env
load_dotenv()

# Initialize client
client = genai.Client(api_key=os.getenv(""))


def clean_json(text):
    """Remove markdown wrappers like ```json ... ```"""
    text = text.strip()

    if text.startswith("```"):
        text = text.split("```")[1]  # remove first ```
        text = text.replace("json", "", 1).strip()

    return text


def generate_ddr(inspection_text, thermal_text):

    prompt = f"""
You are an expert building inspection analyst.

Generate a Detailed Diagnostic Report (DDR).

STRICT RULES:
- Do NOT invent information
- If missing → "Not Available"
- If conflict → explicitly mention
- Use simple client-friendly language

IMPORTANT:
Return ONLY valid JSON.
Do NOT wrap in markdown.
Do NOT add explanations.

INPUT:

Inspection Report:
{inspection_text}

Thermal Report:
{thermal_text}

OUTPUT FORMAT:

{{
  "Property Issue Summary": "",
  "Area-wise Observations": [
    {{
      "area": "",
      "observation": "",
      "issue": ""
    }}
  ],
  "Probable Root Cause": "",
  "Severity Assessment": "",
  "Recommended Actions": "",
  "Additional Notes": "",
  "Missing Information": ""
}}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    content = response.text

    # ✅ Clean markdown
    content = clean_json(content)

    try:
        return json.loads(content)
    except Exception as e:
        print("⚠️ JSON parsing failed")
        print("Error:", e)
        print("Cleaned Output:\n", content)
        return None