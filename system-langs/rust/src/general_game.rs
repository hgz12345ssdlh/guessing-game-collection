//! General game skeleton.


/// What a CLI game should implement.
pub trait CLIGame<T: std::fmt::Debug> {

    /// Base play handler.
    fn play(&mut self) {
        println!("Base player handler called!");
    }
}
