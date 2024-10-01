from keras.layers import Input, Conv2D, MaxPooling2D, concatenate, UpSampling2D
from keras.models import Model

def conv_block(inputs, filters):
    conv = Conv2D(filters, (3, 3), activation='relu', padding='same')(inputs)
    conv = Conv2D(filters, (3, 3), activation='relu', padding='same')(conv)
    return conv

def nested_unet(input_shape):
    inputs = Input(input_shape)

    conv1 = conv_block(inputs, 64)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = conv_block(pool1, 128)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = conv_block(pool2, 256)
    up2 = UpSampling2D(size=(2, 2))(conv3)
    up2 = concatenate([up2, conv2], axis=3)

    conv4 = conv_block(up2, 128)
    up1 = UpSampling2D(size=(2, 2))(conv4)
    up1 = concatenate([up1, conv1], axis=3)

    conv5 = conv_block(up1, 64)
    outputs = Conv2D(1, (1, 1), activation='sigmoid')(conv5)

    model = Model(inputs=[inputs], outputs=[outputs])
    return model
