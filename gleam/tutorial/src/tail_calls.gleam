import gleam/io

/// Example of tail call recursive
pub fn tail_call(){
    io.println("===Tail Call===")
    factorial(5)
    |> io.debug

    factorial(7)
    |> io.debug
}

fn factorial(x: Int) -> Int{
    do_factorial(x, 1)
}

fn do_factorial(x: Int, acc: Int) -> Int{
    case x{
        1 -> acc
        _ -> do_factorial(x - 1, acc * x)
    }
}