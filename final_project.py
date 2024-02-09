# create a notepad that can save anything you with timer

import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time

def update_timer():
    current_time = time.time() - start_time_var.get()
    timer_var.set(f"Elapsed Time: {int(current_time // 60):02d}:{int(current_time % 60):02d}")
    notepad.after(1000, update_timer)

def save_to_file():
    content = text_entry.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Save Successful", f"Content saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save content: {str(e)}")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
                text_entry.delete("1.0", tk.END)
                text_entry.insert(tk.END, content)
            messagebox.showinfo("File Opened", f"Opened {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {str(e)}")

def update_word_count(event=None):
    content = text_entry.get("1.0", tk.END)
    words = content.split()
    word_count_var.set(f"Word Count: {len(words)}")


# Create the main notepad window
notepad = tk.Tk()
notepad.title("Notepad")

# Create a text entry widget
text_entry = tk.Text(notepad, wrap="word", font=('Arial', 14), undo=True)
text_entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
text_entry.focus_set()
text_entry.bind("<KeyRelease>", update_word_count)

# Timer display
timer_var = tk.StringVar()
timer_var.set("Elapsed Time: 00:00")
timer_label = tk.Label(notepad, textvariable=timer_var, font=('Arial', 12))
timer_label.grid(row=1, column=0, columnspan=5)

# Word count display
word_count_var = tk.StringVar()
word_count_var.set("Word Count: 0")
word_count_label = tk.Label(notepad, textvariable=word_count_var, font=('Arial', 12))
word_count_label.grid(row=2, column=0, columnspan=5)

# Save button
save_button = tk.Button(notepad, text="Save (Ctrl+S)", width=15, command=save_to_file)
save_button.grid(row=3, column=1, pady=5)

# Open button
open_button = tk.Button(notepad, text="Open (Ctrl+O)", width=15, command=open_file)
open_button.grid(row=3, column=2, pady=5)

# Exit button
exit_button = tk.Button(notepad, text="Exit (Ctrl+Q)", width=15, command=notepad.destroy)
exit_button.grid(row=3, column=3, pady=5)

# Keyboard shortcuts
notepad.bind("<Control-s>", lambda event: save_to_file())
notepad.bind("<Control-o>", lambda event: open_file())
notepad.bind("<Control-q>", lambda event: notepad.destroy())

# Run the application
start_time_var = tk.DoubleVar()
start_time_var.set(time.time())
update_timer()
notepad.mainloop()
