import gleam/io


/// Example of recursion
pub fn recursion(){
    io.println("===Recursion===")
    factorial(5)
    |>io.debug

    factorial(7)
    |> io.debug
}

pub fn factorial(x: Int) -> Int{
    case x{
        1 -> 1
        _ -> x * factorial(x - 1)
    }
}