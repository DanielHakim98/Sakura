import gleam/io
import gleam/int

pub fn ints(){
    // arithmetic
    io.debug(1 + 1)
    io.debug(5 - 1)
    io.debug(5 / 2)
    io.debug(3 * 3)
    io.debug(5 % 2)

    // comparisons
    io.debug(2 > 1)
    io.debug(2 < 1)
    io.debug(2 >= 1)
    io.debug(2 <= 1)

    // equality
    io.debug(1 == 1)
    io.debug(2 == 1)

    // standard lib int
    io.debug(int.max(42,77))
    io.debug(int.clamp(5, 10, 20))
}