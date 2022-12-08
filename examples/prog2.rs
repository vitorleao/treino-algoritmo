fn func(a: &Vec<usize>, b: &Vec<usize>) -> bool {
    let tamanho_a = a.len();
    let tamanho_b = b.len();
    let mut posicao_a = 0;
    let mut posicao_b = 0;
    let mut valor_a = a[posicao_a];
    let mut valor_b = b[posicao_b];
    loop {
        if valor_a == valor_b {
            return true;
        }
        if valor_a < valor_b {
            posicao_a += 1;
            if posicao_a >= tamanho_a {
                return false;
            }
            valor_a = a[posicao_a];
        } else {
            posicao_b += 1;
            if posicao_b >= tamanho_b {
                return false;
            }
            valor_b = b[posicao_b];
        }
    }
}

fn main() {
    let a: Vec<usize> = (0..1_000_000).map(|i| i * 2).collect();
    let b: Vec<usize> = (0..1_000_000).map(|i| i * 2 + 1).collect();

    func(&a, &b);
}
