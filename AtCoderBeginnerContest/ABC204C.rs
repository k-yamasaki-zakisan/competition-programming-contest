// https://atcoder.jp/contests/abc204/tasks/abc204_c

use proconio::input;
use proconio::marker::Usize1;

fn main() {
    input! {
        n: usize,
        m: usize,
        edges: [(Usize1, Usize1); m],
    }

    let adj = {
        let mut adj = vec![vec![]; n];
        for &(a, b) in edges.iter() {
            adj[a].push(b);
        }
        adj
    };

    let mut total = 0;
    for v in 0..n {
        let mut reachable = 0;
        let mut visited = vec![false; n];
        let mut stack = vec![v];
        visited[v] = true;
        while let Some(top) = stack.pop() {
            reachable += 1;
            for &w in adj[top].iter() {
                if !visited[w] {
                    stack.push(w);
                    visited[w] = true;
                }
            }
        }
        total += reachable
    }
    println!("{}", total)
}