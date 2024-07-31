const canvas = document.querySelector("canvas")
const eraseButton = document.querySelector("button")
const context = canvas.getContext("2d");
let x = Math.random() * canvas.width;
let y = Math.random() * canvas.height;
// const {width, height} = canvas;

context.lineCap = "round";
context.lineJoin = "round";
context.lineWidth = 5;

context.beginPath();
context.moveTo(100, 100);
context.lineTo(x, y);
context.stroke();


function erasing () {
    context.reset();
}

function handleClick (event) {
    console.log(event);
}
window.addEventListener("keypress", handleClick);

eraseButton.addEventListener("click", handleClick);

