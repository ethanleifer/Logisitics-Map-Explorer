# imports:
from DEgraphics import *
from random import random
import sys
import time
global REQUIREMENTS, FUNCTIONDESCRIPTIONS, MENULAYOUT, PROJECTINFO

'''
	Name: Ethan Leifer
	File: LogisticMapExplorerELV5.py
	Date Created: October 24, 2019
	Date Last Modifed: November 5, 2019
'''

# function variables
PROJECTINFO = "\nName: Ethan Leifer\
	\nFile: LogisticMapExplorerELV5.py\
	\nDate Created: October 24, 2019\
	\nDate Last Modifed: November 5, 2019"
REQUIREMENTS = "\nINPUTS:\
		\n\t• the dynamic parameter, R, in the logistic equation.\
		\n\t• the number of transient iterations\
		\n\t• the number of iterations to graph\
		\n\t• the ability to zoom in and out on the bifurcation diagram\
		\nOUTPUTS\
		\n\t• the bifurcation diagram\
		\n\t• the cobweb diagram\
		\n\t• the time-series graph\
		\n\t• the periodicity (or aperiodicity) of a particular R-value\
		\nAll graphs should be clearly and effectively labeled. Each graph should\
		\nhave its own window."
FUNCTIONDESCRIPTIONS = "\nBifurcation Diagram Class: To graph Bifurcation Diagram\
			\n\t• graphBifurcation: graphs bifurcation\
			\n\t• closeWin: closes Bifurcation window\
			\n\t• labelAxis: labels the axis with two text objects\
		\n\nCWTS Diagram class: To graph the Cobweb and Time series diagrams\
			\n\t• graphIterateonX: graphs a veritcal line\
			\n\t• graphIterateonY: graphs a horizontal line\
			\n\t• graphfx: graphs the f(x) function on cobweb\
			\n\t• graphCobweb: graphs the cobweb iterations on cobweb diagram\
			\n\t• clearGraphs: clears the cobweb and time series diagrams\
			\n\t• regraph: clears the graphs then regraphs them\
			\n\t• graphTimeSeries: graphs time series\
			\n\t• closeWins: closes the two graph windows\
			\n\t• labelAxis: label the two graphs axis\
		\n\nOther Functions\
		\n\t• f: returns value of f(x)\
		\n\t• confirmOption, getOption: makes sure an option is in a list\
		\n\t• confirmOptionBetweenNum: makes sure an option is a number\
		\n\t• generatex0: generates a new x0 value\
		\n\t• generateRvalue: generates a new R value\
		\n\t• getPeriod: returns periodicity of R value\
		\n\t• zoom: mangages program flow of zoom functionality of the 3 windows\
		\n\t• changeValues: manges program flow of changing specific function values\
		\n\t• showInformation: manages program flow of printing information about program\
		\n\t• intro: prints basic information about my code\
		\n\t•main: manages while loop to control certain program flow"
MENULAYOUT = "\nMenu Layout / Instructions:\
		\n This will show a layout of the menu options. \
		\nEnter intial values for Bifurcation and cobweb diagram\
		\n0: Quit\
		\n1: Change Time series and cobweb values\
			\n\t0: Go Back\
			\n\t1: Change x0 Value\
			\n\t2: Change R value\
				\n\t\t0: Go Back\
				\n\t\t1: Click R value on Bifurcation\
				\n\t\t2: Enter R Value\
				\n\t\t3: Enter periodicity\
			\n\t3: Change Iterations on Cobweb\
			\n\t4: Change transient Iterations for Time Series\
			\n\t5: Chang Iterations to display on cobweb\
		\n2: ZOOM\
			\n\t0: Go back\
			\n\tc: Cobweb Diagram\
				\n\t\tin: zoom in\
				\n\t\tout: zoom out (only if user has zoomed in before)\
			\n\tb: Bifurcation\
				\n\t\tin: zoom in\
				\n\t\tout: zoom out (only if user has zoomed in before)\
			\n\tt: Tim Series\
				\n\t\tin: zoom in\
				\n\t\tout: zoom out (only if user has zoomed in before)\
		\n3: Get periodicity for current R value\
		\n4: Show information about project\
			\n\t0: Go back\
			\n\t1: show project REQUIREMENTS\
			\n\t2: to show basic information about File\
			\n\t3: to show discriptions of functions\
			\n\t4: to show Instructions"

