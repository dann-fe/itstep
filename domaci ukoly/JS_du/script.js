
// 1 lehci)
// let question = prompt("Rozumis vinu?");
// if (question == "ano") {
//     console.log("nejlepsi vino");
// }
// else {
//     console.log("nejhorsi vino");
// }


// 6 tezsi)
// let number = prompt("Write a number");
// if (number > 10 && number < 20 || number > 40 && number < 50) {
//     alert("number is allowed");
// }
// else {
//     alert("number is not allowed");
// }

// 7 tezsi)
let height = 180;
let agelimit = 28;
let height2 = prompt("Write the persons height");
let agelimit2 = prompt("Write the persons age");
if (height2 >= height && agelimit2 <= agelimit) {
    alert("Perfect partner");
} 
if ((height2 >= height && agelimit2 > agelimit) || (height2 < height && agelimit2 <= agelimit)) {
    alert("Almost a perfect partner");
} 
if (height2 < height && agelimit2 > agelimit) {
    alert("No");
}