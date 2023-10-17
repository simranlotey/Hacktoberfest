class URLShortener{
    private urlMap: Map<string,string>;
    private readonly alphabet: string;
    private readonly ourUrl: string;

    constructor(){
        this.urlMap = new Map()
        this.alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        this.ourUrl = "www.biiitlyy.com/"  // kinda like bitly and other urlShortner link
    }

    encode(longUrl:string):string{
        const key = this.generateRandomKey();
        this.urlMap.set(key, longUrl);
        return this.ourUrl+key;  // concat ourUrl and key. Then returns
    }

    decode(key:string):string | undefined{
        key = key.split(this.ourUrl)[1]
        return this.urlMap.get(key);
    }

    private generateRandomKey():string{
        let key='';
        key = Array.from({length: 6}, ()=> this.alphabet[Math.floor(Math.random() * this.alphabet.length)]).join("")
        return this.urlMap.has(key) ? this.generateRandomKey() : key;  // checks if key was already made if yes then make a new one else return key
    }
}

const shortner = new URLShortener();

const shortUrl = shortner.encode("www.gogodools.com/helloWorld");
// console.log(shortUrl)

const longUrl =  shortner.decode(shortUrl);
// console.log(longUrl)

