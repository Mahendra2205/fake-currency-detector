from fastapi import FastAPI, UploadFile, File
from app.predict import predict_currency_note

app = FastAPI(title="Fake Currency Detector API")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    prediction = predict_currency_note(contents)
    return {"prediction": prediction}
