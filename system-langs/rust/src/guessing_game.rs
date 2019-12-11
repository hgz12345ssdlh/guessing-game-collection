//! Guessing game module.


use rand::Rng;
use std::io::{self, Write};


use crate::general_game::CLIGame;


/// Guessing game struct.
pub struct GuessingGame {
    magic: i32,         // Magic number to guess.
    tries: Vec<i32>,    // User tries record.
    win: bool,          // Current game status.
}

impl GuessingGame {

    /// Initializer.
    pub fn new() -> GuessingGame {
        let magic = rand::thread_rng().gen_range(1, 101);
        GuessingGame {
            magic,
            tries: vec![],
            win: false,
        }
    }

    /// Check a guess against the magic number & record this try.
    /// Returns true if correct else false.
    fn check(&mut self, guess: i32) -> bool {
        self.tries.push(guess);
        if guess == self.magic {
            println!("Correct!");
            true
        } else {
            if guess < self.magic {
                println!("Too small!");
            } else if guess > self.magic {
                println!("Too large!");
            }
            false
        }
    }

    /// Show game stats & reset game status.
    fn stats(&mut self) {
        println!("<Game stats>");
        print!("  You tried: ");
        for num in &self.tries {
            print!("{} ", num);
        }
        println!();
        println!("  In total {} tries used.", self.tries.len());

        self.tries.clear();
        self.win = false;
    }
}

impl CLIGame<i32> for GuessingGame {

    /// Play handler.
    fn play(&mut self) {
        println!("Welcome to Guanzhou's guessing game!");

        // Guessing loop.
        loop {
            print!("Enter an int ∈ [1, 100], or 'q' to quit: ");
            io::stdout().flush().unwrap();
            let mut buf = String::new();
            match io::stdin().read_line(&mut buf) {
                Ok(_) => {
                    let ipt = buf.trim();
                    if ipt.len() <= 0 {         // Empty input.
                        continue;
                    }
                    if ipt.starts_with('q') {   // Quit signal.
                        break;
                    }
                    if let Ok(guess) = ipt.parse::<i32>() {
                        match guess {
                            1..=100 => {
                                print!("  Your guess is... ");
                                if self.check(guess) {
                                    self.win = true;
                                    break;
                                }
                            },
                            _ => println!("WARN: valid input ∈ [1, 100]. Try again..."),
                        }
                    } else {
                        println!("WARN: not a valid integer. Try again...");
                    }
                },
                Err(err) => println!("Input ERROR: {}", err),
            }
        }

        // Ending message.
        match self.win {
            true  => println!("You win! Congrats ;)"),
            false => println!("Sad to see you go :("),
        }
        self.stats();
    }
}
