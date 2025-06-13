import os 
import random
import sys
import time
try:
    from ANSI import *
    from cases import *
except ImportError:
    from .ANSI import *
    from .cases import *
if os.name != "nt":
    import readline # for linux CLI purposes (don't mind her)

# v0.5

"""
WE LIVE AND DIE IN THE SHADOWS
FOR THOSE WE HOLD CLOSE
AND FOR THOSE WE NEVER MEET
"""

fileName = os.path.basename(sys.argv[0])

HELP = f"""{BRIGHT_GREEN}
CLEAR | CLS ----------- CLEARS TERMINAL SCREEN!
ABORT | EXIT | QUIT --- KILLS {fileName}!
HELP ------------------ PRINTS THIS!
""" # it'll be reset-ed if concatenated in the main file... 

registry = {} # she's the command registry

def regedit(cmds: tuple, func: callable) -> None:
    """
    SHE ADDS CALLABLE FUNCTIONS TO COMMAND TUPLES
    """
    if func and cmds:
        registry[cmds] = func

def monica() -> None:
    """
    SHE LOVES CLEANING... THE TERMINAL SCREEN
    """
    os.system("cls" if os.name == "nt" else "clear")

def eject(msg: str = "GOODBYE!") -> None:
    """
    THE PRESIDENT HAS INITATED GHOST... I MEAN, TERMINATION PROTOCOL...
    THE ENTIRE IMF... I MEAN, TERMINAL IS DISAVOWED... I MEAN TERMINATED!!!
    """
    sys.exit(f"{BRIGHT_RED}{msg.upper()}{RST}\n")


def penny(steps: int = 35, delay: tuple = (0.005, 0.05),
              openingCredits: str = fileName, endCredits: str = "READY!") -> None:
    """
    SHE'S SHORT, SWEET, AND A LITTLE STUPID...
    SHE'S PENNY FROM TBBT...
    BUT SHE'S JUST A LOADING BAR!!!
    """
    monica() # monica monica have a happy hanukkah
    print(f"{BLUE}messierCOBALT {ITALIC}presents...{RST} {BLUE}{openingCredits}{RST}\n")

    for i in range(steps + 1):
        bar = f"{BLUE}{'█' * i}{RST}{DIM}{'_' * (steps - i)}{RST}"
        pct = f"{(i / steps) * 100:>3.0f}%"
        tail = f"{GREEN} {endCredits}" if i == steps else ""
        print(f"\r[{bar}] {pct}{tail}{RST}", end="", flush=True)
        time.sleep(random.uniform(*delay))

    time.sleep(random.uniform(0.1, 0.4))
    monica() # can i clean up?

def main():
    try:
        penny()
        print(f"{BRIGHT_BLUE}TESTING, ATTENTION PLEASE!!!")
    except Exception:
        print(f"{BRIGHT_RED}E:{RST} {Exception}")
    
if __name__ == "__main__":
    main()

"""
YOU KNOW? EXTREME GRAVITY BENDS SPACE-TIME MESH.
WHY DON'T I STRETCH THIS??
HOW ABOUT I TELL YOU A STORY???

SO, THERE WAS THIS GUY--MARKUS JONES, HE DOESN'T REMEMBER HIS CHILDHOOD.
AND, ONE DAY, HE WAS AT WORK, HIS WIFE--CYNTHIA WAS COMING BACK HOME (FROM
SHOPPING FOR THEIR SONS BIRTHDAY. WITH HIS SON--PETER.) AND THEN A HOMELESS
FELLA MUGGED THEN KILLED HER INFRONT OF PETER!

AFTER THAT EVENING, MARKUS STARTED DRINKING--AGAIN, NEGLECTING PETER. THE
FOSTER PEOPLE TOOK PETER FAR AWAY...

~ PS: THIS IS JUST STARTING CRUMS OF EARLY DRAFTS OF MY SHORT STORY, 
TITLED: BOLT MAN... I KNOW IT'S SILLY BUT CUT ME SOME SLACK, I HAD
THIS IDEA WHEN I WAS 13 OR 14...
"""
