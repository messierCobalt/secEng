import os 
import random
import sys
import time
try: from rachel import *
except ImportError: from .rachel import *
if os.name != "nt": import readline # for unix CLI purposes (don't mind her)

# v0.5.1

"""
WE LIVE AND DIE IN THE SHADOWS
FOR THOSE WE HOLD CLOSE
AND FOR THOSE WE NEVER MEET
"""

fileName = os.path.basename(sys.argv[0])

HELP = f"""
{BOLD}BASIC CMDS:{RST}{BRIGHT_GREEN}
CLEAR | CLS ----------- CLEARS TERMINAL SCREEN!
ABORT | EXIT | QUIT --- KILLS {fileName}!
HELP ------------------ PRINTS THIS!
{RST}
"""

registry = {} # she's the command registry

def regedit(cmd: str, func: callable) -> None:
    """
    SHE ADDS CALLABLE FUNCTIONS TO REGISTRY WITH THEIR CMDS
    I KNOW YOU HAVE HER NUMBER BUT ONLY CALL HER IN UPPERCASE...
    """
    if func and cmd:
        registry[cmd.upper()] = func

def monica() -> None:
    """
    SHE LOVES CLEANING... THE TERMINAL SCREEN...
    AND EVERYTHING ELSE... BUT NOT HERE!!!
    """
    os.system("cls" if os.name == "nt" else "clear")

def terminate(msg: str = "GOODBYE!") -> None:
    """
    THE PRESIDENT HAS INITATED GHOST... I MEAN, TERMINATION PROTOCOL...
    THE ENTIRE IMF... I MEAN, TERMINAL IS DISAVOWED... I MEAN TERMINATED!!!
    """
    sys.exit(f"{BRIGHT_RED}{msg}{RST}")


def penny(steps: int = 28, delay: tuple = (0.01, 0.1), tilte: str = fileName,) -> None:
    """
    SHE'S SHORT, SWEET, AND A LITTLE STUPID...
    TELL HER ANYTHING CRYPTIC (OR RUN THIS CODE)... 
    SHE'LL NEED SOME TIME TO PROCESS...
    SHE'S JUST A LOADING BAR!!!
    """
    monica() # monica monica have a happy hanukkah
    print(f"{BLUE}messierCobalt {ITALIC}PRESENTS...{RST} {BLUE}{tilte}{RST}\n")

    for i in range(steps + 1):
        bar = f"{BLUE}{'█' * i}{RST}{DIM}{'_' * (steps - i)}{RST}"
        pct = f"{(i / steps) * 100:>3.0f}%"
        print(f"\r[{bar}] {pct}{RST}", end="", flush=True)
        time.sleep(random.uniform(*delay))

    time.sleep(random.uniform(0.05, 0.5))
    monica() # can i clean?

def limbo(plants: callable, inputMsg: str = f"{BRIGHT_BLUE}~/{fileName}{RST}$ ") -> None:
    """
    SHE IS STUCK IN A LIMBO
    """
    penny() # what?
    while True:
        try:
            userInput = input(inputMsg).strip()
            if userInput:
                uI_parts = userInput.split()
                cmd = uI_parts[0].upper()

                if len(uI_parts) < 2:
                    if cmd in registry:
                        registry[cmd]()
                else:
                    plants(cmd, uI_parts)

        except Exception as e:
            print(f"E: {e}")

regedit("CLEAR", monica)
regedit("CLEAN", monica)
regedit("CLS", monica)
regedit("MONICA", monica)
regedit("MAID", monica)
regedit("ABORT", terminate)
regedit("CLOSE", terminate)
regedit("EXIT", terminate)
regedit("EJECT", terminate)
regedit("TERMINATE", terminate)
regedit("QUIT", terminate)

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
