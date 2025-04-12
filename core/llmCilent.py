import os
from openai import OpenAI
import logging

class OpenAIClient:
    def __init__(self, model="deepseek-chat"):
        self.client= OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),base_url=os.environ.get("OPENAI_API_BASE"))
        # self.client = OpenAI(api_key='sk-360efc7c486d4d34bd81f3d6e79d82c3', base_url='https://api.deepseek.com')
        self.model=model
        self.logger=logging.getLogger()

    def chat(self, messages):
        try:
            self.logger.info(f"Sending messages: {messages}")
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[OpenAI Error] {str(e)}"

