function getInputInfo() {
    e.preventDefault();
    let input = document.getElementById("input-main");
    console.log(input.value);
    input.value = "";
}










function conStrings() {
    let username = prompt("enter name")
    let surname = prompt("enter surname")

    alert(username + " " + surname);
}
conStrings()

