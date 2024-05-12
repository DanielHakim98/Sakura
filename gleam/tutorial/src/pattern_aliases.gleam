import gleam/io

/// Example of 'Pattern Aliases'
pub fn pattern_aliases(){
    io.println("===Pattern Aliases===")
    get_first_non_empty([[], [1,2,3]])
    |> io.debug

    get_first_non_empty([[1,2], [4,5]])
    |> io.debug

    get_first_non_empty([[],[],[]])
    |> io.debug
}

fn get_first_non_empty(list: List(List(t))) -> List(t){
    case list{
        [] -> []
        [[_, ..] as first, ..] -> first
        [_, ..rest] -> get_first_non_empty(rest)
    }
}