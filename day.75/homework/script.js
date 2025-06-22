let count = 1;
let counterInterval = setInterval(() => {
    console.log(count);
    count++;
    if (count > 5) {
        clearInterval(counterInterval);
    }
}, 1000);



let messageInterval = setInterval(() => {
    console.log('Hello every 2 seconds');
}, 2000);

setTimeout(() => {
    clearInterval(messageInterval);
}, 10000);



let colors = ['blue', 'green', 'pink', 'yellow', 'gray'];
let colorIndex = 0;
let colorChangeCount = 0;

let colorInterval = setInterval(() => {
    document.body.style.backgroundColor = colors[colorIndex % colors.length];
    colorIndex++;
    colorChangeCount++;
    if (colorChangeCount === 5) {
        clearInterval(colorInterval);
    }
}, 3000);



let timeInterval = setInterval(() => {
    let now = new Date();
    console.log(now.toLocaleTimeString());
}, 1000);

setTimeout(() => {
    clearInterval(timeInterval);
}, 15000);



let timer = 0;
let timerInterval = setInterval(() => {
    timer++;
    console.log('Timer:', timer);
    if (timer === 10) {
        clearInterval(timerInterval);
    }
}, 1000);