package cli_game


// General CLI game interface.
type CLIGame interface {
	Play(ch chan bool)
}
