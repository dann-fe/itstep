const input = document.getElementById("new-task");
const button = document.querySelector(".add-button")
const list = document.querySelector(".list");


function addNewTask (task) {
    const li = document.createElement("li");
    li.textContent = task;
    li.classList.add("task");
    const div = document.createElement("div");
    const span = document.createElement("span");
    span.textContent = task;
    list.append(li);
}

button.addEventListener("click", function () {
    const newTask = input.value;
    console.log(newTask);
    addNewTask(newTask)
})