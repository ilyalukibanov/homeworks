import numpy as np
from typing import List, Set

from classifier import Classifier
from decision_stump import DecisionStump
from abc import abstractmethod

class Boosting(Classifier):
  	# Boosting from pre-defined classifiers
	def __init__(self, clfs: Set[Classifier], T=0):
		self.clfs = clfs      # set of weak classifiers to be considered
		self.num_clf = len(clfs)
		if T < 1:
			self.T = self.num_clf
		else:
			self.T = T
	
		self.clfs_picked = [] # list of classifiers h_t for t=0,...,T-1
		self.betas = []       # list of weights beta_t for t=0,...,T-1
		return

	@abstractmethod
	def train(self, features: List[List[float]], labels: List[int]):
		return

	def predict(self, features: List[List[float]]) -> List[int]:
		'''
		Inputs:
		- features: the features of all test examples
   
		Returns:
		- the prediction (-1 or +1) for each example (in a list)
		'''
		########################################################
		# TODO: implement "predict"
		########################################################
		N = np.asarray(features).shape[0]
		beta = np.reshape(np.asarray(self.betas),(np.asarray(self.betas).shape[0],1))
		h = np.zeros((self.T,N))
		for t in range(self.T):
			h[t,:] = np.reshape(self.clfs_picked[t].predict(features), (1,N))
		H = np.sign(np.sum(h.T @ beta, axis=1))
		return H.tolist()
		

class AdaBoost(Boosting):
	def __init__(self, clfs: Set[Classifier], T=0):
		Boosting.__init__(self, clfs, T)
		self.clf_name = "AdaBoost"
		return
		
	def train(self, features: List[List[float]], labels: List[int]):
		'''
		Inputs:
		- features: the features of all examples
		- labels: the label of all examples
   
		Require:
		- store what you learn in self.clfs_picked and self.betas
		'''
		############################################################
		# TODO: implement "train"
		############################################################
		y = np.asarray(labels)
		features = np.asarray(features)
		N = features.shape[0]
		D = np.zeros((self.T+1,N))
		h = []
		epsilon = np.zeros(self.T)
		beta = np.zeros(self.T)
		D[0,:] = np.ones(N)/N
		for t in range(self.T):
			best_score = np.Inf
			best_cl = None
			for cl in self.clfs:
				current_score = D[t, :][y != np.reshape(np.asarray(cl.predict(features.tolist())), (y.shape[0],))].sum()
				if current_score < best_score:
					best_cl = cl
					best_score = current_score
			h.append(best_cl)
			current_prediction = np.reshape(np.asarray(h[t].predict(features.tolist())), (y.shape[0],))
			epsilon[t] = D[t, :][y != current_prediction].sum()
			beta[t] = 0.5*np.log((1-epsilon[t])/epsilon[t])
			D[t + 1, :][y == current_prediction] = D[t, :][y == current_prediction] * np.exp(-beta[t])
			D[t + 1, :][y != current_prediction] = D[t, :][y != current_prediction] * np.exp(beta[t])
			D[t + 1, :] = D[t + 1, :]/np.sum(D[t + 1, :])
		self.clfs_picked = h
		self.betas = beta.tolist()
		
		
	def predict(self, features: List[List[float]]) -> List[int]:
		return Boosting.predict(self, features)



	