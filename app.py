import tkinter as tk
import customtkinter as ctk
import random 

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
SLIDER_WIDTH = 350
BUTTON_WIDTH = 35
BUTTON_HEIGHT = 25

# FONTS 
SLIDER_INFO_FONT = ("Arial", 16, 'bold')
COLOR_FONT = ("Arial", 20, 'bold')
BUTTON_FONT = ("Arial", 24, 'bold')
SCORE_FONT = ("Arial", 30, 'bold')

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Color Matcher")
        self.resizable(False,False)

        self.grid_columnconfigure((0,1), weight=1)

        self.last_touched = None

        # FRAMES
        self.game_frame = ctk.CTkFrame(self, corner_radius=0)
        self.game_frame.grid(row=0,column=0, sticky = 'nswe')
        self.game_frame.grid_columnconfigure(0, weight=1)

        self.score_frame = ctk.CTkFrame(self, corner_radius=0)
        self.score_frame.grid(row=0,column=1, sticky = 'nswe')
        self.score_frame.grid_columnconfigure(0, weight=1)
        self.score_frame.grid_rowconfigure((0,1), weight=1)
        self.score_frame.grid_rowconfigure(2, weight=0)

        self.slider_frame = ctk.CTkFrame(self, corner_radius=0)
        self.slider_frame.grid(row=1,column=0, sticky = 'nswe')
        #self.slider_frame.grid_columnconfigure(1, weight=1)
        #self.slider_frame.grid_columnconfigure((0), weight=0)

        self.button_frame = ctk.CTkFrame(self, corner_radius=0)
        self.button_frame.grid(row=1,column=1, sticky = 'nswe')
        self.button_frame.grid_columnconfigure(0, weight=1)

        # GAME FRAME WIDGETS
        ctk.CTkLabel(self.game_frame, text = "Guess", font = COLOR_FONT).grid(row=0,column=0, pady=(10, 0))
        self.correct_color = ctk.CTkButton(self.game_frame, text = '', state="disabled", fg_color=self.get_random_color(), height = 300, width = 300)
        self.correct_color.grid(row=1,column=0, padx=50, pady=(10,50))

        ctk.CTkLabel(self.game_frame, text = "My Color", font = COLOR_FONT).grid(row=0,column=1, pady = (10, 0))
        self.guess_color = ctk.CTkButton(self.game_frame, text = '', state="disabled", height = 300, width = 300)
        self.guess_color.grid(row=1,column=1, padx=50, pady=(10,50))

        # SCORE FRAME WIDGETS
        ctk.CTkLabel(self.score_frame, text = "Score: ", font = SCORE_FONT).grid(row=0,column=0, sticky='nsew', pady=(50, 10))
        self.score_label = ctk.CTkLabel(self.score_frame, text = "0", font = SCORE_FONT)
        self.score_label.grid(row=1,column=0, sticky='ns', pady=10)

        # SLIDER FRAME WIDGETS
        
        # RED SLIDER
        ctk.CTkLabel(self.slider_frame, text = "RED", justify="left", font = SLIDER_INFO_FONT).grid(row=0, column=0, padx=(100, 50))
        self.minus_button_red = ctk.CTkButton(self.slider_frame, text = "-", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, anchor='center', font = BUTTON_FONT, command= lambda c = "red": self.minus_color(c))
        self.minus_button_red.grid(row=0,column=1, padx=(5,25))
        self.slider_red = ctk.CTkSlider(self.slider_frame, from_=0, to=255, number_of_steps=256, width = SLIDER_WIDTH, command = lambda c = "red":self.update_color(None, c))
        self.slider_red.grid(row=0,column=2, sticky='ew',pady = 25)
        self.plus_button_red = ctk.CTkButton(self.slider_frame, text = "+", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, anchor='center', font = BUTTON_FONT, command= lambda c = "red": self.plus_color(c))
        self.plus_button_red.grid(row=0,column=3, sticky='e',padx=25)
        self.slider_red_value = ctk.CTkLabel(self.slider_frame, text = "", justify="center", font = SLIDER_INFO_FONT)
        self.slider_red_value.grid(row=0, column=4, padx=10)

        # GREEN SLIDER
        ctk.CTkLabel(self.slider_frame, text = "GREEN", justify="left", font = SLIDER_INFO_FONT).grid(row=1, column=0, padx=(100, 50))
        self.minus_button_green = ctk.CTkButton(self.slider_frame, text = "-", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, anchor='center', font = BUTTON_FONT, command = lambda c = "green": self.minus_color(c))
        self.minus_button_green.grid(row=1,column=1, padx=(5,25))
        self.slider_green = ctk.CTkSlider(self.slider_frame, from_=0, to=255, number_of_steps=256, width = SLIDER_WIDTH, command = lambda c = "green":self.update_color(c))
        self.slider_green.grid(row=1,column=2, sticky='ew', pady = 25)
        self.plus_button_green = ctk.CTkButton(self.slider_frame, text = "+", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, anchor='center', font = BUTTON_FONT, command= lambda c = "green": self.plus_color(c))
        self.plus_button_green.grid(row=1,column=3, sticky='e',padx=25)
        self.slider_green_value = ctk.CTkLabel(self.slider_frame, text = "", justify="left", font = SLIDER_INFO_FONT)
        self.slider_green_value.grid(row=1, column=4, padx=10)

        # BLUE SLIDER
        ctk.CTkLabel(self.slider_frame, text = "BLUE", justify="left", font = SLIDER_INFO_FONT).grid(row=2, column=0, padx=(100, 50))
        self.minus_button_blue = ctk.CTkButton(self.slider_frame, text = "-", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, anchor='center', font = BUTTON_FONT, command= lambda c = "blue": self.minus_color(c))
        self.minus_button_blue.grid(row=2,column=1, padx=(5,25))
        self.slider_blue = ctk.CTkSlider(self.slider_frame, from_=0, to=255, number_of_steps=256, width = SLIDER_WIDTH, command = lambda c = "blue":self.update_color(c))
        self.slider_blue.grid(row=2,column=2, sticky='ew', pady = 25)
        self.plus_button_blue = ctk.CTkButton(self.slider_frame, text = "+", width = BUTTON_WIDTH, height = BUTTON_HEIGHT, anchor='center', font = BUTTON_FONT, command= lambda c = "blue": self.plus_color(c))
        self.plus_button_blue.grid(row=2,column=3, sticky='e',padx=25)
        self.slider_blue_value = ctk.CTkLabel(self.slider_frame, text = "", justify="left", font = SLIDER_INFO_FONT)
        self.slider_blue_value.grid(row=2, column=4, padx=10)

        # SUBMIT FRAME WIDGETS
        self.submit_button = ctk.CTkButton(self.button_frame, height = 125, width = 250, text = "Submit", font = BUTTON_FONT,command=self.submit_answer)
        self.submit_button.grid(row=0,column=0, padx = 25)

    def minus_color(self, color):
        match color:
            case "red":
                self.slider_red.set(self.slider_red.get()-1)
                self.slider_red_value.configure(text = str(int(self.slider_red.get())))
            case "green":
                self.slider_green.set(self.slider_green.get()-1)
                self.slider_green_value.configure(text = str(int(self.slider_green.get())))
            case "blue":
                self.slider_blue.set(self.slider_blue.get()-1)
                self.slider_blue_value.configure(text = str(int(self.slider_blue.get())))
            case _:
                print("Error: not right color.")

    def plus_color(self, color):
        match color:
            case "red":
                self.slider_red.set(self.slider_red.get()+1)
                self.slider_red_value.configure(text = str(int(self.slider_red.get())))
            case "green":
                self.slider_green.set(self.slider_green.get()+1)
                self.slider_green_value.configure(text = str(int(self.slider_green.get())))
            case "blue":
                self.slider_blue.set(self.slider_blue.get()+1)
                self.slider_blue_value.configure(text = str(int(self.slider_blue.get())))
            case _:
                print("Error: not right color.")



    # upgrades the color of the guess with every tick of the slider
    def update_color(self, value, c):
        print(value, c)
        r,g,b = self.get_guess_colors()
        color = self.make_color(r,g,b)
        self.guess_color.configure(fg_color = color)
        self.slider_red_value.configure(text=int(self.slider_red.get()))
        self.slider_green_value.configure(text=int(self.slider_green.get()))
        self.slider_blue_value.configure(text=int(self.slider_blue.get()))

    # returns the hexidecimal representaion of the RGB value of the color
    def make_color(self, r, g, b):
        color = f"#{r:02x}{g:02x}{b:02x}"
        print(color)
        return color
    
    # returns the RGB value of the current guess color
    def get_guess_colors(self):
        return int(self.slider_red.get()), int(self.slider_green.get()), int(self.slider_blue.get())
    
    # gets a random color for the color we want to guess
    def get_random_color(self):
        self.answer_red = random.randint(0, 255)
        self.answer_green = random.randint(0, 255)
        self.answer_blue = random.randint(0, 255)
        return self.make_color(self.answer_red, self.answer_green, self.answer_blue)
    
    # get score for a single color
    def get_color_score(self, correct, guess):
        # a = [ (x - y)/x ]
        max_num = max(correct, guess)
        min_num = min(correct, guess)
        deviation = (max_num-min_num)/max_num
        # print(deviation)
        return 1 - deviation

    # gets score of current guess
    def get_score(self, correct, guess):
        final_score = 0
        for i in range(len(correct)):
            final_score += self.get_color_score(correct[i], guess[i])
        return f"{(final_score / 3)*100:.2f}"

    # check if the guess is correct and displays the score of the current guess
    def submit_answer(self):
        print(f"Correct color: {self.answer_red}|{self.answer_green}|{self.answer_blue}")
        print(f"Guess Color: {int(self.slider_red.get())}|{int(self.slider_green.get())}|{int(self.slider_blue.get())}")

        correct_colors = self.answer_red, self.answer_green, self.answer_blue
        guess_colors = self.get_guess_colors()

        if correct_colors[0] == guess_colors[0] and correct_colors[1] == guess_colors[1] and correct_colors[2] == guess_colors[2]:
            self.score_label.configure(text='100', text_color='green')
            print('YOU ARE CORRECT\nScore: 100')
            self.submit_button.configure(state="disabled")
        else:
            score = self.get_score(correct_colors, guess_colors)
            self.score_label.configure(text=score)
            print(f"Score: {self.get_score(correct_colors, guess_colors)}")

if __name__ == "__main__":
    app = App()

    ctk.set_appearance_mode("dark")  
    app.mainloop()

