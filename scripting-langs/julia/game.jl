# Guessing game in Julia 1.2.
# Let's call the magic number λ, and a guess γ.


"Showing Julia's functional syntax & multi-dispatch."
equal(λ, x) = λ == x
equal(λ) = x -> equal(λ, x)
# @show equal(37)


"Check a guess against a magic number, and record this try."
function check(λ, γ, tries)
    push!(tries, γ)
    if equal(λ)(γ)
        println("Correct!")
        return true
    else
        if γ < λ
            println("Too small!")
        elseif γ > λ
            println("Too large!")
        end
        return false
    end
end


"Show game stats."
function stats(tries)
    println("<Game stats>")
    print("  You tried: ")
    for num in tries
        print("$num ")
    end
    println()
    println("  In total "*string(length(tries))*" tries used.")
end


"Game logic."
function play()
    println("Welcome to Guanzhou's guessing game!")

    # Generate random number.
    λ = rand(1:100)

    # Guessing loop.
    win = false
    tries = []
    while true
        print("Enter an int ∈ [1, 100], or 'q' to quit: ")
        ipt = strip(readline())
        if length(ipt) == 0     # Empty input.
            continue
        end
        if ipt[1] == 'q'        # Quit signal.
            break
        end
        if (ipt[1] < '0' || ipt[1] > '9') && ipt[1] != '-'
            println("WARN: not a valid integer. Try again...")
        else
            γ = parse(Int, ipt)
            if !(1 <= γ <= 100)
                println("WARN: valid input ∈ [1, 100]. Try again...")
            else
                print("  You guess is... ")
                if check(λ, γ, tries)
                    win = true
                    break
                end
            end
        end
    end

    # Ending message.
    if win
        println("You win! Congrats ;)")
    else
        println("Sad to see you go :(")
    end
    stats(tries)
end


play();
