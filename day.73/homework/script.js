let p = document.createElement('p');
p.textContent = 'This is a new paragraph.';
document.body.appendChild(p);



let h1 = document.createElement('h1');
h1.textContent = 'Hello from H1';
document.getElementById('myDiv').appendChild(h1);



let button = document.createElement('button');
button.textContent = 'Click me';
document.body.appendChild(button);



let ul = document.createElement('ul');
let li1 = document.createElement('li');
li1.textContent = 'Item 1';
let li2 = document.createElement('li');
li2.textContent = 'Item 2';
let li3 = document.createElement('li');
li3.textContent = 'Item 3';
ul.appendChild(li1);
ul.appendChild(li2);
ul.appendChild(li3);
document.body.appendChild(ul);



let contentDiv = document.getElementById('content');
let firstChild = contentDiv.firstElementChild;
contentDiv.removeChild(firstChild);



let list = document.createElement('ul');
let l1 = document.createElement('li');
l1.textContent = 'One';
let l2 = document.createElement('li');
l2.textContent = 'Two';
let l3 = document.createElement('li');
l3.textContent = 'Three';
list.appendChild(l1);
list.appendChild(l2);
list.appendChild(l3);
document.body.appendChild(list);
list.removeChild(list.lastElementChild);



let newP = document.createElement('p');
newP.textContent = 'New paragraph';
let textContainer = document.getElementById('textContainer');
let oldP = textContainer.querySelector('p');
textContainer.replaceChild(newP, oldP);



let newSpan = document.createElement('span');
newSpan.textContent = 'New Span';
let buttonDiv = document.getElementById('buttonDiv');
let oldButton = buttonDiv.querySelector('button');
buttonDiv.replaceChild(newSpan, oldButton);



let newLi = document.createElement('li');
newLi.textContent = 'New List Item';
let singleList = document.getElementById('singleItemList');
let oldLi = singleList.querySelector('li');
singleList.replaceChild(newLi, oldLi);



let newHeading = document.createElement('h1');
newHeading.textContent = 'New H1 Heading';
let headingDiv = document.getElementById('headingDiv');
let oldHeading = headingDiv.querySelector('h2');
headingDiv.replaceChild(newHeading, oldHeading);