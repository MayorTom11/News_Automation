import customtkinter as ctk
import main
import mail


class App(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.title = title
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.title_frame = TitleFrame(self, fg_color="transparent")
        self.options_frame = OptionsFrame(self, fg_color="transparent")
        button = ctk.CTkButton(self, text="Buscar noticias!", command=self.send_email_with_input)
        button.grid(row=2, column=0, pady=12, padx=10)
        self.checkbox = ctk.CTkCheckBox(self, text="Recordar configuración")
        self.checkbox.grid(row=3, column=0, pady=12, padx=12)

    def send_email_with_input(self):
        title_input = self.title_frame.q.get()
        sort_by_input = self.options_frame.options_frame1.sort_by.get()
        date_input = self.options_frame.options_frame2.rango_fecha.get()
        if self.checkbox.get() == 1:
            print("Checkbox ticked")
        else:
            print("Checkbox not ticked")
        if title_input == "" or sort_by_input == "Elegí una de las opciones" or date_input == "Elegí una de las opciones":
            self.show_error("Por favor revisar la información ingresada")
        else:
            main.news(title_input, sort_by_input, date_input)
        mail.send_email(title_input)

    def show_error(self, message):
        error_window = ctk.CTk()
        error_window.title("Error")
        error_window.geometry("300x100")

        error_label = ctk.CTkLabel(error_window, text=message)
        error_label.pack(pady=10)

        ok_button = ctk.CTkButton(error_window, text="OK", command=error_window.destroy)
        ok_button.pack(pady=5)

        error_window.mainloop()


class TitleFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid(row=0, column=0, padx=15, pady=15)
        self.widgets()

    def widgets(self):
        titulo = ctk.CTkLabel(self, text="Búsqueda de noticias", font=("Roboto", 32))
        titulo.pack(pady=12, padx=10)
        self.q = ctk.CTkEntry(self, placeholder_text="Ingresa la categoría", width=400)
        self.q.pack(pady=12, padx=10)


class OptionsFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.options_frame1 = OptionsFrame1(self)
        self.options_frame2 = OptionsFrame2(self)
        self.grid(row=1, column=0, padx=15, pady=15)


class OptionsFrame1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=1, column=0, padx=15, pady=15)
        self.widgets()

    def widgets(self):
        tipo_orden = ctk.CTkLabel(self, text="Tipo de orden:")
        tipo_orden.pack()
        self.sort_by = ctk.CTkOptionMenu(self, values=["Por Relevancia", "Por Fecha", "Por Popularidad"])
        self.sort_by.set("Elegí una de las opciones")
        self.sort_by.pack(pady=12, padx=10)


class OptionsFrame2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=1, column=1, padx=15, pady=15)
        self.widgets()

    def widgets(self):
        fecha = ctk.CTkLabel(self, text="Qué fecha estabas buscando?")
        fecha.pack()
        self.rango_fecha = ctk.CTkOptionMenu(self, values=["Hoy", "Ayer", "Hace 3 días", "Hace 5 días"])
        self.rango_fecha.set("Elegí una de las opciones")
        self.rango_fecha.pack(pady=12, padx=10)


app = App("App Class Test", (500, 400))
app.mainloop()
