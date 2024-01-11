function findCommonElements(array1, array2) {
   
    const commonElements = array1.filter
    (element => array2.includes(element));
  
    return commonElements;
  }
  
  const arrayA = [1, 2, 3, 4, 5];
  const arrayB = [3, 4, 5, 6, 7];
  const commonElementsArray = findCommonElements(arrayA, arrayB);
  console.log(commonElementsArray); // Output: [3, 4, 5]
  