function isPrime(n) {
    if (n < 2 ) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if(n % 2 == 0){
        return false;
    }
    for (let i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}


onmessage = function (e) {
    const val = e.data.val;
    const result = isPrime(val);
    postMessage(result);
};
