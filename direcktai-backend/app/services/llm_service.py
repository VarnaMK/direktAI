import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMService:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv(
                "OPENAI_API_KEY"
            )
        )        

    def invoke(
        self,
        prompt: str
    ):

        response = (
            self.client.chat.completions.create(
                model="gpt-5",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        return (
            response.choices[0]
            .message.content
        )