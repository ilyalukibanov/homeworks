use std::io::Write;
use std::fs::File;
use std::fs;

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines().next().unwrap().split_whitespace();
    let n = line_iter.next().unwrap().parse::<i64>().unwrap();
    let k = line_iter.next().unwrap().parse::<i64>().unwrap();
    let d = line_iter.next().unwrap().parse::<i32>().unwrap();
    let mut result: i64 = -1;
    let mut result_to_str = format!("{}", result);
    for i in 0..9 {
        if (n * 10 + i) % k == 0 {
            result = n * 10 + i;
            result_to_str = format!("{}{}", result,"0".repeat((d-1) as usize));
        }
    }
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}