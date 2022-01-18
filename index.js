import { postgraphile } from "postgraphile";
import express from "express";
import cors from "cors";
import { generateUploadURL } from "./s3.js";
const app = express();
const port = 5000;

// add cor
app.options("*", cors());
app.use(cors());

app.get("/s3Url", async (req, res) => {
  const { folderName } = req.query;
  console.log("uploading to s3 into folder:", folderName);

  try {
    const url = await generateUploadURL(folderName);
    res.send({ url });
    
  }
  catch(err) {
    console.log(err)
    res.send({});
  }
});

app.get("/envCheck", async (req, res) => {
  res.send(process.env.AWS_ACCESS_KEY_ID || 'nothing')
});

app.use(
  postgraphile(
    process.env.DATABASE_URL ||
      "postgres://postgres:6cqMqw9G1D6wc99b@35.205.136.135:5432/postgres",
    "public",
    {
      watchPg: true,
      graphiql: true,
      enhanceGraphiql: true,
    }
  )
);

app.listen(port, () => console.log("listening on port " + port));
