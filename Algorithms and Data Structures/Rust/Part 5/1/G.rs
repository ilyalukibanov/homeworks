use std::io::Write;
use std::fs::File;
use std::fs;

fn simulate_infantry_fight(ally: i32, enemy: i32) -> i32 {
    let mut ally = ally;
    let mut enemy = enemy;
    let mut count = 0;
    while (ally > 0) & (enemy > 0) {
        count += 1;
        enemy -= ally;
        ally -= enemy;
    } 
    if enemy > 0 {
        -1
    } else {
        count
    }
}

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines();
    let mut x = line_iter.next().unwrap().parse::<i32>().unwrap();
    let mut y = line_iter.next().unwrap().parse::<i32>().unwrap();
    let p = line_iter.next().unwrap().parse::<i32>().unwrap();
    let mut enemies = 0;
    let mut result: i32 = -1;
    let mut min_rounds: i32 = 5001;
    if x >= y {
        result = 1;
    } else {
        y -= x;
        let mut rounds = 1; 
        while ((y > 0) | (enemies > 0)) & (x > 0) {
            rounds += 1;
            if y > 0 {
                enemies += p;
            }
            if ((y <= x) & (x <= p)) | ((x >= 2 * (p-x+y)) & (x > p)) {
                enemies -= x-y;
                y = 0;
            } else {
                if enemies > x {
                    break;
                }
                enemies = 0;
                y -= 0.max(x-p);
            }
            x -= 0.max(enemies);
            let mut n_rounds_infantry = 0;

            if x >= y {
                n_rounds_infantry = simulate_infantry_fight(x-(p-(x-y)), p-(x-y));
                if n_rounds_infantry > -1 {
                    min_rounds = min_rounds.min(rounds+1+n_rounds_infantry);
                }
            }
            if rounds > 5000 {
                break;
            }
            println!("{},{},{},{},{},{},{}",x,y,enemies,n_rounds_infantry, min_rounds,rounds,n_rounds_infantry);
        } 
        if (y <= 0) & (enemies <= 0) {
            result = rounds.min(min_rounds);
        }
    }
    let result_to_str = format!("{}", result);
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}