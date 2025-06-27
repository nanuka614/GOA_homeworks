let count = 10;
let countdown = setInterval(() => {
    console.log(count);
    count--;
    if (count < 0) {
        clearInterval(countdown);
        console.log("Time's up!");
    }
}, 1000);




let toggle = true;
let flashCount = 0;
let flash = setInterval(() => {
    document.title = toggle ? "Hello" : "Goodbye";
    toggle = !toggle;
    flashCount++;
    if (flashCount === 6) clearInterval(flash);
}, 1000);




let position = 0;
let box = document.getElementById("box");
let move = setInterval(() => {
    position += 10;
    box.style.left = position + "px";
    if (position >= 100) clearInterval(move);
}, 200);




let randomCount = 0;
let randomInterval = setInterval(() => {
    let num = Math.floor(Math.random() * 10) + 1;
    console.log(num);
    randomCount++;
    if (randomCount === 5) clearInterval(randomInterval);
}, 1500);




let words = ["apple", "banana", "cherry"];
for (let i = 0; i < words.length; i++) {
    console.log(words[i].toUpperCase());
}



let numbers = [1, 2, 3];
numbers[1] = 0;
console.log(numbers);




let arr = ["a", "b"];
arr.push("c");     
arr.unshift("z"); 
arr.pop();         
console.log(arr);




let nums = [10, 20, 30, 40];
let sum = 0;
for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
}
let avg = sum / nums.length;
console.log("Average:", avg);




let elements = ["x", "y", "z"];
console.log(elements[2]);
console.log(elements[1]);
console.log(elements[0]);