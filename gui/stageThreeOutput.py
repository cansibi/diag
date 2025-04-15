import os
import tkinter as tk
from tkinter import filedialog

class OutputStage(tk.Frame):
    def __init__(self, parent, image_path=""):
        super().__init__(parent)
        self.image_path = image_path
        tk.Label(self, text="📦 阶段三：输出最终结果", font=("Arial", 16)).pack(pady=10)
        tk.Button(self, text="导出为 PNG", command=self.save_as_png).pack(pady=10)


    def save_as_png(self):
        if not self.image_path or not os.path.exists(self.image_path):
            tk.messagebox.showerror("错误", "未找到可导出的图像")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")])
        if file_path:
            try:
                with open(self.image_path, 'rb') as fsrc:
                    with open(file_path, 'wb') as fdst:
                        fdst.write(fsrc.read())
                tk.messagebox.showinfo("成功", f"已保存到: {file_path}")
            except Exception as e:
                tk.messagebox.showerror("保存失败", str(e))
