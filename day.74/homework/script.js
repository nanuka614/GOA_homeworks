let alertButton = document.getElementById('alertButton');
alertButton.addEventListener('click', function() {
    alert('Button was clicked!');
});

let hoverParagraph = document.getElementById('hoverParagraph');
hoverParagraph.addEventListener('mouseover', function() {
    hoverParagraph.textContent = 'Text changed on hover!';
});

let toggleDiv = document.getElementById('toggleDiv');
let isBlue = true;
toggleDiv.addEventListener('click', function() {
    toggleDiv.style.backgroundColor = isBlue ? 'lightgreen' : 'lightblue';
    isBlue = !isBlue;
});

let textInput = document.getElementById('textInput');
textInput.addEventListener('click', function() {
    console.log(textInput.value);
});