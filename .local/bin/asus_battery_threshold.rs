#![feature(format_args_capture)]

use std::env;

fn main() -> std::io::Result<()> {
    if env::args().len() != 2 {
        println!("Usage: {} THRESHOLD", env::args().nth(0).unwrap());
        return Ok(());
    }

    let path = "/sys/class/power_supply/BAT0/charge_control_end_threshold";

    let mut threshold = 60u8;

    match env::args().nth(1).unwrap().to_lowercase().as_str() {
        "60" => threshold = 60,
        "80" => threshold = 80,
        "100" => threshold = 100,
        invalid => eprintln!("Invalid threshold '{invalid}', defaulting to '60'"),
    }


    std::fs::write(path, threshold.to_string())?;

    Ok(())
}
