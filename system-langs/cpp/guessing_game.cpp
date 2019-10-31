#include <iostream>
#include <string>
#include <cstdlib>
#include <boost/algorithm/string/trim.hpp>
#include "guessing_game.hpp"


/**
 *
 * Game constructor.
 * 
 */
GuessingGame::GuessingGame() {
    magic = rand() % 100 + 1;
}


/**
 *
 * Check a guess against the magic number. Returns true if correct else false.
 * 
 */
bool
GuessingGame::check(int guess) {
    if (guess == magic) {
        std::cout << "Correct!" << std::endl;
        return true;
    } else {
        if (guess < magic)
            std::cout << "Too small!" << std::endl;
        else if (guess > magic)
            std::cout << "Too large!" << std::endl;
        return false;
    }
}


/**
 *
 * Gameplay logic.
 * 
 */
void
GuessingGame::play() {
    std::cout << "Welcome to Guanzhou's guessing game!" << std::endl;

    /** Guessing loop. */
    std::string buf;
    bool win = false;
    while (true) {
        std::cout << "Enter an int ∈ [1, 100], or 'q' to quit: ";
        std::getline(std::cin, buf);
        boost::trim(buf);
        if (buf[0] == 'q')
            break;
        else if (buf[0] < '0' || buf[0] > '9')
            std::cerr << "WARN: not a valid integer. Try again..."
                      << std::endl;
        else {
            int guess = std::stoi(buf);
            if (guess < 1 || guess > 100)
                std::cerr << "WARN: valid input ∈ [1, 100]. Try again..."
                          << std::endl;
            else {
                std::cout << "  Your guess is... ";
                if (check(guess)) {
                    win = true;
                    break;
                }
            }
        }
    }

    /** Ending message. */
    if (win)
        std::cout << "You win! Congrats ;)" << std::endl;
    else
        std::cout << "Sad to see you go ;(" << std::endl;
}
