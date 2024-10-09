import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Load data from pickle file
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Assuming data_dict['data'] is a list of arrays with inconsistent shapes
# You need to make sure all elements have the same shape

# Check the shapes of all elements
shapes = [np.array(element).shape for element in data_dict['data']]
print(shapes)

# Find the maximum shape
max_shape = max(shapes, key=len)

# Pad the elements with smaller shapes or truncate the larger ones
processed_data = [np.resize(element, max_shape) for element in data_dict['data']]

# Convert to NumPy array
data = np.asarray(processed_data)

# Proceed with the rest of your code
labels = np.asarray(data_dict['labels'])

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)
model = RandomForestClassifier()

model.fit(x_train, y_train)
y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)
print('{}% of samples were classified correctly!'.format(score * 100))

# Save the model using pickle
with open('model.p', 'wb') as f:
    pickle.dump({'model': model, 'labels': labels}, f)
