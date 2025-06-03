function discountFunc() {
    let age = prompt("enter your age:");

if (age<18) {
    console.log("20%")
}
else if (age>=18 && age<65){
    console.log("5%")
}
else {
    console.log("10%")
}
}