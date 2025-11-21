from MorseListener import MorseListener
from MorseParser import MorseParser

class MorseToPythonString(MorseListener):
    def enterMorse_code(self, ctx:MorseParser.Morse_codeContext):
        print('"', end="")
    def exitMorse_code(self, ctx:MorseParser.Morse_codeContext):
        print('"', end="")

    def enterLetter(self, ctx:MorseParser.LetterContext):

        for child in ctx.getChildren():
            if child.symbol.type == MorseParser.A:
                print("a", end="")
            if child.symbol.type == MorseParser.B:
                print("b", end="")
            if child.symbol.type == MorseParser.C:
                print("c", end="")
            if child.symbol.type == MorseParser.D:
                print("d", end="")
            if child.symbol.type == MorseParser.E:
                print("e", end="")
            if child.symbol.type == MorseParser.F:
                print("f", end="")
            if child.symbol.type == MorseParser.G:
                print("g", end="")
            if child.symbol.type == MorseParser.H:
                print("h", end="")
            if child.symbol.type == MorseParser.I:
                print("i", end="")
            if child.symbol.type == MorseParser.J:
                print("j", end="")
            if child.symbol.type == MorseParser.K:
                print("k", end="")
            if child.symbol.type == MorseParser.L:
                print("l", end="")
            if child.symbol.type == MorseParser.M:
                print("m", end="")
            if child.symbol.type == MorseParser.N:
                print("n", end="")
            if child.symbol.type == MorseParser.O:
                print("o", end="")
            if child.symbol.type == MorseParser.P:
                print("p", end="")
            if child.symbol.type == MorseParser.Q:
                print("q", end="")
            if child.symbol.type == MorseParser.R:
                print("r", end="")
            if child.symbol.type == MorseParser.S:
                print("s", end="")
            if child.symbol.type == MorseParser.T:
                print("t", end="")
            if child.symbol.type == MorseParser.U:
                print("u", end="")
            if child.symbol.type == MorseParser.V:
                print("v", end="")
            if child.symbol.type == MorseParser.W:
                print("w", end="")
            if child.symbol.type == MorseParser.X:
                print("x", end="")  
            if child.symbol.type == MorseParser.Y:
                print("y", end="")
            if child.symbol.type == MorseParser.Z:
                print("z", end="")

    def enterDigit(self, ctx:MorseParser.LetterContext):
        for child in ctx.getChildren():
            if child.symbol.type == MorseParser.ZERO:
                print("0", end="")
            if child.symbol.type == MorseParser.ONE:
                print("1", end="")
            if child.symbol.type == MorseParser.TWO:
                print("2", end="")
            if child.symbol.type == MorseParser.THREE:
                print("3", end="")
            if child.symbol.type == MorseParser.FOUR:
                print("4", end="")
            if child.symbol.type == MorseParser.FIVE:
                print("5", end="")
            if child.symbol.type == MorseParser.SIX:
                print("6", end="")
            if child.symbol.type == MorseParser.SEVEN:
                print("7", end="")
            if child.symbol.type == MorseParser.EIGHT:
                print("8", end="")
            if child.symbol.type == MorseParser.NINE:
                print("9", end="")


