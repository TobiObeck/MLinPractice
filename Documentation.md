# Documentation 

In this Project we will train and implement Machine learning model to predect if a tweet is going to be a viral tweet or not.
We will implement trained model to an simple application where we take input from a user and give prediction as output. More details on the application will be explained in section Application.

## Evaluation


### Design Decisions
We have used the following evaluation metrices.
### 1. Accuracy : 
Accuracy is a very simple an deffective metices to evaluate the preddibility of a model. This calculate the percentage of correct prediction. As this is very simple and commonly used metrics to evaluate the model, we have decided to use accuray as one of the evaluation metrices. With a imbalanceAccuracy can be a misleading metric for imbalanced data sets.

Baseline?
### 2. Precision :
Precision provides the information regarding the quality of a positive prediction made by the model. As Accuracy is very simple metrics it does not provide information of how precise/accurate your model is out of those predicted positive, how many of them are actual positive. This is the reason we decide to calculate Precision of model as well.

### 3. Recall:
Recall gives us intuation regarding how many of the Actual Positives our model capture through labeling it as Positive (True Positive). We can use this metric to select best model when we are dealing with dataset that as high cost associated with false negative

### 4. Cohen's kappa : 
We are dealing with an imbalance class, meaning we have data set with only _ % of viral tweet and _% nonviral tweet. And Cohen’s kappa statistic is a very good measure that can handle very well an dataset with imbalanced class. 

### 5. F1-score: 

### 6 Jaccard 


### Results


### Interpretation


## Preprocessing
In this step we cleaned the provided data set and made the data set ready for the model training.
### Design Decisions
The first step we implemented is, remove rows that doesnot have english languase Tweet. This decission was made because in our data set we have dominient english language tweet. This is done with script in src/preprocessing/preprocessors/non_english_remover.py
In second step we remove columns which we consider not much relevent in the decision making process. And we also removed columns that has more than 80 % NAN values. This process is a important steps in data wrangling. In this step we removed total 22 columns. This is done with script in src/preprocessing/preprocessors/column_droper.py.
We also clean the "Tweet" column. Tweet contains emojis, mentions, hashtags, and links, which are bad for the NLP so we remove those with regex. This is done with script in src/preprocessing/preprocessors/tweet_clean.py
### Results
After preprocessing we end up with less columns. This already reduced dimention of the dataset for the Model training. And we have a tweet with only with characters that are good for NLP.


### Interpretation



## Feature Extraction



### Design Decisions



### Results


### Interpretation


## Dimensionality Reduction



### Design Decisions



### Results



### Interpretation


## Classification

### Design Decisions


### Results


### Interpretation


