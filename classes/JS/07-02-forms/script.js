const input = document.querySelector(".main-input");
const paragraph = document.querySelector(".paragraph");
const checkbox = document.querySelector('[type="checkbox"]');

input.addEventListener("change" /*"input" "focus" "blur"*/, function(event) {
    const value = event.target.value;
    console.log(value);
    // paragraph.textContent = value;
    paragraph.innerHTML = `<p>is your name ${value}?</p>`;
})

checkbox.addEventListener("input", function(event){
    console.log(event.target.checked);
})