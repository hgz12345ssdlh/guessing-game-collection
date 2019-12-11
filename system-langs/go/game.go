package main


import "cli_game"


func main() {
	guessing_game := cli_game.NewGuessingGame()
	var game cli_game.CLIGame = &guessing_game
	
	ch := make(chan bool)
	go game.Play(ch)
	
	_ = <-ch 	// Not used. Just playing with channels.
}
