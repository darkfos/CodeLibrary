function squareDigits(num){
  // 7kyu
  let result = "";
  
  for (let numb of String(num)) {
    result += (Number(numb)**2);
  }
  return Number(result);
}