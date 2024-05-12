import gleam/io
import gleam/string

pub fn strings(){
    io.debug("👩‍💻 こんにちは Gleam")
    io.debug(
        "multi
        line
        string",
    )
    io.debug("\u{1F600}")

    io.println("\"X\" marks the spot")

    io.debug("One " <> "Two")

    io.debug(string.reverse("1 2 3 4 5"))
    io.debug(string.append("abc", "def"))
}