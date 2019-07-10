import numpy

def skewSymmetricMatrix(vector):
	return numpy.array( [[0, -vector[2], vector[1]], [vector[2],0,-vector[0]], [-vector[1],vector[0],0] ] )
#
def rotationX( t ):
	c = numpy.cos(t)
	s = numpy.sin(t)
	return numpy.asarray( [[1,0,0], [0,c,-s], [0,s,c]] )
#
def rotationY( t ):
	c = numpy.cos(t)
	s = numpy.sin(t)
	return numpy.asarray( [[c,0,s],[0,1,0],[-s,0,c]] )
#
def rotationZ( t ):
	c = numpy.cos(t)
	s = numpy.sin(t)
	return numpy.asarray( [[c,-s,0],[s,c,0],[0,0,1]] )
#