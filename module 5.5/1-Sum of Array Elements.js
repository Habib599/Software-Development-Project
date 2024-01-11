function sumArrayElements(array) {
    let sum = 0;
    for (let i = 0; i < array.length; i++) {
      sum += array[i];
    }
    return sum;
  }
  

  var numbers = [1, 2, 3, 4, 5,6];
  var result = sumArrayElements(numbers);
  console.log(result); // Output: 15
  