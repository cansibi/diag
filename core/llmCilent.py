import os
from openai import OpenAI
from dotenv import load_dotenv
import sys
import logging

# ✅ 正确加载 .env

class OpenAIClient:
    def __init__(self, model="deepseek-chat"):
        load_dotenv(dotenv_path=self.resource_path(".env"))
        logging.debug("🔑 OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
        print("🔑 OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
        self.client= OpenAI(api_key=os.getenv("OPENAI_API_KEY"),base_url=os.getenv("OPENAI_API_BASE"))
        # self.client = OpenAI(api_key='sk-360efc7c486d4d34bd81f3d6e79d82c3', base_url='https://api.deepseek.com')
        self.model=model

    def resource_path(self,relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def chat(self, messages):
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[OpenAI Error] {str(e)}"

    def generate_flow_text(self, description):
        prompt= f"""
你是一个流程图生成器，请根据下面的业务描述，生成一个流程图的结构,输出中不要含有类似###的无意义符号，输出格式为两个部分：

1.节点定义：每行格式为 节点ID: 名称, 类型（start/process/decision/input/output/connector/end）

2.连接关系：每行格式为 起始ID -> 目标ID。

描述：
{description}
"""
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[OpenAI Error] {str(e)}"
