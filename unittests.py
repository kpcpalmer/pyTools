import numpy
import numpy.random
import unittest

from polynomialTools import makePoly_Q0V0A0QTVT
from polynomialTools import makePoly_Q0V0A0

class Test_A_polynomialTools( unittest.TestCase ):
	def test_A000_makePoly_Q0V0A0QTVT(self):
		# no motion
		r0 = numpy.random.random()*10 - 5
		v0 = 0
		a0 = 0
		rT = r0
		vT = 0
		target = [r0, 0, 0, 0, 0]
		result = makePoly_Q0V0A0QTVT(r0, v0, a0, rT, vT)
		self.assertTrue( numpy.allclose( target, result ) )
		
		# no initial acceleration
		r0 = numpy.random.random()*10 - 5
		v0 = numpy.random.random()*2 - 1
		a0 = 0
		rT = numpy.random.random()*10 - 5
		vT = v0
		target = [r0, v0, 0, 4*(rT - r0 - v0), -3*(rT - r0 - v0)]
		result = makePoly_Q0V0A0QTVT(r0, v0, a0, rT, vT)
		self.assertTrue( numpy.allclose( target, result ) )
		
		return
	#
	def test_A001_makePoly_Q0V0A0(self):
		r0 = numpy.random.random()*10 - 5
		v0 = numpy.random.random()*10 - 5
		a0 = numpy.random.random()*10 - 5
		target = [r0, v0, 0.5*a0]
		result = makePoly_Q0V0A0(r0, v0, a0)
		self.assertTrue( numpy.allclose( target, result ) )
		return
	#
#

if( __name__ == '__main__' ):
	unittest.main()
#