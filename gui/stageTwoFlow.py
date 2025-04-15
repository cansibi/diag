import re
import tkinter as tk
from tkinter import scrolledtext
import logging
from PIL import Image, ImageTk
import tempfile
import os
from graphviz import Digraph
from core.llmCilent import OpenAIClient
class FlowStage(tk.Frame):
    def __init__(self, parent,last_reply=''):
        super().__init__(parent)
        tk.Label(self, text="📊 阶段二：代码图片生成", font=("Arial", 16)).pack(pady=10)
        self.last_reply=last_reply
        self.code_area = scrolledtext.ScrolledText(self, height=10)
        self.api_client = OpenAIClient()
        self.logger = logging.getLogger(__name__)
        self.generated_image_path=None
        # 如果有self.last_reply，输入到日志里
        self.logger.debug(f"用户意图：{self.last_reply}")
        self.temp_img_path = os.path.join(tempfile.gettempdir(), "graphviz_flow.png")
        self.generate_btn = tk.Button(self, text="✅ 生成流程图", command=self.generate_and_render)
        self.generate_btn.pack(pady=5)

        self.image_label = tk.Label(self)
        self.image_label.pack(pady=10)
        self.code_area.pack(padx=20, pady=10, fill="both", expand=True)

        if self.last_reply.strip():
            self.generate_mermaid(self.last_reply)

    def generate_mermaid(self, description):
        self.code_area.insert("end", "🤖 正在生成 mermaid 代码...\n")
        self.code_area.update()

        response = self.api_client.generate_flow_text(description)

        self.code_area.delete("1.0", "end")
        self.code_area.insert("end", response)

        self.render_graphviz(response)

    def generate_and_render(self):
        self.generate_mermaid(self.last_reply)
        text = self.code_area.get("1.0", "end").strip()
        self.render_graphviz(text)

    def render_graphviz(self, raw_text):
        nodes = {}
        edges = []
        mode = None
        for line in raw_text.splitlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("1. 节点定义：") or line.startswith('1.节点定义：'):
                mode = "nodes"
                continue
            elif line.startswith("2. 连接关系")or line.startswith('2.连接关系：'):
                mode = "edges"
                continue

            if mode == "nodes":
                match = re.match(r"(\w+):\s*(.+?),\s*(\w+)", line)
                if match:
                    node_id, label, ntype = match.groups()
                    nodes[node_id] = (label, ntype)
            elif mode == "edges":
                if "->" in line:
                    parts = line.split("->")
                    if len(parts) == 2:
                        edges.append((parts[0].strip(), parts[1].strip()))

        self.draw_graphviz(nodes, edges)

    def draw_graphviz(self, nodes, edges):
        dot = Digraph(format="png")
        dot.attr('node', fontname='Microsoft YaHei')
        dot.attr('edge', fontname='Microsoft YaHei')

        shape_map = {
            "start": "ellipse",
            "end": "ellipse",
            "process": "rectangle",
            "decision": "diamond",
            "input": "parallelogram",
            "output": "parallelogram",
            "connector": "circle"
        }

        for node_id, (label, ntype) in nodes.items():
            shape = shape_map.get(ntype.lower(), "rectangle")
            dot.node(node_id, label, shape=shape)

        for start, end in edges:
            dot.edge(start, end)

        output_path = os.path.splitext(self.temp_img_path)[0]
        dot.render(output_path, cleanup=True)
        self.generated_image_path=self.temp_img_path
        self.display_image()

    def display_image(self):
        try:
            image = Image.open(self.temp_img_path)
            image.thumbnail((900, 700))
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo
        except Exception as e:
            self.code_area.insert("end", f"\n[图片显示失败] {e}\n")
