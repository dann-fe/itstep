console.log("OOP = object oriented programming")
// const jmeno = "Alik";
// let weight = 15;
// let age = 1;
// const color = "red";
// const breed  = "akita";

let dog1 = {
    jmeno: "Alik",
    weight: 15,
    age: 1,
    color: "red",
    breed: "akita",
    isAgressive: false,
    bark: function () {  //function inside an object = method
        console.log("woof")
    },
    describe: function () {
       return `this is my dog ${this.jmeno} and its a ${this.color} ${this.breed}`
    } 
    
}

let dog2 = {
    jmeno: "ferdinand",
    weight: 2,
    age: 13,
    color: "black",
    breed: "civava",
    isAgressive: true,
    friend: dog1,
    bark: function () {  //function inside an object = method
        console.log("woof")
    },
    describe: function () {
        return `this is my dog ${this.jmeno} and its a ${this.color} ${this.breed}`
     } 
}

dog1.friend = dog2;
const dogInfo = () => {
    console.log(`this is my dog ${dog1.jmeno} and its a ${dog1.color} ${dog1.breed}`)
}
dog1.jmeno = "aliiik";


dogInfo();

dog1.bark