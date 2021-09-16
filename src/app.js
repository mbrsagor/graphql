import express from 'express';
import {graphqlHTTP} from 'express-graphql';
import resolvers from './resolvers';
import schema from './schema';


const app = express();

app.get('/', (req, res) =>{
    res.send("GraphQl are ready...");
})


// const root = {lco:() => console.log('https://mbrsagorbd.wordpress.com/')}
const root = resolvers;

app.use('/graphql', graphqlHTTP({
    schema:schema,
    rootValue:root,
    graphiql:true,
}))

app.listen(3000, () => console.log("GraphQl server is listening 3000 port"));
