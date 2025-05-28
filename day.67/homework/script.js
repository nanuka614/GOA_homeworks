function runTasks() {
    console.clear(); 


    let emptyObj = {};
    console.log("1. Empty Object:", emptyObj);


    let myInfo = {
        name: "John",
        age: 25,
        city: "Tbilisi"
    };
    console.log("2. My Info:", myInfo);
    console.log("3. Name:", myInfo.name);


    myInfo.country = "Georgia";
    console.log("4. Added Country:", myInfo);


    let user = {
        name: "Anna",
        address: {
            city: "Kutaisi",
            zip: "4600"
        }
    };
    console.log("5. Nested Object:", user.address.city);


    myInfo.age = 30;
    console.log("6. Changed Age:", myInfo.age);


    let a = 15, b = 20;
    if (a > 10 && b > 10) {
        console.log("8. Both a and b are greater than 10");
    }


    let x = 5, y = 20;
    if (x > 10 || y > 10) {
        console.log("9. At least one is greater than 10");
    }


    let isOnline = false;
    console.log("10. NOT isOnline:", !isOnline);


    let score = 85;
    let passed = true;
    if (score > 80 && passed && !false) {
        console.log("11. Passed with high score");
    }


    let num = 123;
    let strNum = String(num);
    console.log("12. Number to String:", strNum, typeof strNum);


    let bool = true;
    let strBool = String(bool);
    console.log("13. Boolean to String:", strBool, typeof strBool);


    let str = "456";
    let converted = Number(str);
    console.log("14. String to Number:", converted, typeof converted);
}