# constants
GRAPHCOLOR = "red"
LINECOLOR = "black"

# GET R VALUE DOESNT WORK

# f(x) function
def f(R, x):
	"""f(x) = Rx(1-x)."""
	return R * x * (1.0 - x)
	Rx - Rx ^ 2

class BifurcationDiagram:

	def __init__(self):
		print("Bifurcation Window setup: ")
		# Create intial Bifurcation window
		self.win = DEGraphWin(title="Bifurcation Diagram", width=800, height=200, defCoords=[-.1, -.1, 4.2, 1.05])
		self.win.toggleAxes()
		self.labelAxis()

		# Intialize variables used in Bifurcation Diagram
		self.step = (self.win.currentCoords[2] - self.win.currentCoords[0]) / self.win.width
		self.iterations = int(self.win.height / 2)
		self.zoomIn = False  # if the user has zoom in yet

		# asks user to set number of transient iterations
		self.transients = confirmOptionBetweenNum(False, [0, sys.maxsize], "Please enter the amount of transient iterations.")

		# graphs Bifurcation Diagram
		self.graphBifurcation()

	def graphBifurcation(self):
		# Intialize R to 0
		RBif = 0.0
		# For every iteration of R graph the iterations
		while RBif <= 4:
			# generate a random intial condition in [0,1]
			x0 = random()
			# iterate away a large transients
			for i in range(self.transients):
				x0 = f(RBif, x0)
			# iterate some number of iterates and plot as fcn of R
			for n in range(self.iterations):
				x0 = f(RBif, x0)
				self.win.plot(RBif, x0, GRAPHCOLOR)

			RBif += self.step

	def closeWin(self):
		# closes the Bifurcation Diagram
		self.win.close()

	def labelAxis(self):
		# labels x and y axis on bifurcation window
		Text(Point(2.1, -.05), "R value").draw(self.win)
		Text(Point(-.05, .5), "x").draw(self.win)

