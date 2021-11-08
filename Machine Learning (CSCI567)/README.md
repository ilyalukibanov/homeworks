# Machine Learning
This folder contains my Python impementations of different Machine Learning Algorithms as a part of solutions of Machine Learning homework assignments. The assignments contained input and output structures and some parts of the classes. In the following subsections, I clarify what I implemented in these assignments.

## 1. P1: KNN, Linear Rergession
#### KNN (knn.py)
1. Distance function
2. Label prediction function
3. Accuracy score computing function
4. Choosing the best k (tuning the hyper-parameter) function

#### Linear Regression (linear_regression.py)
1. Closed-form solution function
2. Ridge closed-form solution function
3. Lambda (hyper-parameter) tuning function 
4. Test errors computing function

## 2. P2: Logistic Regression, DNN, CNN
#### Logistic Regression (logistic.py)
1. Train function
2. Predict function

#### Multinomial Logistic Regression (logistic.py)
1. Train function
2. Predict function

#### One-versus-rest classification (logistic.py)
1. Train function (based on the logistic regression)
2. Predict function

#### DNN (dnn_misc.py)
1. Linear forward pass and backward pass functions
2. ReLu forward pass and backward pass functions
3. Backward pass function for dropout class

#### CNN (dnn_cnn.py)
* Connected the layers with forward and backward passes

## 3. P3: SVM, Decision Tree

#### Support Vector Machine (pegasos.py)
1. Loss function
2. Train function
3. Test function

#### Decision Tree (decision_tree.py)
Split function:
1. Conditional entropy sub-function
2. Choose a node to split based on entropy 
3. Split and add children

#### Decision Stump (decision_stump.py)
* Predict function

#### Boosting classifier (boosting.py)
1. Predict function
2. AdaBoost function (train)

## 4. P4: KMeans, GMM (Gausian Mixture model)

#### KMeans (kmeans.py)
1. Fit function
2. KMeansClassifier: fit and predict functions

#### GMM (gmm.py)
1. Gaussian pdf function
2. Get likelihood function
3. Compute log likelihood function
4. Sample function
5. Expectation–Maximization algorithm 

## 5. P5: PCA, HMM

#### PCA (pca.py)
1. PCA function to compress the image
2. Decompress function (to reconstruct the image)
3. Reconstruction error function

#### HMM (hmm.py)
1. Forward message function
2. Backward message function
3. Computing probability of observing the whole sequence using the forward messages function
4. Computing probability of observing the whole sequence using the backward messages function
5. Viterbi algorithm function



