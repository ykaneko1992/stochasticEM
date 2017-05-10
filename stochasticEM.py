import numpy as np

class stochasticEM:
	"""docstring for stochasticEM"""
	def __init__(self, a, b, r, gamma, X, S, W, D, N, num_iter):
		self.a = a
		self.b = b
		self.r = r
		self.gamma = gamma
		self.X = X
		self.S = S
		self.W = W
		self.D = D
		self.N = N
		self.num_iter = num_iter

	def first_factor(self, J_n):
		self.J_n = 1

		if j <= J_n:
			first_f = N_nj / D-1+gamma
		else:
			first_f = gamma / D-1-gamma	
			

		return first_f
	
	def new_a(self, Md):
		self.Md = Md ### 各ベクトルの次元. 行列でsigmaつかう
		
		for i in range(Md):
			a = a + (Md(i) * N)/2
		return a	
	
	def rem_a(self,k):
		self.k = k

		rem_a = a -  (Md(k) * N)/2

		return rem_a

	def inv_Cnj(self):
		
		for i in range(W):
			inv_C_nj = W[i:]*W[:i] + r* np.identity() #### 雑なので絶対確認

		return inv_C_nj

	def mu_nj(self):
				

	def new_b(self):	



	def second_factor(self,Md,K):
			self.K = K

			