let table = document.querySelector("table");
let tableContent = "";

for (let i = 1000; i>0; i--) {
    tableContent += "<tr>";
    for (let j = 1; j<= 10; j++ )
    tableContent += `<td>${i*j}</td>`;
    tableContent += "</tr>"
}


table.innerHTML = tableContent;

let index = 5;
while (index <= 15) {
    console.log(index);
    index++;
}

  