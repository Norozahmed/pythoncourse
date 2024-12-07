import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()


# Function to perform translation
def translate_text():
    source_text = source_textbox.get("1.0", tk.END).strip()
    source_lang = source_lang_combobox.get()
    target_lang = target_lang_combobox.get()

    if source_text and source_lang and target_lang:
        try:
            translation = translator.translate(
                source_text,
                src=source_lang,
                dest=target_lang
            )
            target_textbox.delete("1.0", tk.END)
            target_textbox.insert(tk.END, translation.text)
        except Exception as e:
            target_textbox.delete("1.0", tk.END)
            target_textbox.insert(tk.END, f"Error: {e}")


# Create the main window
app = tk.Tk()
app.title("Real-Time Translator")
app.geometry("600x400")

# Title Label
title_label = tk.Label(app, text="Real-Time Translator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Source Language Selection
source_lang_label = tk.Label(app, text="Source Language:")
source_lang_label.pack(anchor=tk.W, padx=20)
source_lang_combobox = ttk.Combobox(app, values=list(LANGUAGES.values()), state="readonly")
source_lang_combobox.set("English")  # Default value
source_lang_combobox.pack(fill=tk.X, padx=20, pady=5)

# Target Language Selection
target_lang_label = tk.Label(app, text="Target Language:")
target_lang_label.pack(anchor=tk.W, padx=20)
target_lang_combobox = ttk.Combobox(app, values=list(LANGUAGES.values()), state="readonly")
target_lang_combobox.set("Spanish")  # Default value
target_lang_combobox.pack(fill=tk.X, padx=20, pady=5)

# Source Text Box
source_textbox_label = tk.Label(app, text="Enter Text to Translate:")
source_textbox_label.pack(anchor=tk.W, padx=20)
source_textbox = tk.Text(app, height=5, wrap=tk.WORD)
source_textbox.pack(fill=tk.X, padx=20, pady=5)

# Translate Button
translate_button = tk.Button(app, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
translate_button.pack(pady=10)

# Target Text Box
target_textbox_label = tk.Label(app, text="Translated Text:")
target_textbox_label.pack(anchor=tk.W, padx=20)
target_textbox = tk.Text(app, height=5, wrap=tk.WORD, state=tk.NORMAL)
target_textbox.pack(fill=tk.X, padx=20, pady=5)

# Run the main loop
app.mainloop()
