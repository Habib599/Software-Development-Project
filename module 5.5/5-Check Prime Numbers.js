function isPrime(number) {

    for (let i = 2; i <= Math.sqrt(number); i++) {
      if (number % i === 0) {
        return false; // Not a prime number
      }
    }
  
    return number > 1; // Prime number
  }
  
  const checkNumber = 18;
  const isPrimeResult = isPrime(checkNumber);
  console.log(isPrimeResult); // Output: true
  