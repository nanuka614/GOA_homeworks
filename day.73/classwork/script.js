function addNewElement() {
    let div = document.getElementById("div1");
    let button = document.createElement("button");
    let text = button.textContent = ("click me");
    div.appendChild(button);
}

addNewElement()


function removeElement() {
    let div = document.getElementById("div2");
    let button = document.getElementById("button");
    div.removeChild(button);
    let paragraph = document.getElementById('p1');
    let italic = document.createElement('i');
    italic.textContent = 'it is i tag';
    div.replaceChild(italic, paragraph);
}

removeElement()

