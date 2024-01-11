function findMaxValue(array) {
    const max = Math.max(...array);
  
    return max;
  }
  
  const numbers = [3, 7, 1, 9, 4, 6];
  const maxValue = findMaxValue(numbers);
  console.log(maxValue); // Output: 9
  