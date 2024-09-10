let randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;
let highScore = localStorage.getItem('highscore') || Infinity;

document.getElementById('highscoreMessage').innerText = `Highscore: ${highScore === Infinity ? 'No highscore yet' : highScore + ' attempts'}`;

function playGame() {
    const userInput = document.getElementById('userInput').value;
    const resultMessage = document.getElementById('resultMessage');
    const attemptMessage = document.getElementById('attemptMessage');

    if (!userInput || userInput < 1 || userInput > 100) {
        resultMessage.innerText = 'Please enter a valid number between 1 and 100.';
        return;
    }

    attempts++;
    if (userInput > randomNumber) {
        resultMessage.innerText = 'Your guess is too high.';
    } else if (userInput < randomNumber) {
        resultMessage.innerText = 'Your guess is too low.';
    } else {
        resultMessage.innerText = `Congratulations! You guessed the correct number ${randomNumber} in ${attempts} attempts.`;
        checkHighScore();
        document.getElementById('restartButton').classList.remove('hidden');
    }

    attemptMessage.innerText = `Attempts: ${attempts}`;
}

function checkHighScore() {
    if (attempts < highScore) {
        highScore = attempts;
        localStorage.setItem('highscore', highScore);
        document.getElementById('highscoreMessage').innerText = `New Highscore: ${highScore} attempts!`;
    } else {
        document.getElementById('highscoreMessage').innerText = `Highscore: ${highScore} attempts`;
    }
}

function restartGame() {
    attempts = 0;
    randomNumber = Math.floor(Math.random() * 100) + 1;
    document.getElementById('resultMessage').innerText = '';
    document.getElementById('attemptMessage').innerText = '';
    document.getElementById('userInput').value = '';
    document.getElementById('restartButton').classList.add('hidden');
}
