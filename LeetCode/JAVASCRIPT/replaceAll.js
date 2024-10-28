/**
 * @param {string} s
 * @return {string}
 */
var modifyString = function(s) {
    /*
    EASY
    
    Given a string s containing only lowercase English letters and the '?' character, convert
    all the '?' characters into lowercase letters such that the final string does not contain
    any consecutive repeating characters. You cannot modify the non '?' characters.
    It is guaranteed that there are no consecutive repeating characters in the given string
    except for '?'.
    Return the final string after all the conversions (possibly zero) have been made. If there
    is more than one solution, return any of them. It can be shown that an answer is always possible with the given constraints.
    */


    let symbols = "abcdefghijklmnopqrstuvwxyz";
    let newString = "";

    for (let word = 0; word < s.length; word++) {
        if (s.at(word) === "?") {
            for (let el = 0; el < symbols.length; el++) {
                if (newString[newString.length-1] !== symbols[el] && s[word+1] !== symbols[el]) {
                    newString += symbols[el];
                    break
                }
            }
        } else {
            newString += s.at(word);
        }
    }

    return newString
};