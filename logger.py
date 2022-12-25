import customtkinter


class Logger:
    
    def logMessage(textbox: customtkinter.CTkTextbox, text: str):
        textbox.configure(state="normal")
        textbox.insert(
            index=customtkinter.END,
            text=text + "\n"
        )
        textbox.configure(state="disabled")

        print(text)


    def logErrorMessage(textbox: customtkinter.CTkTextbox, text: str):
        textbox.configure(state="normal")
        textbox.insert(
            index=customtkinter.END,
            text="[ERROR] " + text + "\n"
        )
        textbox.configure(state="disabled")

        print("[ERROR] " + text)

