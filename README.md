# Guessing Game Collection

![Languages](https://img.shields.io/github/languages/count/hgz12345ssdlh/guessing-game-collection)
![Code-size](https://img.shields.io/github/languages/code-size/hgz12345ssdlh/guessing-game-collection?color=purple)

A collection of the number guessing game in different languages - weekly update ;)

Aimed to help me explore & touch new languages & technologies.


## Progress List

System programming languages:

- [x] C
- [x] C++
- [ ] Rust
- [ ] Go

Common scripting languages:

- [x] Python
- [ ] Ruby
- [ ] Julia
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
TODO
```

> Binary search should be the best strategy overall, but you can get lucky sometimes ;)

**Robustness requirements** under boundary conditions:

```bash
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
```
