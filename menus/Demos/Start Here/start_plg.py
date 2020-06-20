from imagepy.core.engine import Free

class HelloWorld(Free):
	title = 'Hello World'

	def run(self, para=None):
		self.app.alert('Hello World, I am ImagePy!')

class WhoAreYou(Free):
	title = 'Who Are You'
	para = {'name':'', 'age':0}
	view = [(str, 'name', 'name', 'please'),
			(int, 'age', (0,120), 0, 'age', 'years old')]

	def run(self, para=None):
	    self.app.alert('Name:\t%s\r\nAge:\t%d'%(para['name'], para['age']))

class Questionnaire(Free):
	title = 'Questionnaire'

	para = {'name':'yxdragon', 'age':10, 'h':1.72, 'w':70, 'sport':True, 'sys':'Mac', 'lan':['C/C++', 'Python'], 'c':(255,0,0)} 

	view = [('lab', 'lab', 'This is a questionnaire'),                       # 标签
			(str, 'name', 'name', 'please'),                                         # 字符
			(int, 'age', (0,150), 0, 'age', 'years old'),                  # 整数
			(float, 'h', (0.3, 2.5), 2, 'height', 'm'),                  # 浮点
			('slide', 'w', (1, 150), 0, 'kg'),                              # 滑块
			(bool, 'sport', 'do you like sport'),                               # 勾选
			(list, 'sys', ['Windows','Mac','Linux'], str, 'favourite', 'system'),                     # 单选
			('chos', 'lan', ['C/C++','Java','Python'], 'lanuage you like(multi)'), # 多选
			('color', 'c', 'which', 'you like')]                                     # 颜色

	def run(self, para=None):
		rst = ['Questionnaire Result', 
			'Name:%s'%para['name'], 
			'Age:%s'%para['age'],
			'Height:%sm'%para['h'], 
			'Weight:%skg'%para['w'], 
			'Like Sport:%s'%para['sport'],
			'Favourite System:%s'%para['sys'],
			'Like lanuage:%s'%para['lan'],
			'Favourite Color:%s'%str(para['c'])]

		self.app.alert('\r\n'.join(rst))

plgs = [HelloWorld, WhoAreYou, Questionnaire]