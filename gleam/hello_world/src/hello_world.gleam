import gleam/io
import file_streams/read_stream.{type ReadStream}
import file_streams/read_stream_error
import gleam/bool
import gleam/bit_array

pub fn open_file(file_name) -> ReadStream {
  case read_stream.open(file_name) {
    Error(_e) -> panic
    Ok(v) -> v
  }
}

pub fn iterator_read_byte_by_size(rs: ReadStream, buf_size: Int, acc: BitArray) {
  case read_stream.read_bytes(rs, buf_size) {
    Error(e) -> {
      case e {
        read_stream_error.EndOfStream -> acc
        _ -> panic
      }
    }
    Ok(v) -> iterator_read_byte_by_size(rs, buf_size, bit_array.append(acc, v))
  }
}

pub fn read_bytes_by_size(rs: ReadStream, buf_size: Int) -> BitArray {
  let default = bit_array.from_string("")
  use <- bool.guard(when: buf_size <= 0, return: default)
  iterator_read_byte_by_size(rs, buf_size, default)
}

pub fn bitarray_to_string(bytes: BitArray) -> String {
  case bit_array.to_string(bytes) {
    Error(_e) -> panic
    Ok(i) -> i
  }
}

pub fn main() {
  io.println("Reading file...\n")
  open_file("./data/test.txt")
  |> read_bytes_by_size(8)
  |> bitarray_to_string
  |> io.println
}
