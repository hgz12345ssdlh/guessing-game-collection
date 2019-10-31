# Guessing game in Python 3.


import random


class GuessingGame:
    """
    Guessing game structure.
    """

    def __init__(self):
        self.magic = random.randint(1, 100)

    def check(self, guess):
        """
        Check a guess, shows if it is too large / small, or correct.
        Returns true if correct, otherwise false.
        """
        if guess == self.magic:
            print("Correct!")
            return True
        else:
            if guess < self.magic:
                print("Too small!")
            elif guess > self.magic:
                print("Too large!")
            return False

    def play(self):
        """
        Plays an guessing interactively in the shell.
        """
        print("Welcome to Guanzhou's guessing game!")

        win = False
        while True:
            ipt = input("Enter an int ∈ [1, 100], or 'q' to quit: ").strip()
            if ipt == 'q':
                break
            else:
                try:
                    guess = int(ipt)
                    if not 1 <= guess <= 100:
                        print("WARN: valid input ∈ [1, 100]. Try again...")
                    else:
                        print("  You guess is... ", end='')
                        if self.check(guess):
                            win = True
                            break
                except ValueError:
                    print("WARN: not a valid integer. Try again...")

        if win:
            print("You win! Congrats ;)")
        else:
            print("Sad to see you go :(")


if __name__ == "__main__":
    game = GuessingGame()
    game.play()
