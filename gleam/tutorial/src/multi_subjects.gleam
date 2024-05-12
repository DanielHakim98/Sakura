import gleam/io
import gleam/int

/// Example of multiple subjects
pub fn multiple_subjects(){
    io.println("===Multiple Subjects===")
    let x = int.random(2)
    let y = int.random(2)

    io.debug(x)
    io.debug(y)


    case x, y{
        0, 0 -> "both are zero"
        0, _ -> "First is zero"
        _, 0 -> "Second is zero"
        _, _ -> "Neither are zero"
    }
    |> io.debug
}