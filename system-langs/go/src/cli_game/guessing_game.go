package cli_game


import (
	"bufio"
	"os"
	"fmt"
	"math/rand"
	"strings"
	"strconv"
)


const RECORD_LENGTH = 100 	// Max # tries that can record.


// Guessing game struct of int.
type GuessingGame struct {
	magic int
	tries []int
	win bool
}


//
// Public API.
//

// Guessing game initializer.
func NewGuessingGame() GuessingGame {
	return GuessingGame{
		magic: rand.Intn(100)+1,
		tries: make([]int, 0, RECORD_LENGTH),
		win: false,
	}
}

// Play handler exploiting goroutine's concurrency features.
// Invoke by kicking off a `go xxx.Play(ch)` goroutine.
func (game *GuessingGame) Play(ch chan bool) {
	guessing_game := NewGuessingGame()
	guessing_game.play()
	ch <- guessing_game.win
}


//
// Private methods.
//

// Play handler single-threaded.
func (game *GuessingGame) play() {
	fmt.Println("Welcome to Guanzhou's guessing game!")

	// Guessing loop.
	reader := bufio.NewReader(os.Stdin)
	for {
		fmt.Printf("Enter an int ∈ [1, 100], or 'q' to quit: ")
		ipt, _ := reader.ReadString('\n')
		ipt = strings.TrimSpace(ipt)
		if len(ipt) <= 0 { 	// Empty input
			continue
		}
		if ipt[0] == 'q' {	// Quit signal.
			break
		}
		guess, err := strconv.Atoi(ipt)
		if err != nil {
			fmt.Println("WARN: not a valid integer. Try again...")
		} else if 1 <= guess && guess <= 100 {
			fmt.Printf("  Your guess is... ")
			if game.check(guess) {
				game.win = true
				break
			}
		} else {
			fmt.Println("WARN: valid input ∈ [1, 100]. Try again...")
		}
	}

	// Ending message.
	defer game.stats() 	// Just playing with defer.
	switch game.win {
	case true:
		fmt.Println("You win! Congrats ;)")
	case false:
		fmt.Println("Sad to see you go :(")
	}
}

// Check a guess against the magic number & record this try.
// Returns true if correct else false.
func (game *GuessingGame) check(guess int) bool {
	game.tries = append(game.tries, guess)
	if guess == game.magic {
		fmt.Println("Correct!")
		return true
	} else {
		if guess < game.magic {
			fmt.Println("Too small!")
		} else if guess > game.magic {
			fmt.Println("Too large!")
		}
		return false
	}
}

// Show game stats & reset game status.
func (game *GuessingGame) stats() {
	fmt.Println("<Game stats>")
	fmt.Printf("  You tried: ")
	for _, num := range game.tries {
		fmt.Printf("%d ", num)
	}
	fmt.Printf("\n  In total %d tries used.\n", len(game.tries))

	game.tries = game.tries[:0]
	game.win = false
}
