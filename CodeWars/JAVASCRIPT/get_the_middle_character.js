/*
    You are going to be given a word. Your job is to return the middle
    character of the word. If the word's length is odd, return the
    middle character. If the word's length is even, return the middle
    2 characters.
*/

function getMiddle(s)
{
  // 7 kyu

  if (s.length % 2 === 0) {
    let middle = Math.round(s.length / 2);
    return s[middle-1] + s[middle];
  } else {
    return s[Math.round(s.length / 2)-1]
  }
}