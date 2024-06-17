import tkinter as tk
import customtkinter as ctk

class Main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Color mixer")
        self.geometry("600x400")

        self.color_light = tk.StringVar()
        self.color_object = tk.StringVar()
        self.color_final = tk.StringVar()

        #Color of the light source
        colorlight_label = ctk.CTkLabel(self, bg_color="transparent", text="Color of the light source").place(relx=0.1, rely=0.14, anchor="nw")
        colorlight_entry = ctk.CTkEntry(self, textvariable=self.color_light).place(relx=0.1, rely=0.2, anchor="nw")

        try:
            print(self.color_light.get())
            self.colorlight_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_light.get()}", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
        except:
            self.colorlight_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)

        ctk.CTkButton(self, command=lambda: self.change_colors(), text="Change").place(anchor="center", relx=0.5, rely=0.95)

        #Color of the object
        colorobject_label = ctk.CTkLabel(self, bg_color="transparent", text="Color of the material").place(relx=0.1, rely=0.54, anchor="nw")
        colorobject_entry = ctk.CTkEntry(self, textvariable=self.color_object).place(relx=0.1, rely=0.6, anchor="nw")

        try:
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
            color_light = f"#{self.color_light.get()}"
            color_object = f"#{self.color_object.get()}"
            self.colorlight_canvas = ctk.CTkCanvas(self, bg=color_light, borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
            self.colorobject_canvas = ctk.CTkCanvas(self, bg=color_object, borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.58, anchor="nw", relheight=0.1, relwidth=0.07)
        except:
            self.colorlight_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
        
        finally:
            self.final_light_calculator()

    def conversor_to_decimal(self, hex_color):
        red_light = hex_color[0:2]
        green_light = hex_color[2:4]
        blue_light =  hex_color[4:6]

        red_light = int(red_light, 16)
        green_light = int(green_light, 16)
        blue_light =  int(blue_light, 16)

        rgb = [red_light, green_light, blue_light]

        return(rgb)
    
    def final_light_calculator(self):
        #normalize
        rgb_light = self.conversor_to_decimal(self.color_light.get())

        rgb_object = self.conversor_to_decimal(self.color_object.get())

        print(rgb_light)
        print(rgb_object)

        rgb_final = []
        
        rgb_final.append(rgb_light[0] * rgb_object[0] // 255)
        rgb_final.append(rgb_light[1] * rgb_object[1] // 255)
        rgb_final.append(rgb_light[2] * rgb_object[2] // 255)

        print(f"Final {rgb_final}")
        self.conversor_to_hex(rgb_final)
    
    def conversor_to_hex(self, value):
        print(value)
        red = str(hex(value[0]))
        if len(red) == 1:
            red.insert[0,0]
        green = str(hex(value[1]))
        if len(green) == 1:
            green.insert[0,0]
        blue = str(hex(value[2]))
        if len(blue) == 1:
            blue.insert[0,0]
        final = (red[2:4]+green[2:4]+blue[2:4])
        print(final)

        #self.colorfinal_entry = ctk.CTkLabel(self, text=final).place(relx=0.7, rely=0.4, anchor="nw")
        #self.colorfinal_canvas = ctk.CTkCanvas(self, bg=f"#{final}", borderwidth=0, highlightthickness=0).place(relx=0.615, rely=0.38, anchor="nw", relheight=0.1, relwidth=0.07)
        

        

App = Main()
App.run_window()