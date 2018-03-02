class Person:
	def __init__(self,name,job,pay=0)
		self.name=name
		self.job=job
		self.pay=pay
	def lastName(self):
		self.name=self.name.swapcase()
	def giveRise(self,percent):
		self.pay=int(self.pay*(1+percent))
	def __repr__(self):
		return'[%s,%s]'%(self.name,self.pay)
class Management:
	def __init__(self,name,pay):
		Person.__init__(self,name,'mgr',pay)
	def giveRise(self,percent,bonus=0.10):
		Pesron.giveRise(self,percent+bonus)
if __name__=='__main__':
	p1=Person('satya narayana')
	p2=Person('Gagan dattaa',job='dev',pay=10,000)
	print(p1)
	