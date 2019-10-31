/**
 *
 * Class of a guessing game.
 * 
 */
class GuessingGame {
private:
    int magic;  // Magic number to guess.
    bool check(int guess);

public:
    GuessingGame();
    void play();
};
