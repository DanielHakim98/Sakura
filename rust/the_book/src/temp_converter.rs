enum TempConvrt {
    FtoC,
    CtoF,
}

pub fn run_example() {
    let celsius_temp = 23.0;
    println!(
        "Celcius to Fahrenheit: {}",
        temperature_convert(celsius_temp, TempConvrt::CtoF)
    );

    let fahrenheit_temp = 73.4;
    println!(
        "Fahrenheit to Celcius: {}",
        temperature_convert(fahrenheit_temp, TempConvrt::FtoC),
    );
    println!()
}

fn temperature_convert(temp: f64, convert: TempConvrt) -> f64 {
    let diff = 32.0;
    let multiplier = 5.0 / 9.0;

    let res = match convert {
        TempConvrt::FtoC => (temp - diff) * (multiplier),
        TempConvrt::CtoF => ((1.0 / multiplier) * temp) + diff,
    };

    let decimal_places = 2;
    let corrector = f64::powf(10.0, decimal_places as f64);
    (res * corrector).round() / corrector
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_celsius_to_fahrenheit() {
        let temp = 23.0; // 23.0 Celsius
        let got = temperature_convert(temp, TempConvrt::CtoF);
        let want = 73.4;
        assert_eq!(got, want);
    }

    #[test]
    fn test_fahrenheit_to_celsius() {
        let temp = 73.4;
        let got = temperature_convert(temp, TempConvrt::FtoC);
        let want = 23.0;
        assert_eq!(got, want);
    }
}
