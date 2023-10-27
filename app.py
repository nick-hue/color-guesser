import tkinter as tk
import customtkinter as ctk
from PIL import Image
import random 

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

SLIDER_WIDTH = 300

# FONTS 
COLOR_FONT = ("Arial", 20, 'bold')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Color Matcher")
        self.resizable(False,False)
        #self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        # FRAMES
        self.game_frame = ctk.CTkFrame(self, corner_radius=0)
        self.game_frame.grid(row=0,column=0, sticky = 'nswe')

        self.slider_frame = ctk.CTkFrame(self, corner_radius=0)
        self.slider_frame.grid(row=1,column=0, sticky = 'nswe')

        # GAME FRAME WIDGETS
        ctk.CTkLabel(self.game_frame, text = "Guess", font = COLOR_FONT).grid(row=0,column=0)
        self.correct_color = ctk.CTkButton(self.game_frame, text = '', state="disabled", fg_color=self.get_random_color(), height = 300, width = 300)
        self.correct_color.grid(row=1,column=0, padx=50, pady=(10,50))

        ctk.CTkLabel(self.game_frame, text = "My Color", font = COLOR_FONT).grid(row=0,column=1)
        self.guess_color = ctk.CTkButton(self.game_frame, text = '', state="disabled", height = 300, width = 300)
        self.guess_color.grid(row=1,column=1, padx=50, pady=(10,50))


        # SLIDER FRAME WIDGETS 
        self.slider_red = ctk.CTkSlider(self.slider_frame, from_=0, to=255, number_of_steps=256, width = SLIDER_WIDTH, command=self.update_color)
        self.slider_red.grid(row=0,column=0, pady = 25)
        
        self.slider_green = ctk.CTkSlider(self.slider_frame, from_=0, to=255, number_of_steps=256, width = SLIDER_WIDTH, command=self.update_color)
        self.slider_green.grid(row=1,column=0, pady = 25)

        self.slider_blue = ctk.CTkSlider(self.slider_frame, from_=0, to=255, number_of_steps=256, width = SLIDER_WIDTH, command=self.update_color)
        self.slider_blue.grid(row=2,column=0, pady = 25)

    def update_color(self, value):
        color = self.make_color(int(self.slider_red.get()), int(self.slider_green.get()), int(self.slider_blue.get()))
        self.guess_color.configure(fg_color = color)

    def make_color(self, r, g, b):
        color = f"#{r:02x}{g:02x}{b:02x}"
        print(color)
        return color
    
    def get_random_color(self):
        return self.make_color(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    


if __name__ == "__main__":
    app = App()

    ctk.set_appearance_mode("dark")  
    app.mainloop()

