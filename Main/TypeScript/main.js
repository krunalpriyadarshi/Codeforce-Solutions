"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function val() {
    // Simulating a function that returns one of the specified string literals
    return "k";
}
var data = val();
switch (data) {
    case "k":
        console.log("This is k");
        break;
    case "l":
        console.log("This is l");
        break;
    case "m":
        console.log("This is m");
        break;
    default:
        console.log("This is default");
}
