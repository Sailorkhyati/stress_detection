# -*- coding: utf-8 -*-
"""😶‍🌫️🙇🏻‍♀️ Stress Level Detection

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/#fileId=https%3A//storage.googleapis.com/kaggle-colab-exported-notebooks/stress-level-detection-0e8d51c1-2f90-4938-ae0f-ce77054d5f80.ipynb%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com/20240131/auto/storage/goog4_request%26X-Goog-Date%3D20240131T151752Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3Dc0015a9f9a2cabaef26f644748dbdb5d34eb6c5068ffa8821694e9796ba603752ef20586d2afe23e7184cbba128bc884077894d53f31dd3b64f2a1e20d252debc630880f476a2488d1556beb0e92efdb6e175fbd923fa585e98039e17ac5261f99c332cff1b3bf35e5b4466540c10c2ab2eba5fc9e06f7cb329a510a1282b23c1d31ad7401014fe73706e49b38c97639bd46f8bb29f7e39549913b25e4a8baf76b71ce3326a8d1cde4b8dbc0e5295f87b0dc546da630cb98df489fb08ca7494ca7adf30f5278b671504ec6e924825cb7948fd03eb9b565e14d6046ce6622072e9ff520076cbb206fee8d764a7be4e68d325ff04bfabb76de3d180c5ecaa54d48
"""

# IMPORTANT: RUN THIS CELL IN ORDER TO IMPORT YOUR KAGGLE DATA SOURCES
# TO THE CORRECT LOCATION (/kaggle/input) IN YOUR NOTEBOOK,
# THEN FEEL FREE TO DELETE THIS CELL.
# NOTE: THIS NOTEBOOK ENVIRONMENT DIFFERS FROM KAGGLE'S PYTHON
# ENVIRONMENT SO THERE MAY BE MISSING LIBRARIES USED BY YOUR
# NOTEBOOK.

import os
import sys
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from urllib.parse import unquote, urlparse
from urllib.error import HTTPError
from zipfile import ZipFile
import tarfile
import shutil

CHUNK_SIZE = 40960
DATA_SOURCE_MAPPING = 'input-data:https%3A%2F%2Fstorage.googleapis.com%2Fkaggle-data-sets%2F2789271%2F4816636%2Fbundle%2Farchive.zip%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20240131%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20240131T151751Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D8db3bc8efef31f2836cbcf328ef1ffcef6ec1a7ea25c835ffe88a88175e1eaf7d32e94ba65936c257fcc2ee8357dfa49b5fae17ed443a40566d243408c61e036605cfff2d1abd49bcc07733437891426bf29a3a65d854cae465d3dbba4f01f9bfd0b8ccce48a41bb94bba072617464cfa3afa8f1fc1272ee972df4b0d39223fa17c01adb904121258fa43308b28f23fb71e1de4da805f34108c5c6faf4dc18e7bca1dc5ce5357559b0e8c1f6e3e9f9789152f6423b7c3b5935f6cf9a992b0e2ed4bb82f38cbbb4b6cbe8f37eac10ff44eacf34ccb511954f4159215659eaf01c81d9725de41b1b3792ec4982c7c490786fc8f8a4bbac7a6cbca533818594941a'

KAGGLE_INPUT_PATH='/kaggle/input'
KAGGLE_WORKING_PATH='/kaggle/working'
KAGGLE_SYMLINK='kaggle'

!umount /kaggle/input/ 2> /dev/null
shutil.rmtree('/kaggle/input', ignore_errors=True)
os.makedirs(KAGGLE_INPUT_PATH, 0o777, exist_ok=True)
os.makedirs(KAGGLE_WORKING_PATH, 0o777, exist_ok=True)

try:
  os.symlink(KAGGLE_INPUT_PATH, os.path.join("..", 'input'), target_is_directory=True)
except FileExistsError:
  pass
try:
  os.symlink(KAGGLE_WORKING_PATH, os.path.join("..", 'working'), target_is_directory=True)
except FileExistsError:
  pass

for data_source_mapping in DATA_SOURCE_MAPPING.split(','):
    directory, download_url_encoded = data_source_mapping.split(':')
    download_url = unquote(download_url_encoded)
    filename = urlparse(download_url).path
    destination_path = os.path.join(KAGGLE_INPUT_PATH, directory)
    try:
        with urlopen(download_url) as fileres, NamedTemporaryFile() as tfile:
            total_length = fileres.headers['content-length']
            print(f'Downloading {directory}, {total_length} bytes compressed')
            dl = 0
            data = fileres.read(CHUNK_SIZE)
            while len(data) > 0:
                dl += len(data)
                tfile.write(data)
                done = int(50 * dl / int(total_length))
                sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {dl} bytes downloaded")
                sys.stdout.flush()
                data = fileres.read(CHUNK_SIZE)
            if filename.endswith('.zip'):
              with ZipFile(tfile) as zfile:
                zfile.extractall(destination_path)
            else:
              with tarfile.open(tfile.name) as tarfile:
                tarfile.extractall(destination_path)
            print(f'\nDownloaded and uncompressed: {directory}')
    except HTTPError as e:
        print(f'Failed to load (likely expired) {download_url} to path {destination_path}')
        continue
    except OSError as e:
        print(f'Failed to load {download_url} to path {destination_path}')
        continue

