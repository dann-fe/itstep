let heading = document.querySelector("#heading");
heading.textContent = "modified heading";

let paragraph = document.querySelectorAll(".paragraph");
console.log(paragraph);
paragraph[1].textContent = "modified paragraph";

let lastParagraph = document.querySelector(".last");
lastParagraph.style.color = "red";
lastParagraph.style.border = "5px solid red";
lastParagraph.style.margin = "50px";
lastParagraph.style.borderRadius = "20px";


heading.classList.add("JS-heading-class");
console.log(heading.classList)