import gleam/io
import gleam/int

pub fn case_expression(){
    io.println("===Case Expression===")
    let x = int.random(5)
    io.debug(x)

    case x {
        0 -> "Zero"
        1 -> "One"

        _ -> "Other"
    }
    |> io.debug
}