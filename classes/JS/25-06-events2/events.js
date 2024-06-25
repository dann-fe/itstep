const buttons = document.querySelectorAll("button");
const heading = document.querySelector("h1");

//event handler
function handleClick(event) {
    for (let i = 0; i < buttons.length; i++) {
        buttons[i].classList.remove("red");
    }
    console.log("clicked");
    console.log(event.target);
    console.log(`the coordinates are ${event.x}x and ${event.y}y`);
    event.target.classList.add("red");
}

buttons[0].addEventListener("click", handleClick);
buttons[1].addEventListener("click", handleClick);
buttons[2].addEventListener("click", handleClick);
buttons[3].addEventListener("click", handleClick);
buttons[4].addEventListener("click", handleClick);



    setTimeout (() => {
    heading.classList.toggle("red")
}, 1000);


function handleMouseEnter (event)  {
    console.log("handleMouseEnter");
    console.log(event);
    console.log(event.target);
}

heading.addEventListener("mouseenter", handleMouseEnter)

