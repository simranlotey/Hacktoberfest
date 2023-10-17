"use strict";
class URLShortener {
    urlMap;
    alphabet;
    ourUrl;
    constructor() {
        this.urlMap = new Map();
        this.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        this.ourUrl = "www.biiitlyy.com/"; // kinda like bitly and other urlShortner link
    }
    encode(longUrl) {
        const key = this.generateRandomKey();
        this.urlMap.set(key, longUrl);
        return this.ourUrl + key; // concat ourUrl and key. then returns
    }
    decode(key) {
        key = key.split(this.ourUrl)[1];
        return this.urlMap.get(key);
    }
    generateRandomKey() {
        let key = '';
        key = Array.from({ length: 6 }, () => this.alphabet[Math.floor(Math.random() * this.alphabet.length)]).join("");
        return this.urlMap.has(key) ? this.generateRandomKey() : key; // checks if key was already made if yes then make a new one else return key
    }
}
const shortner = new URLShortener();
const shortUrl = shortner.encode("www.gogodools.com/helloWorld");
// console.log(shortUrl)
const longUrl = shortner.decode(shortUrl);
// console.log(longUrl)
