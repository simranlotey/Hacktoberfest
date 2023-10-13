
function fibonacci_prime_numbers(n) {
    let a = 1, b = 1, c = 0, count = 0;
    while (count < n) {
        c = a + b;
        a = b;
        b = c;
        if (is_prime(c)) {
            count++;
            console.log(c);
        }
    }
}

function is_prime(n) {
    if (n < 2) return false;
    for (let i = 2; i < n; i++)
        if (n % i === 0) return false;
    return true;
}

console.log(fibonacci_prime_numbers(10));