class CWTSDiagram:

	def __init__(self, R):
		# instance variables for Time Series Diagram
		print("\nTime Series Setup: ")
		self.winTS = DEGraphWin(width=800, height=200, defCoords=[-5, -.2, 100, 1.05], title="Time Series")
		self.winTS.toggleAxes()

		# asks user to set values for time series
		self.iterations = confirmOptionBetweenNum(False, [100, 10000], "Please enter an amount of iterations you want to display. ")
		self.transients = confirmOptionBetweenNum(False, [0, sys.maxsize], "Please enter the amount of transient iterations. ")
		self.x0 = generatex0()

		# Intialize variables usinbg on Time series diagram
		self.stepTS = (self.winTS.currentCoords[2] / self.iterations)
		self.R = R
		self.zoomInTS = False  # if the user has zoomed in yet

		# graphs Time series
		self.graphTimeSeries()

		# creates and setup graph window
		print("\nCobweb Setup: ")
		self.winCW = DEGraphWin(title="Cobweb Diagram", width=400, height=400, defCoords=[-.1, -.1, 1, 1])
		self.winCW.toggleAxes()

		# Intialize variables usinbg on Cobweb Diagram diagram
		self.stepCW = (self.winCW.currentCoords[2] - self.winCW.currentCoords[0]) / self.winCW.width
		self.lines = []  # list of all of the iteration lines to make it easy to clear
		self.zoomInCW = False

		# asks user to input values used in Cobweb Diagram
		self.iterates = confirmOptionBetweenNum(False, [1, 100], "Please enter an iterate. ")

		# creates steady state line
		origin = Point(0, 0)
		oneOne = Point(1, 1)
		self.steadyState = Line(origin, oneOne, 'solid')

		# grapghs the cobweb diagram
		self.graphCobweb()

		# label axis for both
		self.labelAxis()

	def graphIterateonX(self, x, y, finaly):
		# Graphs a horizontal line between y and finaly at x and returns cooresponding line obj
		line = Line(Point(x, y), Point(x, finaly), "solid")
		line.draw(self.winCW)
		return line

	def graphIterateonY(self, x, finalx, y):
		# Graphs a vertical line between y and finaly at x and returns cooresponding line obj
		line = Line(Point(x, y), Point(finalx, y), "solid")
		line.draw(self.winCW)
		return line

	def graphfx(self):
		# Graphs f(x) between 0 and 1
		x = 0
		while x <= 1:
			self.winCW.plot(x, f(self.R, x), GRAPHCOLOR)
			x += self.stepCW

	def graphCobweb(self):

		# graphs f(x) and steady state line
		self.graphfx()
		self.steadyState.draw(self.winCW)

		# current iterate
		i = 0
		# next two x values
		x = self.x0
		x1 = f(self.R, x)

		# creates of all of the line objects for x iterates
		while i < self.iterates:
			# if it is the first iterate start at 0
			if i == 0:
				self.lines.append(self.graphIterateonX(x, 0, x1))
			# otherwise start at steady steadystate
			else:
				self.lines.append(self.graphIterateonX(x, x1, x))
			# graph the cooresponding y lines (from f(x) to steady state)
			self.lines.append(self.graphIterateonY(x, x1, x1))

			# iterate the two x values
			x = x1
			x1 = f(self.R, x)
			# increase current iterate
			i += 1

	def clearGraphs(self):
		# clears the cobweb
		self.winCW.clear()
		self.winTS.clear()

		# removes the line objects from the iterates
		for line in self.lines:
			line.undraw()
		self.lines = []
		self.steadyState.undraw()

	def regraph(self):
		# clear the old cobweb
		self.clearGraphs()

		# regraph functions
		self.graphCobweb()
		self.graphTimeSeries()

	def graphTimeSeries(self):
		# x = current value after iteration of f(x)
		x = self.x0

		# iterate through transient values of x
		for i in range(self.transients):
			x = float(f(self.R, self.x0))

		# iterate through x values and graph on time series
		i = 0.0
		while i < self.winTS.currentCoords[2]:
			x = f(self.R, x)
			self.winTS.plot(i, f(self.R, x))
			i += self.stepTS

	def closeWins(self):
		# closes the Cobweb and Time Series
		self.winCW.close()
		self.winTS.close()

	def labelAxis(self):
		# draws text labels for Cobweb
		Text(Point(0.5, -0.05), "x").draw(self.winCW)
		Text(Point(-0.05, 0.5), "f(x)").draw(self.winCW)

		# draw text labels for Time Series
		Text(Point(50, -0.05), "x").draw(self.winTS)
		Text(Point(-2.5, 0.5), "f(R, x)").draw(self.winTS)

# Two functions that make sure an item is a set of values (one for a set of options and one that checks if a number is inbetween two numbers)
def confirmOption(options, statement):
	# A string that is all of the items of options formatted through for loop below
	optionsstr = " "
	for i in options:
		if i == options[len(options) - 1]:
			optionsstr += "'" + i + "')"
		elif i == options[0]:
			optionsstr += "('" + i + "', "
		else:
			optionsstr += "'" + i + "', "
	optionsstr += ": "
	# asks the user for intial input
	userinput = input(statement + optionsstr)
	# makes sure the user enters an input which is an option
	while not(userinput in options):
		userinput = input("You entered an incorrect value. You have to enter " + optionsstr)
	return userinput

