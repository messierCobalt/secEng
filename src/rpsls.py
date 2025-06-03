from modules.CLI import *
import random, sys

"""
THERE ARE WAY TOO MANY REFERENCES
FROM MISSION: IMPOSSIBLE MOVIES,
AND THE BIG BANG THEORY... 

TRY TO FIND 'EM
"""

RULES = {
    "ROCK": ["SCISSORS", "LIZARD"],
    "PAPER": ["ROCK", "SPOCK"],
    "SCISSORS": ["PAPER", "LIZARD"],
    "LIZARD": ["SPOCK", "PAPER"],
    "SPOCK": ["SCISSORS", "ROCK"]
}

SHELDON = f"""
{BLUE}SCISSORS{RST} cuts {WHITE}PAPER{RST}
{WHITE}PAPER{RST} covers {BLACK}ROCK{RST}
{BLACK}ROCK{RST} crushes {GREEN}LIZARD{RST}
{GREEN}LIZARD{RST} poisons {YELLOW}SPOCK{RST}
{YELLOW}SPOCK{RST} smashes {BLUE}SCISSORS{RST}
{BLUE}SCISSORS{RST} decapitates {GREEN}LIZARD{RST}
{GREEN}LIZARD{RST} eats {WHITE}PAPER{RST}
{WHITE}PAPER{RST} disproves {YELLOW}SPOCK{RST}
{YELLOW}SPOCK{RST} vaporizes {BLACK}ROCK{RST}

and as it always has

{BLACK}ROCK{RST} crushes {BLUE}SCISSORS{RST}
"""

OPTIONS = list(RULES)

def getENTITYchoice():
    return random.choice(OPTIONS)

def getETHANchoice():
    while True:
        ethanInput = input(f"{RED}ETHAN: ").strip().upper()
        if ethanInput in {"ABORT", "EXIT", "QUIT"}:
            slowPrint(f"{RED}GOOD LUCK!")
            sys.exit(0)
        elif ethanInput in {"CLEAR", "CLS"}:
            clear()
        elif ethanInput in {"SHELDON", "MANUAL"}:
            slowPrint(SHELDON)
        elif ethanInput == "HELP":
            slowPrint(hT)
        elif ethanInput in {"PODKOVA", "POISON", "PILL"}:
            break
        elif ethanInput in OPTIONS:
            return ethanInput
        else:
            slowPrint(f"{RED}MY {UND}EARPIECE{RST} {RED}IS FAILING...")

def determineWinner(ETHAN, ENTITY):
    if ETHAN == ENTITY:
        return "TIE"
    if ENTITY in RULES[ETHAN]:
        return "ETHAN"
    return "ENTITY"

def displayResult(ENTITY, winner):
    slowPrint(f"{BLUE}ENTITY: {ENTITY}{RST}")
    slowPrint(f"\n{"IT'S A TIE!" if winner == "TIE" else f"{RED if winner == 'ETHAN' else BLUE}{winner} WINS!{RST}"}\n")

def main():
    clear()
    ETHAN_score = 0
    ENTITY_score = 0

    slowPrint(f"""
{BLD}==== {BLACK}ROCK{RST} {WHITE}PAPER{RST} {BLUE}SCISSORS{RST} {GREEN}LIZARD{RST} {YELLOW}SPOCK{RST} {BLD}===={RST}

THE {UND}ANTI-GOD{RST}.
AN ENEMY THAT'S {UND}EVERYWHERE{RST} AND {UND}NOWHERE{RST}.
A {UND}SELF-AWARE{RST}, {UND}SELF-LEARNING{RST}, {UND}TRUTH EATING{RST}, {UND}DIGITAL PARASITE{RST}.
""")

    while True:
        ETHAN_choice = getETHANchoice()
        if ETHAN_choice is None:
            break

        ENTITY_choice = getENTITYchoice()
        winner = determineWinner(ETHAN_choice, ENTITY_choice)

        displayResult(ENTITY_choice, winner)

        if winner == "ETHAN":
            ETHAN_score += 1
        elif winner == "ENTITY":
            ENTITY_score += 1

    slowPrint(f"""
{BLD}==== {YELLOW}YOUR FINAL RECKONING{RST} {BLD}===={RST}

{ITL}EVERYTHING YOU WERE, EVERYTHING YOU'VE DONE, HAS COME TO THIS...{RST}

{RED}ETHAN{RST}  = {ETHAN_score}
{BLUE}ENTITY{RST} = {ENTITY_score}
{RED if ETHAN_score > ENTITY_score else BLUE if ENTITY_score > ETHAN_score else YELLOW}
{"ETHAN WINS!" if ETHAN_score > ENTITY_score else "ENTITY WINS!" if ENTITY_score > ETHAN_score else "IT'S A TIE!"}{RST}
""")

if __name__ == "__main__":
    main()