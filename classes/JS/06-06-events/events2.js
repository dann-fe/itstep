let button = document.querySelector("button");
let heading = document.querySelector("h1");
let paragraph = document.querySelector("p");

// function headingColor() {
//     heading.style.color = "red";
// }

function redBackground() {
    heading.classList.toggle("red"); 
}


heading.addEventListener("click",redBackground);
button.addEventListener("click", redBackground);
paragraph.addEventListener("mousemove", function () {
    paragraph.classList.add("red"); 
});
paragraph.addEventListener("mouseleave", function () {
    paragraph.classList.remove("red"); 
});