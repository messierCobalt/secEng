import os
import random
import sys
import time

# ANSIcodes
RST = "\033[0m"   # reset
BLD = "\033[1m"   # bold
DIM = "\033[2m"   # dim
ITL = "\033[3m"   # italic
UND = "\033[4m"   # underline
STR = "\033[9m"   # strikeThrough

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = [f"\033[3{i}m" for i in range(8)]
BG = [f"\033[4{i}m" for i in range(8)]

# thisDon'tNeedExplaining
fileName = os.path.basename(sys.argv[0])

# hT = helpText
hT = f"""{GREEN}
CLEAR | CLS | CLEAN      CLEARS SCREEN
HELP | GUIDE | MANUAL    PRINTS THIS
EXIT | QUIT | CLOSE      KILLS {BLD}{UND}{fileName}{RST}"""

# theBasics_funcs
clear = lambda: os.system("cls" if os.name == "nt" else "clear")

def slowPrint(text, t=0.01, T=0.05, newlineCinema=True, curtainCall_in=0.1, end=""):
    for char in text:
        print(char, flush=True, end=end)
        time.sleep(random.uniform(t, T))
    if newlineCinema:
        print()
    time.sleep(curtainCall_in)

def close():
    slowPrint(f"{BLD}{RED}GOODBYE!{RST}")
    sys.exit(0)

def loadinBar(steps=25, delay=(0.01, 0.1), openingCredits=fileName,
              endCredits="READY!", monologue=" "):
    clear()
    for i in range(steps + 1):
        bar = "█" * i + "_" * (steps - i)
        pct = f"{(i / steps) * 100:.0f}%"
        end = f" {endCredits}" if i == steps else ""
        print(f"\r{BLD}{BLUE}messierCOBALT PRESENTS... {openingCredits} [{bar}] {pct}{end}{RST}", end="", flush=True)
        time.sleep(random.uniform(*delay))
    time.sleep(random.uniform(0.1, 0.7))
    clear()
    slowPrint(monologue)

# mainLoop
def mainLoop(firstMsg=""):
    loadinBar(monologue=firstMsg)
    while True:
        try:
            userInput = input(f"{BLD}{BLUE}~/{fileName}$ {RST}").strip()
            if not userInput:
                continue

            cmd = userInput.upper()

            if cmd in ("EXIT", "QUIT", "CLOSE"): close()
            elif cmd in ("CLEAR", "CLS", "CLEAN"): clear()
            elif cmd in ("HELP", "GUIDE", "MANUAL"): slowPrint(f"{hT}\n")
            else: return userInput
        except (KeyboardInterrupt, EOFError): close()

# TEST_CODE
if __name__ == "__main__":
    mainLoop(firstMsg=f"{BLD}==== {RED}WE LIVE AND DIE IN THE SHADOWS{RST} {BLD}===={RST}\n")