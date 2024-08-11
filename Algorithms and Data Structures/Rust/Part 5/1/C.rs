use std::io::Write;
use std::fs::File;
use std::fs;

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines();
    let n = line_iter.next().unwrap().parse::<i32>().unwrap();
    let mut result: i64 = 0;
    let remainders: [i64; 4] = [0, 1, 2, 2]; 
    for _ in 0..n {
        let a = line_iter.next().unwrap().parse::<i64>().unwrap();
        result += (a/4) + remainders[(a%4) as usize];
    }
    let result_to_str = format!("{}", result);
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}