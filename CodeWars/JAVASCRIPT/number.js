function solve(s){
  // 7 kyu

  let hasMap = {letters: 0, lowercase: 0, numbers: 0, special: 0};

  for (let el of s) {
    if (/[a-zA-Z]/.test(el)) {
      if (el === el.toUpperCase()) {
        hasMap.letters += 1;
      }
      else if (el === el.toLowerCase()) {
        hasMap.lowercase += 1;
      }
    }
    else if (["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].includes(el)) {
      hasMap.numbers += 1;
    }
    else {
      hasMap.special += 1;
    }
  }

  return Object.values(hasMap);
}