from keras.layers import Activation, multiply, add, UpSampling2D, Conv2D, MaxPooling2D
from keras.layers import Input, concatenate
from keras.models import Model

def attention_block(x, g, inter_channel):
    theta_x = Conv2D(inter_channel, (2, 2), strides=(2, 2), padding='same')(x)
    phi_g = Conv2D(inter_channel, (1, 1), padding='same')(g)

    f = Activation('relu')(add([theta_x, phi_g]))
    psi_f = Conv2D(1, (1, 1), padding='same')(f)
    psi_f = Activation('sigmoid')(psi_f)
    return multiply([x, psi_f])

def attention_unet(input_shape):
    inputs = Input(input_shape)

    conv1 = conv_block(inputs, 64)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = conv_block(pool1, 128)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = conv_block(pool2, 256)
    up2 = UpSampling2D(size=(2, 2))(conv3)
    attention2 = attention_block(conv2, up2, 128)
    up2 = concatenate([up2, attention2], axis=3)

    conv4 = conv_block(up2, 128)
    up1 = UpSampling2D(size=(2, 2))(conv4)
    attention1 = attention_block(conv1, up1, 64)
    up1 = concatenate([up1, attention1], axis=3)

    conv5 = conv_block(up1, 64)
    outputs = Conv2D(1, (1, 1), activation='sigmoid')(conv5)

    model = Model(inputs=[inputs], outputs=[outputs])
    return model
