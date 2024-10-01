import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Normalization
def normalize_image(image):
    return image / 255.0

# Augmentation (rotation, flip, zoom)
datagen = ImageDataGenerator(
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest'
)

# Apply the augmentation to training data
def augment_data(image):
    image = np.expand_dims(image, 0)  # Expanding dimensions for datagen flow
    augmented_image = datagen.flow(image, batch_size=1)[0].astype('float32')
    return augmented_image
