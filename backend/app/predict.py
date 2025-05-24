import torch
from torchvision import transforms
from PIL import Image
from io import BytesIO
from app.model import CurrencyCNN
from app.utils import preprocess_image

model = CurrencyCNN()
model.load_state_dict(torch.load("model/currency_cnn.pth", map_location=torch.device('cpu')))
model.eval()

classes = ["Fake", "Real"]

def predict_currency_note(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert("RGB")
    tensor = preprocess_image(image)
    with torch.no_grad():
        output = model(tensor)
        _, predicted = torch.max(output, 1)
    return classes[predicted.item()]
