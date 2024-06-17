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

        def change(self):
            try:
                print(self.color_light.get())
                colorlight_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_light.get()}", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
                colorobject_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_object.get()}", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
                colorfinal_canvas = ctk.CTkCanvas(self, bg=f"#{calculate_hex}", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
                self.colorfinal_entry.set()
            except:
                colorlight_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
                colorobject_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
        
        def calculate_hex(self):
            #Light
            hdc_light = self.color_light

            red_light = hdc_light[0] + hdc_light[1]
            green_light = hdc_light[2] + hdc_light[3]
            blue_light =  hdc_light[4] + hdc_light[5]

            #normalize

            red_light = int(red_light, 16)/255
            green_light = int(green_light, 16)/255
            blue_light =  int(blue_light, 16)/255

            #Material
            hdc_object = self.color_object

            red_object = hdc_object[0] + hdc_object[1]
            green_object = hdc_object[2] + hdc_object[3]
            blue_object =  hdc_object[4] + hdc_object[5]

            #normalize

            red_object = int(red_object, 16)
            green_object = int(green_object, 16)
            blue_object =  int(blue_object, 16)

            #final rgb
            
            red_final = red_light*red_object 
            green_final = green_light*green_object
            blue_final = blue_light*blue_object

            #conversor
            red_final = hex(red_final)[2:4]
            green_final = hex(green_final)[2:4]
            blue_final = hex(blue_final)[2:4]


            rgb_final = red_final+green_final+blue_final

            return (rgb_final)

    
        #Color of the light source
        colorlight_label = ctk.CTkLabel(self, bg_color="transparent", text="Color of the light source").place(relx=0.1, rely=0.14, anchor="nw")
        colorlight_entry = ctk.CTkEntry(self, textvariable=self.color_light).place(relx=0.1, rely=0.2, anchor="nw")

        try:
            print(self.color_light.get())
            colorlight_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_light.get()}", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)
        except:
            colorlight_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.18, anchor="nw", relheight=0.1, relwidth=0.07)

        #Color of the object
        colorobject_label = ctk.CTkLabel(self, bg_color="transparent", text="Color of the material").place(relx=0.1, rely=0.54, anchor="nw")
        colorobject_entry = ctk.CTkEntry(self, textvariable=self.color_object).place(relx=0.1, rely=0.6, anchor="nw")

        try:
            print(self.color_light.get())
            colorobject_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_object.get()}", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.58, anchor="nw", relheight=0.1, relwidth=0.07)
        except:
            colorobject_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.015, rely=0.58, anchor="nw", relheight=0.1, relwidth=0.07)

    
        ctk.CTkButton(self, command=lambda: change(self), text="Change").place(anchor="center", relx=0.5, rely=0.95)



        #final
        colorfinal_label = ctk.CTkLabel(self, bg_color="transparent", text="Reflected light").place(relx=0.7, rely=0.34, anchor="nw")
        self.colorfinal_entry = ctk.CTkLabel(self, text="None").place(relx=0.7, rely=0.4, anchor="nw")

        try:
            print(self.color_light.get())
            colorfinal_canvas = ctk.CTkCanvas(self, bg=f"#{self.color_final.get()}", borderwidth=0, highlightthickness=0).place(relx=0.615, rely=0.38, anchor="nw", relheight=0.1, relwidth=0.07)
        except:
            colorfinal_canvas = ctk.CTkCanvas(self, bg="#ffffff", borderwidth=0, highlightthickness=0).place(relx=0.615, rely=0.38, anchor="nw", relheight=0.1, relwidth=0.07)
                  

        self.mainloop()

App = Main()
App.run_window()