const readline = require('readline');

// Create a readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Prompt the user to enter a number and its base
rl.question("Enter a number: ", (number) => {
  rl.question("Enter the base of the number: ", (base) => {
    base = parseInt(base, 10);

    // Convert the number to decimal
    const decimal = parseInt(number, base);

    // Convert the decimal number to other bases
    const binary = decimal.toString(2);
    const octal = decimal.toString(8);
    const hexadecimal = decimal.toString(16);

    // Output the results
    console.log(`Binary: ${binary}`);
    console.log(`Octal: ${octal}`);
    console.log(`Decimal: ${decimal}`);
    console.log(`Hexadecimal: ${hexadecimal}`);

    // Close the readline interface
    rl.close();
  });
});