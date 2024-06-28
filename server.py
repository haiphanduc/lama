import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()
import uuid
import example

IMAGERDIR = "src/input/"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    with open(f"{IMAGERDIR}{file.filename}", "wb") as f:
        f.write(contents)

        return FileResponse(f"{IMAGERDIR}{file.filename}")


@app.post("/file_uploading")
async def upload_file(file: UploadFile = File(...),mask: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.png"
    # contents = await file.read()
    #
    # with open(f"{IMAGERDIR}{file.filename}", "wb") as f:
    #     f.write(contents)

    mask.filename = f"{uuid.uuid4()}.png"
    # contents1 = await mask.read()
    #
    # with open(f"{IMAGERDIR}{mask.filename}", "wb") as f:
    #     f.write(contents1)

    # url = IMAGERDIR+""+file.filename
    # url_mask = IMAGERDIR+""+mask.filename
    path = await example.removeObject(file,mask,file.filename)
    return FileResponse(f"{path}")

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.0.247", port=8000)
