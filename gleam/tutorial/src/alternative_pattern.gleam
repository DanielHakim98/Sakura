import gleam/io
import gleam/int

/// Example of 'Alternative Pattern'
pub fn alternative_pattern(){
    io.println("===Alternative Pattern===")
    let number = int.random(10)
    io.debug(number)

    case number{
        2 | 4 | 6 | 8 -> "This is an even number"
        1 | 3 | 5 | 7 -> "This is an odd number"
        _ -> "I'm not sure"
    }
    |> io.debug
}