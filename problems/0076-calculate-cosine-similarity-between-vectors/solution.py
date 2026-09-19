import numpy as np

def norm(v):
	sqr = 0
	for i in v:
		sqr += i**2 

	return pow(sqr,0.5)

def dot_product(v1,v2):
	prod = 0

	for i in range(len(v1)):
		prod += v1[i] * v2[i]

	return prod


def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here

	return dot_product(v1,v2)/(norm(v1)*norm(v2))

	pass