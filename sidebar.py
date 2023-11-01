import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, sidebar_button_event, change_appearance_mode_event, change_scaling_event):
        super().__init__(parent, width=140, corner_radius=0, fg_color="#3f3f3f", bg_color="#121212")
        self.parent = parent
        self.sidebar_button_event = sidebar_button_event
        self.change_appearance_mode_event = change_appearance_mode_event
        self.change_scaling_event = change_scaling_event
        self.setup_sidebar()
    
    def setup_sidebar(self):
        ##### Left Frame #####
        # Main Title
        self.logo_label = ctk.CTkLabel(self, text="Weather App", font=ctk.CTkFont(size=20, weight="bold"), )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # menu bar buttons
        self.sidebar_button_1 = ctk.CTkButton(self, 
                                                text="Step by step",
                                                command=self.sidebar_button_event,
                                                fg_color="#a688fa",
                                                text_color="#121212",
                                                font=ctk.CTkFont(size=12, weight="bold"),
                                                hover_color="#9171f8"
                                                )
        self.sidebar_button_1.grid(row=1, 
                                        column=0, 
                                        padx=20, 
                                        pady=10
                                        )
        self.sidebar_button_2 = ctk.CTkButton(self, 
                                                text="Help",
                                                command=self.sidebar_button_event,
                                                fg_color="#a688fa",
                                                text_color="#121212",
                                                font=ctk.CTkFont(size=12, weight="bold"),
                                                hover_color="#9171f8"
                                                )
        self.sidebar_button_2.grid(row=2, 
                                        column=0, 
                                        padx=20, 
                                        pady=10
                                        )
        self.sidebar_button_3 = ctk.CTkButton(self, 
                                                text="Feedback",
                                                command=self.sidebar_button_event,
                                                fg_color="#a688fa",
                                                text_color="#121212",
                                                font=ctk.CTkFont(size=12, weight="bold"),
                                                hover_color="#9171f8"
                                                )
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # Configure grid rows to push options to the bottom
        self.grid_rowconfigure(4, weight=1)
        
        # Appearance Mode and UI Scaling
        self.appearance_mode_label = ctk.CTkLabel(self, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self, 
                                                                values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event,
                                                                fg_color="#a688fa",
                                                                button_color="#9171f8",
                                                                text_color="#121212",
                                                                hover=False
                                                                )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self, values=["80%", "90%", "100%", "110%", "120%"],
                                                                command=self.change_scaling_event,
                                                                fg_color="#a688fa",
                                                                button_color="#9171f8",
                                                                text_color="#121212",
                                                                hover=False
                                                                )
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))