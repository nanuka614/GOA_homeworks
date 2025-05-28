let obj = {
    name: "nika",
    surname: "bendeliani",
    academy: "goa academy",
    city: "Tbilisi",
    role: "Student",
    favColor: "red",

    fullName () {
        console.log(this.name + " " + this.surname);
    },

    showFavColor () {
        console.log( this.favColor);
    }
}

console.log(obj);
console.log(obj.city);
obj.fullName();

obj.favColor = "green";
console.log(obj.favColor);

obj.showFavColor();

function userOperations() {
    let answer1 = true;
    let answer2 = false;

    console.log(answer1 && answer2);
    console.log( answer1 || answer2);
}

window.onload = userOperations;