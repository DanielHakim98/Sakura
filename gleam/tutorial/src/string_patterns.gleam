import gleam/io

pub fn string_pattern(){
    io.println("===String Pattern===")
    io.debug(get_name("Hello, Joe"))
    io.debug(get_name("Hello, Mike"))
    io.debug(get_name("System still working?"))
}

fn get_name(x: String) -> String{
    case x {
        "Hello, " <> name -> name
        _ -> "Unknown"
    }
}