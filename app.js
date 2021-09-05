import express from 'express';

const app = express();

app.get('/', (req, res) =>{
    res.send("GraphQl are ready...");
})

app.listen(3000, () => console.log("GraphQl server is listening 3000 port"));
