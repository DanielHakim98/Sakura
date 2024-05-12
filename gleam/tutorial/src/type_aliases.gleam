import gleam/io

pub type UserId = Int

pub fn type_aliases(){
    let one: UserId = 1
    let two: Int = 1

    io.print("Is UserId and Int the same? ")
    io.debug(one == two)
}