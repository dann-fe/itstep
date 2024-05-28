// function addingNumbers(num1, num2) {
//     let result = num1 + num2;
//     alert("Your result is " + result);
//     return result;
// }

// let num1 = 5;
// let num2 = 8;

// let result = addingNumbers(num1, num2);
// console.log("Last time, the answer was " + result);

function countRevenue (prijmy, vydaje) {
    let revenue = prijmy - vydaje;
    console.log(revenue);
    return revenue;
}

let vydajeThisYear = 90000;
let prijmyThisYear = 100000;
countRevenue(prijmyThisYear, vydajeThisYear);