from roboflow import Roboflow
from dotenv import dotenv_values


config = dotenv_values('../.env')

rf = Roboflow(api_key=config['API_KEY'])
project = rf.workspace().project('playing-cards-ow27d')
model = project.version(4).model

# infer on a local image
print(model.predict('playing_card.jpg', confidence=40, overlap=30).json())

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
