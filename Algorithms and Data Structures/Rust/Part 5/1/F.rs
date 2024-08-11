use std::io::Write;
use std::fs::File;
use std::fs;

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines();
    let n = line_iter.next().unwrap().parse::<i32>().unwrap();
    let mut num_iter = line_iter.next().unwrap().split_whitespace();
    let mut is_odd_found = false; 
    let mut is_trailing_odd_tail = false;
    let mut result = String::new();
    for _ in 0..n-1 {
        let number = num_iter.next().unwrap().parse::<i64>().unwrap(); 
        let is_number_odd = (number % 2 == 1) | (number % 2 == -1);
        if !is_odd_found & is_number_odd {
            if result.len() > 0 {
                result.pop();
                result += "+";
            }
            result += "+";
            is_odd_found = true;
            is_trailing_odd_tail = true;
        } else if is_trailing_odd_tail & is_number_odd {
            result.pop();
            result += "x+";
        }   else {
            result += "x";
            is_trailing_odd_tail = false;
        }
    }
    let number = num_iter.next().unwrap().parse::<i64>().unwrap(); 
    if (number % 2 == 1) | (number % 2 == -1) {
        if !is_odd_found & (result.len() > 0) {
            result.pop();
            result += "+";
        } else if is_trailing_odd_tail {
            result.pop();
            result += "x";
        }
    }
    let result_to_str = format!("{}", result);
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}