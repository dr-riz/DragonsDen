

# import 
import pandas
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix

# get data
header = pd.read_csv("./header_tp.csv")
data = pd.read_csv("./data_tp.csv",names=header)


# summarize the dataset -- need pandas only
- dimensions of the dataset
- peak at data
- Data Type For Each Attribute
- statistical summary descriptive stats
- skewness of attributes
data.skew()
- correlation between attributes
data.corr()

- class distribution (for classification problems only)

# visualize the data -- need pandas, matplotlib.pyplot, numpy for correlation matrix plot, 
- histogram
data.hist()
- frequency plot
data.plot(kind='density', subplots=True, layout=(3,6), sharex=False)

- univariate plot with box plot
df.plot(kind='box', subplots=True, layout=(3,6), sharex=False, sharey=False)
plt.show()

- multivariate plot
scatter_matrix(df)

# clean/massage data
- remove outliers
- standardize/normalize

# feature selection
from sklearn.ensemble import ExtraTreesClassifier

# evaluate algorithms
- split train/test sets
- test harness
- build/evaluate models


# make predictions
- 


