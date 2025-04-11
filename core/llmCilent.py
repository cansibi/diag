import os
from openai import OpenAI
import logging

class OpenAIClient:
    def __init__(self, model="deepseek-chat",instruction=None):
        self.client= OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),base_url=os.environ.get("OPENAI_API_BASE"))
        # self.client = OpenAI(api_key='sk-360efc7c486d4d34bd81f3d6e79d82c3', base_url='https://api.deepseek.com')
        self.model=model
        if instruction:
            self.instruction=instruction
        else:
            self.instruction="你是一个流程图助手，请根据用户意图生成流程描述。"
        self.logger=logging.getLogger()

    def chat(self, messages):
        """
        messages: List[dict], e.g.
        [{"role": "system", "content": "You are a helpful assistant."},
         {"role": "user", "content": "我想要一个审批流程"}]
        """
        try:
            # response = self.client.responses.create(
            #     model=self.model,
            #     instructions=self.instruction,
            #     input=messages
            # )
            # 输出日志 message是什么
            self.logger.info(f"Sending messages: {messages}")
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[OpenAI Error] {str(e)}"

if __name__ == "__main__":
    client = OpenAIClient()
    messages = [
        {"role": "system", "content": "你是一个流程图助手，请根据用户意图生成流程描述。"},
        {"role": "user", "content": "我想要一个审批流程"}
    ]
    response = client.chat(messages)
    print(response)
