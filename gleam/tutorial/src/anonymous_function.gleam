import gleam/io

pub fn anon_fn(){
    io.println("===Anonymous Function===")
    let add_one = fn(a) {a + 1}
    io.debug(twice(1, add_one))

    io.debug(twice(1, fn(a){a+1}))
}

fn twice(arg: Int, passed_fn: fn(Int)->Int) -> Int{
    passed_fn(passed_fn(arg))
}