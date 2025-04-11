import tkinter as tk

class FlowStage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="📊 阶段二：生成流程图和代码", font=("Arial", 16)).pack(pady=10)

        self.code_area = tk.Text(self, height=10)
        self.code_area.pack(padx=20, pady=10, fill="both", expand=True)

        tk.Label(self, text="👉 预览图将在这里展示（后续可接入 Graphviz）").pack(pady=5)
