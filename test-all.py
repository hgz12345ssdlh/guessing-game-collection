# Run all tests in batch.

# Usage: python3 test-all.py


import os


#
# All games' locations & run commands.
#
# Entry format:
#
#   "language": {
#       "path":     "folder_path",
#       "make":     "make_cmd",     # Optional.
#       "cmd":      "run_cmd",
#       "clean":    "clean_cmd",    # Optional.
#   },
#

games = {

    "Python3": {
        "path":     "scripting-langs/python",
        "make":     None,
        "cmd":      "python3 game.py",
        "clean":    None,
    },

    "Julia": {
        "path":     "scripting-langs/julia",
        "make":     None,
        "cmd":      "julia game.jl",
        "clean":    None,
    },

    "C": {
        "path":     "system-langs/c",
        "make":     "make -s",
        "cmd":      "./game",
        "clean":    "make -s clean",
    },

    "C++": {
        "path":     "system-langs/cpp",
        "make":     "make -s",
        "cmd":      "./game 2>&1",
        "clean":    "make -s clean",
    },

    "Rust": {
        "path":     "system-langs/rust",
        "make":     "cargo -q build",
        "cmd":      "cargo -q run",
        "clean":    "cargo -q clean",
    },

    "Go": {
        "path":     "system-langs/go",
        "make":     "export GOPATH=$( pwd ); go build -o game",
        "cmd":      "./game",
        "clean":    "go clean; unset GOPATH"
    }
}


#
# Run all tests.
#

class cd(object):
    """
    Context manager for changing the current working directory.
    """
    def __init__(self, new_path):
        self.new_path = os.path.expanduser(new_path)

    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.old_path)

class Ecolors(object):
    BOLD = '\033[1m'
    ENDC = '\033[0m'

for lang in games:
    print(Ecolors.BOLD+"Testing game: "+Ecolors.ENDC+lang)

    assert os.path.isdir(games[lang]["path"])
    os.system("cp -r tester/* %s/" % (games[lang]["path"],))

    with cd(games[lang]["path"]):
        if os.path.isdir("outputs/"):
            os.system("rm -rf outputs/")

        if games[lang]["make"] is not None:
            os.system(games[lang]["make"])

        os.system("./feed-tests.sh \"%s\"" % (games[lang]["cmd"],))
        os.system("python3 check-outs.py")

        os.system("rm -rf inputs/ check-outs.py feed-tests.sh")

        if games[lang]["clean"] is not None:
            os.system(games[lang]["clean"])

print(Ecolors.BOLD+"NOTE: "+Ecolors.ENDC+"Check \'<target_path>/outputs\' "
                                         "for test outputs.")
