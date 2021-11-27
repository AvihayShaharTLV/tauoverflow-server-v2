const express = require('express')
const cors = require('cors')
const { postgraphile } = require("postgraphile");
const app = express()
const port = 5000

app.options('*', cors()) 
app.use(cors())

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.use(
    postgraphile(
      process.env.DATABASE_URL || "postgres://postgres:password@localhost:5432/postgres",
      "public",
      {
        watchPg: true,
        graphiql: true,
        enhanceGraphiql: true,
      }
    )
  );


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})

