import gleam/io
import gleam/int

pub fn variable_pattern(){
    io.println("===Variable Pattern===")
    case int.random(5){
        0 -> "Zero"
        1 -> "One"
        other -> "It is "<> int.to_string(other)
    }
    |> io.debug
}