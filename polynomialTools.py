import numpy

def polyCoeffs_q0v0a0( T, q0, v0, a0 ):
	A = numpy.array([	[1,		0,		0 ],
						[0,		1.,		0 ],
						[0,		0,		2 ]
					])
	Q = numpy.array([q0, v0, a0])
	return numpy.flip( numpy.matmul( numpy.linalg.inv(A), Q ) )
#
def polyCoeffs_q0v0a0qT( T, q0, v0, a0, qT ):
	A = numpy.array([	[1,	0,	0,		0],
						[0,	1,	0,		0],
						[0,	0,	2,		0],
						[1,	T,	T**2,	T**3]
					])
	Q = numpy.array([q0, v0, a0, qT])
	return numpy.flip( numpy.matmul( numpy.linalg.inv(A), Q ) )
#
def polyCoeffs_q0v0a0qTvT( T, q0, v0, a0, qT, vT ):
	A = numpy.array([	[1,	0,	0,		0,		0],
						[0, 1,	0,		0,		0],
						[0,	0,	2,		0,		0],
						[1,	T,	T**2,	T**3,	T**4],
						[0,	1,	2*T,	3*T**2,	4*T**3]
					])
	Q = numpy.array([q0, v0, a0, qT, vT])
	return numpy.flip( numpy.matmul( numpy.linalg.inv(A), Q ) )
#
def polyCoeffs_q0v0a0vT( T, q0, v0, a0, vT ):
	A = numpy.array([	[1,	0,	0,	0],
						[0,	1,	0,	0],
						[0,	0,	2,	0],
						[0,	1,	2*T,3*T**3]
				])
	Q = numpy.array([q0, v0, a0, vT])
	return numpy.flip( numpy.matmul( numpy.linalg.inv(A), Q ) )
#