import tkinter as tk
from gui.stageOneChat import ChatStage
from gui.stageTwoFlow import FlowStage
from gui.stageThreeOutput import OutputStage

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("对话生成流程图系统")
        self.root.geometry("1000x600")

        self.current_stage_frame = None

        self.sidebar = tk.Frame(self.root, width=150, bg="lightgray")
        self.sidebar.pack(side="left", fill="y")

        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(side="right", expand=True, fill="both")

        self._create_buttons()

        self.switch_stage("chat")  # 默认进入第一阶段

    def _create_buttons(self):
        tk.Button(self.sidebar, text="阶段一：意图对话", command=lambda: self.switch_stage("chat")).pack(pady=20)
        tk.Button(self.sidebar, text="阶段二：生成流程图", command=lambda: self.switch_stage("flow")).pack(pady=20)
        tk.Button(self.sidebar, text="阶段三：输出结果", command=lambda: self.switch_stage("output")).pack(pady=20)

    def switch_stage(self, stage_name):
        if self.current_stage_frame:
            self.current_stage_frame.destroy()

        if stage_name == "chat":
            self.current_stage_frame = ChatStage(self.main_frame)
        elif stage_name == "flow":
            self.current_stage_frame = FlowStage(self.main_frame)
        elif stage_name == "output":
            self.current_stage_frame = OutputStage(self.main_frame)

        self.current_stage_frame.pack(expand=True, fill="both")

    def run(self):
        self.root.mainloop()
