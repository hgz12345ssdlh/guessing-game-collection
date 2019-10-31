#include <stdio.h>
#include <stdlib.h>
#include "guessing_game.h"


/** Helper functions. */
static int check(int magic, int guess);


/**
 *
 * Gameplay logic.
 * 
 */
void
gg_play() {
    printf("Welcome to Guanzhou's guessing game!\n");

    /** Generate magic number. */
    int magic = rand() % 100 + 1;

    /** Guessing loop. */
    char buf[INPUT_BUF_SIZE], ipt[INPUT_BUF_SIZE];
    int win = 0;
    while (1) {
        printf("Enter an int ∈ [1, 100], or 'q' to quit: ");
        /** Wrap a `fgets` to handle empty inputs. */
        if (fgets(buf, sizeof(buf), stdin) != NULL) {
            printf("!!N: %s\n", buf);
            sscanf(buf, "%s", ipt);
            printf("!!S: %s\n", ipt);
            if (ipt[0] == 'q')
                break;
            else if (ipt[0] < '0' || ipt[0] > '9')
                printf("WARN: not a valid integer. Try again...\n");
            else {
                int guess;
                sscanf(ipt, "%d", &guess);
                if (guess < 1 || guess > 100)
                    printf("WARN: valid input ∈ [1, 100]. Try again...\n");
                else {
                    printf("  Your guess is... ");
                    if (check(magic, guess)) {
                        win = 1;
                        break;
                    }
                }
            }
        }
    }

    /** Ending message. */
    if (win)
        printf("You win! Congrats ;)\n");
    else
        printf("Sad to see you go ;(\n");
}


/**
 *
 * Check a guess against the magic number. Returns 1 if correct else 0.
 * 
 */
static int
check(int magic, int guess) {
    if (guess == magic) {
        printf("Correct!\n");
        return 1;
    } else {
        if (guess < magic)
            printf("Too small!\n");
        else if (guess > magic)
            printf("Too large!\n");
        return 0;
    }
}
