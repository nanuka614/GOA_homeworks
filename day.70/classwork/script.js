function isVowel() {
    let char = prompt("enter one character")
    let vowels = "aeiouAEIOU"

    if (vowels.includes(char)){
        console.log("character is vowel")
    }
    else{
        console.log("character is consonant")
    }
}


function numsSum() {
    let sum = 0;
    for (let i = 1; i<6; i++){
        console.log(i)
        sum+=i;
    }

    console.log("sum of numbers is", sum)
}