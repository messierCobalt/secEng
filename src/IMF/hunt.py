import os 
import random
import sys
import time
try: from rachel import *
except ImportError: from .rachel import *
if os.name != "nt": import readline # for unix CLI purposes

__version__ = "v0.2.9"

fileName = os.path.basename(sys.argv[0])

CMDS = {}  # she's the command registry
HELP = f"""
{BOLD}Basic cmds:{RST}{BRIGHT_GREEN}
clear | cls ----- clears terminal screen!
exit | quit ----- kills {fileName}!
help | manual --- prints this!
{RST}
""" # your helper... your light...

def bob(cmds: tuple[str], func: callable):
    """
    Registers cmds to a function and updates HELP.
    """
    for cmd in cmds:
        CMDS[cmd.lower()] = func

monica = lambda: os.system("cls" if os.name == "nt" else "clear") # She loves to clean the terminal screen!
terminate = lambda msg = "Goodbye!" : sys.exit(f"{BRIGHT_RED}{msg}{RST}") # hasta la vista, baby!    

def penny(steps: int = 28, delay: tuple = (0.01, 0.1), title: str = fileName,) -> None:
    """
    She needs time to process. She's a loadin' bar!
    """
    monica() # monica monica have a happy hanukkah
    print(f"{BLUE}messierCobalt {ITALIC}PRESENTS...{RST} {BLUE}{title}{RST}\n") # feels like a MISSION: IMPOSSIBLE intro (kinda)

    for i in range(steps + 1):
        bar = f"{BLUE}{'█' * i}{RST}{DIM}{'_' * (steps - i)}{RST}"
        pct = f"{(i / steps) * 100:>3.0f}%"
        print(f"\r[{bar}] {pct}{RST}", end="", flush=True)
        time.sleep(random.uniform(*delay))

    time.sleep(random.uniform(0.05, 0.5))
    monica() # can I clean?

def turtle(txt: str, end: str = "", fast: bool = False) -> None:
    """
    slowPrint
    fastTurtle
    Note: you should eat slow.
    """
    brkDwn = 0.010 if fast else 0.020
    for char in txt:
        print(char, end = end, flush = True)
        time.sleep(brkDwn)
    # curtain call comin' up
    time.sleep(0.25)
    print()

def limbo(plants: callable, inputMsg: str = f"{BRIGHT_BLUE}~/{fileName}{RST}$ ", v: str = __version__, HLP: str = HELP) -> None:
    """
    Playdead will get you stuck in a LIMBO
    Just kiddin'... nope!
    It's a mainLoop() function.

    importantNOTE: When you pass plants callable... don't use the () unless you are using lambda 
    """
    bob(("help", "manual", "guide", "light", "ray"), lambda: turtle(HLP, fast = True))
    bob(("--version", "version", "ver", "-v"), lambda: turtle(v))
    penny() # what?
    while True:
        try:
            userInput = input(inputMsg).strip()
            if userInput:
                uI_parts = userInput.split()
                cmd = uI_parts[0].lower()

                if len(uI_parts) < 2:
                    if cmd in CMDS:
                        CMDS[cmd]()
                else:
                    plants(cmd, uI_parts)

        except Exception as e:
            print(f"{BRIGHT_RED}err:{RST} {e}")

bob(("clear", "clean", "cls", "monica", "maid"), monica)
bob(("abort", "close", "exit", "eject", "terminate", "quit"), terminate)

# this is how you'll call him... and yes.
# yes... I know I could have added them
# in the dict. but I wanted to demonstrate
# make sure you are using uppercase for cmds.

RAY = """
This module was crafted to be the backbone of every CLI program in this repo.
Ethan Hunt (Team leader) will be your point man as usual!

Oath: We live and die in the shadows
      For those we hold close
      And for those we never meet
"""
