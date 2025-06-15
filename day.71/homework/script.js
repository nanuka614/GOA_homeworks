for (let i = 1; i <= 10; i++) {
    console.log(i);
}

let even = 2;
while (even <= 20) {
    console.log(even);
    even += 2;
}

for (let i = 10; i >= 1; i--) {
    console.log(i);
}

let count = 1;
while (count <= 5) {
    console.log(count * 3);
    count++;
}

let str = "Hello";
for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
}


function changeColor() {
    document.getElementById("colorDiv").style.backgroundColor = "skyblue";
}

function changeFontSize() {
    document.getElementById("myHeading").style.fontSize = "36px";
}

function hideDiv() {
    document.getElementById("hideDiv").style.display = "none";
}

function showAlert() {
    alert("This is a custom alert message.");
}