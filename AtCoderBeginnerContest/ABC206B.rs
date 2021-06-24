// https://atcoder.jp/contests/abc206/tasks/abc206_b

use proconio::input;
// use proconio::marker::Usize1;

fn main() {
    input! {
        n: u32,
    };
    let mut money = 0;
    let mut ans = 0;
    while money < n {
        money += ans + 1;
        ans += 1;
    }
    println!("{}", ans);
}