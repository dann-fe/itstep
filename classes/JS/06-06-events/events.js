let button = document.querySelector("button");
button.style.padding = "300px";

let count = 0;
function typeInConsole() {

    count = count + 1;
    console.log(`button was clicked ${count} times so far!`);
}

let heading = document.querySelector("h1");
function headingColor() {
    heading.style.color = "red";
}

button.addEventListener("click", headingColor);
button.addEventListener("click", typeInConsole);

