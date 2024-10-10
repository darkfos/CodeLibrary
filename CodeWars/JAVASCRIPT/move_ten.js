/*
    Move every letter in the provided string forward 10 letters through the alphabet.
    If it goes past 'z', start again at 'a'.
    Input will be a string with length > 0.
*/

function moveTen(s) {
  // 7 kyu

  let stringResult = ""
  let arrayLetters = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz".split();
  let isUpper = false;

  for (let el in s) {
    el = s[el];
    if (el === el.toUpperCase()) {
      isUpper = true;
    } else {
      isUpper = false;
    }

    let indx = arrayLetters[0].indexOf(el.toLowerCase()) + 10;
    stringResult += isUpper? arrayLetters[0][indx].toUpperCase(): arrayLetters[0][indx];
  }

  return stringResult
}