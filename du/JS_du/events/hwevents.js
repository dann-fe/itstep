let button = document.querySelector("button");
let h1 = document.querySelector("h1");
let h2 = document.querySelector("h2");
let paragraph = document.querySelector("p");
h2.classList.add("blue");
paragraph.classList.add("hide-display");
function hideParagraph () {
    paragraph.classList.toggle("hide-display");
}

function redColor () {
    h1.style.color = "red";
}
function redColorDelete () {
    h1.style.color = "black";
}
function toggleBlue () {
    h2.classList.toggle("blue");
}

button.addEventListener("click", hideParagraph);
h1.addEventListener("mousemove", redColor);
h1.addEventListener("mouseleave", redColorDelete);
h2.addEventListener("click", toggleBlue);