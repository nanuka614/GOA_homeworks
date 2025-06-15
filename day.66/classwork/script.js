function getFormDara() {
    e.preventDefault();

    let form = document.getElementById("main-form")

    let name = form.elements.name.value;
    let surname = form.elements.surname.value;
    let academy = form.elements.sacademy.value;

    console.log(name, surname, academy);

    form.reset();
}