function createPyramid(rows) {
    for (let i = 1; i <= rows; i++) {
      let output = '';
      
      // Add spaces before the stars
      for (let j = 1; j <= rows - i; j++) {
        output += ' ';
      }
      
      // Add stars
      for (let k = 1; k <= 2 * i - 1; k++) {
        output += '*';
      }
      
      console.log(output);
    }
  }
  
  // Call the function with the number of rows you want in the pyramid
  createPyramid(5);
