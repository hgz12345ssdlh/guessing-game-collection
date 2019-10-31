#include <vector>


/**
 *
 * Class of a guessing game.
 * 
 */
class GuessingGame {
private:
    int magic;                  // Magic number to guess.
    std::vector<int> tries;     // User tries record.
    bool win;                   // Current game status.

    bool check(int guess);
    void stats();

public:
    GuessingGame();
    void play();
};
