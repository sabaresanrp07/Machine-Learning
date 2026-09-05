# Scikit learn

This notes helps begineers to learn scklearn faster and much more easier,before starting scklearn u have to start with ml concepts 


# Machine Learning Fundamentals

## What is Machine Learning?
## Dataset, features, labels, samples
## Supervised vs unsupervised learning
## Training vs testing vs prediction
## Model, parameters, hyperparameters
## Linear Regression
## Loss / cost function
## Gradient Descent
## Classification
## Logistic Regression
## Overfitting / underfitting
## Regularization
## Feature scaling
## k-NN
## Decision Trees
## Random Forest
## SVM
## Clustering / K-Means
## PCA
## Cross-validation
## Evaluation metrics
## Pipelines
## Hyperparameter tuning


# Machine learning

- we give data to the machine(computer) like hours studied and marks scored we feed enough data and later we give only hours studied using the pattern computer predict score.

# Model

- The model is basically the thing that has learned the relationship/pattern in your data.

- For our example, perhaps it learns something approximately like:   score=7.5(hours)+28 this is linear regression (we see abt this later)

- if u give 8 hours it predict like 88

- The ML algorithm learns the parameters of the model from data , our model __score = w x hours + b__

here 

- score  is target(output)
- hours is feature(input)

ML algoritham learns this parameter from our given data

- w -> parameter
- b -> parameter

# Features and target

- This terminology is absolutely critical for scikit-learn.

- as we have seen before 

Feature (The information we use to make the prediction.) means input(hours studied)

Usually represented as: X (we see this in sklearn)

Target (What we're trying to predict.) means output(score)

Usually represented as: y

- so X = hours studied , y = exam score

- In sklearn we see this constantly __model.fit(X, y)__

this means 

Take my training data X and the correct answers y, and learn the model's parameters from them.

Ex:

X = [[1], [2], [3], [5]] maybe these represent Years of experience

y = [30000, 40000, 50000, 70000] These are the corresponding salaries.

- model.fit(X, y) so when we write this you're telling the model:

Here are inputs (X) and their correct outputs (y). Find the parameters that allow you to predict y from X. 

basically ,fit() means learn 

So the model has learned:
    w = 10000
    b = 20000

Then you can ask it to predict:
    model.predict([[4]])


## sample & feautre
Target is also a column(feature) in datasheet but which machine predicts like mark

- Each row is a sample (or observation).
- Each col is a feature (basically attributes/matadata of a row like age,height,marks,hours etc)

| Sample    | Age | Height | Marks |
| --------- | --: | -----: | ----: |
| Student 1 |  20 |    175 |    85 |
| Student 2 |  21 |    168 |    72 |
| Student 3 |  19 |    180 |    91 |

- student 1 ,2 ,3 are sample
- age , height , marks are features


# Supervised Learning

- Our previous example is supervised learning where we give the algorithm both the input data and the correct answers, and it learns a relationship between them.

### Lable 

- A label is basically the known answer associated with a training sample.

Email                    Label
--------------------------------
"Win ₹1 crore!"          Spam
"Meeting at 5 PM"        Not spam
"Congratulations!"       Spam

- this is what happens while supervised learning

     Training data
       X and y
           ↓
     Make prediction
           ↓
    Compare prediction
       with actual y
           ↓
      Calculate error
           ↓
     Adjust parameters
           ↓
       Repeat

- 2 types of supervised learning 

## Regression 

- predict a numerical/continuous value Eg:- slary,score etc a numerical value 88,50,000 like this.

Common algorithms:

- Linear Regression
- Polynomial Regression
- Decision Tree Regression
- Random Forest Regression
- Gradient Boosting Regression
- Support Vector Regression

## Classification

- Predicts a category/class Eg:- email → spam / not spam this predict a category 

### Binary classification

 true/fales , pass/fail , spam/not spam.

### Multiclass classification

more than 2 class Ex: target can be Cat/Dog/Horse/Bird in binary only Dog/Cat

algorithms:

- Logistic Regression
- Decision Trees
- Random Forest
- SVM
- K-Nearest Neighbors
- Neural Networks

### Multilabel classification

A single sample can belong to multiple classes simultaneously Eg: A movie can be Action/Comedy/Sci-Fi all three can be true one sample -> multiple classes but in multiclass one sample -> one class

# Unsupervised Learning

earning patterns from data without target labels.

## why we need unsupervised learning

like imagine we have 10,000 customer data

Age    Income    Purchases
22     25k       2
24     28k       3
45     90k       15
48     100k      18
...

You don't know what "type" each customer is , so we could ask an unsupervised algorithm __Can you find groups of customers that behave similarly__

so it might discover 

- Cluster 1 → young + low income + few purchases
- Cluster 2 → middle-aged + high income + many purchases
- Cluster 3 → young + high income + moderate purchases 

We don't tell the algoritham these groups,it discovered them from the data (no target lable is given )

Unsupervised Learning
│
├── Clustering
│   ├── K-Means
│   ├── DBSCAN
│   ├── Agglomerative Clustering
│   └── Gaussian Mixture
│
├── Dimensionality Reduction
│   ├── PCA
│   ├── TruncatedSVD
│   └── t-SNE
│
├── Anomaly / Outlier Detection
│   ├── Isolation Forest
│   ├── One-Class SVM
│   └── Local Outlier Factor
│
└── Density Estimation
    └── Kernel Density Estimation


## Clustering 

Clustering means Putting similar observations into groups but there are no labels saying customer under this condition this group no , machine finds out using those data.

### K-Means

This is one of the most important algorithms in scikit-learn.















### Training vs prediction vs Testing

- model.fit(X, y) - to  make the model learn (training).

- model.predict(X_new)- the learned model to produce outputs for new input data.

- Testing is like model evaluation and validation 


