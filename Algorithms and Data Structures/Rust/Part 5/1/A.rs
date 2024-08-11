use std::io::Write;
use std::fs::File;
use std::{fs,mem};

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines();
    let mut first_line = line_iter.next().unwrap().split_whitespace();
    let mut p = first_line.next().unwrap().parse::<i64>().unwrap();
    let mut v = first_line.next().unwrap().parse::<i64>().unwrap();
    let mut second_line = line_iter.next().unwrap().split_whitespace();
    let mut q = second_line.next().unwrap().parse::<i64>().unwrap();
    let mut m = second_line.next().unwrap().parse::<i64>().unwrap();
    let mut result: i64 = 0;
    if p > q {
        mem::swap(&mut p, &mut q);
        mem::swap(&mut m, &mut v);
    }
    if (p + v) < (q - m) {
        result = 2*v + 2*m + 2;
    }
    else if (p + v) > (q + m) {
        result = 2*v + 1;
    }
    else if (p - v) > (q - m) {
        result = 2*m + 1;
    }
    else {
        result = v + m + (q-p+1);
    }
        
    let result_to_str = format!("{}", result);
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}