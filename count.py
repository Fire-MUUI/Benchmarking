import tkinter as tk

class CounterWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("")  # 设置空标题

        # 设置窗口图标
        self.window.iconbitmap("count.ico")

        self.counter = 0  # 计数器初始值为0
        self.label = tk.Label(self.window, text=str(self.counter))
        self.label.pack(pady=20)

        self.update_counter()  # 启动定时器

        self.window.mainloop()  # 进入消息循环

    def update_counter(self):
        self.counter += 1
        self.label.configure(text=str(self.counter))  # 更新计数器的值
        self.window.after(1000, self.update_counter)  # 一秒后再次触发更新

CounterWindow()