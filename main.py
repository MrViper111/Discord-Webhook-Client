import requests
import time
import os


program = "Webhook Client"
system = "[System] "
error = "[Error] "
success = "[Success] "


def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


clearScreen()
os.system("title Webhook Client")
os.system("color f")
print("--- "+program+" ---")
print("This program is only supported by Windows")
print("and may be unstable on other operating systems.")
time.sleep(2)
clearScreen()

while True:
    webhookUrl = input(system + "Webhook URL: ")
    if webhookUrl.startswith("https://discord.com/api/webhooks"):
        break
    else:
        print(error+"Invalid webhook URL.")

webhookName = input(system + "Webhook name: ")

def executePayloadDelivery():
    url = webhookUrl
    data = {
        "content": dataInput,
        "username": webhookName
    }
    result = requests.post(url, json=data)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(system + error + err)
    else:
        print(
            system + success + "Payload delivered successfully! (HTTP Code {}".format(result.status_code) + ")")

while True:
    dataInput = input(system + "Input: ")

    if dataInput.lower() == "/changeurl":
        webhookUrl = input(system + "Webhook URL: ")
        if webhookUrl.startswith("https://discord.com/api/webhooks"):
            break
        else:
            print(error+"Invalid webhook URL.")
        print(system+f"You have changed the webhook URL to \"{webhookUrl}\".")
    elif dataInput.lower() == "/changename":
        webhookName = input(system + "Webhook name: ")
        print(system+f"You have changed the webhook name to \"{webhookName}\".")
    elif dataInput.lower() == "/spam":
        dataInput = input(system + "[Spam] " + "Input: ")

        while True:
            try:
                spamNum = int(input(system + "Spam amount: "))
                break
            except ValueError:
                print(error+"Expected an integer.")
        while True:
            try:
                spamDelay = float(input(system + "Spam delay: "))
                break
            except ValueError:
                print(error+"Expected an integer.")

        for i in range(spamNum):
            time.sleep(float(spamDelay))
            executePayloadDelivery()
    elif (dataInput.lower() == "/clear") or (dataInput.lower() == "/cls"):
        clearScreen()
    else:
        executePayloadDelivery()
