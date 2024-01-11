function removeDuplicates(array) {

    const uniqueArray = [...new Set(array)];
  
    return uniqueArray;
  }
  
  const arrayWithDuplicates = [1, 2, 2, 3, 4, 4, 5];
  const withoutDuplicates = removeDuplicates(arrayWithDuplicates);
  console.log(withoutDuplicates); // Output: [1, 2, 3, 4, 5]
  