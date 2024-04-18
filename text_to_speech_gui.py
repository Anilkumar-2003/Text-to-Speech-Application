import tkinter as tk
from tkinter import ttk, filedialog
import pyttsx3
import tempfile
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define global variables
audio_file_path = None

def convert_text_to_speech():
    global audio_file_path

    # Get text from the text entry
    text = text_entry.get("1.0", "end-1c")

    # Configure engine properties
    selected_voice = voice_var.get()
    rate = rate_scale.get()
    pitch = pitch_scale.get()
    volume = volume_scale.get()

    engine.setProperty('voice', selected_voice)
    engine.setProperty('rate', rate)
    engine.setProperty('pitch', pitch)
    engine.setProperty('volume', volume)

    # Save speech as audio file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        audio_file_path = temp_file.name
        engine.save_to_file(text, audio_file_path)
        engine.runAndWait()

def play():
    if audio_file_path:
        engine.stop()
        engine.say(text_entry.get("1.0", "end-1c"))
        engine.runAndWait()

def pause():
    engine.stop()

def stop():
    engine.stop()

def replay():
    if audio_file_path:
        engine.stop()
        engine.say(text_entry.get("1.0", "end-1c"))
        engine.runAndWait()

def save_audio():
    if audio_file_path:
        destination = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav"), ("MP3 files", "*.mp3")])
        if destination:
            format = os.path.splitext(destination)[1][1:]  # Extract file extension without the dot
            engine.save_to_file(text_entry.get("1.0", "end-1c"), destination)
            engine.runAndWait()

# Create main application window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Create text entry widget
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

# Create frame for options
options_frame = ttk.Frame(root)
options_frame.pack()

# Voice selection
voice_var = tk.StringVar()
voice_label = ttk.Label(options_frame, text="Select Voice:")
voice_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
voice_dropdown = ttk.Combobox(options_frame, textvariable=voice_var)
voice_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Speech rate adjustment
rate_label = ttk.Label(options_frame, text="Speech Rate:")
rate_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
rate_scale = ttk.Scale(options_frame, from_=50, to=200, length=200, orient="horizontal")
rate_scale.grid(row=1, column=1, padx=5, pady=5)
rate_scale.set(100)

# Pitch adjustment
pitch_label = ttk.Label(options_frame, text="Pitch:")
pitch_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
pitch_scale = ttk.Scale(options_frame, from_=0.5, to=2.0, length=200, orient="horizontal")
pitch_scale.grid(row=2, column=1, padx=5, pady=5)
pitch_scale.set(1.0)

# Volume adjustment
volume_label = ttk.Label(options_frame, text="Volume:")
volume_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
volume_scale = ttk.Scale(options_frame, from_=0.0, to=1.0, length=200, orient="horizontal")
volume_scale.grid(row=3, column=1, padx=5, pady=5)
volume_scale.set(1.0)

# Create buttons for playback controls
play_button = ttk.Button(root, text="Play", command=play)
play_button.pack(side=tk.LEFT, padx=5)
pause_button = ttk.Button(root, text="Pause", command=pause)
pause_button.pack(side=tk.LEFT, padx=5)
stop_button = ttk.Button(root, text="Stop", command=stop)
stop_button.pack(side=tk.LEFT, padx=5)
replay_button = ttk.Button(root, text="Replay", command=replay)
replay_button.pack(side=tk.LEFT, padx=5)

# Create button to convert text to speech and save audio
convert_button = ttk.Button(root, text="Convert to Speech", command=convert_text_to_speech)
convert_button.pack(pady=10)

# Create button to save speech as audio file
save_button = ttk.Button(root, text="Save Audio", command=save_audio)
save_button.pack(pady=10)

root.mainloop()
