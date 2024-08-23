document.getElementById('startButton').addEventListener('click', function() {
    fetch('/game', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ errorMessage: 'Give me a message' }),
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById('errorMessage').innerHTML = data.errorMessage;
    });
    document.getElementById('errorMessage').classList.remove('hidden');
});

const arcadeScreen = document.querySelector('.arcade-screen');

setInterval(() => {
  arcadeScreen.style.opacity = Math.random() > 0.5 ? 1 : 0.5;
}, 100);