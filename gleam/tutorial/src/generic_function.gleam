import gleam/io

pub fn generic_fn(){
    io.println("===Generic Function===")
    let add_one = fn(x) {x + 1}
    let exclaim = fn(x) {x <> "!"}

    io.debug(twice(10, add_one))
    io.debug(twice("Hello", exclaim))
}

fn twice(arg: value, passed_fn: fn(value) -> value) -> value{
    passed_fn(passed_fn(arg))
}