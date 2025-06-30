from shlex import split
import os 
import functools
import random
import sys
import time
# yeah... they are a little weird down there!!! 
try: from rachel import *
except ImportError: from .rachel import *
if os.name != 'nt': import readline

__version__ = 'v0.3.2'
fileName = os.path.basename(sys.argv[0])
CMDS = {}

HELP = f'''
{BOLD}Basic cmds:{RST}{BRIGHT_GREEN}
clear | cls ----- clears terminal screen!
exit | quit ----- kills {fileName}!
help | manual --- prints this!
{RST}'''

@functools.lru_cache(maxsize=128)
def bob(cmds: tuple[str], func: callable) -> None:
    '''
    bob the COMMANDS builder...
    '''
    for cmd in cmds:
        CMDS[cmd.lower()] = func

monica = lambda: os.system('cls' if os.name == 'nt' else 'clear') # I am Monica Gelleeer
terminate = lambda msg = 'Goodbye!': (turtle(f'{BRIGHT_RED}{msg}{RST}'), sys.exit()) # hasta lavista baby

def penny(steps: int = 28, delay: tuple[int] = (0.001, 0.1), title: str = fileName,) -> None:
    '''
    She's Penelope Hofstadter
    She's needs time to process
    '''
    monica()
    print(f'{BLUE}messierCobalt {ITALIC}PRESENTS...{RST} {BLUE}{title}{RST}\n') # kinda like Mission: Impossible Opening Credits!
    for i in range(steps + 1):
        bar = f'{BLUE}{"█" * i}{RST}{DIM}{"=" * (steps - i)}{RST}'
        pct = f'{(i / steps) * 100:>3.0f}%'
        print(f'\r[{bar}] {pct}{RST}', end='', flush=True)
        time.sleep(random.uniform(*delay))
    time.sleep(random.uniform(0.05, 0.5))
    monica()

def turtle(txt: str, end: str = '', ender: str = '\n', fast: bool = False) -> None:
    '''
    slowPrint()
    slowPrint(faster)
    '''
    brkDwn = 0.001 if fast else 0.005
    for char in txt:
        print(char, end = end, flush = True)
        time.sleep(brkDwn)
    time.sleep(0.2)
    print('', end = ender)

def limbo(plants: callable = lambda: print('', end = ''),
          inputMsg: str = f'{BRIGHT_BLUE}~/{fileName}{RST}$ ',
          v: str = __version__,
          HLP: str = HELP,
          shell: bool = True,
          usage: str = '')-> None:
    '''
    PLAYDEAD will get you stuck in a limbo
    It's the main loop for everything CLI!
    '''
    bob(('help', 'manual', 'guide', 'light', 'ray'), lambda: turtle(HLP, fast = True))
    bob(('--version', 'version', 'ver', '-v'), lambda: turtle(v))
    penny()
    
    while True:
        try:
            userInput = input(inputMsg).strip()
            if not userInput:
                continue
            uI_parts = split(userInput) if shell else userInput.split()
            if not uI_parts:
                continue
            if len(uI_parts) < 1:
                turtle(usage)
                return
            cmd = uI_parts[0].lower()
            if cmd in CMDS:
                CMDS[cmd]()
            else:
                plants(cmd, *uI_parts[1:]) 
        except KeyboardInterrupt:
            tears("011", close = True)
        except EOFError:
            tears("012", close = True)
        except Exception as e:
            tears('007', e)

def tears(code, e = '', close = False) -> None:
    '''
    I cry... out the error...
    '''
    err = str(e).split() if str(e) else []
    
    cryBaby = {
        '001': '',
        '002': 'notEnoughInputsWasPassed',
        '003': 'unknownError',
        '004': 'fileAccessDenied',
        '005': 'it\'sTheSyntax',
        '006': 'unknownCmd',
        '007': f'{err[0].casefold() + "".join(w.capitalize() for w in err[1:])}' if err else 'wildCard', # The Name's Bond... James Bond!!!
        '011': 'keyboardInterruptionDetected',
        '012': 'endO\'File'
    }
    msg = cryBaby.get(code, 'unknownErrorCode')
    print(f'{BRIGHT_RED}err:{RST} {msg}')
    if close:
        sys.exit(0)

bob(('clear', 'clean', 'cls', 'monica', 'maid'), monica)
bob(('abort', 'close', 'exit', 'eject', 'terminate', 'quit'), terminate)

#                  ^
#                  |
# this is how you'll call him... and yes.
# yes... I know I could have added them
# in the dict. but I wanted to demonstrate
# make sure you are using uppercase for cmds.

'''
This module was crafted to be the backbone of every CLI program in this repo.
Ethan Hunt (Team leader) will be your point man as usual!
Oath: We live and die in the shadows
    For those we hold close
    And for those we never meet
'''