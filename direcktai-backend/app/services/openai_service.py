import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class OpenAIService:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )

    def generate_steps(
        self,
        requirement: str
    ):

        prompt = f"""
You are a senior QA automation architect.

Convert the requirement into a test title and test steps.

Return ONLY valid JSON.

Format:

{{
    "title": "",
    "steps": []
}}

Requirement:

{requirement}
"""

        response = self.client.chat.completions.create(
            model="gpt-5",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = (
            response.choices[0]
            .message
            .content
        )

        return json.loads(
            content
        )