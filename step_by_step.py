import customtkinter as ctk
from PIL import Image

STEP_ONE_DESC = """
There are three different ways to input a location: \n\
    • City: Name of a city \n\
        - ex Seattle, Noosa, San Francisco \n\
    • Postal Code: Zip code for loaction \n\
        - ex 98065, 98072, 98210 \n\
    • Coordinates: lat and lon for location (lat, lon) \n\
        - ex 47.535997856, -122.162520842
"""

class StepByStep(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=20, fg_color="#282828", 
                         bg_color="#121212", 
                         )

        self.grid_rowconfigure(8, weight=1)
        self.columnconfigure(1, weight=1)

        ## title
        description = ctk.CTkLabel(self,
                                        text="Step-by-Step instructions.",
                                        font=ctk.CTkFont(size=20, weight="bold"),
                                        )
        description.grid(row=0, column=0, pady=(20, 10), padx=(20, 20))

        ## enter location Step one 
        stepOneTitle = ctk.CTkLabel(self, 
                               text='Step 1: Input a specific location to view its current weather conditions',
                               font=ctk.CTkFont(size=15, weight="bold"),
                               justify='left'
                              )
        stepOneTitle.grid(row=1, column=0, padx=(15, 15), pady=(0, 0), sticky="w")

        stepOneTitle = ctk.CTkLabel(self, 
                               text=STEP_ONE_DESC,
                               font=ctk.CTkFont(size=15),
                               justify='left'
                              )
        stepOneTitle.grid(row=2, column=0, padx=(15, 15), pady=(0, 0), sticky="w")

        ## enter location image
        input_weather_image = ctk.CTkImage(light_image=Image.open("/Users/vanwykjo/jo-documents/OSU/Software engineering/MicroserviceProject/Images/input_weather.png"),
                                  dark_image=Image.open("/Users/vanwykjo/jo-documents/OSU/Software engineering/MicroserviceProject/Images/input_weather.png"),
                                  size=(705, 250))

        image_label = ctk.CTkLabel(self, image=input_weather_image, text="")  # display image with a CTkLabel
        image_label.grid(row=3, column=0, padx=(15, 15), pady=(0, 0))

        # Submit step 2
        stepTwoTitle = ctk.CTkLabel(self, 
                               text='Step 2: Submit the location input',
                               font=ctk.CTkFont(size=15, weight="bold"),
                               justify='left'
                              )
        stepTwoTitle.grid(row=4, column=0, padx=(15, 15), pady=(5, 5), sticky="w")

        submit_image = ctk.CTkImage(light_image=Image.open("Images/submit_input.png"),
                                  dark_image=Image.open("Images/submit_input.png"),
                                  size=(705, 250))

        image_label = ctk.CTkLabel(self, image=submit_image, text="")  # display image with a CTkLabel
        image_label.grid(row=5, column=0, padx=(15, 15), pady=(5, 5))

        # View step 3
        stepTwoTitle = ctk.CTkLabel(self, 
                               text='Step 3: View weather output',
                               font=ctk.CTkFont(size=15, weight="bold"),
                               justify='left'
                              )
        stepTwoTitle.grid(row=6, column=0, padx=(15, 15), pady=(5, 5), sticky="w")

        view_output_image = ctk.CTkImage(light_image=Image.open("Images/view_output.png"),
                                  dark_image=Image.open("Images/view_output.png"),
                                  size=(705, 400))

        image_label = ctk.CTkLabel(self, image=view_output_image, text="")  # display image with a CTkLabel
        image_label.grid(row=7, column=0, padx=(15, 15), pady=(5, 5))
