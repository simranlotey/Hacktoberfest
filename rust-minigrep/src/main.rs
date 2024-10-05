use std::{env,process};
use minigrep::Config;

fn main() {
    
    let config  = Config::build(env::args()).unwrap_or_else(|err|{
        eprintln!("Problem prasing {}" ,err);
        process::exit(0);
    });

        println!("Searching for {}", config.query);
        println!("In file {}", config.file_path);

    if let Err(e) = minigrep::run(config){
        eprintln!("An error {e} occured");
        process::exit(0);
    };

}

