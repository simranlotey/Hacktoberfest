#!/bin/bash

# Password Generator
# To use:
# -> pwdgen.sh lengthValueInString
# E.g: pwdgen.sh 9

all_chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*(_)-+=<>?"

pwd_gen(){
    local password_len="$1"
    local password=""

    for ((i = 0; i < password_len; i++)); do
        # $RANDOM = random num from 0-32767, ${#string} -> gives length, basically generate a index of 0 - str_len -1;
        index=$((RANDOM % ${#all_chars}))
        # extracting text of generated index.
        password="$password${all_chars:index:1}"  
    done

    echo $password
}

pwd_generated=$(pwd_gen $1) 
echo $pwd_generated;