def confirmOptionBetweenNum(returnFloat, between, statement):
	# Ask user to input a number (float if true, false if int) between between[0] INCLUDING and between[1] checks if it is in that range returns it
	run = True
	while run:
		try:
			# if the user wants a float ot be returned
			if returnFloat:
				# asks the user for a float input
				userInput = float(input(statement + "A float between [" + str(between[0]) + ", " + str(between[1]) + "]: "))
				# checks if the input is between between[0] and between[1]
				if userInput >= float(between[0]) and userInput <= float(between[1]):
					return userInput
				# if not rasie a ValueError (for except statement)
				else:
					raise ValueError
			# if the user wants a integer returned
			else:
				# asks the user for a integer input
				userInput = int(input(statement + "A Integer between [" + str(between[0]) + ", " + str(between[1]) + "]: "))
				# checks if the input is between between[0] and between[1]
				if userInput >= int(between[0]) and userInput <= int(between[1]):
					return userInput
				# if not rasie a ValueError (for except statement)
				else:
					raise ValueError
		# if the input isnt a number between between[0] and between[1] try again
		except ValueError:
			print("INVALID! Try again.")
			# brings user back to the begining of the while loop
			continue
		else:
			# returns userinput if it is the right datatype and is between between[0] and between[1]
			return userinput
			run = False

# better formated confirmOption (better for a list with more than just 2 options)
def getOption(options, statement):
	# statemnt is a string that is all of the items of options formatted so you can show what each option does
	# asks the user for intial input

	# prints formated options
	print(statement)
	# makes sure the user enters an input which is an option
	userinput = input("Please enter a option: ")
	while not(userinput in options):
		print("INVALID INPUT! Please try again:\n" + statement)
		userinput = input("Please enter a option: ")

	# returns checked user input
	return userinput

# Generates either a random x0 value or make sure the user enters one that is greater than 0
def generatex0():
	# Asks the user if they want to enter their own intial condition
	userinput = confirmOption(['y', 'n'], "Do you want to choose your intial condition?")
	if userinput == 'y':
		# makes sure the user entered intial condition is > 0
		x0 = confirmOptionBetweenNum(True, [0, 1], "Please enter a x0. ")
	# other wise randomly generate an intial condition
	else:
		x0 = random()
		print("Your randomized x0 value is " + str(x0))

	return x0

# Generates either a R value between 0 and 4 depending on user prefernces
def generateRvalue(BF):
	print("\nGenerating R Value...")
	R = 0.0
	# asks user to either click bifurcation window or enter a custom R value
	option = getOption(['enter', 'click'], "'enter' to enter a custom R value\n'click' to click r value on bifurcation diagram")
	if option == 'enter':
		# asks user to enter a custom R value
		R = confirmOptionBetweenNum(True, [0, 4], "Please enter an R value. ")
		print("You entered an R value of " + str(R))
	else:
		# asks user to click bifurcation window
		print("Please click on bifurcation window")
		R = BF.win.getMouse().getX()
		print("You clicked R value of " + str(R))

	return R

# to get periodicity of R
def getPeriod(R, x0=random(), numIterations=10000, numTransients=10000, epsilon=1.0e-15):

	# iterate through f(x) a trivally large time to make sure f(x) is at final condition
	for i in range(numTransients):
		x0 = f(R, x0)

	run = True
	# lowest period is equal to 1
	period = 1
	# to see if firstValue repeats
	firstValue = x0

	while run:
		# iterate f(x)
		x0 = f(R, x0)

		# check if the difference between x0 and the firstValue is trivally small that their is not a difference
		if abs(x0 - firstValue) < epsilon:
			return period
		# if it is aperiodic return -1
		if period == numIterations:
			return -1
		period += 1

