mod general_game;
mod guessing_game;
use general_game::CLIGame;
use guessing_game::GuessingGame;


fn main() {
    let mut game = GuessingGame::new();
    game.play();
}
