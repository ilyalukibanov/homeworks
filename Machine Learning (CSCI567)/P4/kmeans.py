import numpy as np


class KMeans():

    '''
        Class KMeans:
        Attr:
            n_cluster - Number of cluster for kmeans clustering (Int)
            max_iter - maximum updates for kmeans clustering (Int) 
            e - error tolerance (Float)
    '''

    def __init__(self, n_cluster, max_iter=100, e=0.0001):
        self.n_cluster = n_cluster
        self.max_iter = max_iter
        self.e = e

    def fit(self, x):
        '''
            Finds n_cluster in the data x
            params:
                x - N X D numpy array
            returns:
                A tuple
                (centroids a n_cluster X D numpy array, y a size (N,) numpy array where cell i is the ith sample's assigned cluster, number_of_updates an Int)
            Note: Number of iterations is the number of time you update the assignment
        ''' 
        assert len(x.shape) == 2, "fit function takes 2-D numpy arrays as input"
        np.random.seed(42)
        N, D = x.shape

        # TODO:
        # - comment/remove the exception.
        # - Initialize means by picking self.n_cluster from N data points
        # - Update means and membership until convergence or until you have made self.max_iter updates.
        # - return (means, membership, number_of_updates)

        # DONOT CHANGE CODE ABOVE THIS LINE
        #raise Exception(
        #   'Implement fit function in KMeans class (filename: kmeans.py)')
        means = x[np.random.choice(N, self.n_cluster), :]
        J = np.Inf
        distances = np.zeros((N, self.n_cluster))
        for i in range(self.max_iter):
            for j in range(self.n_cluster):
                distances[:, j] = np.sum(np.square(x - means[j, :]), axis=1)
            membership = np.argmin(distances, axis=1)
            J_new = np.mean(np.amin(distances, axis=1))
            if np.abs(J_new - J) <= self.e:
                break
            J = J_new
            for j in range(self.n_cluster):
                if x[membership == j].size != 0:
                    means[j, :] = np.mean(x[membership == j, :], axis=0)
        return means, membership, i
        # DONOT CHANGE CODE BELOW THIS LINE
class KMeansClassifier():

    '''
        Class KMeansClassifier:
        Attr:
            n_cluster - Number of cluster for kmeans clustering (Int)
            max_iter - maximum updates for kmeans clustering (Int) 
            e - error tolerance (Float) 
    '''

    def __init__(self, n_cluster, max_iter=100, e=1e-6):
        self.n_cluster = n_cluster
        self.max_iter = max_iter
        self.e = e

    def fit(self, x, y):
        '''
            Train the classifier
            params:
                x - N X D size  numpy array
                y - (N,) size numpy array of labels
            returns:
                None
            Stores following attributes:
                self.centroids : centroids obtained by kmeans clustering (n_cluster X D numpy array)
                self.centroid_labels : labels of each centroid obtained by 
                    majority voting ((N,) numpy array) 
        '''

        assert len(x.shape) == 2, "x should be a 2-D numpy array"
        assert len(y.shape) == 1, "y should be a 1-D numpy array"
        assert y.shape[0] == x.shape[0], "y and x should have same rows"

        np.random.seed(42)
        N, D = x.shape
        # TODO:
        # - comment/remove the exception.
        # - Implement the classifier
        # - assign means to centroids
        # - assign labels to centroid_labels

        # DONOT CHANGE CODE ABOVE THIS LINE
        #raise Exception(
        #    'Implement fit function in KMeansClassifier class (filename: kmeans.py)')

        centroids, membership, _ = KMeans(n_cluster=self.n_cluster, max_iter=self.max_iter, e=self.e).fit(x)
        centroid_labels = np.zeros((self.n_cluster,))
        unique_classes = np.unique(y)
        for i in range(self.n_cluster):
            max_unique = 0
            subset = y[membership == i]
            for u in unique_classes:
                current_sum =  np.count_nonzero([subset == u])
                if current_sum > max_unique:
                    centroid_labels[i] = u
                    max_unique = current_sum
        # DONOT CHANGE CODE BELOW THIS LINE

        self.centroid_labels = centroid_labels
        self.centroids = centroids

        assert self.centroid_labels.shape == (self.n_cluster,), 'centroid_labels should be a numpy array of shape ({},)'.format(
            self.n_cluster)

        assert self.centroids.shape == (self.n_cluster, D), 'centroid should be a numpy array of shape {} X {}'.format(
            self.n_cluster, D)

    def predict(self, x):
        '''
            Predict function

            params:
                x - N X D size  numpy array
            returns:
                predicted labels - numpy array of size (N,)
        '''

        assert len(x.shape) == 2, "x should be a 2-D numpy array"

        np.random.seed(42)
        N, D = x.shape
        # TODO:
        # - comment/remove the exception.
        # - Implement the prediction algorithm
        # - return labels
        # DONOT CHANGE CODE ABOVE THIS LINE
        #raise Exception(
        #    'Implement predict function in KMeansClassifier class (filename: kmeans.py)')
        distances = np.zeros((N, self.n_cluster))
        for j in range(self.n_cluster):
            distances[:, j] = np.sum(np.square(x - self.centroids[j]), axis=1)
        membership = np.argmin(distances, axis=1)
        labels = np.zeros(N)
        for j in range(self.n_cluster):
            labels[membership == j] = self.centroid_labels[j]
        # DONOT CHANGE CODE BELOW THIS LINE
        return labels

