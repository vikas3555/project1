import tkinter as tk
class Stopwatch:
    def _init_(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.running = False
        self.time = 0  

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 40))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def update(self):
        if self.running:
            self.time += 1
            self.label.config(text=self.time_format(self.time))
            self.root.after(1000, self.update)

    def time_format(self, seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

    def start(self):
        if not self.running:
            self.running = True
            self.update()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.time = 0
        self.label.config(text="00:00:00")

root = tk.Tk()
app = Stopwatch(root)
root.mainloop()