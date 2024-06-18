/*
    Write a function argumentsLength that returns the count of arguments passed to it.
*/


var argumentsLength = function(...args) {
    #Easy
    let count_elements = 0;
    args.forEach((el) => {
        count_elements++;
    })
    return count_elements
};