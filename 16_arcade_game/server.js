const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.use(express.static(path.resolve(__dirname, 'public')));
app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'index.html'));
});

app.post('/givemetheFlag', (req, res) => {
    try {
        const bodyString = JSON.stringify(req.body).toLowerCase();
        if (bodyString.includes("cryptonite") && bodyString.includes("5")) {
            return res.json({ errorMessage: 'Well Done Player! Here\'s your prize: OASIS{G37_d035_n07_4lw4y5_G37_th1ng5} for knowing about them' });
        } else {
            return res.json({ errorMessage: 'Answer not found' });
        }
    } catch (error) {
        return res.json({ errorMessage: 'Invalid format' });
    }
});

app.post('/game', (req, res) => {
    if (req.headers['user-agent'] !== 'OASISPlayer') {
        return res.json({ errorMessage: "You need to be OASISPlayer to start the game" });
    }
    if (req.headers['x-tes-custom'] !== '127.0.0.1') {
        return res.json({ errorMessage: "Riddle me this, why are you originating from outside?" });
    }
    return res.json({ errorMessage: "Oh you're local! Then give me the name and 2023 CTF ranking of MIT's premier cybersecurity project on /givemetheFlag" });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
