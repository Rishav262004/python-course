// Function to call the translation API
async function translateText(text, sourceLang, targetLang) {
    const response = await fetch(`https://translate.googleapis.com/translate_a/single?client=gtx&sl=${sourceLang}&tl=${targetLang}&dt=t&q=${encodeURIComponent(text)}`);
    const result = await response.json();
    return result[0][0][0];
}

// Event listeners for buttons
document.getElementById('translateToEnglish').addEventListener('click', async () => {
    const inputText = document.getElementById('inputText').value;
    if (inputText) {
        const translation = await translateText(inputText, 'hi', 'en');
        document.getElementById('outputText').textContent = translation;
    }
});

document.getElementById('translateToHindi').addEventListener('click', async () => {
    const inputText = document.getElementById('inputText').value;
    if (inputText) {
        const translation = await translateText(inputText, 'en', 'hi');
        document.getElementById('outputText').textContent = translation;
    }
});
