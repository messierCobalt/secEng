from modules.CLI import * # get used to it
import random

# v0.4

"""
SHE REFERENCES...
FROM MISSION: IMPOSSIBLE MOVIES, AND THE BIG BANG THEORY...
BUT IT ALL STARTED WITH THE BIG BANG!!! (LITERALLY)

TRY TO FIND 'EM! JUST DON'T DISSECT HER MERCILESSLY
I'LL TELL YOU WHAT TO LOOK OUT FOR DOWN BELOW!
"""

LAWS = {
    "ROCK": ["SCISSORS", "LIZARD"],
    "PAPER": ["ROCK", "SPOCK"],
    "SCISSORS": ["PAPER", "LIZARD"],
    "LIZARD": ["SPOCK", "PAPER"],
    "SPOCK": ["SCISSORS", "ROCK"]
}

SHELDON = f"""
{YELLOW}SCISSORS{RST} cuts {WHITE}PAPER{RST}
{WHITE}PAPER{RST} covers {BLACK}ROCK{RST}
{BLACK}ROCK{RST} crushes {GREEN}LIZARD{RST}
{GREEN}LIZARD{RST} poisons {BLUE}SPOCK{RST}
{BLUE}SPOCK{RST} smashes {YELLOW}SCISSORS{RST}
{YELLOW}SCISSORS{RST} decapitates {GREEN}LIZARD{RST}
{GREEN}LIZARD{RST} eats {WHITE}PAPER{RST}
{WHITE}PAPER{RST} disproves {BLUE}SPOCK{RST}
{BLUE}SPOCK{RST} vaporizes {BLACK}ROCK{RST}

{ITALIC}and as it always has{RST}

{BLACK}ROCK{RST} crushes {YELLOW}SCISSORS{RST}
""" # don't make him repeat...

HELP += f"""
IN GAME CMDS:
SHELDON | MANUAL --- SUMMONS SHELDON LEE COOPER!
PODKOVA | PILL ----- CONCLUDES GAME!
{RST}\n""" # told ya!

ARSENAL = list(LAWS)

regedit(("HELP"), lambda: print(HELP))
regedit(("SHELDON", "MANUAL"), lambda: print(SHELDON))

def HUNTsChoice() -> str:
    """
    BECOME HUNT... 
    PICK A WEAPON...
    FIGHT THE ENTITY...
    """
    while True:
        ethanInput = input(f"{RED}ETHAN: {RST}").strip().upper()
        for key, value in registry.items():
            if ethanInput in key:
                value()
                break
        else:
            if ethanInput in ("PODKOVA", "PILL", "CONCLUDE"):
                break
            elif ethanInput in ARSENAL:
                return ethanInput
            else:
                print(f"{BRIGHT_RED}E:{RST} UNKNOWN ERROR OCCURED")

def main() -> None:
    """
    "EVERYTHING... HAS LED TO THIS!" 
    - TOM CRUISE
    
    HE SAID THAT IN SUPER BOWL 59
    """
    try:
        ETHANscore = 0
        ENTITYscore = 0

        penny()
        print(f"{BLACK}ROCK{RST} {WHITE}PAPER{RST} {YELLOW}SCISSORS{RST} {GREEN}LIZARD{RST} {BLUE}SPOCK{RST}\n")
        
        while True:
            ETHANchoice = HUNTsChoice()
            if ETHANchoice is None:
                break

            ENTITYchoice = random.choice(ARSENAL)
            winner = "TIE" if ETHANchoice == ENTITYchoice else "ETHAN" if ENTITYchoice in LAWS[ETHANchoice] else "ENTITY"

            print(f"{BLUE}ENTITY: {ENTITYchoice}{RST}")

            time.sleep(1) # not a (long pause)!

            COLOR = RED if winner == "ETHAN" else BLUE
            print(f"\nTIE!\n" if winner == "TIE" else f"\n{COLOR}{winner} WINS!{RST}\n")

            if winner == "ETHAN":
                ETHANscore += 1
            elif winner == "ENTITY":
                ENTITYscore += 1
        finalReckoning = [
            f"{YELLOW}THIS IS IT... YOUR FINAL RECKONING...{RST}",
            f"{ITALIC}EVERYTHING YOU WERE, EVERYTHING YOU'VE DONE, HAS COME TO THIS...{RST}\n"
            f"{ITALIC}{RED}ETHAN{RST}  = {ETHANscore}{RST}",
            f"{BLUE}ENTITY{RST} = {ENTITYscore}",
            f"{RED if ETHANscore > ENTITYscore else BLUE if ENTITYscore > ETHANscore else YELLOW}",
            f"{'ETHAN WINS!' if ETHANscore > ENTITYscore else 'ENTITY WINS!' if ENTITYscore > ETHANscore else 'TIE!'}{RST}"
        ]
        for fR in finalReckoning:
            time.sleep(random.uniform(0.8, 2.8))
            print(fR)

    except Exception:
        print(f"{BRIGHT_RED}E:{RST} {Exception}")

if __name__ == "__main__":
    main()

"""
YOU WON'T GET THEM—THE REF.s UNLESS YOU HAVE WATCHED:
- ALL 12 SEASONS OF TBBT—WATCH THEM... THEY'RE GOLD (NOT BETTER THAN FRIENDS... 
...AND IF YOU ARE LIKE PENNY/ME... YOU'LL MISS SCI-JOKES! :guilty-face-emoji)
- MISSION: IMPOSSIBLE 96
- MISSION: IMPOSSIBLE III (YEAH... SKIP THE 2ND ONE... NO ONE CARES... IT'S WATCHABLE THO)
- MISSION: IMPOSSIBLE - GHOST PROTOCOL (I KNOW... BUT STILL... WATCH IT)
- MISSION: IMPOSSIBLE - ROGUE NATION (SAME)
- MISSION: IMPOSSIBLE - FALLOUT (EVERYONE LOVES IT)
- MISSION: IMPOSSIBLE - DEAD RECKONING (MY 2ND FAV MOVIE OF ALL TIME... NOTHING CAN BEAT INTERSTELLAR!)
- MISSION: IMPOSSIBLE - THE FINAL RECKONING (ME AFTER READING EARLY REVIEWS, "THIS CAN'T ALL BE TRUE"...
ALSO ME AFTER WATCHING THE MOVIE, "EVERY WORD")
"""