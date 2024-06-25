const buttons = document.querySelectorAll(".colorful");
const newButton = document.querySelector(".add");
const div = document.querySelector(".buttons")
let count = 5;
function createButton () {
    count++;
    let button = document.createElement("button");
    button.classList.add("colorful");
    button.textContent = `click ${count}`;
    div.append(button);
}

function handleClick(event) {
    if (event.target.nodeName !== "BUTTON") return;
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove("red");
    }
    event.target.classList.add("red");
}

div.addEventListener("click", handleClick)

buttons[0].addEventListener("click", handleClick);
buttons[1].addEventListener("click", handleClick);
buttons[2].addEventListener("click", handleClick);
buttons[3].addEventListener("click", handleClick);
buttons[4].addEventListener("click", handleClick);
newButton.addEventListener("click", createButton)
for (let i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener("click", handleClick);
}