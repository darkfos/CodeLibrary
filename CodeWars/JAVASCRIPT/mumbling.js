/*
  This time no story, no theory. The examples below
  show you how to write function accum:
  The parameter of accum is a string which includes
  only letters from a..z and A..Z.
*/

function accum(s) {
  // 7 kyu

	let resultString = "";

  for (let el in s) {
    resultString += (s[el].toUpperCase()+s[el].toLowerCase().repeat(el)+"-");
  }
  return resultString.slice(0, -1);
}