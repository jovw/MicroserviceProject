from tkinter import *
import customtkinter as ctk

class LocationInput(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=10, fg_color="#282828")
        
        # Configure layout
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(3, weight=0)
        
        # Create widgets
        self._create_widgets()
        
    def _create_widgets(self):
        # Header
        header2 = ctk.CTkLabel(self, 
                               text='How would you like to enter your address?',
                               font=ctk.CTkFont(size=15)
                              )
        header2.grid(row=0, column=0, padx=(15, 15), pady=(15, 15), sticky="nsew")

        # Tabview for different input methods
        self._create_tabview()
        
        # Buttons
        self._create_buttons()

    def _create_tabview(self):
        tabview = ctk.CTkTabview(self, 
                                 width=700, 
                                 height=110, 
                                 fg_color="#3f3f3f", 
                                 segmented_button_selected_color="#a688fa",
                                 text_color="#fff",
                                 segmented_button_unselected_color="#121212",
                                 segmented_button_fg_color="#121212",
                                 segmented_button_unselected_hover_color="#282828",
                                 segmented_button_selected_hover_color="#282828")
        tabview.grid(row=1, padx=(20, 20), pady=(0, 20), sticky="nsew")
        tabview.grid_rowconfigure(2, weight=0)

        tabview.add("City")
        tabview.add("Postal Code")
        tabview.add("Coordinates")

        self._create_city_tab(tabview.tab("City"))
        self._create_postal_code_tab(tabview.tab("Postal Code"))
        self._create_coordinates_tab(tabview.tab("Coordinates"))

    def _create_city_tab(self, parent):
        # City input form
        form_frame = ctk.CTkFrame(parent, fg_color="#3f3f3f")
        form_frame.grid(row=0, pady=(15, 15), padx=(15, 15))
        form_frame.grid_rowconfigure(2, weight=0)
        form_frame.grid_columnconfigure(1, weight=0)

        # City label and entry
        location_city = ctk.CTkLabel(form_frame, text="City:")
        location_city.grid(row=0, column=0, padx=(15, 15))
        city_entry = ctk.CTkEntry(form_frame, placeholder_text="Seattle", width=360)
        city_entry.grid(row=0, column=1, padx=0, pady=0)

    def _create_postal_code_tab(self, parent):
        # Postal code input form
        postal_code_frame = ctk.CTkFrame(parent, fg_color="#3f3f3f")
        postal_code_frame.grid(row=0, pady=(15, 15))
        postal_code_frame.grid_rowconfigure(1, weight=0)
        postal_code_frame.grid_columnconfigure(2, weight=0)

        # Postal code and country input
        code_frame = ctk.CTkFrame(postal_code_frame, fg_color="#3f3f3f")
        code_frame.grid(row=0, column=0, sticky='w', padx=(15, 15), pady=0)
        code_frame.grid_columnconfigure(2, weight=1)

        code_label = ctk.CTkLabel(code_frame, text="Postal Code:")
        code_label.grid(row=0, column=0)
        code_entry = ctk.CTkEntry(code_frame, placeholder_text="98065")
        code_entry.grid(row=0, column=1, padx=(15,0), pady=0)

        country_frame = ctk.CTkFrame(postal_code_frame, fg_color="#3f3f3f")
        country_frame.grid(row=0, column=1, sticky='w', padx=0, pady=0)
        country_frame.grid_columnconfigure(2, weight=1)

        country_label = ctk.CTkLabel(country_frame, text="Country:")
        country_label.grid(row=0, column=0, padx=(15, 0), pady=0)
        country_entry = ctk.CTkEntry(country_frame, placeholder_text="US")
        country_entry.grid(row=0, column=1, padx=(15, 15), pady=0)

    def _create_coordinates_tab(self, parent):
        # Coordinates input form
        coordinate_frame = ctk.CTkFrame(parent, fg_color="#3f3f3f")
        coordinate_frame.grid(row=0, pady=(15, 15), padx=(15, 15))
        coordinate_frame.grid_rowconfigure(1, weight=0)
        coordinate_frame.grid_columnconfigure(2, weight=0)

        # Latitude and longitude input
        lat_frame = ctk.CTkFrame(coordinate_frame, fg_color="#3f3f3f")
        lat_frame.grid(row=0, column=0, sticky='w', padx=(15, 15), pady=0)
        lat_frame.grid_columnconfigure(2, weight=1)

        lat_label = ctk.CTkLabel(lat_frame, text="Lat:")
        lat_label.grid(row=0, column=0)
        lat_entry = ctk.CTkEntry(lat_frame, placeholder_text="47.535997856")
        lat_entry.grid(row=0, column=1, padx=(15,0), pady=0)

        long_frame = ctk.CTkFrame(coordinate_frame, fg_color="#3f3f3f")
        long_frame.grid(row=0, column=1, sticky='w', padx=0, pady=0)
        long_frame.grid_columnconfigure(2, weight=1)

        long_label = ctk.CTkLabel(long_frame, text="Long:")
        long_label.grid(row=0, column=0, padx=(15, 0), pady=0)
        long_entry = ctk.CTkEntry(long_frame, placeholder_text="-122.162520842")
        long_entry.grid(row=0, column=1, padx=(15, 15), pady=0)

    def _create_buttons(self):
        # Buttons
        button_frame = ctk.CTkFrame(self, fg_color="#282828")
        button_frame.grid(row=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        button_frame.grid_rowconfigure(0, weight=0)
        button_frame.grid_columnconfigure(3, weight=1)

        undo_button = ctk.CTkButton(button_frame, 
                                    text="Submit", 
                                    fg_color="#a688fa", 
                                    text_color="#121212",
                                    font=ctk.CTkFont(size=12, weight="bold"),
                                    hover_color="#9171f8",
                                    command="")
        undo_button.grid(row=0, column=0, padx=0, pady=0, sticky="w")

        redo_button = ctk.CTkButton(button_frame, 
                                    text="Clear", 
                                    fg_color="#282828", 
                                    hover_color="#9171f8",
                                    border_color="white",
                                    border_width=1,
                                    font=ctk.CTkFont(size=12, weight="bold"))
        redo_button.grid(row=0, column=1, padx=(15, 15), pady=0, sticky="w")

        submit_button = ctk.CTkButton(button_frame, 
                                      text="Undo", 
                                      fg_color="#282828", 
                                      hover_color="#9171f8",
                                      border_color="white",
                                      border_width=1,
                                      font=ctk.CTkFont(size=12, weight="bold"))
        submit_button.grid(row=0, column=2, padx=0, pady=0, sticky="e")
