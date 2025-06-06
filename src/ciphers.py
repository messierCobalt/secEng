from modules.CLI import *
import random
import string

"""
THE CIPHER LIST:
1. CAESAR CIPHER     - SHIFTS LETTERS BY SET NUMBER
2. ATBASH CIPHER     - MIRRORS ALPHABETS
3. RANDOM SUBST.     - SHUFFLES ALPHABETS
4. MORSE CODE        - LETTERS BECOMES DOTS AND DASHES
"""

def caesar(text, shift, encrypt=True):
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

def atBash(text):
    output = ""
    for c in text:
        if c.isupper():
            output += chr(ord('Z') - (ord(c) - ord('A')))
        elif c.islower():
            output += chr(ord('z') - (ord(c) - ord('a')))
        else:
            output += c
    return output

def randSubs(text, encrypt=True):
    chars = list(" " + string.ascii_letters + string.digits + string.punctuation)
    shuffled = chars.copy()
    random.shuffle(shuffled)

    output = ""
    for c in text:
        if c not in chars:
            output += c
            continue
        if encrypt:
            output += shuffled[chars.index(c)]
        else:
            output += chars[shuffled.index(c)]
    return output

def morse(text, encrypt=True):
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

def main():
    while True:
        userInput = input(f"{BLUE}~/text$ {RST}").strip()
        if not userInput:
            continue
        cmd = userInput.lower()
        if cmd in {"exit", "quit"}:
            close()
        elif cmd in {"clear", "cls"}:
            clear()
        elif cmd in {"help"}:
            slowPrint(hT)
        else:
            slowPrint(f"""{GREEN}
- CAESAR CIPHER
- ATBASH CIPHER
- RANDOM SUBSTITUTION
- MORSE CODE{RST}
""")
            cipher = input(f"{BLACK}~/cipher? {RST}").strip().upper()
            if cipher not in {"CAESAR", "CAESAR CIPHER", "ATBASH", "ATBASH CIPHER", "RAND", "RANDOM", "RANDOM SUBSTITUTION", "MORSE", "MORSE CODE"}:
                slowPrint(f"{RED}cipherNotKnown{RST}")
                continue

            mode = input(f"{BLUE}ENCRYPT? (Y/n) {RST}").strip().lower()
            encrypt = mode in {"y", "yes", "encrypt"}

            if cipher in {"CAESAR", "CAESAR CIPHER"}:
                while True:
                    try:
                        shift = int(input(f"{YELLOW}SHIFT (int.)? {RST}").strip())
                        break
                    except ValueError:
                        slowPrint(f"{RED}INVALID SHIFT.{RST}")
                        continue
                output = caesar(userInput, shift, encrypt)

            elif cipher in {"ATBASH", "ATBASH CIPHER"}:
                output = atBash(userInput)

            elif cipher in {"RAND", "RANDOM SUBSTITUTION"}:
                output = randSubs(userInput, encrypt)

            elif cipher in {"MORSE", "MORSE CODE"}:
                output = morse(userInput, encrypt)

            slowPrint(f"{CYAN}> {output}{RST}\n")

if __name__ == "__main__":
    main()