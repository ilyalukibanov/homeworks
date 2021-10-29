import numpy as np
from kmeans import KMeans

class GMM():
    '''
        Fits a Gausian Mixture model to the data.

        attrs:
            n_cluster : Number of mixtures (Int)
            e : error tolerance (Float) 
            max_iter : maximum number of updates (Int)
            init : initialization of means and variance
                Can be 'random' or 'kmeans' 
            means : means of Gaussian mixtures (n_cluster X D numpy array)
            variances : variance of Gaussian mixtures (n_cluster X D X D numpy array) 
            pi_k : mixture probabilities of different component ((n_cluster,) size numpy array)
    '''

    def __init__(self, n_cluster, init='k_means', max_iter=100, e=0.0001):
        self.n_cluster = n_cluster
        self.e = e
        self.max_iter = max_iter
        self.init = init
        self.means = None
        self.variances = None
        self.pi_k = None

    def fit(self, x):
        '''
            Fits a GMM to x.

            x: is a NXD size numpy array
            updates:
                self.means
                self.variances
                self.pi_k
        '''
        assert len(x.shape) == 2, 'x can only be 2 dimensional'

        np.random.seed(42)
        N, D = x.shape

        if (self.init == 'k_means'):
            # TODO
            # - comment/remove the exception
            # - initialize means using k-means clustering
            # - compute variance and pi_k (see P4.pdf)

            # DONOT MODIFY CODE ABOVE THIS LINE
            #raise Exception(
            #    'Implement initialization of variances, means, pi_k using k-means')
            self.means, membership, _ = KMeans(n_cluster=self.n_cluster, max_iter=self.max_iter, e=self.e).fit(x)
            self.variances = np.zeros((self.n_cluster, D, D))
            self.pi_k = np.zeros(self.n_cluster)
            ones = np.ones(N)
            add_to_positive = 0.001 * np.identity(D)
            for i in range(self.n_cluster):
                elements = membership == i
                N_k = ones[elements].sum()
                self.pi_k[i] = N_k / N
                self.variances[i, :, :] = (x[elements] - self.means[i]).T @ (x[elements] - self.means[i]) / N_k
                while np.linalg.det(self.variances[i, :, :]) == 0:
                    self.variances[i, :, :] += add_to_positive
            # DONOT MODIFY CODE BELOW THIS LINE

        elif (self.init == 'random'):
            # TODO
            # - comment/remove the exception
            # - initialize means randomly
            # - initialize variance to be identity and pi_k to be uniform

            # DONOT MODIFY CODE ABOVE THIS LINE
            #raise Exception(
            #    'Implement initialization of variances, means, pi_k randomly')
            self.means = np.random.rand(self.n_cluster,D)
            self.variances = np.zeros((self.n_cluster, D, D))
            identity = np.identity(D)
            for i in range(self.n_cluster):
                self.variances[i, :, :] = identity
            self.pi_k = np.ones(self.n_cluster)/self.n_cluster
            # DONOT MODIFY CODE BELOW THIS LINE

        else:
            raise Exception('Invalid initialization provided')

        # TODO
        # - comment/remove the exception
        # - Use EM to learn the means, variances, and pi_k and assign them to self
        # - Update until convergence or until you have made self.max_iter updates.
        # - Return the number of E/M-Steps executed (Int) 
        # Hint: Try to separate E & M step for clarity
        # DONOT MODIFY CODE ABOVE THIS LINE
        #raise Exception('Implement fit function (filename: gmm.py)')
        ll = self.compute_log_likelihood(x, self.means, self.variances, self.pi_k)
        gamma = np.zeros((N, self.n_cluster))
        for i in range(self.max_iter):
            #E step
            for k in range(self.n_cluster):
                gaussian_k = self.Gaussian_pdf(self.means[k], self.variances[k, :, :])
                for n in range(N):
                    gamma[n, k] = self.pi_k[k] * gaussian_k.getLikelihood(x[n, :])
            gamma = (gamma.T / np.sum(gamma, axis=1).T).T
            #M step
            N_k = np.sum(gamma, axis=0)
            self.means = np.zeros((self.n_cluster, D))
            self.variances = np.zeros((self.n_cluster, D, D))
            for k in range(self.n_cluster):
                self.means[k, :] = np.sum(x.T * gamma[:, k].T, axis=1) / N_k[k]
                self.variances[k, :, :] = (x - self.means[k, :]).T @ (gamma[:, k].T * (x - self.means[k, :]).T).T / N_k[k]
            self.pi_k = N_k / N
            ll_new = self.compute_log_likelihood(x, self.means, self.variances, self.pi_k)
            #print(ll_new)
            if np.abs(ll - ll_new) <= self.e:
                break
            ll = ll_new
        return i
        # DONOT MODIFY CODE BELOW THIS LINE

		
    def sample(self, N):
        '''
        sample from the GMM model

        N is a positive integer
        return : NXD array of samples

        '''
        assert type(N) == int and N > 0, 'N should be a positive integer'
        np.random.seed(42)
        if (self.means is None):
            raise Exception('Train GMM before sampling')

        # TODO
        # - comment/remove the exception
        # - generate samples from the GMM
        # - return the samples

        # DONOT MODIFY CODE ABOVE THIS LINE
        #raise Exception('Implement sample function in gmm.py')
        clusters = np.random.choice(range(self.n_cluster), size=N, p=self.pi_k)
        samples = np.zeros((N, self.means.shape[1]))
        for k in range(self.n_cluster):
           samples[clusters == k] = np.random.multivariate_normal(self.means[k], self.variances[k], (np.count_nonzero([clusters == k]),))
        # DONOT MODIFY CODE BELOW THIS LINE
        return samples        

    def compute_log_likelihood(self, x, means=None, variances=None, pi_k=None):
        '''
            Return log-likelihood for the data

            x is a NXD matrix
            return : a float number which is the log-likelihood of data
        '''
        assert len(x.shape) == 2,  'x can only be 2 dimensional'
        if means is None:
            means = self.means
        if variances is None:
            variances = self.variances
        if pi_k is None:
            pi_k = self.pi_k    
        # TODO
        # - comment/remove the exception
        # - calculate log-likelihood using means, variances and pi_k attr in self
        # - return the log-likelihood (Float)
        # Note: you can call this function in fit function (if required)
        # DONOT MODIFY CODE ABOVE THIS LINE
        #raise Exception('Implement compute_log_likelihood function in gmm.py')
        log_likelihood = 0
        N, D = x.shape
        gaussian = []
        for k in range(self.n_cluster):
            gaussian.append(self.Gaussian_pdf(self.means[k], self.variances[k, :, :]))
        for n in range(N):
            partial_log_likelihood = 0
            for k in range(self.n_cluster):
                partial_log_likelihood += pi_k[k] * gaussian[k].getLikelihood(x[n, :])
            log_likelihood += np.log(partial_log_likelihood)
        log_likelihood = float(log_likelihood)
        # DONOT MODIFY CODE BELOW THIS LINE
        return log_likelihood

    class Gaussian_pdf():
        def __init__(self,mean,variance):
            self.mean = mean
            self.variance = variance
            self.c = None
            self.inv = None
            '''
                Input: 
                    Means: A 1 X D numpy array of the Gaussian mean
                    Variance: A D X D numpy array of the Gaussian covariance matrix
                Output: 
                    None: 
            '''
            # TODO
            # - comment/remove the exception
            # - Set self.inv equal to the inverse the variance matrix (after ensuring it is full rank - see P4.pdf)
            # - Set self.c equal to ((2pi)^D) * det(variance) (after ensuring the variance matrix is full rank)
            # Note you can call this class in compute_log_likelihood and fit
            # DONOT MODIFY CODE ABOVE THIS LINE
            #raise Exception('Impliment Guassian_pdf __init__')
            D = variance.shape[0]
            add_to_positive = 0.001 * np.identity(D)
            while np.linalg.det(variance) == 0:
                variance += add_to_positive
            self.inv = np.linalg.inv(variance)
            self.c = np.power(2 * np.pi, D) * np.linalg.det(variance)
            # DONOT MODIFY CODE BELOW THIS LINE

        def getLikelihood(self,x):
            '''
                Input: 
                    x: a 1 X D numpy array representing a sample
                Output: 
                    p: a numpy float, the likelihood sample x was generated by this Gaussian
                Hint: 
                    p = e^(-0.5(x-mean)*(inv(variance))*(x-mean)'/sqrt(c))
                    where ' is transpose and * is matrix multiplication
            '''
            #TODO
            # - Comment/remove the exception
            # - Calculate the likelihood of sample x generated by this Gaussian
            # Note: use the described implementation of a Gaussian to ensure compatibility with the solutions
            # DONOT MODIFY CODE ABOVE THIS LINE
            #raise Exception('Impliment Guassian_pdf getLikelihood')
            p = np.exp(-0.5 * (x-self.mean) @ self.inv  @ (x - self.mean).T) / np.sqrt(self.c)
            # DONOT MODIFY CODE BELOW THIS LINE
            return p
