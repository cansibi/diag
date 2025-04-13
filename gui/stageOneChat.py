import tkinter as tk
import logging

from core.llmCilent import OpenAIClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class ChatStage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        api_key= os.getenv("OPENAI_API_KEY")
        tk.Label(self, text="👤 阶段一：用户与大模型对话", font=("Arial", 16)).pack(pady=10)

        self.chat_box = tk.Text(self, height=20)
        self.chat_box.pack(padx=20, pady=10, fill="both", expand=True)

        self.entry = tk.Entry(self)
        self.entry.pack(padx=20, pady=5, fill="x")

        tk.Button(self, text="发送", command=self.send_message).pack(pady=5)
        tk.Button(self, text="清空对话", command=self.clear_chat).pack(pady=5)
        self.api_client = OpenAIClient()  # 建议从环境变量读取
        self.messages = [
            {"role": "system", "content": "你是一个流程图助手，请根据用户意图生成流程描述。"}
        ]
        self.last_reply=''
        self.logger = logging.getLogger(__name__)

    def send_message(self):
        user_input = self.entry.get()
        if user_input.strip():
            # 显示用户输入
            self.chat_box.insert("end", f"你：{user_input}\n")
            self.entry.delete(0, "end")

            # 添加到消息历史
            self.messages.append({"role": "user", "content": user_input})

            # 调用 LLM API
            self.chat_box.insert("end", "🤖 正在生成回复，请稍等...\n")
            self.chat_box.update()

            reply = self.api_client.chat(self.messages)
            self.messages.append({"role": "assistant", "content": reply})
            self.last_reply=reply
            self.logger.info(f"大模型回复：{self.last_reply}")

            self.chat_box.insert("end", f"🤖 大模型：{reply}\n\n")
            self.chat_box.see("end")

    def clear_chat(self):
        self.chat_box.delete("1.0", "end")
        self.entry.delete(0, "end")
        self.messages = [
            {"role": "system", "content": "你是一个流程图助手，请根据用户意图生成流程描述。"}
        ]
        self.last_reply = ""