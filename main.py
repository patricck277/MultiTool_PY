import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pdf_converter import PDFConverter


class MultiTool(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('MultiTool')
        self.geometry('800x600')

        # Utwórz ramkę dla menu
        self.menu_frame = tk.Frame(self, width=200, bg='gray')
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Utwórz ramkę dla narzędzi
        self.tool_frame = tk.Frame(self, bg='white')
        self.tool_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Dodaj przykładowe przyciski do menu
        self.add_menu_buttons()

        self.converter = PDFConverter()

    def add_menu_buttons(self):
        # Przycisk dla narzędzia konwersji plików
        # 1
        convert_button = ttk.Button(self.menu_frame, text='PDF TO DOCX', command=self.show_pdf_to_docx_converter)
        convert_button.pack(pady=10)
        # 2
        convert_button = ttk.Button(self.menu_frame, text='Inny 1', command=self.show_inny_tool)
        convert_button.pack(pady=10)
        # 3
        convert_button = ttk.Button(self.menu_frame, text='Inny 2', command=self.show_inny2_tool)
        convert_button.pack(pady=10)
        # 4
        convert_button = ttk.Button(self.menu_frame, text='Inny 3', command=self.show_inny3_tool)
        convert_button.pack(pady=10)

        # Możesz dodać więcej przycisków do innych narzędzi tutaj

    def clear_tool_frame(self):
        # Czyści aktualne narzędzia z ramki
        for widget in self.tool_frame.winfo_children():
            widget.destroy()

    # ################################################PDF_TO_DOCX######################################################

    def show_pdf_to_docx_converter(self):
        self.clear_tool_frame()
        label = tk.Label(self.tool_frame, text='Konwertuj PDF na DOCX', bg='white')
        label.pack(pady=20)

        convert_button = tk.Button(self.tool_frame, text="Wybierz PDF i konwertuj", command=self.convert_pdf_to_docx_ui)
        convert_button.pack(pady=10)

    def convert_pdf_to_docx_ui(self):
        pdf_file = filedialog.askopenfilename(title="Wybierz plik PDF", filetypes=[("Pliki PDF", "*.pdf")])
        if not pdf_file:
            return

        docx_file = filedialog.asksaveasfilename(title="Zapisz jako DOCX", filetypes=[("Pliki DOCX", "*.docx")],
                                                 defaultextension=".docx")
        if not docx_file:
            return

        # Użyj metody z klasy PDFConverter do konwersji
        self.converter.convert_pdf_to_docx(pdf_file, docx_file)

        messagebox.showinfo("Konwersja zakończona", "Konwersja PDF na DOCX zakończona pomyślnie!")

    # ################################################PDF_TO_DOCX######################################################
    def show_inny_tool(self):
        self.clear_tool_frame()
        label = tk.Label(self.tool_frame, text='Inny', bg='white')
        label.pack(pady=20)

    def show_inny2_tool(self):
        self.clear_tool_frame()
        label = tk.Label(self.tool_frame, text='Inny2', bg='white')
        label.pack(pady=20)

    def show_inny3_tool(self):
        self.clear_tool_frame()
        label = tk.Label(self.tool_frame, text='Inny3', bg='white')
        label.pack(pady=20)

        # Tutaj można dodać więcej elementów interfejsu specyficznych dla narzędzia konwersji plików


if __name__ == '__main__':
    app = MultiTool()
    app.mainloop()
