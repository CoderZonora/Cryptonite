const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

app.use(express.static(path.join(__dirname, '')));

app.use(express.json());

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/', (req, res) => {
    res.json({ message: 'Got Game! Starting OASIS{G37_d035_n07_4lw4y5_G37_th1ng5}' });
});

/* app.head('/', (req, res) => {
    res.json({ message: 'Error: POST request received!' });
}); */

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
