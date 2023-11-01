# header.py
import customtkinter as ctk

class Header(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=20, fg_color="#282828", 
                         bg_color="#121212", 
                         )

        self.grid_rowconfigure(2, weight=1)
        self.columnconfigure(1, weight=1)

        self.description = ctk.CTkLabel(self,
                                        text="Stay ahead of the weather with our user-friendly app, providing real-time \n forecasts and updates for your location.",
                                        font=ctk.CTkFont(size=20, weight="bold"),
                                        )
        self.description.grid(row=0, column=0, pady=(20, 10), padx=(20, 20))

        self.tip = ctk.CTkLabel(self,
                                text="Enter your location to see current weather predictions for the day \n Up to date predictions such as temp, precipitation, wind, sunrise and sunset",
                                font=ctk.CTkFont(size=15),
                                fg_color="#3f3f3f",
                                padx=20,
                                pady=20,
                                corner_radius=15
                                )
        self.tip.grid(row=1, column=0, pady=(20, 20), padx=(20, 20))
