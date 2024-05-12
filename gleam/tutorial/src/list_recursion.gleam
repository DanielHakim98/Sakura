import gleam/io

/// Example of list recursion
pub fn list_recursion(){
    io.println("===List Recursion===")
    sum_list([18,56, 35, 85, 91], 0)
    |> io.debug
}

fn sum_list(seq: List(Int), acc: Int) -> Int{
    case seq {
        [] -> acc
        [first,..rest] -> sum_list(rest, acc+first)
    }
}