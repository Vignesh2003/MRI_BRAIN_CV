from fastapi import FastAPI, File, UploadFile
from io import BytesIO
import numpy as np
from PIL import Image
import uvicorn

app = FastAPI()

# Load the trained model (assuming it's already saved)
# model = tf.keras.models.load_model('best_model.h5', custom_objects={'dice_score': dice_score})

def read_imagefile(file) -> Image.Image:
    return Image.open(BytesIO(file))

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = read_imagefile(await file.read())
    image = image.resize((256, 256))  # Assuming input shape
    image = np.expand_dims(np.array(image), axis=0)
    
    # Get prediction from model
    # pred = model.predict(image)
    
    return {"result": "segmentation"}  # Example, replace with actual result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
