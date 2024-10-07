function getCount(str) {
    // 7kyu
    let counter = 0;
    
    for (let s of str) {
      if ("aeiou".indexOf(s.toLowerCase()) != -1) {
        counter += 1;
      }
    }
    return counter;
  }