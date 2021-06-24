// https://atcoder.jp/contests/abc206/tasks/abc206_a

use proconio::input;

fn main() {
    input! {
        n: u64,
    };
    let a = n * 108 / 100;
    if a < 206 {
        println!("Yay!");
    } else if a == 206 {
        println!("so-so");
    } else {
        println!(":(");
    }
}