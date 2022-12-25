import customtkinter
import os


def clearConsole(textbox: customtkinter.CTkTextbox):
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.configure(state="disabled")


def clearTerminal():
    if os.name == "nt":
        os.system("cls")
    else:
        try:
            os.system("clear")
        except:
            print("\n" * 100)
