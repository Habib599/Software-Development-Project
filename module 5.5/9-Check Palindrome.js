function isPalindrome(inputString) {

    // Remove non-alphanumeric characters and convert to lowercase
    const cleanString = inputString.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  
    // Use two pointers to check for palindrome
    let left = 0;
    let right = cleanString.length - 1;
  
    while (left < right) {
      if (cleanString[left] !== cleanString[right]) {
        return false; // Not a palindrome
      }
      left++;
      right--;
    }
  
    return true; // Palindrome
  }
  
  const palindromeString = 'A man, a plan, a canal, Panama!';
  const isPalindromeResult = isPalindrome(palindromeString);
  console.log(isPalindromeResult); // Output: true
  