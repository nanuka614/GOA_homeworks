let i = 10;
while (i >= 1) {
    document.write(i );
    i--;
}

for (let j = 1; j <= 10; j++) {
    document.write(j );
}

for (let k = 1; k <= 5; k++) {
    document.write(3 * k );
}

for (let l = 10; l >= 1; l--) {
    document.write(l);
}

for (let m = 1; m <= 20; m++) {
    if (m % 2 == 0) {
        document.write(m);
    }
}

let sum = 0;
for (let n = 1; n <= 5; n++) {
    sum = sum + n;
}
document.write(sum);


let num = prompt("Enter a number:");
if (num % 2 == 0) {
    document.write("Even");
} else {
    document.write("Odd");
}

let score = prompt("Enter your score:");
if (score >= 90) {
    document.write("Grade A");
} else if (score >= 80) {
    document.write("Grade B");
} else if (score >= 70) {
    document.write("Grade C");
} else if (score >= 60) {
    document.write("Grade D");
} else {
    document.write("Fail");
}

let n = prompt("Enter a number to check divisibility:");
if (n % 3 == 0 && n % 5 == 0) {
    document.write("Divisible by both");
} else if (n % 3 == 0) {
    document.write("Divisible by 3 only");
} else if (n % 5 == 0) {
    document.write("Divisible by 5 only");
} else {
    document.write("Not divisible by either");
}