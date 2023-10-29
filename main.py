from tkinter import *
import customtkinter as ctk
from sidebar import Sidebar
from header import Header
from location import LocationInput

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Weather App")
        self.geometry("960x1200")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        ##############################################
        # Create sidebar
        self.sidebar = Sidebar(self, self.sidebar_button_event, self.change_appearance_mode_event, self.change_scaling_event)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

        ##############################################
        # Create header (Description and tip)
        self.header = Header(self)
        self.header.grid(row=0, column=1, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        ##############################################
        # Weather input frame
        self.location_input = LocationInput(self)
        self.location_input.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        ##############################################

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()