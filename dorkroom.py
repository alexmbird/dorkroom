#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
import subprocess


class Timer(object):
	
	'''
	Simple stopwatch.
	'''
	
	def __init__(self):
		super(Timer,self).__init__()
		self._last			= time.time()
	
	def waituntil(self, n, reset=False):
		"Sleep until it is n seconds past the last reset"
		if reset:
			self._last = time.time()
		waketime 		= self._last + n
		while time.time() < waketime:
			print(int(waketime-time.time()))
			time.sleep(1)
		self._last = waketime

def say(s):
	"Use speech synth to say something"
	print(s)
	cmd = ["say", s]
	subprocess.call(cmd)
	

	
if __name__ == '__main__':
	
	t = Timer()
	
	say("Pour in developer")
	
	# The following agitation is recommended for spiral tank processing with
	# ILFORD chemicals. Invert the tank four times during the first 10 seconds.
	# Repeat these four inversions during the first 10 seconds of each subsequent
	# minute of development.
	
	for minute in range(0, 5):
		say("minute %d - invert four times" % minute)
		t.waituntil(60)
	
	say("Last minute - invert four times")
	say("Get ready to drain developer")
	t.waituntil(50)
	say("Drain developer")
	t.waituntil(10)
	
	say("Pour in stop; minimum 10 seconds")
	t.waituntil(10)
	say("Drain stop; press enter to continue")
	input()
	
	say("Pour in fix; 2 to 5 minutes")
	t.waituntil(60*3, reset=True)
	say("Drain fixer; press enter to continue")
	input()
	
	say("Wash for 5 to 10 minutes")
	t.waituntil(60*5, reset=True)
	say("Wash complete")
