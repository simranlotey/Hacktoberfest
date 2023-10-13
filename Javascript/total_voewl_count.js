// count total number of vowels in a string

function countVowels(str) {
    let count = 0;
    const vowels = "aeiou";
    
    for (let char of str.toLowerCase()) {
        if (vowels.includes(char)) {
        count++;
        }
    }
    
    return count;
    }

    console.log(countVowels("hello world")); 