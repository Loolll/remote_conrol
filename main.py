from modules import settings
from modules import functions
import os


if __name__ == '__main__':
	associations = {}
	try:  # Parsing already created associations from file
		with open('settings') as file:
			temp = ''.join([x for x in file.read()]).split('\n')	
			for string in temp:
				string = string.split('~')
				try:
					associations['_'.join((string[0].split()))] = string[-1].lstrip()
				except IndexError:
					pass
	except FileNotFoundError:
		pass

	print('Init....OK')
	while True:
		functions.audio_recording(filename='temp.wav')
		words = functions.recognize_speech('temp.wav')
		print(words)
		key = '_'.join(words.split()) 
		if key in associations:
			with open('log.log', 'a') as log:
				output = os.system('cmd /c {}'.format(associations[key]))
				log.write(associations[key])
			