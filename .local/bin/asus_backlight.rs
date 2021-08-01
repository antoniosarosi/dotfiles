#![feature(format_args_capture)]

use std::env;

fn main() -> std::io::Result<()> {
    if env::args().len() != 2 {
        println!(
            "Usage: {} {{off,low,normal,high}}",
            env::args().nth(0).unwrap()
        );

        return Ok(());
    }

    let path = "/sys/devices/platform/asus-nb-wmi/leds/asus::kbd_backlight/brightness";

    let mut intensity = 2u8;

    match env::args().nth(1).unwrap().to_lowercase().as_str() {
        "off" | "0" => intensity = 0,
        "low" | "1" => intensity = 1,
        "normal" | "2" => intensity = 2,
        "high" | "3" => intensity = 3,
        invalid => eprintln!("Invalid intensity '{invalid}', defaulting to 'normal'"),
    }

    std::fs::write(path, intensity.to_string())?;
    Ok(())
}
