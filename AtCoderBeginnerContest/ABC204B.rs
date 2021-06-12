// https://atcoder.jp/contests/abc204/tasks/abc204_b

use proconio::input;

fn main() {
    input! {
        n: usize,
        a: [usize; n],
    }

    let mut _ans = 0;
    for i in 0..n {
        if 10 < a[i] {
            _ans += a[i] - 10;
        }
    }
    println!("{}", _ans)
}