mod guessing_game;
use guessing_game::GuessingGame;


fn main() {
    let mut game = GuessingGame::new();
    game.play();
}