# manage zooming of different windows
def zoom(BF, CWTS):

	# values for getting option from user
	zoomGraphOptions = ["c", "b", "t"]
	zoomGraphStatement = "'c' to change zoom on cobweb diagram\n'b' to change zoom on bifircation diagram\n't' to change zoom on time series"
	zoomOptions = ['in', 'out']
	zoomStatment = "'in' to zoom in\n'out' to zoom out (to default coordinates)"
	# get input from user
	graph = getOption(zoomGraphOptions, zoomGraphStatement)

	while not(graph == '0'):

		# asks user to zoom in on bifurcation window
		if graph == 'b':
			# if bifurcation has not been zoom in before only let user zoom in
			if not(BF.zoomIn):
				print("You must zoom in first")
				BF.win.zoom("in")

				# Changed coordinates you have to change step size to make graph look good
				BF.step = (BF.win.currentCoords[2] - BF.win.currentCoords[0]) / BF.win.width
				# you have zoomed in so change cooresponding variables
				BF.zoomIn = True
			# ask user if they want to zoom in
			else:
				if getOption(zoomOptions, zoomStatment) == 'in':
					BF.win.zoom("in")

					# Changed coordinates you have to change step size to make graph look good
					BF.step = (BF.win.currentCoords[2] - BF.win.currentCoords[0]) / BF.win.width
					# you have zoomed in so change cooresponding variables
					BF.zoomIn = True

				else:
					BF.win.zoom("out")
					# you have zoomed in so change cooresponding variables
					BF.zoomIn = False
			# regraph
			BF.graphBifurcation()

		# asks user to zoom in on cobweb window
		if graph == 'c':
			# if cobweb has not been zoom in before only let user zoom in
			if not(CWTS.zoomInCW):
				print("You must zoom in first")
				CWTS.winCW.zoom()
				CWTS.zoomInCW = True

				# Changed coordinates you have to change step size to make graph look good
				CWTS.stepCW = (CWTS.winCW.currentCoords[2] - CWTS.winCW.currentCoords[0]) / CWTS.winCW.width
			else:
				# ask user if they want to zoom in
				if getOption(zoomOptions, zoomStatment) == 'in':
					CWTS.winCW.zoom("in")
					CWTS.zoomInCW = True

					# Changed coordinates you have to change step size to make graph look good
					CWTS.stepCW = (CWTS.winCW.currentCoords[2] - CWTS.winCW.currentCoords[0]) / CWTS.winCW.width
				# if not zoom out
				else:
					CWTS.winCW.zoom("out")
					CWTS.zoomInCW = False
			# regraph
			CWTS.regraph()

		# asks user to zoom in on time series window
		if graph == 't':
			# if time series has not been zoom in before only let user zoom in
			if not(CWTS.zoomInTS):
				print("You must zoom in first")
				CWTS.winTS.zoom("in")
				CWTS.zoomInTS = True
			else:
				# ask user if they want to zoom in
				if getOption(zoomOptions, zoomStatment) == 'in':
					CWTS.wnTS.zoom("in")
					CWTS.zoomInTS = True
				# if not zoom out
				else:
					CWTS.winTS.zoom("out")
					CWTS.zoomInTS = False
					# you dont have to change step for time series
			# regraph
			CWTS.regraph()
		# make sure user is is done zooming
		if confirmOption(['y', 'n'], "Do you want to zoom again? ") == 'n':
			graph = '0'
		# if not get new input
		else:
			graph = getOption(zoomGraphOptions, zoomGraphStatement)

