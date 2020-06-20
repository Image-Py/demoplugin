from imagepy.core.engine import Free, Table
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Score(Free):
	title = 'Student Score'

	def run(self, para=None):
		index = ['Stutent%s'%i for i in range(1,6)]
		columns = ['Math', 'Physics', 'Biology', 'History']
		score = (np.random.rand(20)*40+60).reshape((5,4)).astype(np.uint8)
		self.app.show_table(pd.DataFrame(score, index, columns), 'Scores')

class Sort(Table):
	title = 'Table Sort Demo'

	para = {'by':'Math'}
	view = [('field', 'by', 'item', '')]

	def run(self, tps, snap, data, para=None):
		tps.data.sort_values(by=para['by'], inplace=True)

class Bar(Table):
	title = 'Score Chart Demo'
	asyn = False

	para = {'item':[]}
	view = [('fields', 'item', 'select items')]

	def run(self, tps, snap, data, para = None):
		data[para['item']].plot.bar(stacked=True, grid=True, title='Score Chart')
		plt.show()

plgs = [Score, Sort, Bar]