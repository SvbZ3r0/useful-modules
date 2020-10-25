from time import perf_counter

def timer(func):

	def wrapper(*args):
		t = perf_counter()
		res = func(*args)
		print(func.__name__, perf_counter()-t)
		return res

	return wrapper


# from https://stackoverflow.com/a/12344609
import atexit
from datetime import timedelta
from time import strftime, localtime

def secondsToStr(elapsed=None):
	if elapsed is None:
		return strftime("%Y-%m-%d %H:%M:%S", localtime())
	else:
		return str(timedelta(seconds=elapsed))

def startlog():
	global start
	start = perf_counter()
	atexit.register(endlog)
	log("Start Program")

def log(s, elapsed=None):
	line = "="*40
	print(line)
	print(secondsToStr(), '-', s)
	if elapsed:
		print("Elapsed time:", elapsed)
	print(line)
	print()

def endlog():
	global start
	end = perf_counter()
	elapsed = end-start
	log("End Program", secondsToStr(elapsed))