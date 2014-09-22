from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

"""
	Stuff for parsing and storing configuration files' data.
"""

import os.path
from ConfigParser import SafeConfigParser as _ConfParser


class _BaseConfig (object):
	"""
		Parses and stores data from config file/s
	"""
	def __init__ (self, *args):
		"""
			Reads in all the conf files whose filenames have been passed
			in as anonymous arguments. The files will be read in the order
			they were given, so settings in later files will override
			earlier ones.
		"""
		self.clear()
		self.load(args)
		
	
	def __repr__ (self):
		params = (self.__module__, self.__class__.__name__, len(self._files))
		return '<{0}.{1} using {2!s} files>'.format(params)
	
	def clear (self):
		"""
			Clears out any old config data.
		"""
		self._files = []
		self._parser = _ConfParser()
		
	
	def load (self, filenames):
		"""
			Loads in the configuration data from the given list of
			filenames.
		"""
		self._files.extend(filenames)
		
		found = self._parser.read(filenames)
		
		# Output warnings for files which couldn't be used.
		if len(found) < len(filenames):
			for file in filenames:
				if file not in found:
					print('WARNING: Unable to load "{0}"'.format(file))
		
	
	def reload (self):
		"""
			Reloads previously loaded config files.
		"""
		filenames = self._files
		self.clear()
		self.load(filenames)
		
	


class MonitorConfig (_BaseConfig):
	"""
		Parses and stores settings for the Pystromo monitor script.
	"""
	def clear (self):
		self._files = []
		# This is a list of 2-tuples; (process,filename)
		# It's a list, and not a dict, to maintain the order.
		self.mappings = []
		
	
	def load (self, filenames):
		"""
			Loads configuration data from the given list of files.
		"""
		# The format of these files differs from standard Conf files,
		# so we do all the work ourselves. :/
		self._files.extend(filenames)
		for file in filenames:
			try:
				fd = open(file)
			except IOError:
				print('WARNING: Unable to load "{0}"'.format(file))
				continue
			
			for line in fd.readlines():
				line = line.rstrip()
				if not line:
					# Blank
					continue
				if line[0] in ('#', ';'):
					# Comment
					continue
				
				# Separation of process and conf
				try:
					process, conf = line.split('=')
				except ValueError:
					print('WARNING: Invalid config line "{0}"'.format(line))
					continue
				
				if process.strip() == '*':
					process = None
				conf = conf.strip()
				
				self.mappings.append((process, conf))
				
			
		
	
