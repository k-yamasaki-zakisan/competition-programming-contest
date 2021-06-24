// https://atcoder.jp/contests/abc206/tasks/abc206_c

use proconio::input;
use std::collections::HashMap;
// use proconio::marker::Usize1;

fn main() {
    input! {
        n: usize,
        mut a: [usize;n],
    };
    let mut memo: HashMap<usize, usize> = HashMap::new();
    for v in a {
        let count = memo.entry(v).or_insert(0);
        *count += 1;
    }
    let all = n * (n - 1) / 2;
    let mut complement = 0;
    for (_key, &value) in memo.iter() {
        if value > 1 {
            complement += value * (value - 1) / 2;
        }
    }
    let ans = all - complement;
    println!("{}", ans);
}