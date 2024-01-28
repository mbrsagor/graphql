import { GraphQLClient } from 'graphql-request'

const document = gql`
  {
    company {
      ceo
    }
  }
`
const client = new GraphQLClient(endpoint)
await request('https://api.spacex.land/graphql/', document)
