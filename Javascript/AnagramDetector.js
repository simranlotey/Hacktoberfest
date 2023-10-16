function areAnagrams(word1, word2) {
    const cleanWord1 = word1.replace(/\s/g, '').toLowerCase();
    const cleanWord2 = word2.replace(/\s/g, '').toLowerCase();
  
    if (cleanWord1.length !== cleanWord2.length) {
      return false;
    }
  
    const sortedWord1 = cleanWord1.split('').sort().join('');
    const sortedWord2 = cleanWord2.split('').sort().join('');
  
    return sortedWord1 === sortedWord2;
  }
  
  const word1 = "listen";
  const word2 = "silent";
  
  if (areAnagrams(word1, word2)) {
    console.log(`${word1} and ${word2} are anagrams.`);
  } else {
    console.log(`${word1} and ${word2} are not anagrams.`);
  }
