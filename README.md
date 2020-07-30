# Variable Factor Map

## 1) Description
The package provides a convinient way for Python users to plot the Variable Factor Map.

## 2) Installation
#### a) Download the package
```
pip install -i https://test.pypi.org/simple/ variable-factor-map-Huy-Bui==0.0.3
```
#### b) using example
```
from variable_factor_map import pca_map 
from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
X=pd.DataFrame(data=iris.data,columns=iris.feature_names)
pca_map(X, figsize=(10,10), sup="Iris", print_values= False)
```

The `pca_map` function takes 4 inputs:
* **X**: pandas Data Frame
* **figsize** (float, float): the width and height of the output. Default is (10,10)
* **sup** (string): The title of the plot. Default is an empty string
* **print_values** (boolean): Display the vector values. Default is False

## 3) Requirement
Python 3.6 and above