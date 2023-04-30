import time
import tkinter as tk
from tkinter import ttk

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.sentence = "The quick brown fox jumps over the lazy dog"
        self.label = tk.Label(master, text="Type the following sentence:\n" + self.sentence)
        self.label.pack()
        self.entry = tk.Entry(master, width=70) # Set the width to 50 (450 pixels)
        self.entry.pack()
        self.button = tk.Button(master, text="Start", command=self.start_test)
        self.button.pack()
        self.accuracy_progress = ttk.Progressbar(master, orient='horizontal', length=200, mode='determinate')
        self.accuracy_progress.pack(pady=5)
        self.accuracy_label = tk.Label(master, text="Accuracy: 0%")
        self.accuracy_label.pack(pady=5)
        self.speed_label = tk.Label(master, text="Typing Speed: 0 wpm")
        self.speed_label.pack(pady=5)

    def start_test(self):
        self.start_time = time.time()
        self.entry.config(state="normal")
        self.button.config(state="disabled")
        self.entry.bind("<Return>", self.submit)

    def submit(self, event):
        self.end_time = time.time()
        time_taken = self.end_time - self.start_time
        typed_text = self.entry.get()
        errors = sum([1 for i, j in zip(self.sentence.split(), typed_text.split()) if i != j])
        accuracy = ((len(self.sentence.split()) - errors) / len(self.sentence.split())) * 100
        speed = (len(self.sentence.split()) - errors) / time_taken * 60
        result = f"Accuracy: {accuracy:.2f}%"
        self.accuracy_label.config(text=result)
        self.entry.config(state="disabled")
        self.button.config(state="normal")
        self.entry.unbind("<Return>")
        self.accuracy_progress["value"] = accuracy
        self.accuracy_progress.update()
        speed_result = f"Typing Speed: {speed:.2f} wpm"
        self.speed_label.config(text=speed_result)

root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("500x250")
typing_speed_test = TypingSpeedTest(root)
root.mainloop()
