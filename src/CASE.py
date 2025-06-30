from IMF.hunt import HELP, limbo, turtle, tears
from IMF.rachel import *
import functools
import random

__version__ = 'v0.4.1'

T2L = lambda txt: txt.casefold().replace('-', ' ').replace('_', ' ').split() if txt else []
flatcase = lambda txt: ''.join(char.casefold() for char in txt if (char.isalnum() and not char.isspace())) if txt else ''
wSep = lambda W, sep: sep.join(W)

def alt(txt: str, nW: str = '', up: bool = True) -> str:
    for c in txt:
        nW += (c.upper() if up else c.lower()) if c.isalpha() else c
        up = up ^ c.isalpha()
    return nW

@functools.lru_cache(maxsize=256)
def switch(style: str, txt: str = '') -> str:
    '''
    Everything resides here!
    '''
    try:
        s = flatcase(style) # s = style
        W = T2L(txt) # W, w = words, word

        if 'up' in s and 'f' not in s:
            return txt.upper()
        
        if 'low' in s:
            return txt.casefold()
        
        if 'tit' in s or s == 't': # woah
            return txt.title()
        
        if 'cap' in s:
            return txt.capitalize()
        
        if 'swap' in s or s == 'swp':
            return txt.swapcase()
        
        if 'alt' in s and 'c' not in s:
            return alt(txt)
        
        if 'cam' in s or s == 'c':
            if not W:
                return ''
            return W[0].casefold() + ''.join(w.capitalize() for w in W[1:])
        
        if 'pas' in s or s == 'p':
            return ''.join(w.capitalize() for w in W)
        
        if any(c in s for c in ['snake', 'scream', 'constant', 's', 'ss', 'con']):
            scream = 'ss' in s or 'con' in s or 'scream' in s
            return '_'.join(W).upper() if scream else '_'.join(W).casefold()
        
        if any(c in s for c in ['ke', 'par']):
            return wSep(W, '-')
        
        if 'dot' in s or s == 'd':
            return wSep(W, '.')
        
        if 'path' in s or s == 'pth':
            return wSep(W, '/')
        
        if 'tr' in s or 'head' in s:
            return '-'.join(w.capitalize() for w in W)
        
        if 'rand' in s or s == 'r':
            return ''.join(random.choice([c.upper(), c.casefold()]) if c.isalpha() else c for c in txt)
        
        if 'cul' in s or any(c in s for c in ['ac', 'cu', 'altc', 'alternatec', 'alternatingc']):
            isAlt = 'a' in s
            return ''.join(w.upper() if (i % 2 == 0) == isAlt else w.casefold() for i, w in enumerate(W))
        
        if any(c in s for c in ['f', 'upf', 'upperf', 'uf']):
            flat = flatcase(txt)
            return flat.upper() if 'up' in s else flat
        
        return txt
    
    except Exception as e:
        tears('007', e)

HELP += f'''
{BOLD}CASE conv. cmds:{RST}{BRIGHT_GREEN}
low [txt] --- lower case
up [txt] ---- UPPER CASE
t [txt] ----- Title Case
cap [txt] --- Capitalized case
swp [txt] --- Swap Case -> sWAP cASE
a [txt] ----- aLtErNaTiNg CaSe
c [txt] ----- camelCase
p [txt] ----- PascalCase
s [txt] ----- snake_case
ss [txt] ---- CONSTANT_SCREAMING_CASE
k [txt] ----- kebab-case
tr [txt] ---- Train-Case
r [txt] ----- rAnDOM cAse
cul [txt] --- cullenCASE (inventedHIM)
ac [txt] ---- ALTcullenCASE (INVENTEDhimTOO)
d [txt] ----- dot.case
pth [txt] --- path/case
f [txt] ----- flatcase
uf [txt] ---- UPPERFLATCASE{RST}

{BOLD}Notes:{RST} {BRIGHT_GREEN}
Yes, you can use similar commands.
This is just the tip of the iceberg.
{RST}'''

def main() -> None:
    limbo(lambda cmd, *parts: turtle(switch(cmd, txt = ' '.join(parts) if parts else '')), 
          HLP= HELP, 
          v = __version__,
          shell = False)

if __name__ == '__main__':
    main()

'''
Ever used Flow Launcher?
Ever added that plugin that does what this does? 

Anyways, I made this to showcase cullenCASE & ALTcullenCASE

He maybe called CASE but he's more of TARS!
'''