import customtkinter
import requests
import datetime

from logger import Logger
from utils import clearConsole, clearTerminal


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x1100")
root.title("Discord Webhook Client")
clearTerminal()

keep_input = False



def main():
    global webhook_url_textbox, webhook_name_textbox, webhook_icon_textbox, input_textbox, console_textbox, keep_input

    title_label = customtkinter.CTkLabel(
        master=root,
        text="Discord Webhook Client",
        font=("Roboto", 30),
        text_color="white"
    )
    title_label.pack(pady=15)



    webhook_data_frame = customtkinter.CTkFrame(
        master=root,
        corner_radius=5
    )
    webhook_data_frame.pack(pady=20)


    webhook_url_textbox = customtkinter.CTkEntry(
        master=webhook_data_frame,
        width=500,
        height=30,
        corner_radius=8,
        placeholder_text="Enter your webhook URL here..."
    )
    webhook_url_textbox.grid(pady=3)

    webhook_name_textbox = customtkinter.CTkEntry(
        master=webhook_data_frame,
        width=500,
        height=30,
        corner_radius=8,
        placeholder_text="Enter your webhook name here... (Optional)"
    )
    webhook_name_textbox.grid(pady=5)

    webhook_icon_textbox = customtkinter.CTkEntry(
        master=webhook_data_frame,
        width=500,
        height=30,
        corner_radius=8,
        placeholder_text="Enter the webhook icon link here... (Optional)"
    )
    webhook_icon_textbox.grid(pady=3)



    console_frame = customtkinter.CTkFrame(
        master=root,
        corner_radius=10,
        width=1000,
        height=700
    )
    console_frame.pack(pady=20)


    console_textbox = customtkinter.CTkTextbox(
        master=console_frame,
        width=800,
        height=600,
        corner_radius=3
    )
    console_textbox.configure(state="disabled")
    console_textbox.grid(row=0, column=0, pady=8, padx=8)

    input_textbox = customtkinter.CTkEntry(
        master=console_frame,
        width=700,
        height=35,
        corner_radius=10,
        placeholder_text="Enter text here..."
    )
    input_textbox.grid(row=3, column=0, pady=3)

    input_submit_button = customtkinter.CTkButton(
        master=console_frame,
        text="Enter",
        command=lambda: submitText(input_textbox.get()),
        corner_radius=15
    )
    input_submit_button.grid(row=5, column=0, padx=5)



    options_frame = customtkinter.CTkFrame(
        master=root,
        corner_radius=10,
        width=800,
        height=500
    )
    options_frame.pack(pady=10)


    options_title_label = customtkinter.CTkLabel(
        master=options_frame,
        text="Options",
        font=("Roboto", 25),
        text_color="white"
    )
    options_title_label.grid(pady=10, padx=75)


    keep_input_switch = customtkinter.CTkSwitch(
        master=options_frame,
        command=lambda: toggleKeepInput()
    )
    keep_input_switch.configure(text="Keep input")
    keep_input_switch.grid()


    clear_console_button = customtkinter.CTkButton(
        master=options_frame,
        text="Clear Console",
        command=lambda: clearConsole(console_textbox),
        corner_radius=15
    )
    clear_console_button.grid(pady=10)



def toggleKeepInput():
    global keep_input

    keep_input = not keep_input



def submitText(text: str):
    if not keep_input:
        input_textbox.delete(0, customtkinter.END)

    if not webhook_url_textbox.get().startswith("https://discord.com/api/webhooks"):
        Logger.logErrorMessage(
            textbox=console_textbox,
            text="Invalid webhook URL."
        )
        return

    webhook_url = webhook_url_textbox.get()
    username = webhook_name_textbox.get()
    icon_url = webhook_icon_textbox.get()

    data = {
        "content": text,
        "username": username,
        "avatar_url": icon_url
    }

    result = requests.post(
        url=webhook_url, 
        json=data
    )

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as error:
        Logger.logErrorMessage(
            textbox=console_textbox,
            text=str(error)
        )
    else:
        username_prefix = data["username"] + ": "

        if data["username"] == "":
            username_prefix = ""

        Logger.logMessage(
            textbox=console_textbox,
            text=f"{str(datetime.datetime.now())[:19]}        {username_prefix} {text}"
        )





if __name__ == "__main__":
    main()
    root.mainloop()
