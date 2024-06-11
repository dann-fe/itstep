// nasobilka 5
// for(let i = 1; i <= 10; i++) {
//     console.log(i * 5);
// }

//multiples of a specified num

// let num = prompt("number");
// for(let i = 100; i >= 0; i--) {
//     if(i % num === 0) {
//         console.log(i);
// }
// }


// range sum

// let start = prompt("starting number");
// let last = prompt("last number");
// let result = 0;
// // let range = last - start;
// // alert(range);
// for (let i = Number(start); i <= Number(last); i++) {
//     result = result + 1;
//     console.log(result);
// }

// calculator loop

// let num1 = prompt("num1");
// let num2 = prompt("num2");
// let operator = prompt("operator (+, -, *, /)"); 

// while (true) {
//     if (operator === "+") {
//         console.log(parseFloat(num1) + parseFloat(num2));
//     }
//     if (operator === "-") {
//         console.log(parseFloat(num1) - parseFloat(num2));
//     }
//     if (operator === "*") {
//         console.log(parseFloat(num1) * parseFloat(num2));
//     }
//     if (operator === "/") {
//         console.log(parseFloat(num1) / parseFloat(num2));
//     }
//     let continuePrompt = prompt("Do you want to continue? (yes/no)");
//     if (continuePrompt == "no") {
//         break;
//     }
// }

// sachovnice



for (let i = 1; i>=4; i++) {
    tableContent += "<tr>";
    for (let j = 1; j<= 10; j++ )
    tableContent += `<td>${i*j}</td>`;
    tableContent += "</tr>"
}
