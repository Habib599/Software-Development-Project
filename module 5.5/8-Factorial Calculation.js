function calculateFactorial(number) 
{
    let factorial = 1;
    for (let i = 2; i <= number; i++) {
      factorial *= i;
    }
    return factorial;
  }
  
  const factorialNumber = 5;
  const result = calculateFactorial(factorialNumber);
  console.log(result); // Output: 120
  