let fruits = ["apple", "banana", "cherry", "grape", "mango"];
console.log(fruits[0]);
console.log(fruits[fruits.length - 1]);
console.log(fruits.length);


let colors = ["red", "green", "blue"];
colors.push("yellow");
colors.shift();
colors.unshift("purple");
console.log(colors);


let arr = [2, 3, 4, 5];
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i] * 2);
}



function getRandom() {
    return Math.floor(Math.random() * 10) + 1;
}
console.log(getRandom());

let movies = ["Inception", "Interstellar", "Gladiator", "Joker", "Matrix"];
let userMovie = prompt("Type a movie name:");
if (movies.includes(userMovie)) {
    alert("Yes, it's one of my favorites!");
} else {
    alert("No, I don't like that one much.");
}




let words = ["banana", "apple", "pear", "orange"];
words.sort();
let result = words.join(", ");
console.log(result);




let narr = [2, 3, 4, 5, 6];
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i] * 2);
}



function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}
console.log(sumArray([1, 2, 3]));






function findLargest(arr) {
    let largest = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }
    return largest;
}
console.log(findLargest([4, 7, 2, 9, 5]));