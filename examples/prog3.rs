use std::collections::HashSet;
use std::iter::FromIterator;

fn func(a: &Vec<usize>, b: &Vec<usize>) -> bool {
    let b: HashSet<usize> = HashSet::from_iter(b.clone());
    for i in a {
        if b.contains(i) {
            return true;
        }
    }
    return false;
}

fn main() {
    let a: Vec<usize> = (0..1_000_000).map(|i| i * 2).collect();
    let b: Vec<usize> = (0..1_000_000).map(|i| i * 2 + 1).collect();

    func(&a, &b);
}
