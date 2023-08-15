const express = require("express");
const fs = require("fs");
const path = require("path");
const stream = require("stream");

const IMAGES_DIR = path.join(__dirname, "..", "images");

const app = express();
app.use(express.json());

app.get("/images", async (req, res, next) => {
  const files = fs.readdirSync(IMAGES_DIR);

  const filesObj = {};

  for (const file of files) {
    const [name, ext] = file.split(".");

    if (!filesObj.hasOwnProperty(name)) filesObj[name] = {};

    if (ext === "txt") {
      const caption = fs.readFileSync(path.join(IMAGES_DIR, file), "utf-8");
      filesObj[name].caption = caption;
    } else if (ext === "png") {
      filesObj[name].image = file;
    }
  }

  return res.json(filesObj);
});

app.patch("/caption/:id", async (req, res, next) => {
  const { caption } = req.body;
  const id = req.params.id;

  console.log(id, "->", caption);

  const targetFile = path.join(IMAGES_DIR, `${id}.txt`);
  fs.writeFileSync(targetFile, caption, { encoding: "utf-8", flag: "w" });

  res.sendStatus(200);
});

app.delete("/caption/:id", async (req, res, next) => {
  const id = req.params.id;

  console.log(id, "-> Deleted");

  const targetCaptionFile = path.join(IMAGES_DIR, `${id}.txt`);
  const targetImageFile = path.join(IMAGES_DIR, `${id}.png`);

  fs.existsSync(targetCaptionFile) && fs.unlinkSync(targetCaptionFile);
  fs.existsSync(targetImageFile) && fs.unlinkSync(targetImageFile);

  res.sendStatus(200);
});

app.get("/file/:filename", async (req, res, next) => {
  res.sendFile(path.join(IMAGES_DIR, req.params.filename));
});

app.get("/", async (req, res, next) => {
  res.sendFile(path.join(__dirname, "/index.html"));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
