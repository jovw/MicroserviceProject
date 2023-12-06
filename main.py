import tkinter as tk
import customtkinter as ctk
from sidebar import Sidebar
from header import Header
from location import LocationInput
from weather_ouput import WeatherOutput
from step_by_step import StepByStep

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Weather App")
        self.geometry("960x1300")
        self.config(bg="#121212")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        ##############################################
        # Create sidebar
        self.sidebar = Sidebar(self, self.sidebar_button_event, self.change_appearance_mode_event, self.change_scaling_event)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        ### Main Screen ###
        ##############################################
        # Create header (Description and tip)
        self.header = Header(self)
        self.header.grid(row=0, column=1, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        ##############################################
        # Weather input frame
        self.weather = WeatherOutput(self)
        self.location_input = LocationInput(self, self.weather)
        self.location_input.grid(row=1, column=1, columnspan=1, padx=(20, 20), pady=(0, 20), sticky="nsew")

        ##############################################

        # Main weather frame
        # self.weather = WeatherOutput(self)
        self.weather.grid(row=2, column=1, columnspan=1, padx=(20, 20), pady=(0, 20), sticky="nsew")

        ### Step-by-step screen ###
        # self.step_by_step = StepByStep(self)


    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self, button_name):
        if button_name == 'Step by step':
            # Hide current components
            self.header.grid_forget()
            self.location_input.grid_forget()
            self.weather.grid_forget()
            # Show step-by-step instrecutions
            self.step_by_step = StepByStep(self)
            self.step_by_step.grid(row=0, column=1, columnspan=1, rowspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        if button_name == 'Home':
            # Hide current components
            self.step_by_step.grid_forget()
            # Show home page
            self.header = Header(self)
            self.header.grid(row=0, column=1, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
            self.location_input = LocationInput(self, self.weather)
            self.location_input.grid(row=1, column=1, columnspan=1, padx=(20, 20), pady=(0, 20), sticky="nsew")
            self.weather = WeatherOutput(self)
            self.weather.grid(row=2, column=1, columnspan=1, padx=(20, 20), pady=(0, 20), sticky="nsew")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()

    #47.535997856
    #-122.162520842