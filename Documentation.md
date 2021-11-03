# Documentation Example

In this Project we will train and implement Machine learning model to predect if a tweet is going to be a viral tweet or not.
We will implement trained model to an simple application where we take input from a user and give prediction as output. More details on the application will be explained in section Application.

## Evaluation


### Design Decisions
We have used the following evaluation metrices.
### 1. Accuracy : 
Accuracy is a very simple an deffective metices to evaluate the preddibility of a model. This calculate the percentage of correctprediction. As this is very simple and commonly used metrics to evaluate the model, we have decided to use accuray as one of the evaluation metrices.

Baseline?
### 2. Precision :
Precision provides the information regarding the quality of a positive prediction made by the model. As Accuracy is very simple metrics it does not provide information of how precise/accurate your model is out of those predicted positive, how many of them are actual positive. This is the reason we decide to calculate Precision of model as well.
### 3. Cohen's kappa : 
We are dealing with an imbalance class, meaning we have data set with only _ % of viral tweet and _% nonviral tweet. And Cohen’s kappa statistic is a very good measure that can handle very well an dataset with imbalanced class. 

### 4. Recall: 
