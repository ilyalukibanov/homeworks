use std::io::Write;
use std::fs::File;
use std::fs;

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines().next().unwrap().split_whitespace();
    let l = line_iter.next().unwrap().parse::<f64>().unwrap();
    let x1 = line_iter.next().unwrap().parse::<f64>().unwrap();
    let v1 = line_iter.next().unwrap().parse::<f64>().unwrap();
    let x2 = line_iter.next().unwrap().parse::<f64>().unwrap();
    let v2 = line_iter.next().unwrap().parse::<f64>().unwrap();
    let mut result: i64 = -1;
    let mut result_to_str = format!("{}", result);
    if ((v1 == 0.0) & (v2 == 0.0)) & ((x1-l).abs() != (x2-l).abs()) {
        result_to_str = "NO".to_string(); 
    } else {
        result_to_str = "YES\n0".to_string(); 
    }
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}