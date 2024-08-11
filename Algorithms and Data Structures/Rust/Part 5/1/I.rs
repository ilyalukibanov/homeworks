use std::io::Write;
use std::fs::File;
use std::fs;
use std::collections::HashMap;

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines();
    let n = line_iter.next().unwrap().parse::<i32>().unwrap();
    let year = line_iter.next().unwrap().parse::<i32>().unwrap();

    let leap = if (year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0)) {1} else {0};
    let mut n_holidays_per_day = [0; 7];
    n_holidays_per_day[0] = -1;
    n_holidays_per_day[1] = -leap;
    let dow_to_day = HashMap::from([(0,"Monday"),(1,"Tuesday"),(2,"Wednesday"),(3,"Thursday"),(4,"Friday"),(5,"Saturday"),(6,"Sunday")]);
    let day_to_dow = HashMap::from([("Monday",0),("Tuesday",1),("Wednesday",2),("Thursday",3),("Friday",4),("Saturday",5),("Sunday",6)]);
    let months_to_days = [0, 31, 59+leap,90+leap,120+leap,151+leap,181+leap,212+leap,243+leap,273+leap,304+leap,334+leap];
    let months_to_num = HashMap::from([("January", 0), ("February", 1),("March", 2),("April", 3),("May", 4),
        ("June", 5),("July", 6),("August", 7),("September", 8),("October", 9),("November", 10),("December", 11)]);
    for _ in 0..n {
        let mut num_iter = line_iter.next().unwrap().split_whitespace();
        let day = num_iter.next().unwrap().parse::<i64>().unwrap();
        let month = num_iter.next().unwrap();
        n_holidays_per_day[((months_to_days[months_to_num[month]]+day-1)%7) as usize] += 1;
    }
    let mut min_day = 0;
    let mut min_day_count = 400;
    let mut max_day = 0;
    let mut max_day_count = -2;
    for i in 0..7 {
        if n_holidays_per_day[i] < min_day_count {
            min_day = i;
            min_day_count = n_holidays_per_day[i];
        }
        if n_holidays_per_day[i] > max_day_count {
            max_day = i;
            max_day_count = n_holidays_per_day[i];
        }
    }
    let dow_start = day_to_dow[line_iter.next().unwrap()];    
    let result_to_str = format!("{} {}", dow_to_day[&(((min_day+dow_start)%7) as i32)], dow_to_day[&(((max_day+dow_start)%7) as i32)]);
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}