from time import perf_counter, process_time
from functools import partial, wraps

fn = {	
		'sys': perf_counter, 
		'pro': process_time
	 }

def get_fn(ctr):
	try:
		return fn[ctr]
	except KeyError as e:
		# from https://stackoverflow.com/a/6062799
		import sys
		raise ValueError('ctr only takes arguments: \'sys\' and \'pro\'').with_traceback(sys.exc_info()[2])

def timer(func=None, ctr='sys'):
	''' Wrapper to time a function '''

	# double wrapper logic from https://stackoverflow.com/a/39335652
	if func is None:
		 return partial(timer, ctr=ctr)

	tm = get_fn(ctr)

	@wraps(func)
	def wrapper(*args, **kwargs):
		t = tm()
		res = func(*args, **kwargs)
		print(func.__name__, tm()-t)
		return res

	return wrapper


# from https://stackoverflow.com/a/12344609
import atexit
from datetime import timedelta
from time import strftime, localtime

def secondsToStr(elapsed=None):
	if elapsed is None:
		return strftime('%Y-%m-%d %H:%M:%S', localtime())
	else:
		return str(timedelta(seconds=elapsed))

def startlog(ctr='sys'):
	global start
	global tm

	tm = get_fn(ctr)
	start = tm()
	atexit.register(endlog)
	log('Start Program', elapsed=False)

def log(s, elapsed=True):
	global start
	global tm
	line = '='*40
	print(line)
	print(f'{secondsToStr()} - {s}')
	if elapsed:
		print(f'Elapsed time: {secondsToStr(tm() - start)}')
	print(line)
	print()

def endlog():
	atexit.unregister(endlog)
	log('End Program')