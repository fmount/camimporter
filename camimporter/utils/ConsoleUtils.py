#!/usr/bin/env python
#


# ansi colors
class ANSIColors(object):
	def __init__(self):
		self.escapecode = '\033[%s;%sm'

		self.colors = {
			'RED': 1,
			'GREEN': 2,
			'YELLOW': 3,
			'BLUE': 4,
			'PURPLE': 5,
			'CYAN': 6,
			'WHITE': 7,
			'BLACK': 0
		}

		self.modifiers = {
			'BRIGHT': 1,
			'NORMAL': 0
		}

		# build color codes hashes
		self.compile_ansicolors_hash()

	# compile colors
	def compile_ansicolors_hash(self):
		colorlist = {}
		for intensity in self.modifiers.keys():
			colorlist[intensity] = {}
			for color in self.colors.keys():
				colorlist[intensity][color] = self.escapecode % (self.modifiers[intensity], 30 + self.colors[color])
		colorlist['RESET'] = '\033[0m'
		# update ansi colorlist hash
		self.ansi_escapes = colorlist

	# get colorlist
	def get_ansicolors_hash(self):
		return self.ansi_escapes

	# def get ansi code for color
	def get_code_for_color(self, mod, color):
		if mod in self.ansi_escapes.keys():
			if color in self.ansi_escapes[mod].keys():
				return self.ansi_escapes[mod][color]
		return None

	# output color text
	def write_color_code(self, text, mod="NORMAL", color="WHITE"):
		return "%s%s%s" % (self.get_code_for_color(mod, color), text, self.ansi_escapes['RESET'])

	# print with color
	def print_with_color(self, text, mod="NORMAL", color="WHITE"):
		print("%s%s%s" % (self.get_code_for_color(mod, color), text, self.ansi_escapes['RESET']))

	# print error message
	def s_error(self, text):
		print("%s%s%s" % (self.get_code_for_color(mod='BRIGHT', color='RED'), text, self.ansi_escapes['RESET']))

	# return error message
	def error(self, text):
		return "%s%s%s" % (self.get_code_for_color(mod='BRIGHT', color='RED'), text, self.ansi_escapes['RESET'])

	# print warning message
	def s_warning(self, text):
		print("%s%s%s" % (self.get_code_for_color(mod='BRIGHT', color='YELLOW'), text, self.ansi_escapes['RESET']))

	# return warning message
	def warning(self, text):
		return "%s%s%s" % (self.get_code_for_color(mod='BRIGHT', color='YELLOW'), text, self.ansi_escapes['RESET'])


	# print success message with more than one section
	def s_success(self, header, text=None):
		if text is not None:
			print("%s%s%s%s" % (self.get_code_for_color(mod='BRIGHT', color='GREEN'), \
					header, self.ansi_escapes['RESET'], text))
		else:
			print("%s%s%s" % (self.get_code_for_color(mod='BRIGHT', color='GREEN'), \
					header, self.ansi_escapes['RESET']))

	# return success message
	def success(self, text):
		return "%s%s%s" % (self.get_code_for_color(mod='BRIGHT', color='GREEN'), text, self.ansi_escapes['RESET'])

	# print normal message
	def print_normal(self, text):
		print("%s%s%s" % (self.get_code_for_color(mod='NORMAL', color='WHITE'), text, self.ansi_escapes['RESET']))

	# return normal message
	def normal(self, text):
		return "%s%s%s" % (self.get_code_for_color(mod='NORMAL', color='WHITE'), text, self.ansi_escapes['RESET'])
