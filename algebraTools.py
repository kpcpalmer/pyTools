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
	#return numpy.asarray( [[c,0,s],[0,1,0],[-s,0,c]] )
	return numpy.asarray( [[c,0,-s],[0,1,0],[s,0,c]] )
#
def rotationZ( t ):
	c = numpy.cos(t)
	s = numpy.sin(t)
	return numpy.asarray( [[c,-s,0],[s,c,0],[0,0,1]] )
#
class quaternion( object ):
	def __init__(self, roll, pitch, yaw):
		cr = numpy.cos( roll )*0.5
		sr = numpy.sin( roll )*0.5
		cp = numpy.cos( pitch )*0.5
		sp = numpy.sin( pitch )*0.5
		cy = numpy.cos( yaw )*0.5
		sy = numpy.sin( yaw )*0.5
		
		
		self.q0 = cr*cp*cy + sr*sp*sy
		self.q1 = sr*cp*cy - cr*sp*sy
		self.q2 = cr*sp*cy + sr*cp*sy
		self.q3 = cr*cp*sy - sr*sp*cy
		
		q = numpy.array( [self.q0, self.q1, self.q2, self.q3] )
		self.q0 = self.q0 / numpy.linalg.norm(q)
		self.q1 = self.q1 / numpy.linalg.norm(q)
		self.q2 = self.q2 / numpy.linalg.norm(q)
		self.q3 = self.q3 / numpy.linalg.norm(q)
		self.n  = numpy.array( [self.q1, self.q2, self.q3] )
		return
	#
	def __str__(self):
		return "(" + str(self.q0) + "," + str(self.n) + ")"
	#
	def __sub__(self, B):
		X = numpy.zeros((4,4))
		X[0,0]  = self.q0
		X[0,1:] = -1*self.n
		X[1:,1] = self.n
		X[1:,1:] = self.q0*numpy.identity(3) + skewSymmetricMatrix(self.n)
		
		Y = numpy.zeros((4))
		Y[0] = B.q0 
		Y[1:] = B.n
		
		T = numpy.matmul(X,Y)
		Q = quaternion(0,0,0)
		Q.q0 = T[0]
		Q.q1 = T[1]
		Q.q2 = T[2]
		Q.q3 = T[3]
		Q.n  = numpy.array([Q.q1, Q.q2, Q.q3])
		return Q
	#
#