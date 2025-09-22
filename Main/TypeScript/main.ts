export {};
function val(): "k" | "l" | "m" {
    // Simulating a function that returns one of the specified string literals
    return "k";
}       

let data: "k" | "l" | "m" = val();

switch(data){
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