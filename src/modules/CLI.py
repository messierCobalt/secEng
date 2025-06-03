import os, random, sys, time

# stringsAttatched

## formaters
RST = "\033[0m"  # reset
BLD = "\033[1m"  # bold
DIM = "\033[2m"  # dim
ITL = "\033[3m"  # italic
UND = "\033[4m"  # underLine
STR = "\033[9m"  # strikeThrough

## colorCodes
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = [f"\033[3{i}m" for i in range(8)]
BG = [f"\033[4{i}m" for i in range(8)]

## weRgonnaNeedIt
fileName = os.path.basename(sys.argv[0])

## howElseWouldUknow?
hT = f"""
{BLD}{GREEN}COMMANDS:{RST}
{GREEN}
CLEAR | CLS | CLEAN      CLEARS SCREEN
HELP | GUIDE | MANUAL    PRINTS THIS
EXIT | QUIT | CLOSE      KILLS {fileName}
""" 

# funkPunk

## theBasics

clear = lambda: os.system("cls" if os.name == "nt" else "clear")
close = lambda: sys.exit(f"GOODBYE!")

## regedit.exe

cmdRegistry = {
    ("CLEAR", "CLS", "CLEAN"): clear,
    ("HELP", "GUIDE", "MANUAL"): lambda: print(hT),
    ("EXIT", "QUIT", "CLOSE"): close,
}

def chkcmd(cmd):
    cmd = cmd.upper()
    for tuple_, func in cmdRegistry.items():
        if cmd in tuple_:
            return func
        
## theNotSoBasics

### inputThatChksCMD

def cmdInput(label):
    uI = input(f"{label} ").strip().upper() #userInput
    if not uI:
        return None
    parts = uI.split() # weRgonnaNeedIt
    if not parts:
        return None
    func = chkcmd(parts[0])
    if func:
        return func()
    else:
        slowPrint(f"{RED}cmdNOTknown -> {parts[0]}") #404
    return None

### Loading-Bar

def loadinBar(totalSteps=25, delayRange=(0.01, 0.1), openingCredits=fileName, endCredits="READY!") -> None:
    clear() # it does this undivided attention kinda thing.
    for i in range(totalSteps + 1):
        bar = "█" * i + "_" * (totalSteps - i)
        percentage = f"{(i/totalSteps)*100:.0f}%"
        line = f"\r{BLD}{BLUE}messierCOBALT PRESENTS... {openingCredits} [{bar}] {percentage}{' ' + endCredits if i == totalSteps else ''}" 
        print(line, end="", flush=True)
        time.sleep(random.uniform(*delayRange))
    time.sleep(random.uniform(0.1, 0.7))
    clear() # loadin's done...

### walkslow... Imean, printSlow

def slowPrint(text, t=0.01, T=0.05, newlineCinema=True, curtainCall_in=0.1): 
    # t = minimum time, T = maximum time
    for char in text:
        print(char, end="", flush=True)
        time.sleep(random.uniform(t, T))
    if newlineCinema: # br = breakLine
        print()
    time.sleep(curtainCall_in)

# TEST_CODE 

def main():
    loadinBar()
    for _ in range(27):
        cmdInput(f"{BLUE}testin'$")
        slowPrint(f"{BLUE}WE LIVE AND DIE IN THE SHADOWS.")
    slowPrint(f"{BLUE}GOODBYE!")

if __name__ == "__main__":
    main()