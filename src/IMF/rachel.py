import functools

__version__ = "v0.8.2"

ESC = "\033["

@functools.lru_cache
def _emma(low: int, high: int) -> list:
    """
    SHE GENERATES ANSI CODES--A LITTLE BIT FASTER!
    SHE'S THE GIRL OF ROSS AND RACHEL--EMMA GELLER GREENE!
    """
    return [f"{ESC}{i}m" for i in range(low, high)]

# reset Maine, Derry... (i mean main reset--sorry, mob mentality or whatever...)
RST, RST_FG, RST_BG = _emma(0, 1)[0], _emma(39, 40)[0], _emma(49, 50)[0]
# text styles
BOLD, DIM, ITALIC, UNDER, BLINK, RAPID_BLINK, REVERSE, HIDDEN, STRIKE = _emma(1, 10)
# other resets
RST_BOLD, RST_DIM, RST_ITALIC, RST_UNDER, RST_BLINK, RST_REVERSE, RST_HIDDEN, RST_STRIKE = _emma(21, 29)
# fg colors
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = _emma(30, 38)
# bg colors
BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE = _emma(40, 48)
# bright fg colors
BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE = _emma(90, 98)
# bright bg colors
BG_BRIGHT_BLACK, BG_BRIGHT_RED, BG_BRIGHT_GREEN, BG_BRIGHT_YELLOW, BG_BRIGHT_BLUE, BG_BRIGHT_MAGENTA, BG_BRIGHT_CYAN, BG_BRIGHT_WHITE = _emma(100, 108)
    
RAY = f"""
Just to set up ANSI codes in clean format!

{ITALIC}I went to the zoo yesterday, now I am a koala bear.{RST}
And that is how you'll use it!
"""