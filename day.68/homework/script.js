function checkNumber() {
    let num = Number(document.getElementById("numCheck").value);
    let result = "";

    if (num > 0) {
        result = "The number is positive.";
    } else if (num < 0) {
        result = "The number is negative.";
    } else {
        result = "The number is zero.";
    }

    document.getElementById("numberResult").textContent = result;
}



function checkVoting() {
    let age = Number(document.getElementById("ageCheck").value);
    let message = age >= 18 ? "You can vote!" : "You are not eligible to vote.";
    document.getElementById("votingResult").textContent = message;
}



function compareNumbers() {
    let num1 = Number(document.getElementById("firstNum").value);
    let num2 = Number(document.getElementById("secondNum").value);
    let message = "";

    if (num1 > num2) {
        message = "The first number is larger.";
    } else if (num2 > num1) {
        message = "The second number is larger.";
    } else {
        message = "Both numbers are equal.";
    }

    document.getElementById("compareResult").textContent = message;
}