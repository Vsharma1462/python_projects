import webbrowser
import time
from datetime import datetime
import random
import pyautogui
from fetch_data import get_data

# Path to your Chrome browser
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to your Chrome executable
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open("https://damangames.bet")

# Pause for the browser to load
time.sleep(5)

# Image Paths
image_paths = {
    "login": r"C:\vikash\daman\images\login.png",
    "loginbar": r"C:\vikash\daman\images\loginbar.png",
    "confirm": r"C:\vikash\daman\images\confirm677.png",
    "receive": r"C:\vikash\daman\images\receive677.png",
    "wingo": r"C:\vikash\daman\images\wingo677.png",
    "big": r"C:\vikash\daman\images\big677.png",
    "small": r"C:\vikash\daman\images\small677.png",
    "bigamount": r"C:\vikash\daman\images\bigamount677.png",
    "smallamount": r"C:\vikash\daman\images\smallamount677.png",
    "totalamount": r"C:\vikash\daman\images\totalamount677.png",
    "totalamountsmall": r"C:\vikash\daman\images\totalamountsmall677.png",
    "walletbalance": r"C:\vikash\daman\images\walletbalance677.png"
}

# Amounts for betting
# amounts = ['20', '60', '140']
# amounts = ['5', '20', '45']
# amounts = ['2', '6', '11']
# amounts = ['10', '30', '70']
# amounts = ['10', '30', '710']
amounts = ['5', '15', '35']
# amounts = ['5', '20', '40']
# amounts = ['10', '25', '55']
# amounts = ['1', '3', '9', '21']
# amounts = ['15', '45', '90']
# Utility to locate and cli10k an image
def locate_and_click(image_key, confidence=0.8, wait_time=1):
    try:
        button_location = pyautogui.locateOnScreen(image_paths[image_key], confidence=confidence)
        if button_location:
            button_center = pyautogui.center(button_location)
            pyautogui.click(button_center)
            time.sleep(wait_time)
            return True
    except Exception as e:
        print(f"Error locating {image_key}: {e}")
    return False

# Handle Confirm and Receive Notifications
def handle_notifications():
    print('Handling notifications...')
    locate_and_click("confirm")
    locate_and_click("receive")

# Wingo Button Click
def click_wingo():
    locate_and_click("wingo")

# Perform Bet on Outcome
def bet(outcome, bet_amount):
    if outcome == 'b':
        locate_and_click("big")
        locate_and_click("bigamount")
    else:
        locate_and_click("small")
        locate_and_click("smallamount")

    # Input bet amount and confirm
    pyautogui.press('backspace')
    pyautogui.write(bet_amount)
    if outcome == 'b':
        locate_and_click("totalamount")
    else:
        locate_and_click("totalamountsmall")

# Betting loop every half-minute
def repeat_each_half_minute():
    random_sb = None
    n = 0
    target = 0
    bet_amount = amounts[0]

    while True:
        current_time = datetime.now()
        seconds = current_time.second

        # Execute every 00 or 30 seconds
        if seconds == 0 or seconds == 30:
            print('target=', round(target, 2))
            if target > 200:
                exit()
            time.sleep(5)

            if locate_and_click("walletbalance"):
                last_sb = get_data()

                # Determine bet amount based on previous results
                if random_sb and random_sb != last_sb:
                    target -= float(bet_amount)
                    n += 1
                    bet_amount = amounts[n % len(amounts)]
                elif random_sb == last_sb:
                    target += float(bet_amount) * 0.96
                    n = 0
                    bet_amount = amounts[n]

                # Randomize small/big bet
                random_sb = random.choice(['s', 'b'])

                # Place bet
                bet(random_sb, bet_amount)

                time.sleep(1)

        time.sleep(0.1)  # Short sleep to reduce CPU usage

# Run the notifications and betting logic
handle_notifications()
click_wingo()
repeat_each_half_minute()