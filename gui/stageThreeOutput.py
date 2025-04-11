import tkinter as tk

class OutputStage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="📦 阶段三：输出最终结果", font=("Arial", 16)).pack(pady=10)

        tk.Button(self, text="导出为 PNG").pack(pady=10)
        tk.Button(self, text="导出为 Markdown").pack(pady=10)
        tk.Button(self, text="保存 JSON").pack(pady=10)
