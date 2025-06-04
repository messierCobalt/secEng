from modules.CLI import *

MORSE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',  ' ': '/'
}

REV_MORSE_DICT = {v: k for k, v in MORSE_DICT.items()}

def ToMorse(text):
    text = text.upper()
    return ' '.join(MORSE_DICT.get(c, '') for c in text)

def FromMorse(morse):
    words = morse.split(" / ")
    out = []
    for w in words:
        out.append(''.join(REV_MORSE_DICT.get(letter, '?') for letter in w.split()))
    return ' '.join(out)

def main():
    userInput = mainLoop(firstMsg=f"{BLD}==== {BLUE}MORSE CODE TRANSLATOR{RST} {BLD}===={RST}\n")
    if all(ch in ".-/ " for ch in userInput):
        slowPrint(f"{CYAN}DECODED:{RST} {FromMorse(userInput)}", t=0.02, T=0.2)
    else:
        slowPrint(f"{CYAN}ENCODED:{RST} {ToMorse(userInput)}", t=0.02, T=0.2)

if __name__ == "__main__":
    main()