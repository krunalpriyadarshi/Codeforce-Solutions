export {};


function add(a: string, b: string){
        return a + b;
}

let message : string = "hi";
let additional : string = "there";

console.log(add(message, additional.toUpperCase()));