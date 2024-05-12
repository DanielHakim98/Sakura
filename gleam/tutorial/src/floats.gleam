import gleam/io
import gleam/float

pub fn floats() {
    // arithmetic
    io.debug(1.0+.1.5)
    io.debug(5.0-.1.5)
    io.debug(5.0/.2.5)
    io.debug(3.0*.3.5)

    // comparisons
    io.debug(2.2 >. 1.3)
    io.debug(2.2 <. 1.3)
    io.debug(2.2 >=. 1.3)
    io.debug(2.2 <=. 1.3)

    // equality
    io.debug(1.1 == 1.1)
    io.debug(2.1 == 1.2)

    io.debug(3.14/. 0.0)

    io.debug(float.max(2.0, 9.5))
    io.debug(float.ceiling(5.4))
}