import tkinter as tk
from tkinter import ttk, messagebox
import pyaudio
import numpy as np
import random
import time
import threading

# Mic setup
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

sentences = [
    "I solemnly swear that I am a human being.",
    "Beep boop, I am definitely not a robot.",
    "Banana phones unite under the jellyfish sun!",
    "My toaster has feelings, please believe me!",
    "LOUDER! Pretend you’re scaring away pigeons!",
]

class HumanVerifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔒 Human Verification")
        self.root.geometry("600x400")
        self.root.configure(bg="#222")

        self.label = tk.Label(root, text="Human Verification Required", font=("Arial", 18, "bold"), fg="white", bg="#222")
        self.label.pack(pady=20)

        self.sentence_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500, fg="lightgreen", bg="#222")
        self.sentence_label.pack(pady=20)

        self.timer_label = tk.Label(root, text="Time left: 15", font=("Arial", 12), fg="white", bg="#222")
        self.timer_label.pack(pady=10)

        # Progress bar for noise
        self.progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
        self.progress.pack(pady=20)

        # Buttons
        self.btn_frame = tk.Frame(root, bg="#222")
        self.btn_frame.pack(pady=20)

        self.try_again_btn = tk.Button(self.btn_frame, text="Try Again", command=self.start_verification, state="disabled")
        self.try_again_btn.grid(row=0, column=0, padx=10)

        self.different_btn = tk.Button(self.btn_frame, text="Different Method", command=self.different_method, state="disabled")
        self.different_btn.grid(row=0, column=1, padx=10)

        self.start_verification()

    def start_verification(self):
        self.sentence = random.choice(sentences)
        self.sentence_label.config(text=f"Please say loudly:\n“{self.sentence}”")
        self.time_left = 15
        self.update_timer()

        self.try_again_btn.config(state="disabled")
        self.different_btn.config(state="disabled")

        # Start listening thread
        threading.Thread(target=self.listen_microphone, daemon=True).start()

    def update_timer(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.fail_verification()

    def listen_microphone(self):
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        start_time = time.time()
        while time.time() - start_time < 15:
            data = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.int16)
            volume = np.linalg.norm(data) / 10000
            level = min(int(volume * 100), 100)

            # Fake flicker: mostly red, sometimes green
            if random.random() < 0.05:
                style = "green.Horizontal.TProgressbar"
            else:
                style = "red.Horizontal.TProgressbar"
            self.progress.config(value=level, style=style)

        stream.stop_stream()
        stream.close()
        p.terminate()

    def fail_verification(self):
        self.timer_label.config(text="❌ Verification failed. Not loud enough!")
        self.try_again_btn.config(state="normal")
        self.different_btn.config(state="normal")

    def different_method(self):
        messagebox.showinfo("Different Method", "🚪 Redirecting to alternative verification...\n\n(just kidding, there is no escape 😂)")
        self.root.destroy()


# Run app
if __name__ == "__main__":
    root = tk.Tk()

    # Style for progress bar
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("red.Horizontal.TProgressbar", troughcolor="#444", background="red")
    style.configure("green.Horizontal.TProgressbar", troughcolor="#444", background="lime")

    app = HumanVerifierApp(root)
    root.mainloop()
