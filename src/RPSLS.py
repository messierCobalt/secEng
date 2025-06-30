from IMF.hunt import HELP, CMDS, penny, turtle, tears, limbo
from IMF.rachel import *
import random
import time

__version__ = 'v0.2.2'

LAWS = {
    'ROCK': ['SCISSORS', 'LIZARD'],
    'PAPER': ['ROCK', 'SPOCK'],
    'SCISSORS': ['PAPER', 'LIZARD'],
    'LIZARD': ['SPOCK', 'PAPER'],
    'SPOCK': ['SCISSORS', 'ROCK']
}

HELP += f'''{BOLD}in-game cmds:{RST}{BRIGHT_GREEN}
podkova | pill --- concludes the game!{RST}

{BOLD}Sheldon:{RST}
{YELLOW}scissors{RST} cuts {WHITE}paper{RST}
{WHITE}paper{RST} covers {BLACK}rock{RST}
{BLACK}rock{RST} crushes {GREEN}lizard{RST}
{GREEN}lizard{RST} poisons {BLUE}spock{RST}
{BLUE}spock{RST} smashes {YELLOW}scissors{RST}
{YELLOW}scissors{RST} decapitates {GREEN}lizard{RST}
{GREEN}lizard{RST} eats {WHITE}paper{RST}
{WHITE}paper{RST} disproves {BLUE}spock{RST}
{BLUE}spock{RST} vaporizes {BLACK}rock{RST}

{ITALIC}and as it always has{RST}

{BLACK}rock{RST} crushes {YELLOW}scissors{RST}
'''

ARSENAL = list(LAWS.keys())

def take() -> str:
    '''
    take take take... what you need... but don't leave me...
    '''
    while True:
        p1Choice = input(f'{RED}ethan: {RST}').strip().upper()
        
        for cmds, fn in CMDS.items():
            if p1Choice.lower() in cmds:
                fn()
                continue
        
        if p1Choice in ('podkova', 'pill', 'conclude'):
            return None
        
        elif p1Choice in ARSENAL:
            return p1Choice
        
        else:
            tears("003")

def water() -> None:
    p1 = 0
    p2 = 0

    penny()
    turtle(f'{BLACK}rock{RST} {WHITE}paper{RST} {YELLOW}scissors{RST} {GREEN}lizard{RST} {BLUE}spock{RST}\n')
    
    while True:
        p1Choice = take()
        if p1Choice is None:
            break

        p2Choice = random.choice(ARSENAL)

        if p1Choice == p2Choice:
            winner = 'tie'
        elif p2Choice in LAWS[p1Choice]:
            winner = 'p1'
        else:
            winner = 'p2'

        turtle(f'{BLUE}p2: {p2Choice.lower()}{RST}')

        time.sleep(1) # not a (long pause)!

        if winner == 'tie':
            turtle(f'\ntie!\n')
        else:
            COLOR = RED if winner == 'p1' else BLUE
            turtle(f'\n{COLOR}{winner} wins!{RST}\n')

        if winner == 'p1':
            p1 += 1
        elif winner == 'p2':
            p2 += 1

    finalReckoning = [
        f'{YELLOW}This is it... Your Final Reckoning...{RST}',
        f'{ITALIC}Everything you were, everything you\'ve done, has come to this...{RST}\n',
        f'{ITALIC}{RED}ethan{RST}  = {p1}{RST}',
        f'{ITALIC}{BLUE}p2{RST} = {p2}{RST}',
    ]
    
    finalReckoning.append(f'{RED}ethan wins!{RST}' if p1 > p2 else f'{BLUE}p2 wins!{RST}' if p2 > p1 else f'{YELLOW}tie!{RST}')

    for reckoning in finalReckoning:
        time.sleep(random.uniform(0.8, 2.8))
        turtle(reckoning)

def main() -> None:
    '''
    "Everything... has led to this" - Tom Cruise @ Superbowl 59
    '''
    limbo(plants=water, v=__version__, HLP=HELP, shell=False)

if __name__ == '__main__':
    main()

'''
rock U paper U scissors U lizard U spock (U = UNION... | IN .py TERMS)

=================================================================================

                            THE HAMBURGER POSTULATE
                                    (S1E5)
                                                                          CUT TO:
Bi-atomic cutscene with blue background for around 4 
seconds.
                                                                      FADE IN TO:
INT. SHELDON AND LEONARD'S APARTMENT - DAY

SHELDON is pissed at LESLIE because she tampered with his whiteboard. 
Apparently, Leslie fixed a problem he was having with his equations. But
Sheldon being Sheldon, he doesn't like that.

                            SHELDON
                Yeah, hold on... 

                            LESLIE
                        (silently)
                What?

                            SHELDON
                Who told you you can touch my board?

                            LESLIE
                No one.

                            SHELDON
                I don't come in your house and touch 
                your board.

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

=================================================================================
'''