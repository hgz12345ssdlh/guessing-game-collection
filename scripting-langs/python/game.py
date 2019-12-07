# Guessing game in Python 3.


import random


class GuessingGame:
    """
    Guessing game structure.
    """

    def __init__(self):
        self.magic = random.randint(1, 100)
        self.tries = []
        self.win = False

    def check(self, guess):
        """
        Check a guess, shows if it is too large / small, or correct, and
        record that try.
        Returns true if correct, otherwise false.
        """
        self.tries.append(guess)
        if guess == self.magic:
            print("Correct!")
            return True
        else:
            if guess < self.magic:
                print("Too small!")
            elif guess > self.magic:
                print("Too large!")
            return False

    def stats(self):
        """
        Show game stats & reset game status.
        """
        print("<Game stats>")
        print("  You tried: ", end='')
        for num in self.tries:
            print(num, end=' ')
        print()
        print("  In total " + str(len(self.tries)) + " tries used.")

        del self.tries[:]
        self.win = False

    def play(self):
        """
        Plays an guessing interactively in the shell.
        """
        print("Welcome to Guanzhou's guessing game!")

        while True:
            ipt = input("Enter an int ∈ [1, 100], or 'q' to quit: ").strip()
            if len(ipt) == 0:   # Empty input.
                continue
            if ipt[0] == 'q':   # Quit signal.
                break
            try:
                guess = int(ipt)
                if not 1 <= guess <= 100:
                    print("WARN: valid input ∈ [1, 100]. Try again...")
                else:
                    print("  Your guess is... ", end='')
                    if self.check(guess):
                        self.win = True
                        break
            except ValueError:
                print("WARN: not a valid integer. Try again...")

        if self.win:
            print("You win! Congrats ;)")
        else:
            print("Sad to see you go :(")
        self.stats()


if __name__ == "__main__":
    game = GuessingGame()
    game.play()
