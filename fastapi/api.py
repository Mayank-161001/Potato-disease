

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model(r"C:\Users\mayan\OneDrive\Desktop\deeplearning\save_modal\my_model.h5")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

def read_file_as_image(data) -> np.ndarray: #take file and return n dimen array
    image = np.array(Image.open(BytesIO(data)))
    return image

#Image.open(BytesIO(data))---jpeg image provide

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)  #uploadFile is a class, file ki datatype uploadFile hai
):
    image = read_file_as_image(await file.read())
    #image=(255,255,3) ki array
    img_batch = np.expand_dims(image, 0)
    # dimention expend 0-> one dimention extend 1d to 2d this single imahe but our model take batch of file so [[njdfjb]]
    
    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
