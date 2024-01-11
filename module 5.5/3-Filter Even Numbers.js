function filterEvenNumbers(array) {
    const evenNumbers = array.filter(num => num % 2 == 0);
  
    return evenNumbers;
  }
  
  // Example usage:
  const numbers = [1, 2, 3, 4, 5, 6];
  const evenNumbers = filterEvenNumbers(numbers);
  console.log(evenNumbers); // Output: [2, 4, 6]
  