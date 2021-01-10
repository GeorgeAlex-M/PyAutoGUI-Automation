import pyautogui
from time import sleep

# Constants
DELAY_BETWEEN_COMMANDS = 1.00

# Main Function
def main():

    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    initializePyAutoGUI()

    # Countdown timer
    countdownTimer()

    ############################
    # Actual Automation Script #
    ############################

    # Attempt to start a new Game Server
    startGameServer()

    #########################
    # Other DEBUG Functions #
    #########################

    # Retrieve mouse position
#    reportMousePosition()

    # Script has been successfully executed
    print("Done")

#############
# Functions #
#############
def startGameServer():
    # Hover our mouse over New Game selection button
    pyautogui.click(549, 427, duration=0.5)
    sleep(DELAY_BETWEEN_COMMANDS)
    # Click the button to start a New Game
    pyautogui.click()

    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click(1335, 679, duration=0.5)

    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click(1285, 668, duration=0.5)

    sleep(DELAY_BETWEEN_COMMANDS)
    pyautogui.click(1045, 661, duration=0.5)

#########
# Utils #
#########
def initializePyAutoGUI():
    pyautogui.FAILSAFE = True

def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)

################
# DO NOT TOUCH #
################
if __name__ == "__main__":
    main()