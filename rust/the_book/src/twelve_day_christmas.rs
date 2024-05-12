static VERSES: [(&str, &str); 12] = [
    ("first", "A patridge in a a pear tree"),
    ("second", "Two turtle doves"),
    ("third", "Three French hens"),
    ("four", "Four calling birds"),
    ("five", "Five gold rings"),
    ("six", "Six geese a-laying"),
    ("seven", "Seven swans a-swimming"),
    ("eight", "Eight maids a-milking"),
    ("nine", "Nine ladies dancing"),
    ("ten", "Ten lords a-leaping"),
    ("eleven", "Eleven pipers piping"),
    ("twelve", "Twelve drummers durmming"),
];

pub fn run_example() {
    println!("verses:\n{}", gen_lyrics(&VERSES));
}

fn gen_lyrics(verse_list: &[(&str, &str)]) -> String {
    let mut lyrics = String::new();
    let mut stacks = String::new();
    for (_, line) in verse_list.iter().enumerate() {
        lyrics_builder(&mut lyrics, line, &mut stacks);
    }

    lyrics.to_string()
}

fn lyrics_builder(main_lyrics: &mut String, line: &(&str, &str), stacks: &mut String) {
    let (day, verse) = line;
    let first_line = format!("On the {} day of Christmas my true love sent to me", day);
    // // push opening chorus
    main_lyrics.push_str(&first_line);
    main_lyrics.push_str("\n");
    // EX: main_lyrics = "On the first of Christmas my true love sent to me\n"

    // insert verse at front of stack
    stacks.insert_str(0, verse);
    // EX: stacks = "A patridge in a pear tree"

    // insert newline right after end of of verse inserted
    stacks.insert_str(verse.len(), "\n");
    // EX: stacks = "\nA patridge in a pear tree"

    // push collected stacks into main lyrics;
    main_lyrics.push_str(&stacks);
    main_lyrics.push_str("\n");
    // EX: main_lyrics = "On the first of Christmas my true love sent to me\nA patridge in a pear tree\n"
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_two_verses() {
        let v = [
            ("first", "A patridge in a a pear tree"),
            ("second", "Two turtle doves"),
        ];
        let got = gen_lyrics(&v);
        let mut want: String =
            "On the first day of Christmas my true love sent to me\n".to_string();
        want.push_str("A patridge in a a pear tree\n\n");
        want.push_str("On the second day of Christmas my true love sent to me\n");
        want.push_str("Two turtle doves\n");
        want.push_str("A patridge in a a pear tree\n\n");

        assert_eq!(got, want)
    }
}
