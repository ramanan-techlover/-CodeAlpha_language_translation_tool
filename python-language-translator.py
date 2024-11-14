from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator

# Initialize GoogleTranslator instance to get supported languages
translator_instance = GoogleTranslator()
languages = translator_instance.get_supported_languages(as_dict=True)
language_names = list(languages.keys())

# Set up the Tkinter window
root = Tk()
root.geometry("600x400")
root.title("Language Translation Tool")

# Heading
Label(root, text="Language Translator", font="Arial 20 bold").pack(pady=10)

# Input Text Area
Label(root, text="Enter Text:", font="Arial 12").pack()
input_text = Text(root, font="Arial 10", height=5, wrap=WORD, padx=5, pady=5)
input_text.pack(pady=5)

# Language Selection
Label(root, text="From Language:", font="Arial 12").pack()
from_language_combo = ttk.Combobox(root, values=language_names, width=30)
from_language_combo.set("english")  # Default language
from_language_combo.pack()

Label(root, text="To Language:", font="Arial 12").pack()
to_language_combo = ttk.Combobox(root, values=language_names, width=30)
to_language_combo.set("spanish")  # Default language
to_language_combo.pack()

# Output Text Area
Label(root, text="Translated Text:", font="Arial 12").pack()
output_text = Text(root, font="Arial 10", height=5, wrap=WORD, padx=5, pady=5)
output_text.pack(pady=5)

# Translate Function
def translate_text():
    source_text = input_text.get("1.0", END).strip()
    src_lang = from_language_combo.get()
    dest_lang = to_language_combo.get()
    
    if not source_text:
        output_text.delete("1.0", END)
        output_text.insert(END, "Please enter text to translate.")
        return
    
    # Perform translation
    try:
        translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(source_text)
        output_text.delete("1.0", END)
        output_text.insert(END, translated_text)
    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Translation failed: {e}")

# Translate Button
translate_button = Button(root, text="Translate", font="Arial 12 bold", command=translate_text, bg="lightblue")
translate_button.pack(pady=10)

root.mainloop()
