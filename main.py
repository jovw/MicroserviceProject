from tkinter import *
import customtkinter as ctk
import config
from sidebar import Sidebar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Weather App")
        self.geometry("960x1200")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        #######################################
        # Create sidebar
        self.sidebar = Sidebar(self, self.sidebar_button_event, self.change_appearance_mode_event, self.change_scaling_event)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

        # Create main content area
        # self.content = Content(self)
        # self.content.grid(row=0, column=1, columnspan=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        # Main descriptoin and tip frame
        self.toprow = ctk.CTkFrame(self, 
                                        corner_radius=10,
                                        fg_color="#282828"
                                        )
        self.toprow.grid(
                row=0, 
                column=1, 
                columnspan=1, 
                padx=(20, 20), 
                pady=(20, 20), 
                sticky="nsew",)
        self.toprow.grid_rowconfigure(2, weight=1)
        self.toprow.columnconfigure(1, weight=1)
        

        self.description = ctk.CTkLabel(self.toprow,
                                text="Stay ahead of the weather with our user-friendly app, providing real-time \n forecasts and updates for your location.",
                                font=ctk.CTkFont(size=20, weight="bold"),
                                )
        self.description.grid(row=0, column=0, pady=(20, 10), padx=(20, 20))

        self.tip = ctk.CTkLabel(self.toprow,
                        text="Enter your location to see current weather predictions for the day \n Up to date predictions such as temp, precipitation, wind, sunrise and sunset",
                        font=ctk.CTkFont(size=15),
                        fg_color="#3f3f3f",
                        padx=20,
                        pady=20,
                        corner_radius=15
                        )
        self.tip.grid(row=1, column=0, pady=(20, 20), padx=(20, 20))

        #         ##############################################
                
        #         # Weather input frame
        #         self.weatherinput_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#282828")
        #         self.weatherinput_frame.grid(
        #                                         row=1, 
        #                                         column=1, 
        #                                         # columnspan=1,
        #                                         padx=(20, 20), 
        #                                         pady=(0, 20), 
        #                                         sticky="nsew"
        #                                         )
        #         self.weatherinput_frame.grid_rowconfigure(3, weight=0)
        #         self.weatherinput_frame.grid_columnconfigure(3, weight=0)

        #         self.header2 = ctk.CTkLabel(self.weatherinput_frame, 
        #                                     text='How would you like to enter your address?',
        #                                     font=ctk.CTkFont(size=15)
        #                                     )
        #         self.header2.grid(row=0,
        #                           column=0,
        #                           padx=(15, 15), 
        #                           pady=(15, 15),
        #                           sticky="nsew"
        #                           )

        #         # diff inputs section
        #         self.tabview = ctk.CTkTabview(self.weatherinput_frame, 
        #                                       width=700, 
        #                                       height=110, 
        #                                       fg_color="#3f3f3f", 
        #                                       segmented_button_selected_color="#a688fa",
        #                                       text_color="#fff",
        #                                       segmented_button_unselected_color="#121212",
        #                                       segmented_button_fg_color="#121212",
        #                                       segmented_button_unselected_hover_color="#282828",
        #                                       segmented_button_selected_hover_color="#282828")
        #         self.tabview.grid(
        #                 row=1, 
        #                 padx=(20, 20), 
        #                 pady=(0, 20),
        #                 sticky="nsew"
        #                 )
        #         self.tabview.grid_rowconfigure(2, weight=0)

        #         self.tabview.add("City")
        #         self.tabview.add("Postal Code")
        #         self.tabview.add("Coordinates")
        #         self.tabview.tab("City").grid_columnconfigure(0, weight=1)
        #         self.tabview.tab("Postal Code").grid_columnconfigure(0, weight=1)
        #         self.tabview.tab("Coordinates").grid_columnconfigure(0, weight=1)

        #         ###### City tab #######
        #         # form frame for city
        #         self.form_frame = ctk.CTkFrame(self.tabview.tab("City"), fg_color="#3f3f3f")
        #         self.form_frame.grid(row=0, pady=(15, 15), padx=(15, 15))
        #         self.form_frame.grid_rowconfigure(2, weight=0)
        #         self.form_frame.grid_columnconfigure(1, weight=0)

        #         # City
        #         self.location_city = ctk.CTkLabel(self.form_frame,
        #                                           text="City:",)
        #         self.location_city.grid(row=0, column=0, padx=(15, 15))
        #         self.city_entry = ctk.CTkEntry(self.form_frame,
        #                                        placeholder_text="Seattle",
        #                                        width=360
        #                                        )
        #         self.city_entry.grid(row=0, column=1, padx=0, pady=0)

        #         ###### Postal Code ########
        #         ## main frame
        #         self.postal_code_frame = ctk.CTkFrame(self.tabview.tab("Postal Code"),
        #                                           fg_color="#3f3f3f")
        #         self.postal_code_frame.grid(row=0, pady=(15, 15))
        #         self.postal_code_frame.grid_rowconfigure(1, weight=0)
        #         self.postal_code_frame.grid_columnconfigure(2, weight=0)

        #         ## postal_code frame
        #         self.code_frame = ctk.CTkFrame(self.postal_code_frame,
        #                                        fg_color="#3f3f3f")
        #         self.code_frame.grid(row=0, column=0, sticky='w', 
        #                              padx=(15, 15), pady=0
        #                              )
        #         self.code_frame.grid_columnconfigure(2, weight=1)
        #         # label
        #         self.code_label = ctk.CTkLabel(self.code_frame,
        #                                          text="Postal Code:",)
        #         self.code_label.grid(row=0, column=0)
        #         # entry
        #         self.code_entry = ctk.CTkEntry(self.code_frame,
        #                                          placeholder_text="98065")
        #         self.code_entry.grid(row=0, column=1, padx=(15,0), pady=0)

        #         ## country frame
        #         self.country_frame = ctk.CTkFrame(self.postal_code_frame,
        #                                         fg_color="#3f3f3f")
        #         self.country_frame.grid(row=0, column=1, sticky='w', 
        #                                 padx=0, pady=0)
        #         self.country_frame.grid_columnconfigure(2, weight=1)
        #         # label
        #         self.country_label = ctk.CTkLabel(self.country_frame,
        #                                          text="Country:",)
        #         self.country_label.grid(row=0, column=0, padx=(15, 0), pady=0)
        #         self.country_entry = ctk.CTkEntry(self.country_frame,
        #                                          placeholder_text="US")
        #         self.country_entry.grid(row=0, column=1, padx=(15, 15), pady=0)

        #         ###### Coordinates ########
        #         ## main frame
        #         self.coordinate_frame = ctk.CTkFrame(self.tabview.tab("Coordinates"),
        #                                           fg_color="#3f3f3f")
        #         self.coordinate_frame.grid(row=0, pady=(15, 15), padx=(15, 15))
        #         self.coordinate_frame.grid_rowconfigure(1, weight=0)
        #         self.coordinate_frame.grid_columnconfigure(2, weight=0)

        #         ## lat frame
        #         self.lat_frame = ctk.CTkFrame(self.coordinate_frame,
        #                                        fg_color="#3f3f3f")
        #         self.lat_frame.grid(row=0, column=0, sticky='w', 
        #                              padx=(15, 15), pady=0
        #                              )
        #         self.lat_frame.grid_columnconfigure(2, weight=1)
        #         # label
        #         self.lat_label = ctk.CTkLabel(self.lat_frame,
        #                                          text="Lat:",)
        #         self.lat_label.grid(row=0, column=0)
        #         # entry
        #         self.lat_entry = ctk.CTkEntry(self.lat_frame,
        #                                          placeholder_text="47.535997856")
        #         self.lat_entry.grid(row=0, column=1, padx=(15,0), pady=0)

        #         ## lon frame
        #         self.lon_frame = ctk.CTkFrame(self.coordinate_frame,
        #                                         fg_color="#3f3f3f")
        #         self.lon_frame.grid(row=0, column=1, sticky='w', 
        #                                 padx=(15, 15), pady=0)
        #         self.lon_frame.grid_columnconfigure(2, weight=1)
        #         # label
        #         self.lon_label = ctk.CTkLabel(self.lon_frame,
        #                                          text="Lon:",)
        #         self.lon_label.grid(row=0, column=0, padx=(15, 0), pady=0)
        #         self.lon_entry = ctk.CTkEntry(self.lon_frame,
        #                                          placeholder_text="-121.856496574")
        #         self.lon_entry.grid(row=0, column=1, padx=(15, 15), pady=0)
                

        #         ####### Buttons for inputs ##########
        #         self.button_frame_1 = ctk.CTkFrame(self.weatherinput_frame,
        #                                          fg_color="#3f3f3f",
        #                                          )
        #         self.button_frame_1.grid(row=2, 
        #                                column=0, 
        #                                columnspan = 3,
        #                                padx=(15, 15), 
        #                                pady=(0, 15))
        #         self.button_frame_1.grid_columnconfigure(3, weight=1)
        #         self.loc_buttons = ctk.CTkButton(self.button_frame_1,
        #                                              text="Submit",
        #                                              fg_color="#a688fa",
        #                                              text_color="#121212",
        #                                              hover_color="#9171f8"
        #                                              )
        #         self.loc_buttons.grid(row=0, column=0, padx=(15, 15), pady=(15, 15))
        #         self.loc_buttons_2 = ctk.CTkButton(self.button_frame_1,
        #                                              text="Undo",
        #                                              fg_color="transparent",
        #                                              border_color="white",
        #                                              border_width=1,
        #                                              hover_color="#a688fa"
        #                                              )
        #         self.loc_buttons_2.grid(row=0, column=1, padx=(0, 15), pady=(15, 15))
        #         self.loc_buttons_3 = ctk.CTkButton(self.button_frame_1,
        #                                              text="Redo",
        #                                              fg_color="transparent",
        #                                              border_color="white",
        #                                              border_width=1,
        #                                              hover_color="#a688fa"
        #                                              )
        #         self.loc_buttons_3.grid(row=0, column=2, padx=(0, 15), pady=(15, 15))

        #         ###################

        #         # Main weather frame
        #         self.weather = ctk.CTkFrame(self, 
        #                                 #    corner_radius=10,
        #                                    fg_color="#1a1a1a"
        #                                 )
        #         self.weather.grid(
        #                row=3, 
        #                column=1, 
        #                columnspan=1, 
        #                padx=(20, 20), 
        #         #        pady=(20, 20), 
        #                sticky="nsew",)
        #         self.weather.grid_rowconfigure(2, weight=1)
        #         self.weather.columnconfigure(1, weight=1)

        #         ###################### current weather frame ######################
        #         self.current = ctk.CTkFrame(self.weather, fg_color="#1a1a1a")
        #         self.current.grid(
        #                row=0,
        #         #        column=1
        #         )
        #         self.current.grid_rowconfigure(4, weight=0)
        #         self.current.grid_columnconfigure(1, weight=0)

        #         # location Name
        #         self.locationName = ctk.CTkLabel(self.current, text='Snoqualmie',
        #                                          font=ctk.CTkFont(size=20, weight="bold"))
        #         self.locationName.grid(row=0)
        #         # Current Temp
        #         self.tempCurrent = ctk.CTkLabel(self.current, text='47°F',
        #                                         font=ctk.CTkFont(size=40, weight="normal"))
        #         self.tempCurrent.grid(row=1)
        #         # condition
        #         self.condition = ctk.CTkLabel(self.current, text='Partly Cloudy',
        #                                       font=ctk.CTkFont(size=15, weight="bold"))
        #         self.condition.grid(row=2)
        #         # High/Low temp
        #         self.temp = ctk.CTkLabel(self.current, text='H:5°F  L:28°F',
        #                                  font=ctk.CTkFont(size=15, weight="bold"))
        #         self.temp.grid(row=3)

        #         ###################### forecast Weather Tabs ######################
        #         self.weather_tabview = ctk.CTkTabview(self.weather, 
        #                                       width=700, 
        #                                 #       height=110, 
        #                                       fg_color="#282828", 
        #                                       segmented_button_selected_color="#a688fa",
        #                                       text_color="#fff",
        #                                       segmented_button_unselected_color="#121212",
        #                                       segmented_button_fg_color="#121212",
        #                                       segmented_button_unselected_hover_color="#282828",
        #                                       segmented_button_selected_hover_color="#282828")
        #         self.weather_tabview.grid(
        #                 row=1, 
        #                 padx=(20, 20), 
        #                 pady=(0, 20),
        #                 sticky="nsew"
        #                 )
        #         self.weather_tabview.grid_rowconfigure(2, weight=0)

        #         self.weather_tabview.add("Day 1")
        #         self.weather_tabview.add("Day 2")
        #         self.weather_tabview.add("Day 3")
        #         self.weather_tabview.add("Day 4")
        #         self.weather_tabview.add("Day 5")
        #         self.weather_tabview.add("Day 6")
        #         self.weather_tabview.add("Day 7")
        #         self.weather_tabview.add("Day 8")
        #         self.weather_tabview.add("Day 9")
        #         self.weather_tabview.add("Day 10")
        #         self.weather_tabview.tab("Day 1").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 2").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 3").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 4").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 5").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 6").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 7").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 8").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 9").grid_columnconfigure(0, weight=1)
        #         self.weather_tabview.tab("Day 10").grid_columnconfigure(0, weight=1)

        #         ###################### Per day Forecast Frame ######################
        #         self.daily_forecast = ctk.CTkFrame(self.weather_tabview, 
        #                                         #     fg_color="#3f3f3f"
        #                                                 fg_color="#282828"
        #                                             )
        #         self.daily_forecast.grid(row=1)
        #         self.daily_forecast.grid_rowconfigure(5, weight=0)

if __name__ == "__main__":
    app = App()
    app.mainloop()