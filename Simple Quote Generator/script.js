const quotes = [
  {
      text: "The only way to do great work is to love what you do.",
      author: "Steve Jobs"
  },
  {
      text: "In three words I can sum up everything I've learned about life: it goes on.",
      author: "Robert Frost"
  },
  {
      text: "Don't watch the clock; do what it does. Keep going.",
      author: "Sam Levenson"
  },
  {
      text: "The only limit to our realization of tomorrow will be our doubts of today.",
      author: "Franklin D. Roosevelt"
  },
  {
      text: "Success is not final, failure is not fatal: It is the courage to continue that counts.",
      author: "Winston Churchill"
  }
];

const quoteElement = document.getElementById("quote");
const authorElement = document.getElementById("author");
const newQuoteButton = document.getElementById("new-quote-button");

function getRandomQuote() {
  const randomIndex = Math.floor(Math.random() * quotes.length);
  const randomQuote = quotes[randomIndex];
  quoteElement.textContent = randomQuote.text;
  authorElement.textContent = `– ${randomQuote.author}`;
}

newQuoteButton.addEventListener("click", getRandomQuote);

// Initial quote when the page loads
getRandomQuote();
