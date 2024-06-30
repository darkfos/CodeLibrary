"""
    Write a function which takes one parameter representing the dimensions of a checkered board.
    The board will always be square, so 5 means you will need a 5x5 board.
    The dark squares will be represented by a unicode white square, while the light squares will
    be represented by a unicode black square (the opposite colours ensure the board doesn't look
    reversed on code wars' dark background). It should return a string of the board with a space in
    between each square and taking into account new lines.

    An even number should return a board that begins with a dark square. An odd number should return
    a board that begins with a light square.   
    There should be no trailing white space at the end of each line, or new line characters at the end of the string.

    Note
    The squares are characters ■ and □ with codes \u25A0 and \u25A1.
    Do not use HTML entities for the squares (e.g. □ for white square) as the code doesn't consider it
    a valid square. A good way to check is if your solution prints a correct checker board on your local terminal.
"""

def checkered_board(n):
    #6 kyu

    res: str = ""
    is_ch: bool = False if n % 2 == 0 else True
    
    for line in range(n):
        for square in range(n):
            if is_ch and square % 2 == 0:
                res += "\u25A0 "
            elif not is_ch and square % 2 != 0:
                res += "\u25A0 "
            else:
                res += "\u25A1 "
        res = res.strip()
        res += "\n"
        
        is_ch = True if is_ch is False else False
    return res.strip()