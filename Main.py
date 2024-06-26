import tkinter as tk
import customtkinter as ctk

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Color mixer")
        self.geometry("600x400")

        #var
        self.color_light = tk.StringVar()
        self.color_object = tk.StringVar()
        self.color_final = tk.StringVar()
        self_hex_list = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    
        #Color of the light source
        colorlight_label = ctk.CTkLabel(self, bg_color="transparent", text="Color of the light source").place(relx=0.1, rely=0.14, anchor="nw")
        colorlight_entry = ctk.CTkEntry(self, textvariable=self.color_light).place(relx=0.1, rely=0.2, anchor="nw")

        try:
            print(self.color_light.get())
            self.colorlight_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_light.get()}", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
        except:
            self.colorlight_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)

        #Color of the object
        colorobject_label = ctk.CTkLabel(self, bg_color="transparent", text="Color of the material").place(relx=0.1, rely=0.54, anchor="nw")
        colorobject_entry = ctk.CTkEntry(self, textvariable=self.color_object).place(relx=0.1, rely=0.6, anchor="nw")

        try:
            print(self.color_light.get())
            self.colorobject_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_object.get()}", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.58, anchor="nw", relheight=0.1, relwidth=0.07)
        except:
            self.colorobject_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.58, anchor="nw", relheight=0.1, relwidth=0.07)

    
        ctk.CTkButton(self, command=lambda: self.change_colors(), text="Change").place(anchor="center", relx=0.5, rely=0.95)



        #final
        colorfinal_label = ctk.CTkLabel(self, bg_color="transparent", text="Reflected light").place(relx=0.7, rely=0.34, anchor="nw")
        self.colorfinal_entry = ctk.CTkLabel(self, text="None").place(relx=0.7, rely=0.4, anchor="nw")

        try:
            print(self.color_light.get())
            self.colorfinal_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_final.get()}", borderwidth=0, highlightthickness=0).place(relx=0.615, rely=0.38, anchor="nw", relheight=0.1, relwidth=0.07)
        except:
            self.colorfinal_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.615, rely=0.38, anchor="nw", relheight=0.1, relwidth=0.07)
                  

        self.mainloop()

    def change_colors(self):
        try:
            print(self.color_light.get())
            self.colorlight_canvas.configure(bg=f"#{self.color_light.get()}")
            self.colorobject_canvas.configure(bg=f"#{self.color_object.get()}")
        except:
            self.colorlight_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
            self.colorobject_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)



App = Main()
App.run_window()