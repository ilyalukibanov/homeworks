use std::io::Write;
use std::fs::File;
use std::{fs,mem};

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines();
    let mut first_line = line_iter.next().unwrap().split(':');
    let mut a1 = first_line.next().unwrap().parse::<i32>().unwrap();
    let mut b1 = first_line.next().unwrap().parse::<i32>().unwrap();
    let mut second_line = line_iter.next().unwrap().split(':');
    let mut a2 = second_line.next().unwrap().parse::<i32>().unwrap();
    let mut b2 = second_line.next().unwrap().parse::<i32>().unwrap();
    let home = line_iter.next().unwrap().parse::<i32>().unwrap();
    let mut result: i32 = 0;
    if home == 2 {
        mem::swap(&mut a1, &mut a2);
        mem::swap(&mut b1, &mut b2);
    }
    if (a1+a2) > (b1+b2) {
        result = 0;
    } else {
        result = (b1+b2)-(a1+a2);
        if ((home == 2) & (b1 >= a2)) | ((home == 1) & (b1 >= a2+result)) {
            result += 1;
        }
    }
        
    let result_to_str = format!("{}", result);
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}