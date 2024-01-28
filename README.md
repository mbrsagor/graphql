# graphql
> JavaScript Graphql Repo.

###### What is Graphql?
This is my simple `GraphQL` web-app which has very quite and simple example of graphql user management system. Be like `Query` and `Mutation` basic operations.

##### Download the repository and run the `Backend` application in your local machine:
please follow the below instructions:

```bash
git clone https://github.com/mbrsagor/graphql.git
cd graphql/server
yarn install
yarn dev
```
Runs the app in the development mode.\
Open [http://localhost:4000](http://localhost:4000) to view it in the browser.

##### Run the `Frontend` part:
```bash
cd client
yarn install
yarn start
```
Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

###### For the `Query` response body:
```javascript
query {
  users {
    id
    name
    email
    age
  }
}
```
###### For the `Mutation` (create/post) response body:
```javascript
mutation {
  createUser(id: 6, name: "Mamun-khan", email: "mamun@gmail.com", age: 29) {
    id
    name
    email
    age
  }
}
```

#### Example of GraphQL if you want to create new one backend:
> Basically if you want to setup newly I recommend you please follow the below instructions:
```bash
yarn init 
yarn add --dev graphpack
```
Then add the code for you project `package.json` file.
```json
"scripts": {
    "dev": "graphpack",
    "build": "graphpack build"
}
```
N:B: Then continue to the following steps which possesses my project `src` directory.


```bash
npm install graphql
```
Then:
```javascript
var { graphql, buildSchema } = require('graphql');

var schema = buildSchema(`
  type Query {
    sagor: String
  }
`);

var root = { sagor: () => 'Hello Sagor!' };

graphql(schema, '{ sagor }', root).then((response) => {
  console.log(response);
});
```

> Frontend
```javascript
import {
  graphql,
  GraphQLSchema,
  GraphQLObjectType,
  GraphQLString,
} from 'graphql';

var schema = new GraphQLSchema({
  query: new GraphQLObjectType({
    name: 'RootQueryType',
    fields: {
      hello: {
        type: GraphQLString,
        resolve() {
          return 'world';
        },
      },
    },
  }),
});
```
