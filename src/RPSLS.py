from IMF.shell import * # get used to it
import random

# v0.4

"""
ROCK U PAPER U SCISSORS U LIZARD U SPOCK (U = UNION... | IN .py TERMS) 
"""

LAWS = {
    "ROCK": ["SCISSORS", "LIZARD"],
    "PAPER": ["ROCK", "SPOCK"],
    "SCISSORS": ["PAPER", "LIZARD"],
    "LIZARD": ["SPOCK", "PAPER"],
    "SPOCK": ["SCISSORS", "ROCK"]
}

HELP += f"""{BOLD}IN GAME CMD:{RST}{BRIGHT_GREEN}
PODKOVA | PILL ----- CONCLUDES GAME!
{RST}
{BOLD}SHELDON:{RST}
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
""" # told ya!

ARSENAL = list(LAWS)

regedit("HELP", lambda: print(HELP))

def letHuntChoose() -> str:
    """
    BECOME HUNT... 
    PICK A WEAPON...
    FIGHT THE ENTITY...
    """
    while True:
        huntChoice = input(f"{RED}ETHAN: {RST}").strip().upper()
        for key, value in registry.items():
            if huntChoice in key:
                value()
                break
        else:
            if huntChoice in ("PODKOVA", "PILL", "CONCLUDE"):
                break
            elif huntChoice in ARSENAL:
                return huntChoice
            else:
                print(f"{BRIGHT_RED}E:{RST} UNKNOWN ERROR OCCURED")

def main() -> None:
    """
    "EVERYTHING... HAS LED TO THIS!" 
    - TOM CRUISE
    
    HE SAID THAT IN SUPER BOWL 59
    """
    try:
        HUNT = 0
        ENTITY = 0

        penny()
        print(f"{BLACK}ROCK{RST} {WHITE}PAPER{RST} {YELLOW}SCISSORS{RST} {GREEN}LIZARD{RST} {BLUE}SPOCK{RST}\n")
        
        while True:
            huntCHOICE = letHuntChoose()
            if huntCHOICE is None:
                break

            entityCHOICE = random.choice(ARSENAL)
            winner = "TIE" if huntCHOICE == entityCHOICE else "ETHAN" if entityCHOICE in LAWS[huntCHOICE] else "ENTITY"

            print(f"{BLUE}ENTITY: {entityCHOICE}{RST}")

            time.sleep(1) # not a (long pause)!

            COLOR = RED if winner == "ETHAN" else BLUE
            print(f"\nTIE!\n" if winner == "TIE" else f"\n{COLOR}{winner} WINS!{RST}\n")

            if winner == "ETHAN":
                HUNT += 1
            elif winner == "ENTITY":
                ENTITY += 1
        finalReckoning = [
            f"{YELLOW}THIS IS IT... YOUR FINAL RECKONING...{RST}",
            f"{ITALIC}EVERYTHING YOU WERE, EVERYTHING YOU'VE DONE, HAS COME TO THIS...{RST}\n"
            f"{ITALIC}{RED}ETHAN{RST}  = {HUNT}{RST}",
            f"{ITALIC}{BLUE}ENTITY{RST} = {ENTITY}",
            f"{RED if HUNT > ENTITY else BLUE if ENTITY > HUNT else YELLOW}",
            f"{'ETHAN WINS!' if HUNT > ENTITY else 'ENTITY WINS!' if ENTITY > HUNT else 'TIE!'}{RST}"
        ]
        for fR in finalReckoning:
            time.sleep(random.uniform(0.8, 2.8))
            print(fR)

    except Exception:
        print(f"{BRIGHT_RED}E:{RST} {Exception}")

if __name__ == "__main__":
    main()

"""
                                                            CUT TO:
Bi-atomic cutscene with blue background for around 4 
seconds.
                                                            FADE IN TO:

INT. SHELDON AND LEONARD'S APARTMENT - DAY

SHELDON is pissed at LESLIE because she tampered 
with his whiteboard. Apparently, Leslie fixed a 
problem he was having with his equations. But Sheldon
being Sheldon, he doesn't like that.

                        SHELDON
            Yeah, hold on... 

                        LESLIE
                (silently)
            What?

                        SHELDON
            Who told you you can touch my
            board?

                        LESLIE
            No one.

                        SHELDON
            I don't come in your house and
            touch your board.

                       LESLIE
            There are no incorrect equations on my
            board.

                        SHELDON
            Oh that is so... so...
                (long pause)

                        LESLIE
            I'm sorry... I gotta run. If you come
            up with an adjective. Text me.

Leslie leaves the apartment.

                        SHELDON
            Inconsiderate, that's the adjective,
            inconsiderate.

Sheldon pulls out his phone. And started texting her.
"""