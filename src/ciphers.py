from modules.CLI import * # like that?
import random
import string

# v0.1

"""
THE CIPHER LIST:
1. CAESAR CIPHER     - SHIFTS LETTERS BY SET NUMBER
2. ATBASH CIPHER     - MIRRORS ALPHABETS
3. RANDOM SUBST.     - SHUFFLES ALPHABETS
4. MORSE CODE        - LETTERS BECOMES DOTS AND DASHES
"""

def caesar(text:str, shift:int, encrypt:bool = True) -> str:
    """
    SHE IS THE MOST INSECURE
    I MEAN, UNSECURE CIPHER!!!
    """
    output = ""
    for c in text:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            offset = ord(c) - ord(base)
            if encrypt:
                offset = (offset + shift) % 26
            else:
                offset = (offset - shift) % 26
            output += chr(ord(base) + offset)
        else:
            output += c
    return output

def atBash(text:str) -> str:
    """
    SHE MIRRORS EVERYTHING...
    THE VIGENERE CIPHER...
    """
    output = ""
    for c in text:
        if c.isupper():
            output += chr(ord('Z') - (ord(c) - ord('A')))
        elif c.islower():
            output += chr(ord('z') - (ord(c) - ord('a')))
        else:
            output += c
    return output

def randSubs(text:str, encrypt:bool = True, key:None = None) -> tuple[str, list]: 
    """
    LOVE ENTROPY?
    """
    chars = list(" " + string.ascii_letters + string.digits + string.punctuation)
    if key is None:
        shuffled = chars.copy()
        random.shuffle(shuffled)
    else:
        shuffled = key

    output = ""
    for c in text:
        if c not in chars:
            output += c
            continue
        if encrypt:
            output += shuffled[chars.index(c)]
        else:
            output += chars[shuffled.index(c)]
    return output, shuffled 

def morse(text:str, encrypt:bool = True) -> str:
    """
    SHE ONCE WAS, morse.py!
    """
    MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',    'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..',  'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--',  'N': '-.',   'O': '---', 'P': '.--.', 'Q': '--.-','R': '.-.',
        'S': '...', 'T': '-',    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--','Z': '--..', '0': '-----','1': '.----','2': '..---','3': '...--',
        '4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.',
        ' ': '/'
    }
    REV = {v: k for k, v in MORSE.items()}

    if encrypt:
        return ' '.join(MORSE.get(c.upper(), '') for c in text)
    else:
        words = text.split(" / ")
        return ' '.join(''.join(REV.get(l, '?') for l in w.split()) for w in words)

def main() -> None:
    """
    SHE RUNS
    YOU CAN TEST
    
    IF SHE DOESN'T--
    TELL ME!!!
    """
    while True:
        userInput = int(input(f"{BRIGHT_BLUE}~/{fileName}$ {RST}").strip().upper())
        for key, value in regedit.items():
            if userInput in key:
                value()
                break
        else:
            print(f"""{GREEN}
- CAESAR CIPHER
- ATBASH CIPHER
- RANDOM SUBSTITUTION
- MORSE CODE{RST}
""")
            cipher = input(f"{BLACK}which cipher? {RST}").strip().upper()
            if cipher not in {"CAESAR", "CAESAR CIPHER", "ATBASH", "ATBASH CIPHER", "RAND", "RANDOM", "RANDOM SUBSTITUTION", "MORSE", "MORSE CODE"}:
                print(f"{RED}E:{RST} CIPHER NOT KNOWN")
                continue

            mode = input(f"{BLUE}ENCRYPT? (Y/n) {RST}").strip().lower()
            encrypt = mode in {"y", "yes", "encrypt"}

            if cipher in {"CAESAR", "CAESAR CIPHER"}:
                while True:
                    try:
                        shift = int(input(f"{YELLOW}SHIFT (int.)? {RST}").strip())
                        break
                    except ValueError:
                        print(f"{RED}INVALID SHIFT.{RST}")
                        continue
                output = caesar(userInput, shift, encrypt)

            elif cipher in {"ATBASH", "ATBASH CIPHER"}:
                output = atBash(userInput)

            elif cipher in {"RAND", "RANDOM SUBSTITUTION"}:
                output = randSubs(userInput, encrypt)

            elif cipher in {"MORSE", "MORSE CODE"}:
                output = morse(userInput, encrypt)

            print(f"{CYAN}> {output}{RST}\n")

if __name__ == "__main__": 
    main()

"""
FUN FACT:

__name__ IS A PRE DEFINED VARIABLE.
IT'S SET "__main__" IF THE CODE IS
RUN DIRECTLY AND NOT IMPORTED TO
ANOTHER FILE.

YOU MIGHT WONDER WHAT VALUE IS IF 
THE PROGRAM IS IMPORTED TO A MODULE?
WELL
GO AND TEST THAT YOUSELF
I AM NOT YOUR MOM.

AND YES, THERE ARE OTHER "SNEAKY",
"HIDDEN", "PRE-DEFINED" STUFF... IT'S
PYTHON NOT C... PYTHON'S LIKE WINDOWS
AND C LIKE LINUX OR BRAVE AND FIREFOX.
"""
