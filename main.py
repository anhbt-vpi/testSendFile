from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/file")
async def send_file(file: UploadFile = File(...), text: str = Form(...)):
    return {"filename": file.filename, "string_data": text}