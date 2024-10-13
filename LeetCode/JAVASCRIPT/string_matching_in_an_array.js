/*
    Given an array of string words, return all strings in
    words that is a substring of another word. You can
    return the answer in any order.

    A substring is a contiguous sequence of characters
    within a string
*/

/**
 * @param {string[]} words
 * @return {string[]}
 */
var stringMatching = function(words) {
    // Easy

    let substrings = new Set();
    words.map((el, indx) => {
        for (let i = 0; i < words.length; i++) {
            if (words[i].includes(el) && words[i] !== el) {
                substrings.add(el);
            }
        }
    })
    return Array(...substrings)
};