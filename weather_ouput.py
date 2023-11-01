import customtkinter as ctk

class WeatherOutput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#282828", bg_color="#121212", corner_radius=20)

        # Configure layout
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(1, weight=0)
        
        # Create widgets
        self._create_widgets()

    def _create_widgets(self):
        # Current Weather
        self._create_current_weather()
        
        # Forecast Weather Tabs
        self._create_forecast_tabs()

    def _create_current_weather(self):
        current_frame = ctk.CTkFrame(self, fg_color="#282828")
        current_frame.grid(row=0, pady=(20, 20))
        current_frame.grid_rowconfigure(4, weight=0)
        current_frame.grid_columnconfigure(1, weight=0)

        # Location Name
        locationName = ctk.CTkLabel(current_frame, text='Snoqualmie',
                                    font=ctk.CTkFont(size=20, weight="bold"))
        locationName.grid(row=0)
        # Current Temp
        tempCurrent = ctk.CTkLabel(current_frame, text='47°F',
                                   font=ctk.CTkFont(size=40, weight="normal"))
        tempCurrent.grid(row=1)
        # Condition
        condition = ctk.CTkLabel(current_frame, text='Partly Cloudy',
                                 font=ctk.CTkFont(size=15, weight="bold"))
        condition.grid(row=2)
        # High/Low temp
        temp = ctk.CTkLabel(current_frame, text='H:5°F  L:28°F',
                            font=ctk.CTkFont(size=15, weight="bold"))
        temp.grid(row=3)

    def _create_forecast_tabs(self):
        weather_tabview = ctk.CTkTabview(self, 
                                         width=700,
                                         height=500,
                                         fg_color="#3f3f3f", 
                                         segmented_button_selected_color="#a688fa",
                                         text_color="#fff",
                                         segmented_button_unselected_color="#121212",
                                         segmented_button_fg_color="#121212",
                                         segmented_button_unselected_hover_color="#282828",
                                         segmented_button_selected_hover_color="#282828")
        weather_tabview.grid(row=1, padx=(20, 20), pady=(0, 20), sticky="nsew")
        weather_tabview.grid_rowconfigure(2, weight=0)
        weather_tabview.grid_columnconfigure(1, weight=0)

        for i in range(1, 11):
            day = f"Day {i}"
            weather_tabview.add(day)
            self._create_daily_forecast_tab(weather_tabview.tab(day))

    def _create_daily_forecast_tab(self, parent):
        daily_forecast_container = ctk.CTkFrame(parent, fg_color="#3f3f3f")
        daily_forecast_container.grid(row=0, pady=(15, 15), padx=(15, 15))
        daily_forecast_container.grid_rowconfigure(0, weight=1)
        daily_forecast_container.grid_columnconfigure(1, weight=0)  # Left and right spacers

        daily_forecast_frame = ctk.CTkFrame(daily_forecast_container, fg_color="#000000") # 3f3f3f The main frame inside container
        daily_forecast_frame.grid(row=0)

        self._create_overview_section(daily_forecast_frame)
        self._create_preciptation_section(daily_forecast_frame)
        self._create_sun_section(daily_forecast_frame)
        self._create_other_section(daily_forecast_frame)
        self._create_wind_section(daily_forecast_frame)

    def _create_overview_section(self, parent):
        over_view = ctk.CTkFrame(parent, fg_color="#3f3f3f")
        # Position in the center column with east-west sticky
        over_view.grid(row=0, column=2)  
        
        # Configure grid inside the overview
        over_view.grid_rowconfigure(3, weight=0)

        over_view_date = ctk.CTkLabel(over_view, text="Oct 29",
                                    font=ctk.CTkFont(size=15, weight="bold"))
        over_view_date.grid(row=1, column=0)
        over_view_condition = ctk.CTkLabel(over_view, text="Few Clouds")
        over_view_condition.grid(row=2, column=0)
        over_view_temp = ctk.CTkLabel(over_view, text="H:50.4°F  L:30.6°F")
        over_view_temp.grid(row=3, column=0)

    def _create_preciptation_section(self, parent):
        precip = ctk.CTkFrame(parent, fg_color="#3f3f3f")
        precip.grid(row=1, columnspan=3, column=1, pady=(20,0), padx=(20,20))
        precip.grid_columnconfigure([0, 1], weight=1)  # Evenly spaced
        
        rain_precip = ctk.CTkFrame(precip, fg_color="#575757")
        rain_precip.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        rain_precip.grid_rowconfigure(3, weight=1)
        rain_label = ctk.CTkLabel(rain_precip, text="Rain Preciptation")
        rain_label.grid(row=0, padx=(10, 20))
        rain_chance = ctk.CTkLabel(rain_precip, text='0"',
                                   font=ctk.CTkFont(size=20, weight="normal"))
        rain_chance.grid(row=1, padx=(30, 20),  pady=(0, 10))

        snow_precip = ctk.CTkFrame(precip, fg_color="#575757")
        snow_precip.grid(row=0, column=1, sticky="nsew", padx=(5, 0))# Set sticky to nsew
        snow_label = ctk.CTkLabel(snow_precip, text="Snow Preciptation")
        snow_label.grid(row=0, padx=(10, 20))
        snow_chance = ctk.CTkLabel(snow_precip, text='0"',
                                   font=ctk.CTkFont(size=20, weight="normal"))
        snow_chance.grid(row=1, padx=(30, 20),  pady=(0, 10))

    def _create_sun_section(self, parent):
        sun_info = ctk.CTkFrame(parent, fg_color="#575757")
        sun_info.grid(row=3, columnspan=3, column=1, pady=(10, 0))
        sun_info.grid_rowconfigure(2, weight=0)
        sun_info.grid_columnconfigure(2, weight=0)

        sun_label = ctk.CTkLabel(sun_info, text="Sunrise and Sunset")
        sun_label.grid(row=0, column=0, padx=(10, 0), pady=0)

        sun_rise = ctk.CTkLabel(sun_info, text="7:56 am", 
                                font=ctk.CTkFont(size=20, weight="normal"))
        sun_rise.grid(row=1, column=0, padx=(0, 0), pady=(0, 10))

        sun_set = ctk.CTkLabel(sun_info, text="5:56 pm",
                               font=ctk.CTkFont(size=20, weight="normal"))
        sun_set.grid(row=1, column=1, padx=(0, 40), pady=(0, 10))

    def _create_other_section(self, parent):
        other_info = ctk.CTkFrame(parent, fg_color="#3f3f3f")
        other_info.grid(row=4, columnspan=3, column=1, pady=(10, 0))
        other_info.grid_columnconfigure([0, 1, 2], weight=1)

        ## Dew Point
        dew_point = ctk.CTkFrame(other_info, fg_color="#575757")
        dew_point.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        dew_point.grid_rowconfigure(2, weight=1)
        ## Dew Label 
        dew_point_label = ctk.CTkLabel(dew_point, text="Dewpoint")
        dew_point_label.grid(row=0, padx=(10, 20))
        ## Dew content
        dew_point_content = ctk.CTkLabel(dew_point, text="29.4°F",
                                         font=ctk.CTkFont(size=20, weight="normal"))
        dew_point_content.grid(row=1, padx=(15, 15))

        ## humidity
        humidity = ctk.CTkFrame(other_info, fg_color="#575757")
        humidity.grid(row=0, column=1, sticky="nsew", padx=(5, 5))
        humidity.grid_rowconfigure(2, weight=1)
        ## Humidity label
        humidity_label = ctk.CTkLabel(humidity, text="Humidity")
        humidity_label.grid(row=0, padx=(10, 20))
        ## Humidity Content
        humidity_content = ctk.CTkLabel(humidity, text="66%",
                                        font=ctk.CTkFont(size=20, weight="normal"))
        humidity_content.grid(row=1, padx=(15, 15))

        ## UV Index
        uv_index = ctk.CTkFrame(other_info, fg_color="#575757")
        uv_index.grid(row=0, column=2, sticky="nsew", padx=(5, 0))
        uv_index.grid_rowconfigure(2, weight=1)
        ## UV index label
        uv_index_label = ctk.CTkLabel(uv_index, text="UV Index")
        uv_index_label.grid(row=0, padx=(10, 20))
        ## UV index Content
        uv_index_content = ctk.CTkLabel(uv_index, text="2",
                                        font=ctk.CTkFont(size=20, weight="normal"))
        uv_index_content.grid(row=1, padx=(15, 15))

    def _create_wind_section(self, parent):
        wind_info = ctk.CTkFrame(parent, fg_color="#575757")
        wind_info.grid(row=5, columnspan=3, column=1, pady=(10, 0))
        wind_info.grid_rowconfigure(2, weight=0)
        wind_info.grid_columnconfigure(3, weight=0)

        # Wind label
        wind_label = ctk.CTkLabel(wind_info, text="Wind")
        wind_label.grid(row=0, padx=(5, 20))
        # Wind Direction
        wind_direction = ctk.CTkLabel(wind_info, text="SSW",
                                      font=ctk.CTkFont(size=20, weight="normal"))
        wind_direction.grid(row=1, column=0, padx=(20,10), pady=(0, 10))

        # Wind Speed Frame
        wind_speed_frame = ctk.CTkFrame(wind_info, fg_color="#575757")
        wind_speed_frame.grid(row=1, column=1, sticky="nswe", padx=(10,10))
        wind_speed_frame.grid_rowconfigure([0, 1], weight=0)
        # # wind speed
        wind_speed = ctk.CTkLabel(wind_speed_frame, text="5.1",
                                  font=ctk.CTkFont(size=20, weight="normal"))
        wind_speed.grid(row=0, column=0, rowspan=2)
        wind_speed_mph = ctk.CTkLabel(wind_speed_frame, text="MPH \n WIND",
                                      font=ctk.CTkFont(size=10, weight="normal"))
        wind_speed_mph.grid(row=0, column=1)

        # Gust Speed Frame
        gust_speed_frame = ctk.CTkFrame(wind_info, fg_color="#575757") 
        gust_speed_frame.grid(row=1, column=2, sticky="nswe", padx=(10,20))
        gust_speed_frame.grid_rowconfigure([0, 1], weight=0)
        # # gust speed
        gust_speed = ctk.CTkLabel(gust_speed_frame, text="3.4",
                                  font=ctk.CTkFont(size=20, weight="normal"))
        gust_speed.grid(row=0, column=0, rowspan=2)
        gust_speed_mph = ctk.CTkLabel(gust_speed_frame, text="MPH \n GUST",
                                      font=ctk.CTkFont(size=10, weight="normal"))
        gust_speed_mph.grid(row=0, column=1)







