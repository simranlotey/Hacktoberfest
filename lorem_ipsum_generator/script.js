const tagOptions = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "span"];

const optionsContainer = document.querySelector(".options");
const outputContainer = document.querySelector(".output");
const tagsSelect = document.getElementById("tags");
const paragraphsSlider = document.getElementById("paragraphs");
const wordsSlider = document.getElementById("words");
const paragraphsValue = document.getElementById("paragraphsValue");
const wordsValue = document.getElementById("wordsValue");

const languages = {
    latin: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    english: "The quick brown fox jumps over the lazy dog. A wizard's job is to vex chumps quickly in fog. Watch Jeopardy!, Alex Trebek's fun TV quiz game. How vexingly quick daft zebras jump!",
    spanish: "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja. Fabio me exige, sin tapujos, que añada cerveza al whisky."
};

function createOptionsUI() {
    tagOptions.forEach((tag) => {
        const option = document.createElement("option");
        option.value = tag;
        option.textContent = `<${tag}>`;
        tagsSelect.appendChild(option);
    });

    paragraphsSlider.addEventListener("input", updateParagraphsValue);
    wordsSlider.addEventListener("input", updateWordsValue);

    const generateButton = document.getElementById("generate");
    generateButton.addEventListener("click", generateLoremIpsum);
}

function updateParagraphsValue() {
    paragraphsValue.textContent = paragraphsSlider.value;
}

function updateWordsValue() {
    wordsValue.textContent = wordsSlider.value;
}

function generateLoremIpsum() {
    outputContainer.innerHTML = '<p>Generating Lorem Ipsum...</p>';
    
    setTimeout(() => {
        try {
            const paragraphs = parseInt(paragraphsSlider.value);
            const tag = document.getElementById("tags").value;
            const includeHtml = document.getElementById("include").value;
            const wordsPerParagraph = parseInt(wordsSlider.value);
            const customText = document.getElementById("customText").value.trim();
            const language = document.getElementById("language").value;

            const loremIpsumText = generateText(paragraphs, tag, includeHtml, wordsPerParagraph, customText, language);
            displayLoremIpsum(loremIpsumText);
        } catch (error) {
            console.error('Error generating Lorem Ipsum:', error);
            outputContainer.innerHTML = '<p style="color: red;">An error occurred while generating Lorem Ipsum. Please try again.</p>';
        }
    }, 10);
}

function generateText(paragraphs, tag, includeHtml, wordsPerParagraph, customText, language) {
    const loremIpsumArray = new Array(paragraphs).fill("").map(() => {
        const words = generateWords(wordsPerParagraph, customText, language);
        return includeHtml === "Yes" ? `<${tag}>${words}</${tag}>` : words;
    });

    return loremIpsumArray.join("\n");
}

function generateWords(numWords, customText, language) {
    const baseText = customText || languages[language];
    const words = baseText.split(/\s+/);
    
    let result = [];
    while (result.length < numWords) {
        const remainingWords = numWords - result.length;
        const startIndex = Math.floor(Math.random() * (words.length - remainingWords + 1));
        result = result.concat(words.slice(startIndex, startIndex + remainingWords));
    }
    
    return formatText(result.join(" "));
}

function formatText(text) {
    if (document.getElementById("uppercase").checked) {
        text = text.toUpperCase();
    }
    if (document.getElementById("capitalize").checked) {
        text = text.replace(/(^\w|\.\s+\w)/gm, letter => letter.toUpperCase());
    }
    return text;
}

function displayLoremIpsum(text) {
    const wordCount = text.split(/\s+/).length;
    outputContainer.innerHTML = `
        <div class="word-count">Total words: ${wordCount}</div>
        ${text}
    `;
    
    const copyButton = document.createElement('button');
    copyButton.textContent = 'Copy to Clipboard';
    copyButton.addEventListener('click', () => {
        navigator.clipboard.writeText(text).then(() => {
            copyButton.textContent = 'Copied!';
            setTimeout(() => {
                copyButton.textContent = 'Copy to Clipboard';
            }, 2000);
        });
    });
    
    outputContainer.appendChild(copyButton);
    
    const saveButton = document.createElement('button');
    saveButton.textContent = 'Save as File';
    saveButton.addEventListener('click', () => {
        const fileType = document.getElementById("include").value === "Yes" ? "html" : "txt";
        saveAsFile(text, fileType);
    });
    
    outputContainer.appendChild(saveButton);
}

function savePreferences() {
    localStorage.setItem('paragraphs', paragraphsSlider.value);
    localStorage.setItem('words', wordsSlider.value);
    localStorage.setItem('tag', tagsSelect.value);
    localStorage.setItem('includeHtml', document.getElementById("include").value);
}

function loadPreferences() {
    paragraphsSlider.value = localStorage.getItem('paragraphs') || 1;
    wordsSlider.value = localStorage.getItem('words') || 10;
    tagsSelect.value = localStorage.getItem('tag') || 'p';
    document.getElementById("include").value = localStorage.getItem('includeHtml') || 'Yes';
    
    updateParagraphsValue();
    updateWordsValue();
}

paragraphsSlider.addEventListener('change', savePreferences);
wordsSlider.addEventListener('change', savePreferences);
tagsSelect.addEventListener('change', savePreferences);
document.getElementById("include").addEventListener('change', savePreferences);

loadPreferences();

createOptionsUI();

const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

darkModeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    localStorage.setItem('dark-mode', body.classList.contains('dark-mode'));
});

if (localStorage.getItem('dark-mode') === 'true') {
    body.classList.add('dark-mode');
}

function saveAsFile(text, fileType) {
    const blob = new Blob([text], { type: `text/${fileType}` });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `lorem-ipsum.${fileType}`;
    link.click();
}