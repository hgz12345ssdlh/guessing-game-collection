#!/bin/bash

# Feed tests to a guessing game program and save the outputs in
# `outputs/` dir for subsequent checking.

# Usage: ./feed-test.sh "<game-command>"


if [ "$#" -ne 1 ]; then
    echo "USAGE: ./feed-test.sh \"<game-command>\""
    exit 1
fi
GAME_CMD=$1

if [ -d "outputs/" ]; then
    echo "ERROR: \'outputs/\' directory already exists."
    exit 1
fi
mkdir outputs/


#
# Normal plays.
#

# Sequential play.
${GAME_CMD} < inputs/seq-play.inp > outputs/win-seq-play.out

# Inversed sequential play.
${GAME_CMD} < inputs/inv-play.inp > outputs/win-inv-play.out

# Crossed play.
${GAME_CMD} < inputs/crs-play.inp > outputs/win-crs-play.out


#
# Side conditions.
#

# Quit signal.
${GAME_CMD} <<'EOF' > outputs/quit-signal.out
q
EOF

# Invalid input.
${GAME_CMD} <<'EOF' > outputs/invalid-input.out
elf
@#$
q
EOF

# Out-of-range.
${GAME_CMD} <<'EOF' > outputs/out-of-range.out
7923
-141
q
EOF

# Whitespaces.
${GAME_CMD} <<'EOF' > outputs/whitespaces.out
    50  
q
EOF

# Empty input.
${GAME_CMD} <<'EOF' > outputs/empty-input.out

q
EOF

# Start with `q`.
${GAME_CMD} <<'EOF' > outputs/start-with-q.out
qewq
EOF
