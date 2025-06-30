from IMF.hunt import limbo, HELP, turtle, tears
from IMF.rachel import *
import random
import string

__version__ = 'v0.2.4'

chars = list(' ' + string.ascii_letters + string.digits + string.punctuation)
    
shuffled = chars.copy()
random.shuffle(shuffled)
    

def caesar(text: str, shift: int, bury: bool = True) -> str:
    '''
    He's the most insecure, I mean unsecure cipher!
    '''
    output = ''
    for c in text:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            offset = ord(c) - ord(base)
            offset = (offset + shift) % 26 if bury else (offset - shift) % 26
            output += chr(ord(base) + offset)
        else:
            output += c
    return output

def rand(text: str, bury: bool = True) -> tuple[str, list]: 
    '''
    You like Entropy? ... It's got 'em!
    '''

    output = ''
    for c in text:
        if c not in chars:
            output += c
        else:
            try:
                if bury:
                    output += shuffled[chars.index(c)]
                else:
                    output += chars[shuffled.index(c)]
            except (ValueError, IndexError):
                output += c
    return output

def morse(text: str, bury: bool = True) -> str:
    '''
    Brand did you know? Once upon a time... it was just morse.py!
    '''
    MORSE = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
        'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
        'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
        'y': '-.--', 'z': '--..', '0': '-----','1': '.----','2': '..---',
        '3': '...--','4': '....-','5': '.....','6': '-....','7': '--...',
        '8': '---..','9': '----.',' ': '/'
    }
    REV = {value: key for key, value in MORSE.items()}

    if bury:
        return ' '.join(MORSE.get(c.lower(), c) for c in text if c.lower() in MORSE or not c.isalnum())
    else:
        if '/' in text: 
            words = text.split(' / ')
            return ' '.join(''.join(REV.get(ch, '?') for ch in word.split()) for word in words)
        else:  
            return ''.join(REV.get(ch, '?') for ch in text.split())

HELP += f'''
{BOLD}Ciphers cmds:{RST}{BRIGHT_GREEN}
cae 'txt' -e | -d SHIFT --- caesar cipher
morse 'txt' -e | -d ------- morse code 
rand 'txt' -e | -d -------- random substitution
{RST}'''

def water(cmd: str, *uI_parts) -> None:
    if len(uI_parts) < 1:
        turtle('<cmd> \'txt\' [-e | -d] [SHIFT (if caesar)]')
        return

    txt = uI_parts[0]
    rest = list(uI_parts[1:]) if len(uI_parts) > 1 else []

    bury = '-e' in rest or '--encrypt' in rest
    unbury = '-d' in rest or '--decrypt' in rest

    if not (bury or unbury):
        turtle('specify -e | -d')
        return

    operation = bury  # True 4 encryptin'... False 4 decryptin'

    if cmd in {'cae', 'caesar'}:
        shift = None
        for r in rest:
            if r.lstrip('-').isdigit():
                shift = int(r)
                break
        if shift is None:
            turtle('gimme SHIFT: int (for carsar)')
            return
        result = caesar(txt, shift, operation)
        turtle(result)
        return

    elif cmd in {'rand', 'entropy'}:
        result = rand(txt, None)
        turtle(result)
        return

    elif cmd in {'morse', 'dot', 'dash'}:
        result = morse(txt, operation)
        turtle(result)
        return

    else:
        tears("006")

def main() -> None:
    limbo(plants=water, v=__version__, HLP=HELP)

if __name__ == '__main__':
    main()

'''
You are in my Crypt!

Care for a Fun Fact?

'__name__' is a predefined variable... defaultly, it's set to '__main__' if
the code is run directly and not imported to another file

Are you wondering what it's set to, if the program is imported? Well... go
and test it yourself. I ain't your Mom.

And yes, there are other 'sneaky', 'hidden', 'pre-defined' stuff.
'''