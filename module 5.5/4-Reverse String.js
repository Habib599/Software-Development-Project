function reverseString(inputString) {
    
    let reversedString = '';
    for (let i = inputString.length - 1; i >= 0; i--)
    {
      reversedString += inputString[i];
    }
  
    return reversedString;
  }
  
  const originalString = 'Hello, World!';
  const reversed = reverseString(originalString);
  console.log(reversed); // Output: '!dlroW ,olleH'
  