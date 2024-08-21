document.getElementById('startButton').addEventListener('click', function() {
    document.getElementById('errorMessage').classList.remove('hidden');
    setTimeout(function() {
        location.reload();
    }, (1.5 * 1000));
});

const arcadeScreen = document.querySelector('.arcade-screen');

setInterval(() => {
  arcadeScreen.style.opacity = Math.random() > 0.5 ? 1 : 0.5;
}, 100);