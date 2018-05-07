class A(object):
	def go(self):
		print("A class go ---A")
	def stop(self):
		print("A class stop---A")
	def pause(self):
		raise Exception("A class Pause--A")

class B(A):
	def go(self):
		super(B,self).go()
		print("go B go !---B")
	
class C(A):
	def go(self):
		super(C, self).go()
		print("go C go !----C")
	def stop(self):
		super(C, self).stop()
		print("stop C Stop--C")

class D(B,C):
	def go(self):
		super(D,self).go()
		print("D class Go BC --D")
	def stop(self):
		super(D,self).stop()
		print("Stop D Stop ||---D")
	def pause(self):
		print("Wait D go Paused===D")

class E (B,C):
	pass

a = A()
b = B()
c = C()
d = D()
e = E()

a.go()
b.go()
d. go()
a.stop()
c.go()
c.stop()
d.stop()
d.pause()
e.go()
e.stop()
e.pause()
a.pause()
	
