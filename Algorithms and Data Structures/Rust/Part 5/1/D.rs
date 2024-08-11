use std::io::Write;
use std::fs::File;
use std::fs;

fn main() {
    let file: String = fs::read_to_string("input.txt").unwrap();
    let mut line_iter = file.lines();
    let mut result: i32 = 0;
    let mut matrix = [[1; 8]; 8];
    let rook_moves: [[i32; 2]; 4] = [[1, 0], [-1,0],[0,1], [0,-1]];
    let bishop_moves: [[i32; 2]; 4] = [[1, 1], [-1,-1],[-1,1], [1,-1]];
    for i in 0..8 {
        let mut cell_iterator = line_iter.next().unwrap().chars();
        for j in 0..8 {
            let symbol = cell_iterator.next().unwrap();
            if symbol == 'R' {
                matrix[i][j] = -1;
            } else if symbol == 'B' {
                matrix[i][j] = -2;
            }
        }
    }

    for i in 0..8 {
        for j in 0..8 {
            if matrix[i][j] == -1 {
                for d in rook_moves {
                    let mut ni = i as i32;
                    let mut nj = j as i32; 
                    let di = d[0];
                    let dj = d[1];
                    while (ni+di >= 0) & (ni+di <= 7) & (nj+dj >= 0) & (nj+dj <= 7) {
                        nj += dj;
                        ni += di;
                        if matrix[ni as usize][nj as usize] < 0 {
                            break;
                        }
                        matrix[ni as usize][nj as usize] = 0;
                    }
                }
            }
            if matrix[i][j] == -2 {
                for d in bishop_moves {
                    let mut ni = i as i32;
                    let mut nj = j as i32; 
                    let di = d[0];
                    let dj = d[1];
                    while (ni+di >= 0) & (ni+di <= 7) & (nj+dj >= 0) & (nj+dj <= 7) {
                        nj += dj;
                        ni += di;
                        if matrix[ni as usize][nj as usize] < 0 {
                            break;
                        }
                        matrix[ni as usize][nj as usize] = 0;
                    }
                }
            }
        }
    }
    for i in 0..8 {
        for j in 0..8 {
            if matrix[i][j] == 1 {
                result += 1;
            }
            print!("{}",matrix[i][j]);
        }
        println!();
    }
    let result_to_str = format!("{}", result);
    let mut out = File::create("output.txt").unwrap();
    out.write_all(&result_to_str.as_bytes()).unwrap();
}