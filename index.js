import { postgraphile} from 'postgraphile'
import express from 'express'
import cors from 'cors'
import { generateUploadURL } from './s3.js'
const app = express()
const port = 5000

app.options('*', cors())
app.use(cors())

app.get('/s3Url', async (req, res) => {
  const {folderName} = req.query;
  console.log(folderName)
  const url = await generateUploadURL(folderName)
  res.send({url})
})

// app.use(
//     postgraphile(
//       process.env.DATABASE_URL || "postgres://postgres:password@localhost:5432/postgres",
//       "public",
//       {
//         watchPg: true,
//         graphiql: true,
//         enhanceGraphiql: true,
//       }
//     )
//   );

app.listen(port, () => console.log("listening on port " + port))