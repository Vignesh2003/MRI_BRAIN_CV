from keras.optimizers import Adam

def train_model(model, X_train, y_train, X_test, y_test, epochs=50, batch_size=8):
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=[dice_score])
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=batch_size)
