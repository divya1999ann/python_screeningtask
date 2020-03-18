class Participant:
	def __init__(self,name):
		self.stack=None
		self.type_lm=None
		self.name=name
		self.time_from=None
		self.time_to=None
	def addStacks(self,stack):
		self.stack=stack
	def setMentorOrLearner(self,t):
		if self.t=='L':
			self.type_lm="Learner"
		elif self.t=='M':
			self.type_lm="Mentor"
		else:
			raise Exception()
	def setAvailableTime(self,t_from,t_to):
		if self.type_lm=="Mentor":
			self.time_from=t_from
			self.time_to=t_to
	def getMentor(self,s,t):
		if self.type_lm=="Mentor":
			if self.stack==s and (t>=self.time_from and t<=self.time_to):
				return self.name()
			
