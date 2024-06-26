"""
    There is a robot starting at the position (0, 0), the origin, on a 2D plane. Given a sequence of its moves,
    judge if this robot ends up at (0, 0) after it completes its moves.
    You are given a string moves that represents the move sequence of the robot where moves[i] represents its ith move.
    Valid moves are 'R' (right), 'L' (left), 'U' (up), and 'D' (down).

    Return true if the robot returns to the origin after it finishes all of its moves, or false otherwise.
    Note: The way that the robot is "facing" is irrelevant. 'R' will always make the robot move to the right once,
    'L' will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
"""


class Solution:

    def __init__(self):
        self.place: int = 0
        self.wl: int = 0
        self.up_down: int = 0

    def judgeCircle(self, moves: str) -> bool:
        #Easy

        for action in moves.upper():
            match action:
                case "U":
                    self.up_down += 1
                case "D":
                    self.up_down -= 1
                case "L":
                    self.wl -= 1
                case "R":
                    self.wl += 1
        return self.up_down == self.place and self.wl == self.place
