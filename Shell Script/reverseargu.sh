// QUESTION::  reverse a string using shell script 
// reverse a string is in linux and unix 


  
#!/ bin / bash 

// reading a string 
// using via user input
 
read - p "Enter string:" string 

// getting the length of given string 


    len 
    = $ 
{ 
    #string 
} 


// looping for reversing a string 
// initialize i=len-1 for reversing a string and run till i=0 
// printing in the reverse order of the given string

 
for ((i = $len - 1; i >= 0; i--)) 
    do

    // "${string:$i:1}"extract single character from string.
 
        reverse = "$reverse${string:$i:1}" done 
        echo "$reverse"







