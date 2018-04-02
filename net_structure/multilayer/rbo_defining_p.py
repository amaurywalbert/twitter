from __future__ import division
import numpy as np
def w_rbo(p=0.9, d=10):
	"""Calculate weight of first d rankings with parameter p"""
	w = 1 - p**(d - 1) + ((1 - p) / p) * d * (np.log(1 / (1 - p)) - sum(p**i / i for i in range(1, d)))
	return w

#w_rbo(p=0.9, d=10)
#0.85558544674735182
#pg. 19:

#Equation 21 helps inform the choice of the parameter p, which determines the degree of top-weightedness of the RBO metric. For instance, p=0.9 means that the first 10 ranks have 86% of the weight of the evaluation;

#86%
#0.85558544674735182
#Nice
#to give the top 50 ranks the same weight involves taking p=0.98 as the setting.

#w_rbo(p=0.98, d=50)
#0.85223391031940043
#86%
#0.85223391031940043
#Sick almost, but whatever
#Thus, the experimenter can tune the metric to achieve a given weight for a certain length of prefix.
