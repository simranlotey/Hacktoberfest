use std::{fs,error::Error,env};


pub struct Config{
    pub query:String,
    pub file_path:String,
    pub is_case_sensitive:bool,
}
impl Config {
pub fn build( mut args: impl Iterator <type = String> ) -> Result<Config,&str> {
     args.next();
    let query = match args.next(){
        Some(arg) => arg,
        None => return Err("Query not found"),
    };

    let file_path = match args.next(){
        Some(arg) => arg,
        None => return Err("File path not found"),
    };

    let is_case_sensitive = env::var("CASE_INSENSITIVE").is_ok();

}
}

pub fn run(config: Config) -> Result<(),Box<dyn Error>>{
    

    let content = fs::read_to_string(config.file_path)?;

   
    let results = if config.is_case_sensitive{
        search(&config.query, &content)
    }
    else{
        search_insensitive(&config.query, &content)
    };

    for line in results{
        println!("{}",line);
    } 

    Ok(())

}

pub fn search<'a>(query:&str, content: &'a str) -> Vec<&'a str>{

    contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()

}

pub fn search_insensitive<'a>(query:&str, content: &'a str) -> Vec<&'a str>{
    let query = query.to_lowercase();
  
    let results = contents
        .lines()
        .filter(|line| line.to_lowercase().contains(&query))
        .collect();

}


#[cfg(test)]
mod tests{
    use super::*;

    #[test]
    fn case_sensitive(){

        let query = "cat";
        let content = "\
I love :
cats, dogs and birds" ;

        assert_eq!(vec!["cats, dogs and birds"],search(query,content));
    }



}

    #[test]
    fn case_insenstive(){

        let query = "cAt";
        let content = "\
I love :
cats, dogs and birds" ;

        assert_eq!(vec!["cats, dogs and birds"],search_insensitive(query,content));
    }