from tkinter import *


class Converter():
    """
    Temperature conversion tool (°C to °F or °F to °C)
    """

    def __init__(self):
        """
        Temperature converter GUI
        """

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame,
                                  text="Temperature Convertor",
                                  font=("Arial", "16", "bold"))
        self.temp_heading.grid(row=0)

        instructions = ("Please enter a temperature below and then press one of the buttons "
                        "to convert it from centigrade to Fahrenheit.")
        self.temp_instructions = Label(self.temp_frame, text=instructions, wraplength=250,
                                       width=40, justify="left")
        self.temp_instructions.grid(row=1)

        self.temp_entry = Entry(self.temp_frame, font=("Arial", "14"))
        self.temp_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.temp_error = Label(self.temp_frame, text=error, fg="#9C0000")
        self.temp_error.grid(row=3)

        # Conversion, Help and History / export buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=4)

        self.to_celsius_button = Button(self.button_frame, text="To Celsius",
                                        bg="#990099", fg="#ffffff",
                                        font=("Arial", "12", "bold"), width=12)
        self.to_celsius_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_fahrenheit_button = Button(self.button_frame, text="To Fahrenheit",
                                           bg="#009900", fg="#ffffff",
                                           font=("Arial", "12", "bold"), width=12)
        self.to_fahrenheit_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_help_button = Button(self.button_frame, text="Help / Info",
                                       bg="#CC6600", fg="#ffffff",
                                       font=("Arial", "12", "bold"), width=12)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_history_button = Button(self.button_frame, text="History / Export",
                                            bg="#004C99", fg="#ffffff",
                                            font=("Arial", "12", "bold"), width=12)
        self.to_history_button.grid(row=1, column=1, padx=5, pady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
