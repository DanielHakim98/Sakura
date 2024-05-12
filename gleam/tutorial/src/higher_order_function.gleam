import gleam/io

pub fn higher_order_fn(){
    io.println("===Higher Order Function===")
    io.debug(twice(1,add_one))

    let ass_fn = add_one
    io.debug(ass_fn(100))
}

fn twice(arg: Int, passed_fn: fn(Int)-> Int) -> Int{
    passed_fn(passed_fn(arg))
}

fn add_one(arg: Int) -> Int{
    arg + 1
}