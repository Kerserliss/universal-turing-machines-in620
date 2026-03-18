"""
This file contains a simple parser to run various parts of the project
Uses: argparse (from standard library)
"""
import argparse
import os
import sys
from test import *

parser = argparse.ArgumentParser(
	prog="Universal or Not Turing Machines", 
	description="Runs Turing Machines, specified using the format of: https://turingmachinesimulator.com/",
	epilog="Authors: Kerserlis, Egeyae, Ellyna Soumelis")

parser.add_argument("-v", "--verbose", action="store_true", help="Increase verbosity")
action = parser.add_subparsers(dest="action")

test = action.add_parser("test", help="Execute tests (located in test.py)")
test.add_argument("-w", "--which", choices=["all", "tm", "utm", "uctm"], help="Choose which part of the project you want to test", default="all")

run = action.add_parser("run", help="Executes a Turing Machine on an input")
run.add_argument("file", help="File containing Turing Machine description")
run.add_argument("input", help="Input for the TM, if it is a valid file, loads file content")
run.add_argument("--out", "--output", help="If specified, will write to specified path instead of standard output")
run.add_argument("-of", "--output-format", choices=["normal", "pretty"], default="normal", help="If pretty used, prints all the TM steps, else prints the output only")


args = parser.parse_args()

match args.action:
	case "test":
		match args.w:
			case "all":
				TestTM.runall()
				TestUniversalTM.runall()
				TestUniversalCounterTM.runall()
			case "tm":
				TestTM.runall()
			case "utm":
				TestUniversalTM.runall()
			case "uctm":
				TestUniversalCounterTM.runall()
	case "run":
		assert os.path.isfile(args.file), "Invalid turing machine path specified"

		input_ = args.input_
		if os.path.isfile(args.input):
			with open(args.input) as f:
				input_ = f.read()

		if args.out:
			new_out = open(args.out, "w")
			sys.stdout = new_out

		# TODO: load the TM and init Config

		match args.of:
			case "normal":
				# TODO: run the TM as question 4
				pass
			case "pretty":
				# TODO : run the TM as question 5
				pass