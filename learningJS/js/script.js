
function changeColor (newColor){
    var element = document.getElementById("text");
    element.style.color = newColor;
}

function validationForm(){
    var fname = document.forms["myForm"]["fname"].value;
    var sname = document.forms["myForm"]["sname"].value;
    if (fname == "" && sname == ""){
        alert("Вы не ввели ничего");
        return false;
    } else if(fname == ""){
        alert("Вы не ввели имя")
        return false;
    } else if(sname == ""){
        alert("Вы не ввели фамилию")
        return false;
    }


}












// for (var i=0; i<10; i++){
//     console.log(i);
// }
// var i = 0
// while (i < 10){
//     console.log(i);
//     i++
// }
// var i = 1
// do {
//     console.log("hello igor");
// }while (i > 10);
// var clock = ["hello", "igor", "how's", "life", "?"];
// var i = 0
//
// for (i; i < clock.length; i++){
//     document.write(clock[i] + " ")
// }
// var n1 = prompt("Введите первое число");
// var n2 = prompt("Введите второе число");

// if (Number(n1) == Number(n2)){
//     document.write("Числа " + n1 + " и " + n2 + " равны!");
// } else if ((Number(n1) < Number(n2)) || (Number(n1) > Number(n2))) {
//     document.write("Эти числа не равны")
// } else{
//     document.write("Это вообще не числа")
// }




// if (false){
//     console.log("http response")
// }else if( true ){
//     console.log("http else if")
// }
// else {
//     console.log("http not response")
// }

// var asdf = Number(prompt("Input your value"));
// console.log(asdf, typeof (asdf));
// switch (asdf){
//     case 1:
//         document.write("your value is 1");
//         break;
//     case 2:
//         document.write("your value is 2");
//         break;
//     case 3:
//         document.write("your value is 3");
//         break;
//     case 4:
//         document.write("your value is 4");
//         break;
//     case 5:
//         document.write("your value is 5");
//         break;
//     case 6:
//         document.write("your value is 6");
//         break;
//     case 7:
//         document.write("your value is 7");
//         break;
//     case 8:
//         document.write("your value is 8");
//         break;
//     case 9:
//         document.write("your value is 9");
//         break;
//     default:
//         document.write("It is out of range");// default писать не обязательно, если не нужны определенные значения
// }


//
// function dw(a){
//     document.write(a)
// }
//
// dw("htllo how is life?")


// var person = {
//     first_name: "Igor",
//     age: 21,
//     children: ["Alyona", "Mariah"],
//     address: {
//         street: "Baxodirxon 25",
//         city: "Samarkand",
//         country: "Uzbekistan"
//     },
//     NameChildren: function (){
//         return this.first_name + " and children " + this.children
//     }
// }
// console.log(person.NameChildren())


// function mf(name, age, children){
//     this.name = name;
//     this.age = age;
//     this.children = children;
//     this.I = "Very smart!!!"
// }
//
// var apple = Object();
// apple.color = "Green";
// apple.shape = "round";
// apple.taste = "delicious";
// apple.describe = function (){
//     return "An apple is " + this.taste + " and it's " + this.shape
//
// }
//
// // console.log(apple.describe());
// myname = mf("Igor", 21, "Alyona")
// console.log(myname)



// var num = "htllo worldasd";
// console.log(num);

// var name = prompt("Введите ваше имя ...")

// console.log("Ваше имя - " + name)


// var firstNum = 12;
// var secondNum = 23;
//
// var colors = ["red", "blue", "yellow"];
// var colors2 = new Array ("red", "green", "black");
// colors2.push("pink");
//
//
//
//
//
// document.write(colors2 + "<br>");
//


// document.write("Результат сложения программы - ", firstNum + secondNum)









// "use strict" - объявляется в начале файла и переводит весь скрипт в строгий режим
// var - устаревшее объявление переменной
// let - современное объявление переменной
// const - объявление константы, значение которой нельзя поменять,
// хорошая практика использования констант в ВЕРХНЕМ регистре для "жестко закодированных значение(цветов)"
// const bigInt = 1234567890123456789012345678901234567890n - определяется bigInt(огромное значение числа
        // В строках есть еще обратные кавычки
// let str = "Привет";
// let str2 = 'Одинарные кавычки тоже подойдут';
// let phrase = `Обратные кавычки позволяют встраивать переменные ${str}`;

// значение "null" показывает ничего, пусто, не имеет ссылки на объект
// значение "undefined" представляет что "значение не было присвоено(если
// переменная объявлена, но ей не присвоено никакого значения)


//          преобразование типов:
// String(num)
// Number(str)
// Boolean(sdf)     - любая не пустая строка возвращает true
// || оператор ИЛИ
// && оператор И




