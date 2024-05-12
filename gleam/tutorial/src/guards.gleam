import gleam/io


/// Example of 'Guards'
pub fn guards(){
    io.println("===Guards===")
    let numbers = [1,2,3,4,5]
    get_first_larger(numbers, 3)
    |> io.debug

    get_first_larger(numbers, 5)
    |> io.debug
}

fn get_first_larger(lists: List(Int), limit: Int) -> Int{
    case lists {
        [] -> 0
        [first, ..] if first > limit -> first
        [_, ..rest] -> get_first_larger(rest, limit)
    }
}