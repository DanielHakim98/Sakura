// somehow, naming this file as 'lists.gleam' (with s)
// will cause crash when this code is run with OTP

import gleam/io

pub fn lists() {
    let ints = [1, 2, 3]
    io.debug(ints)

    io.debug([-1, 0 , ..ints])

    io.debug(ints)
}