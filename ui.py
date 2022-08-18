import tkinter
from tkinter import Label, Button,END,Text, messagebox, ttk
import googletrans
import textblob

###CONSTS
headings = ("Montserrat", 15)
textbox_h = 15
textbox_w = 40
bg_color = 'lightgrey'
translate_btn = ("Helvetica", 10, "bold")


class Translator():
    def __init__(self):
        super().__init__()

        ###ROOT
        self.root = tkinter.Tk()
        self.root.title("Translator App ")
        self.root.geometry("900x550")
        self.root.eval('tk::PlaceWindow . center')
        self.root.config(pady=20, padx=20, bg=bg_color)

        ##LANGUAGES
        self.languages = googletrans.LANGUAGES
        self.languages_list = [value.title() for key, value in self.languages.items()]

        ####HEADINGS
        self.original_text = Label(self.root, text="Text", font=headings, bg=bg_color)
        self.original_text.grid(column=0, row=1, sticky="w")
        self.translated_text = Label(self.root, text="Translation", font=headings, bg=bg_color)
        self.translated_text.grid(column=2, row=1, sticky="w")

        ####TEXTBOXES
        self.original_textbox = Text(self.root, height=textbox_h, width=textbox_w, font=("Montserrat", 10))
        self.original_textbox.grid(column=0, row=2)

        self.translated_textbox = Text(self.root, height=textbox_h, width=textbox_w, font=("Montserrat", 10, "italic"))
        self.translated_textbox.grid(column=2, row=2)

        ###BUTTONS
        self.translate_button = Button(self.root, text="Translate !", font=translate_btn, command=self.translate_text)
        self.translate_button.grid(column=1, row=2, padx=20)

        self.clear_button = Button(self.root, text="Clear", command=self.clear_textboxes)
        self.clear_button.grid(row=3, column=1, ipadx=20)

        ###COMBOS
        self.original_combo = ttk.Combobox(self.root, width=40, value=self.languages_list)
        self.original_combo.current(21)
        self.original_combo.grid(row=3, column=0, sticky='w')

        self.translated_combo = ttk.Combobox(self.root, width=40, value=self.languages_list)
        self.translated_combo.current(90)
        self.translated_combo.grid(row=3, column=2, pady=10, sticky='w')

        self.root.mainloop()

    def translate_text(self):
        """translates the input text and renders it in the translation textbox"""
        # clear any text in translation box
        self.translated_textbox.delete(1.0, END)
        try:
            # Get the translate from Language Key
            original_language_key, translation_language_key = "", ""
            for key, value in self.languages.items():
                if value.title() == self.original_combo.get().title():
                    original_language_key = key

            # Get the translate to Language Key
            for key, value in self.languages.items():
                if value.title() == self.translated_combo.get():
                    translation_language_key = key
            # Turn original text to textBlob
            words_to_translate = textblob.TextBlob(self.original_textbox.get(1.0, END))

            # Translate text
            translation = words_to_translate.translate(from_lang=original_language_key, to=translation_language_key)

            # Output to screen
            self.translated_textbox.insert(1.0, translation)

        except Exception as e:
            messagebox.showerror("Translator", e)

    def clear_textboxes(self):
        self.translated_textbox.delete(1.0, END)
        self.original_textbox.delete(1.0, END)


if __name__ == "__main__":
    w = Translator()
