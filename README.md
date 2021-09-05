# graphql
> JavaScript Graphql Repo.

###### What is Graphql?
GraphQL is an open-source data query and manipulation language for APIs, and a runtime for fulfilling queries with existing data. GraphQL was developed internally by Facebook in 2012 before being publicly released in 2015.

##### Download the repository and run the application in your local machine:
please follow the below instructions:

```bash
git clone https://github.com/mbrsagor/graphql.git
cd graphql
yarn install
yarn add express graphql express-graphql nanoid
yarn start
```

#### Example of GraphQL:

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