print('Data source import complete.')

"""# ***STRESS LYSIS***

***ABOUT THE DATA & THE NOTEBOOK***

**Based on the human’s physical activity, the stress levels of the human being are detected and analyzed. A dataset of 2001 samples is provided for human body humidity, body temperature and the number of steps taken by the user. Three different classifications of stress are analyzed such as low stress, normal stress, and high stress.**

**In this notebook, I've analyzed the features of the dataset, trained the model and finally deployed it too.**

**HIT THE UPVOTE 🔼**
"""

# File - Stress_Lysis.ipynb

"""# ***IMPORTS***"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

import os
for dirname, _, filenames in os.walk('/kaggle/input-data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

"""# ***DATA COLLECTION***

* ***Reading the Data Files***
"""

data=pd.read_csv('/kaggle/input/input-data/Stress-Lysis.csv')
data.head()  # displays the first five rows of the dataframe

"""# ***ANALYZING THE DATA***"""

data.shape  # returns a tuple of array dimension that specifies the number of rows and columns

data.info()  # prints the information about the dataframe

data.describe()  # returns the statistical summary of the data

"""# ***DATA CLEANING***

***STEPS:***

***1. Analyze the numerical and categorical features, and convert categorical feature into numerical.***

Stress Level
0 - Low stress
1 - Normal stress
2 - High Stress
"""

data['Stress_Level'].unique()

"""***2. Check for missing values and handle them.***"""

data.isnull().sum()

"""***3.Check for duplicate values***"""

data.duplicated().sum()

"""# ***EDA - EXPLORATORY DATA ANALYSIS***

***1.Univariate Non-Graphical***

***Check for outliers. If present try to handle them.***
"""

data.skew()

plt.figure(figsize=(4,4))
plt.boxplot(data)
plt.show()

"""All 4 columns consists skewness.

***Skewness Reduction***
"""

# Logarithmic Transformation
hum_log = np.log(data['Humidity'])
h = round(hum_log.skew(),10)
print(h)

# SquareRoot Transformation
temp_sqrt = np.sqrt(data['Temperature'])
temp_sqrt.skew()
t = round(temp_sqrt.skew(),10)
print(t)

quantile1=data["Step_count"].quantile(0.25)
quantile2=data["Step_count"].quantile(0.75)

quantile1

quantile2

data["Step_count"]=np.where(data["Step_count"]<quantile1,quantile1,data["Step_count"])
data["Step_count"]=np.where(data["Step_count"]>quantile2,quantile2,data["Step_count"])

s = round(data['Step_count'].skew(),10)
print(s)

# SquareRoot Transformation
stress_sqrt = np.sqrt(data['Stress_Level'])
sl = round(stress_sqrt.skew(),10)
print(sl)

"""***2.Univariate Graphical***"""

column=['Step_count','Humidity']
for category in column:
    plt.figure(figsize=(3,3))
    plt.hist(data[category])
    plt.title(category)
    plt.show()

# histplot (categorical)
plt.figure(figsize=(3,3))
sns.set(font_scale=1)
sns.histplot(data=data, x='Stress_Level')

plt.figure(figsize=(3,3))
sns.boxplot(data['Temperature'])

"""***3.Multivariate Non-Graphical***

***Correlation***
"""

correlation = data.corr()
correlation

plt.figure(figsize=(3,3))
sns.heatmap(correlation,annot=True,cmap='crest',linewidths=0.2)
plt.show()

"""***4.Multivariate Graphical***"""

plt.figure(figsize=(3,3))
sns.scatterplot(x='Humidity',y='Temperature',hue='Stress_Level',data=data)
plt.show()

"""# ***MODELLING***"""

from sklearn.model_selection import train_test_split
X=data.drop(['Stress_Level'],axis=1)
y=data['Stress_Level']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)

"""***LOGISTIC REGRESSION***"""

from sklearn.linear_model import LogisticRegression
regressor = LogisticRegression(C=1.0,random_state=2)
regressor.fit(X_train,y_train)

from sklearn.metrics import accuracy_score, confusion_matrix
prediction = regressor.predict(X_test)
confusionmatrix = confusion_matrix(y_test,prediction)
print(confusionmatrix)

