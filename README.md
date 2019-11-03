# Guessing Game Collection

![Languages](https://img.shields.io/github/languages/count/hgz12345ssdlh/guessing-game-collection)
![Code-size](https://img.shields.io/github/languages/code-size/hgz12345ssdlh/guessing-game-collection?color=purple)

A collection of the number guessing game in different languages - weekly update ;)

Aimed to help me explore & touch new languages & technologies. Writing a simple game definitely cannot exploit the full advantages / disadvantages of a language, but should be a good start towards learning its pipeline of development and basic syntax.


## Progress List

System programming languages:

- [x] C
- [x] C++
- [x] Rust
- [ ] Go

Common scripting languages:

- [x] Python
- [ ] Ruby
- [x] Julia
- [ ] R

Java & its variants:

- [ ] Java
- [ ] Kotlin
- [ ] Dart

Web scripting languages (with sample page in HTML/CSS):

- [ ] JavaScript
- [ ] TypeScript
- [ ] PHP

Other app development:

- [ ] Swift
- [ ] Objective-C
- [ ] C#

Lisp & its dialects:

- [ ] Common Lisp
- [ ] Scala
- [ ] Scheme
- [ ] Clojure

Erlang & its variants:

- [ ] Erlang
- [ ] Elixir

Assembly:

- [ ] MIPS
- [ ] RISC-V
- [ ] x86
- [ ] ARM
- [ ] WebAssembly


## Expected Behavior

**Normal behavior** is a guessing game where the player tries to guess a random integer between 1 to 100.

```
Welcome to Guanzhou's guessing game!
Enter an int ∈ [1, 100], or 'q' to quit: 50
  Your guess is... Too large!
Enter an int ∈ [1, 100], or 'q' to quit: 25
  Your guess is... Too large!
Enter an int ∈ [1, 100], or 'q' to quit: 12
  Your guess is... Too large!
Enter an int ∈ [1, 100], or 'q' to quit: 6
  Your guess is... Too small!
Enter an int ∈ [1, 100], or 'q' to quit: 9
  Your guess is... Too large!
Enter an int ∈ [1, 100], or 'q' to quit: 7
  Your guess is... Too small!
Enter an int ∈ [1, 100], or 'q' to quit: 8
  Your guess is... Correct!
You win! Congrats ;)
<Game stats>
  You tried: 50 25 12 6 9 7 8
  In total 7 tries used.
```

> Binary search should be the best strategy overall, but you can get lucky sometimes ;)

**Robustness requirements** under boundary conditions are defined as the following:

```
# Invalid input.
Enter an int ∈ [1, 100], or 'q' to quit: e
WARN: not a valid integer. Try again...

# Out-of-range input.
Enter an int ∈ [1, 100], or 'q' to quit: -141
WARN: not a valid integer. Try again...

# Allow leading & trailing whitespaces.
Enter an int ∈ [1, 100], or 'q' to quit:   50 \t
  Your guess is... Too large!

# Empty input.
Enter an int ∈ [1, 100], or 'q' to quit:        # Directly display a new prompt.
Enter an int ∈ [1, 100], or 'q' to quit:

# Start with 'q'.
Enter an int ∈ [1, 100], or 'q' to quit: qewe   # Treat as quit signal as well.
Sad to see you go :(
```

All language versions must satisfy this specification.
