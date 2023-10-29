import customtkinter
# import tkinterDnD

# customtkinter.set_ctk_parent_class(tkinterDnD.Tk)

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x780")
app.title("CustomTkinter simple_example.py")

# print(type(app), isinstance(app, tkinterDnD.Tk))

def button_callback():
    print("Button click", combobox_1.get())


def slider_callback(value):
    progressbar_1.set(value)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
label_1.pack(pady=10, padx=10)

progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
progressbar_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
button_1.pack(pady=10, padx=10)

slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("CTkComboBox")

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
checkbox_1.pack(pady=10, padx=10)

radiobutton_var = customtkinter.IntVar(value=1)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=10, padx=10)

switch_1 = customtkinter.CTkSwitch(master=frame_1)
switch_1.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

segmented_button_1 = customtkinter.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
segmented_button_1.pack(pady=10, padx=10)

tabview_1 = customtkinter.CTkTabview(master=frame_1, width=300)
tabview_1.pack(pady=10, padx=10)
tabview_1.add("CTkTabview")
tabview_1.add("Tab 2")

app.mainloop()




               
                
                

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