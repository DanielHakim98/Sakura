import gleam/io

pub fn assignments(){
    let x = "Original"
    io.debug(x)

    let y = x
    io.debug(y)

    let x = "New"
    io.debug(x)

    io.debug(y)
}