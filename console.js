function calculateSum() {
  const num1 = parseFloat(prompt("Enter the first number:"));
  const num2 = parseFloat(prompt("Enter the second number:"));

  if (isNaN(num1) || isNaN(num2)) {
    console.log("Invalid input. Please enter valid numbers.");
    return;
  }

  const sum = num1 + num2;
  console.log(`The sum of ${num1} and ${num2} is: ${sum}`);
}

calculateSum();
