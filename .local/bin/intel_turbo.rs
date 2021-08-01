#![feature(format_args_capture)]

use std::env;

fn main() -> std::io::Result<()> {
    if env::args().len() != 2 {
        println!("Usage: {} {{on,off}}", env::args().nth(0).unwrap());
        return Ok(());
    }

    let path = "/sys/devices/system/cpu/intel_pstate/no_turbo";

    let mut turbo = false;

    match env::args().nth(1).unwrap().to_lowercase().as_str() {
        "on" | "1" => turbo = true,
        "off" | "0" => turbo = false,
        invalid => eprintln!("Invalid option '{invalid}', defaulting to 'off'"),
    }

    let no_turbo = if !turbo { 1 } else { 0 };

    std::fs::write(path, no_turbo.to_string())?;

    Ok(())
}
