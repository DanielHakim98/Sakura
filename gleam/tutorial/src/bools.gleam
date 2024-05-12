import gleam/io
import gleam/bool

pub fn bools(){
    io.debug(True && False)
    io.debug(True && True)
    io.debug(False || False)
    io.debug(False || True)

    io.debug(bool.to_string(True))
    io.debug(bool.to_int(False))
}