print(accuracy_score(y_test,prediction))

"""***RANDOM FOREST CLASSIFICATION***"""

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=100,max_depth=3,random_state=0)
model.fit(X,y)
prediction = model.predict(X_test)
confusionmatrix = confusion_matrix(y_test,prediction)
print(confusionmatrix)

print(accuracy_score(y_test,prediction))

"""***SUPPORT VECTOR MACHINE***"""

!apt-get -qq install -y libfluidsynth1

from sklearn.preprocessing import StandardScaler
standardscaler = StandardScaler()
X_train = standardscaler.fit_transform(X_train)
X_test = standardscaler.transform(X_train)

from sklearn.svm import SVC
classifier = SVC(kernel='linear', random_state=0)
classifier.fit(X_train, y_train)

print("Shape of y_test:", y_test.shape)
print("Shape of y_predict:", y_predict.shape)

"""# ***DEPLOYMENT***

***SAVING THE TRAINED MODEL***
"""

import pickle

filename = 'stress_trained.sav'
pickle.dump(classifier,open(filename,'wb'))

"""***LOADING THE TRAINED MODEL***"""

loaded_model = pickle.load(open('stress_trained.sav','rb'))
# Download the stress_trained.sav model

# Evaluating

input_data = (11.05,80.05,14) #300
#changing the input data into numpy array
id_np_array = np.asarray(input_data)
id_reshaped = id_np_array.reshape(1,-1)

prediction = classifier.predict(id_reshaped)
print(prediction)

if(prediction[0]==0):
    print("Stress Level: LOW")
elif(prediction[0]==1):
    print("Stress Level: MEDIUM")
else:
    print("Stress Level: HIGH")

input_data = (21.38,90.38,128) #100
#changing the input data into numpy array
id_np_array = np.asarray(input_data)
id_reshaped = id_np_array.reshape(1,-1)

prediction = classifier.predict(id_reshaped)
print(prediction)

if(prediction[0]==0):
    print("Stress Level: LOW")
elif(prediction[0]==1):
    print("Stress Level: MEDIUM")
else:
    print("Stress Level: HIGH")

input_data = (25.41,94.41,167) #200
#changing the input data into numpy array
id_np_array = np.asarray(input_data)
id_reshaped = id_np_array.reshape(1,-1)

prediction = classifier.predict(id_reshaped)
print(prediction)

if(prediction[0]==0):
    print("Stress Level: LOW")
elif(prediction[0]==1):
    print("Stress Level: MEDIUM")
else:
    print("Stress Level: HIGH")

# File - Predictive System.py

# Imports
import numpy as np
import pickle

# Loading the trained model
loaded_model = pickle.load(open('stress_trained.sav','rb'))
# stress_trained.sav - replace the path of the file along with the file name
# Example: loaded_model = pickle.load(open('C:/Users/jeyasri/Downloads/PROJECT/stress_trained.sav','rb'))



input_data = (25.41,94.41,167) #200
#changing the input data into numpy array
id_np_array = np.asarray(input_data)
id_reshaped = id_np_array.reshape(1,-1)

prediction = loaded_model.predict(id_reshaped)
print(prediction)

if(prediction[0]==0):
    print("Stress Level: LOW")
elif(prediction[0]==1):
    print("Stress Level: MEDIUM")
else:
    print("Stress Level: HIGH")

# Trying to install streamlit
!pip install -q streamlit

import numpy as np
import pickle
import streamlit as st

# Loading the trained model
loaded_model = pickle.load(open('stress_trained.sav','rb'))
# Replace path over stress_trained.sav

def stresslevel_prediction(input_data):

    #changing the input data into numpy array
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction = loaded_model.predict(id_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "Stress Level: LOW"
    elif(prediction[0]==1):
        return "Stress Level: MEDIUM"
    else:
        return "Stress Level: HIGH"

def main():

    st.title('STRESS LEVEL PREDICTION WEB APP')

    Humidity = st.text_input('Humidity Value')
    Temperature = st.text_input('Body Temperature')
    Step_count = st.text_input('Number of Steps')

    # Prediction code
    diagnosis = ''

    if st.button('PREDICT'):
        diagnosis = stresslevel_prediction([Humidity, Temperature, Step_count])

    st.success(diagnosis)

if __name__=='__main__':
    main()

!streamlit run "Stress Level Prediction Web App.py"

"""**Go to command prompt open the terminal and execute the command.**

streamlit run "path of the file.py"

Example: streamlit run "C:\Users\jeyasri\Downloads\PROJECT\Stress Level Prediction Web App.py"

**Your final result will be like this...**

![Stress.png](attachment:dacc60b2-6304-4afe-b1ca-1ed750052edd.png)
"""
