// console.log("javascript");


// let height = 5;
// let variable1 = "hello"
// let variable2 = 35;

// let age = 25;
// let name = "John";
// // alert("Hello, I'm " + name + " and I'm " + age + " years old.");
// let userAge = Number(prompt("Hello " + name + ", how old are you?"));

// console.log(name + " said that hes " + userAge + " years old");

// let inTenYears = userAge + 10;

// console.log(inTenYears)

let num1 = Number(prompt("Write the first number"));
let num2 = Number(prompt("Write the second number"));
let action = String(prompt("Would you like to add, subtract, multiply or divide your numbers?"))
if (action == "add") {
    console.log(num1 + num2);
}

if (action == "subtract") {
    console.log(num1 - num2);
}

if (action == "multiply") {
    console.log(num1 * num2);
}

if (action == "divide") {
    console.log(num1 / num2);
}