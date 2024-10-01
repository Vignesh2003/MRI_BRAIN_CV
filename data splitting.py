from sklearn.model_selection import train_test_split

def split_data(images, masks):
    X_train, X_test, y_train, y_test = train_test_split(images, masks, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
