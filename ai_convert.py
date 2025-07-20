import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def convert_yaml_with_gpt(gitlab_yaml: str) -> str:
    prompt = f"""
You are a DevOps expert. Convert the following GitLab CI/CD YAML into an equivalent GitHub Actions workflow YAML.
Preserve all job logic, scripts, environment variables, and job names.

GitLab YAML:

GitHub Actions YAML:
"""
    
    chat_response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # ✅ Use this model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=1000
    )

    return chat_response.choices[0].message.content.strip()
