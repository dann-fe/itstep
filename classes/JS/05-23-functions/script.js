

function sayHi(jmeno, movie) {
    console.log("Hello " + jmeno +", Welcome!");
    console.log("Hi");
    console.log("How are you");
    console.log("good morning");
    console.log("would you like to watch " + movie);
    console.log("good night");
    console.log("\n");
    if (movie === undefined) {
        alert("no movie selected!");
    }
}


sayHi("Dan", "taxi driver");
sayHi("Daniel");