# manage changing values of each of the functions
def changeValues(BF, CWTS):
	# values for getting option from user
	changeValuesOptions = ['0', '1', '2', '3', '4', '5']
	changeValuesStatement = "'0' to go back\n'1' to change R value\n'2' to change x0 value\n'3' to change number of iterates (cobweb)\n'4' change number of transient iterations (time series)\n'5' change number of iterations to display (time series)"
	changeValueOption = getOption(changeValuesOptions, changeValuesStatement)
	# while loop condition
	keepRunningChangeValue = True

	while keepRunningChangeValue:
		# change R value
		if changeValueOption == '1':
			CWTS.R = generateRvalue(BF)
		# change x0 value
		if changeValueOption == str('2'):
			CWTS.x0 = generatex0()
		# change amount of iterates for cobweb
		if changeValueOption == '3':
			CWTS.iterates = confirmOptionBetweenNum(False, [1, 100], "Please enter an iterate.")
		# change trainsient iterations for time series
		if changeValueOption == '4':
			CWTS.transients = confirmOptionBetweenNum(False, [0, 10000], "Please enter the amount of transient iterations.")
		# changes iterations to display on
		if changeValueOption == '5':
			CWTS.iterations = confirmOptionBetweenNum(False, [0, 10000], "Please enter the amount of iterations to display")
			CWTS.stepTS = (CWTS.winTS.currentCoords[2] / CWTS.iterations)
		if changeValueOption == '0':
			# goes back a menu level
			keepRunningChangeValue = False
		else:
			print("\nRegraphing...\n")
			CWTS.regraph()
			changeValueOption = getOption(changeValuesOptions, changeValuesStatement)

def showInformation():
	# values for getting option from user
	infoOptions = ["0", "1", "2"]
	infoStatement = "'0' to go back '1' to show project REQUIREMENTS\n'2' to show basic information\n'3' to show discriptions of functions\n'4' to show Instructions"

	# get user input
	infoOption = getOption(infoOptions, infoStatement)

	while not(infoOption == '0'):

		# print project requirements
		if infoOption == '1':
			print("Showing project requirements\n Loading...")
			time.sleep(.5)
			print(REQUIREMENTS)

		# print information about project
		if infoOption == '2':
			print("Showing project information\n Loading...")
			time.sleep(.5)
			print(PROJECTINFO)

		# print descriptions of the functions in this code
		if infoOption == '3':
			print("Showing function discriptions\n Loading...")
			time.sleep(.5)
			print(FUNCTIONDESCRIPTIONS)

		# print menu layout of the code
		if infoOption == '4':
			print("Showing instructions\n Loading...")
			time.sleep(.5)
			print(MENULAYOUT)
		infoOption = getOption(infoOptions, infoStatement)

def showPeriodicity(CWTS):
	# get period for r value
	periodicity = getPeriod(CWTS.R)
	# make sure period is not aperiodic
	if periodicity == -1:
		periodicity = "aperiodic due to computational artifacts"
	# print periodicity
	print("Your current R value of " + str(CWTS.R) + " has a period of " + str(periodicity))

def intro():

	print("Hi. Thank you for trying out my Logistic Map Explorer.")
	time.sleep(1)
	print("This made by Ethan Leifer.")
	time.sleep(1)
	print("You will be asked to enter intial values for the functions to be able to graph.")
	time.sleep(1.5)
	print("After, you will have then be placed in a while loop where you can change values of the graphs, get periodicity of currrent R value, zoom or show more information about function")
	time.sleep(5)
	print("Hope you have fun!")
	time.sleep(.5)

# main function
def main():
	intro()
	print("\nIntializing Windows... \n")
	time.sleep(.3)

	# Intialize windows and r value
	BF = BifurcationDiagram()
	R = generateRvalue(BF)
	CWTS = CWTSDiagram(R)

	# values for getting option from user
	mainOptions = ["0", "1", "2", "3", "4"]
	mainstatement = "'0' to quit\n'1' to change Time Series or Cobweb Values\n'2' to zoom\n'3' to get periodicity for current R value\n'4' to get more information about code"
	option = getOption(mainOptions, mainstatement)

	while not(option == '0'):
		# change values for cobweb or time series diagram
		if option == '1':
			changeValues(BF, CWTS)

		# zoom in or out
		if option == '2':
			zoom(BF, CWTS)

		# gets periodicity for current R value
		if option == '3':
			showPeriodicity(CWTS)

		# To learn more about the code
		if option == '4':
			showInformation()

		# get new user input
		option = getOption(mainOptions, mainstatement)

	# close the two windows
	print("Quiting...\nThanks for playing with the Logistic Map!")
	CWTS.closeWins()
	BF.closeWin()


if __name__ == "__main__":
	main()
