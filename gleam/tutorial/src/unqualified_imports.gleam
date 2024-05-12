import gleam/io.{println}

pub fn unqualifed_imports(){
    io.println("This is qualified")
    println("This is unqualified")
}