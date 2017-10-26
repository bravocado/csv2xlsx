import pandas as pd
import csv, argparse, os, sys, codecs
from openpyxl import Workbook


class Converter(object):
	"""
		Converter class
	"""

	def __init__(self):
		self._wb = Workbook()
		

	def convert(self, input_file, separator):
		sheet = self._wb.active
		output = os.path.basename(input_file)
		output_name = os.path.splitext(output)[0]
		ouput_ = "results/" + output_name + ".xlsx"
		print("converting...")
		with open(input_file) as file:
			reader = csv.reader(file)
			for row in reader:
				sheet.append(row)
			file.close()

		self._wb.save(ouput_)
		print("File converted to: " + ouput_)

def main():
	#   Arguments  #
	parser = argparse.ArgumentParser(description='.csv to .xlsx Converter')
	parser.add_argument("-i", "--input_file", type=str, default=None, required=True,
					help="input file")
	parser.add_argument('-s', '--separator', type=str, default=",", required=True,
						help='csv separator')
	args = parser.parse_args()

	converter = Converter()
	converter.convert(input_file=args.input_file,
					separator=args.separator)

if __name__ == "__main__":
	main()