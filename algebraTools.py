import numpy

def skewSymmetricMatrix(vector):
	return numpy.array( [[0, -vector[2], vector[1]], [vector[2],0,-vector[0]], [-vector[1],vector[0],0] ] )
#