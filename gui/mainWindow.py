import tkinter as tk
from gui.stageOneChat import ChatStage
from gui.stageTwoFlow import FlowStage
from gui.stageThreeOutput import OutputStage
import logging

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

        self.chat_stage=False
        self.flow_stage=False
        self.output_stage=False
        self._create_buttons()
        self.logger=logging.getLogger(__name__)

        self.switch_stage("chat")  # 默认进入第一阶段

    def _create_buttons(self):
        tk.Button(self.sidebar, text="阶段一：意图对话", command=lambda: self.switch_stage("chat")).pack(pady=20)
        tk.Button(self.sidebar, text="阶段二：生成流程图", command=lambda: self.switch_stage("flow")).pack(pady=20)
        tk.Button(self.sidebar, text="阶段三：输出结果", command=lambda: self.switch_stage("output")).pack(pady=20)

    def switch_stage(self, stage_name):
        if self.chat_stage:
            last_reply=self.current_stage_frame.last_reply
        if self.current_stage_frame:
            self.current_stage_frame.destroy()

        if stage_name == "chat":
            self.logger.info("进入阶段一：意图对话")
            self.current_stage_frame = ChatStage(self.main_frame)
            self.chat_stage=True
            self.flow_stage=False
            self.output_stage=False
        elif stage_name == "flow":
            self.chat_stage=False
            self.flow_stage=True
            self.output_stage=False
            self.logger.debug("进入阶段二：生成流程图")
            self.current_stage_frame = FlowStage(self.main_frame,last_reply)
        elif stage_name == "output":
            self.chat_stage=False
            self.flow_stage=False
            self.output_stage=True
            self.current_stage_frame = OutputStage(self.main_frame)

        self.current_stage_frame.pack(expand=True, fill="both")

    def run(self):
        self.root.mainloop()
