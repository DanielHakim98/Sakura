pub fn run_example() {
    let index = 5;
    println!("fibonacci at #{index}: , {}", generate_nth_number(index));

    let index = 30;
    println!("fibonacci at #{index}: , {}", generate_nth_number(index));
    println!()
}

// This assume that Fibonacci starts at 0,
// so F(0) = 0, F(1) = 1, F(2) = 1, and so on.
fn generate_nth_number(n: i32) -> i32 {
    if n < 2 {
        return n;
    }
    let mut prev_nth_2 = 0;
    let mut prev_nth_1 = 1;
    let mut total = 0;
    for _ in 2..n + 1 {
        total = prev_nth_2 + prev_nth_1;
        prev_nth_2 = prev_nth_1;
        prev_nth_1 = total;
    }
    total
}

/* TRY! n = 46; generate_nth_number(46);
fn generate_nth_number(n:i32) -> i32{
    if n < 2{
        return n;
    }
    generate_nth_number(n - 2) + generate_nth_number(n - 1)
}
*/
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_nth_0() {
        let got = generate_nth_number(0);
        let want = 0;
        assert_eq!(got, want);
    }

    #[test]
    fn test_nth_1() {
        let got = generate_nth_number(1);
        let want = 1;
        assert_eq!(got, want);
    }

    #[test]
    fn test_nth_2() {
        let got = generate_nth_number(2);
        let want = 1;
        assert_eq!(got, want);
    }

    #[test]
    fn test_nth_19() {
        let got = generate_nth_number(19);
        let want = 4181;
        assert_eq!(got, want);
    }

    #[test]
    fn test_nth_47() {
        let got = generate_nth_number(46);
        let want = 1836311903; // max before integer overflow
        assert_eq!(got, want);
    }
}
