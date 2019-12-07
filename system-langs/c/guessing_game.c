#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include "guessing_game.h"


/** Helper functions. */
static int check(int magic, int guess);
static void stats(int *tries, int len);


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
    int tries[RECORD_LENGTH], record_idx = 0;
    while (1) {
        printf("Enter an int ∈ [1, 100], or 'q' to quit: ");
        /** Wrap a `fgets` to handle empty inputs. */
        if (fgets(buf, sizeof(buf), stdin) != NULL) {
            sscanf(buf, "%s\n", ipt);
            if (strlen(ipt) <= 0)   /** Empty input. */
                continue;
            if (ipt[0] == 'q')      /** Quit signal. */
                break;
            if ((ipt[0] < '0' || ipt[0] > '9') && ipt[0] != '-')
                printf("WARN: not a valid integer. Try again...\n");
            else {
                int guess;
                assert(sscanf(ipt, "%d", &guess) == 1);
                if (guess < 1 || guess > 100)
                    printf("WARN: valid input ∈ [1, 100]. Try again...\n");
                else {
                    tries[record_idx++] = guess;
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
        printf("Sad to see you go :(\n");
    stats(tries, record_idx);
}


/**
 *
 * Check a guess against the magic number.
 * Returns 1 if correct else 0.
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


/**
 *
 * Show game stats
 * 
 */
static void
stats(int *tries, int len) {
    printf("<Game stats>\n  You tried: ");
    size_t i = 0;
    for (i = 0; i < len; ++i)
        printf("%d ", tries[i]);
    printf("\n  In total %d tries used.\n", len);
}
