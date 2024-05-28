function comparision(num1, num2) {

    if (num1 > num2) {
        return 1;
    }
    if (num1 < num2) {
        return -1;
    }
    if (num1 === num2) {
        return 0;
    }
    else {
        console.log("error");
    }
}

let num1 = Number(prompt("first number"));
let num2 = Number(prompt("second number"));
let result = comparision(num1, num2);

if (result === 1) {
    console.log("first is bigger");
}
if (result === -1) {
    console.log("second is bigger");
}
if (result === 0) {
    console.log("equal");
}