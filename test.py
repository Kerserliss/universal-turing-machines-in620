import parser as p
import turingmachine as TM

class TestTM:
	# TODO: test the Turing Machine class
	@staticmethod
	def runall():
		# TODO: executes all tests of this class
		TestTM.read()
		TestTM.write()
		TestTM.move()

	@staticmethod
	def create_iniy_config():
		pass

	@staticmethod
	def read():
		print("Testing Read")
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		# Test with the first TM - One tape:
		for k in ("0","1","#","_",""):
			config_test = TM_test1.create_init_config(k)
			tuple_test = TM_test1.read(config_test)
			if k == "":
				assert tuple_test == ('q0','_')
			else :
				assert tuple_test == ('q0',k)
	
		# test with the second TM - Two tapes :
		for k in ("0","1","#","_",""):
			for j in ("0","1","#","_",""):
				if k =="" and j =="":
					config_test = TM.Config([[],[]],[[],[]],"q")
				elif k =="": 
					config_test = TM.Config([[],[]],[[],[j]],"q")
				elif j =="" :
					config_test = TM.Config([[],[]],[[k],[]],"q")
				else :
					config_test = TM.Config([[],[]],[[k],[j]],"q")
				tuple_test = TM_test2.read(config_test)


				if k == "" and j == "":
					assert tuple_test == ('q','_' ,'_')
				elif k =="":
					assert tuple_test == ('q','_',j)
				elif j == "":
					assert tuple_test == ('q', k,'_')
				else :
					assert tuple_test == ('q',k,j)

		print("Testing complete")

	@staticmethod
	def write():
		print("Testing Writing") 
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		#Config for one tape :
		config_test = TM_test1.create_init_config("0")
		for k in ("0","1","#","_") :

			TM_test1.write(config_test,k)
			assert config_test.under[0][0] == k
		
		#Config for two tapes :
		config_test = TM.Config([[],[]],[["0"],["0"]],"q")
		for k in ("0","1","#","_") :
			for j in ("0","1","#","_") :
				TM_test2.write(config_test,[k,j])
				assert config_test.under[0][0] == k
				assert config_test.under[1][0] == j

		print ("Testing complete")

	@staticmethod
	def move() :
		print("Testing Moving") 
		TM_test1 = p.load_from_file("./files/test_1tape.tm")
		TM_test2 = p.load_from_file("./files/test_2tapes.tm")

		#Config for one tape :
		config_test = TM_test1.create_init_config("0")
		
		TM_test1.move(config_test,['>'])
		assert config_test.under[0][0] == '_'
		assert config_test.before[0][0] == '0'
		TM_test1.move(config_test,['<'])
		assert config_test.under[0][0] == '0'

		#Config for two tapes :
		config_test = TM.Config([[],[]],[["0"],["0"]],"q")
		TM_test2.move(config_test,['<','<'])
		assert config_test.under[0][0] == '_'
		assert config_test.under[1][0] == '_'
		TM_test2.move(config_test,['>','>'])
		assert config_test.under[0][0] == '0'
		assert config_test.under[1][0] == '0'
		assert config_test.before[0][0] == '_'
		assert config_test.before[1][0] == '_'

		print("Testing Complete")

	@staticmethod
	def next_move():
		pass


class TestUniversalTM:
	# TODO: test the Universal Turing Machine class
	@staticmethod
	def runall():
		# TODO: executes all tests of this class
		pass

class TestUniversalCounterTM:
	# TODO: test the Universal + Counter Turing Machine class
	@staticmethod
	def runall():
		# TODO: executes all tests of this class
		pass

TestTM.runall()