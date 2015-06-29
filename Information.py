#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *

import sys

class Information(QDialog):
	def __init__(self, type):
		super(Information, self).__init__()

		self.type = type;

		self.setWindowTitle(self.type)
		self.setGeometry(420,180,680,300)

		text = self.read()
		label = QLabel(text, self)

	def read(self):
		text = ''

		if self.type == 'License':
			archive = 'License.txt'
		else:
			archive = 'Credits.txt'

		with open(archive, 'r') as f:
			for l in f:
				text = text + l
		return text

def main():
	app = QApplication(sys.argv)
	inf = Information('License')
	inf.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()