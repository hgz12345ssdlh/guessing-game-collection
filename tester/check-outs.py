# Check the test outputs under `outputs/` folder.

# Usage: python3 check-outs.py


import os


#
# Check output files existence.
#

output_list = [
    "win-seq-play.out",
    "win-inv-play.out",
    "win-crs-play.out",
    "quit-signal.out",
    "invalid-input.out",
    "out-of-range.out",
    "whitespaces.out",
    "empty-input.out",
    "start-with-q.out"
]

if not os.path.isdir("outputs/"):
    print("  Incomplete outputs!")
    exit(1)

for fout in output_list:
    if not os.path.isfile("outputs/"+fout):
        print("  Incomplete outputs!")
        exit(1)


results = dict()


#
# Normal plays.
#

# Sequential play.
with open("outputs/win-seq-play.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        answer = 1
        line = f.readline().strip()
        while line == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                      "  Your guess is... Too small!":
            answer += 1
            line = f.readline().strip()
        assert line == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                       "  Your guess is... Correct!"
        assert f.readline().strip() == "You win! Congrats ;)"
        assert f.readline().strip() == "<Game stats>"
        line = f.readline().strip()
        assert line.startswith("You tried: ")
        tries = list(map(lambda t: int(t), line[10:].strip().split(' ')))
        assert tries == [t for t in range(1, answer+1)]
        assert f.readline().strip() == "In total %d tries used." % (answer,)
        results["seq-play"] = True
    except:
        results["seq-play"] = False

# Inversed sequential play.
with open("outputs/win-inv-play.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        answer = 100
        line = f.readline().strip()
        while line == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                      "  Your guess is... Too large!":
            answer -= 1
            line = f.readline().strip()
        assert line == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                       "  Your guess is... Correct!"
        assert f.readline().strip() == "You win! Congrats ;)"
        assert f.readline().strip() == "<Game stats>"
        line = f.readline().strip()
        assert line.startswith("You tried: ")
        tries = list(map(lambda t: int(t), line[10:].strip().split(' ')))
        assert tries == [t for t in range(100, answer-1, -1)]
        assert f.readline().strip() == "In total %d tries used." % (101-answer,)
        results["inv-play"] = True
    except:
        results["inv-play"] = False

# Crossed play.
with open("outputs/win-crs-play.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        count, small_round = 0, True
        tries_ref = []
        line = f.readline().strip()
        while line.startswith("Enter an int ∈ [1, 100], or 'q' to quit: "):
            count += 1
            tries_ref.append((count+1)//2 if small_round else 101-(count+1)//2)
            if line[40:].strip() == "Your guess is... Correct!":
                break
            elif small_round:
                assert line[40:].strip() == "Your guess is... Too small!"
            else:
                assert line[40:].strip() == "Your guess is... Too large!"
            line = f.readline().strip()
            small_round = not small_round
        assert f.readline().strip() == "You win! Congrats ;)"
        assert f.readline().strip() == "<Game stats>"
        line = f.readline().strip()
        assert line.startswith("You tried: ")
        tries = list(map(lambda t: int(t), line[10:].strip().split(' ')))
        assert tries == tries_ref
        assert f.readline().strip() == "In total %d tries used." % (count,)
        results["crs-play"] = True
    except:
        results["crs-play"] = False


#
# Side conditions.
#

# Quit signal.
with open("outputs/quit-signal.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        assert f.readline().strip() == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                                       "Sad to see you go :("
        results["quit-signal"] = True
    except:
        results["quit-signal"] = False

# Invalid input.
with open("outputs/invalid-input.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        assert f.readline().strip() == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                                       "WARN: not a valid integer. Try again..."
        assert f.readline().strip() == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                                       "WARN: not a valid integer. Try again..."
        results["invalid-input"] = True
    except:
        results["invalid-input"] = False

# Out-of-range.
with open("outputs/out-of-range.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        assert f.readline().strip() == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                                       "WARN: valid input ∈ [1, 100]. Try again..."
        assert f.readline().strip() == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                                       "WARN: valid input ∈ [1, 100]. Try again..."
        results["out-of-range"] = True
    except:
        results["out-of-range"] = False

# Whitespaces.
with open("outputs/whitespaces.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        line = f.readline().strip()
        assert line.startswith("Enter an int ∈ [1, 100], or 'q' to quit: ")
        assert line[40:].strip().startswith("Your guess is... Too")
        results["whitespaces"] = True
    except:
        results["whitespaces"] = False

# Empty input.
with open("outputs/empty-input.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        line = f.readline().strip()
        assert line.startswith("Enter an int ∈ [1, 100], or 'q' to quit: ")
        assert line[40:].strip().startswith("Enter an int ∈ [1, 100]")
        results["empty-input"] = True
    except:
        results["empty-input"] = False

# Start with `q`.
with open("outputs/start-with-q.out", 'r') as f:
    try:
        assert f.readline().strip() == "Welcome to Guanzhou's guessing game!"
        assert f.readline().strip() == "Enter an int ∈ [1, 100], or 'q' to quit: " \
                                       "Sad to see you go :("
        results["start-with-q"] = True
    except:
        results["start-with-q"] = False


#
# Display test results.
#

class Ecolors(object):
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

print("  Test results...")
passed = 0
for test in results:
    print("    %-15s" % (test,), end='')
    if results[test]:
        print(Ecolors.GREEN+"OK"+Ecolors.ENDC)
        passed += 1
    else:
        print(Ecolors.RED+"FAIL"+Ecolors.ENDC)
print("  In total %d / %d passed." % (passed, len(results)))
