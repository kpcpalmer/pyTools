import numpy

def makePoly_Q0V0A0QTVT( q0, v0, a0, qt, vt):
	A = numpy.array([	[1,0,0,0,0],
						[0,1,0,0,0],
						[0,0,2,0,0],
						[1,1,1,1,1],
						[0,1,2,3,4]
					])
	
	Q = numpy.array([q0, v0   , a0      , qt, vt   ])
	return numpy.matmul( numpy.linalg.inv( A ), Q )
#
def makePoly_Q0V0A0( q0, v0, a0 ):
	return numpy.array([q0, v0, 0.5*a0])
#