from torchvision import transforms

def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor()
    ])
    return transform(image).unsqueeze(0)
