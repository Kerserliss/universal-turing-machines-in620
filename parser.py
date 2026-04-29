import re
from turingmachine import TM, Config
import os


# Valid chars used to name a state
STATE_R = r"[a-zA-Z0-9]+"
# The alphabet is all printable ASCII chars except space and del (cf: https://en.wikipedia.org/wiki/ASCII)
ALPHA_R = r"[\x21-\x7E]+"

# For the name of the Turing Machine, we allow spaces
NAME_R = r"^name: ([\x20-\x7E]+)$"

INIT_R = rf"^init: ({STATE_R})$"
ACCEPT_R = rf"^accept: ({STATE_R})$"

# Finds every groups of read + transition
BLOCK_R = rf"^({STATE_R}),((?:{ALPHA_R})+)\n({STATE_R}),((?:{ALPHA_R})+)$"

def load_from_file(filepath: str) -> TM:
	if not (os.path.isfile(filepath) and os.path.splitext(filepath)[-1] in (".tm", ".utm")):
		raise ValueError(f"{filepath} is not a valid path or is not a recognized extension")

	with open(filepath, 'r') as f:
		content = f.read()

	name = re.search(NAME_R, content, re.MULTILINE)
	name = name.group(1) if name else "N/A"

	init = re.search(INIT_R, content, re.MULTILINE)
	accept = re.search(ACCEPT_R, content, re.MULTILINE)

	if not init or not accept:
		raise ValueError("Provided file is invalid, does not contain init and/or accept states description")

	init = init.group(1)
	accept = accept.group(1)

	blocks = re.findall(BLOCK_R, content, re.MULTILINE)

	# the 2nd group of the first match defines the number of tapes for the rest of the load
	number_tapes = len(blocks[0][1].split(",")) 

	# defines a lambda to check quickly if any block is invalid
	_check_block = lambda b: True if (len(b[1].split(","))==number_tapes and len(b[3].split(","))==2*number_tapes) else False

	states = set()
	transitions = dict()
	for block in blocks:
		if not _check_block(block):
			raise ValueError(f"Number of tapes is not consistent ! ({ block = })")

		states.add(block[0])
		states.add(block[2])
		read = tuple([block[0],] + block[1].split(","))
		write = tuple([block[2],] + [block[3].split(",")[:number_tapes],] + [block[3].split(",")[number_tapes:]])
		
		transitions[read] = write

	return TM(name,states,init,accept,number_tapes,transitions)

if __name__ == '__main__':
	x=load_from_file("./files/test_2tapes.tm")
	print(x)

	c = x.create_init_config("1001010100")
	print(x.next_step(c))

def binary_conversion(number, nb_bits):
	"""Function that ables to convert decimal numbers in binary numbers
	Parameter : number which represents the decimal number"""
	reste = []

	if number == 0 and nb_bits is None:
		return '0'
	
	binary = bin(number)[2:]
	
	if nb_bits is not None :
		if len(binary) > nb_bits : 
			raise ValueError(f"{number} cannot fit in {nb_bits} bits")
		return binary.zfill(nb_bits)
	return binary
	

def rename_states(machine, nb_bits = 8) :
	"""Renames all the states with a binary number instead
	We force the naming of the initial state and the accept state to 0 and 1 each
	Parameters : machine which represents the turing machine we want to convert
	"""
	max_states = 2 **nb_bits
	if len(machine.states) > max_states :
		raise ValueError(f"Too many states ({len(machine.states)}) for {nb_bits} bits (max{max_states})")
	
	dico_states = {}
	dico_states[machine.init] = binary_conversion(0, nb_bits)
	dico_states[machine.accept] = binary_conversion(1, nb_bits)

	counter = 2

	for state in machine.states :
		if state not in dico_states:
			dico_states[state] = binary_conversion(counter, nb_bits)
			counter+=1
	
	return(dico_states)

def conversion_binaire_alphabet(symbol, nb_bits = 8):
	return binary_conversion(ord(symbol), nb_bits)

def encode_alphabet(machine, nb_bits = 8):
	alphabet = set()

	for key,value in machine.transitions.items():
		alphabet.add(key[1])
		alphabet.add(value[1][0])

	max_symbols = 2**nb_bits
	if len(alphabet)>max_symbols : 
		raise ValueError(f"Too many symbols ({len(alphabet)} for {nb_bits} bits (max {max_symbols}))")
	
	alphabet_bis = {}

	for symbol in alphabet :
		alphabet_bis[symbol] = conversion_binaire_alphabet(symbol, nb_bits)
	return alphabet_bis

MOVEMENTS = {'>' : 0, '-' : 1, '<':2 }

def encode_movement(movement, nb_bits = 8):
	if movement not in MOVEMENTS:
		raise ValueError(f"Uknown movement :{movement}")
	return binary_conversion(MOVEMENTS[movement], nb_bits)


def encode_transition(machine, state_bits = 8, alphabet_bits = 8):
	"""Transforms the syntax of the MT transitions into the syntax wanted
	Parameter : MT"""

	states = rename_states(machine, state_bits)
	alphabet_machine = encode_alphabet(machine, alphabet_bits)
	t_transitions = []
	
	for key,value in machine.transitions.items() :
		current_state = states[key[0]]
		symbol_read = alphabet_machine[key[1]]
		new_state = states[value[0]]
		symbol_written = alphabet_machine[value[1][0]]
		movement = value[2][0]
		t_transitions.append(current_state + "|" + symbol_read + "|" + symbol_written + "|" + movement + "|" + new_state)

	return "|".join(t_transitions)

def universal_machine(filepath):
	"""Final function to determine a universal machine 
	Parameter : filepath"""
	machine = load_from_file(filepath)
	machine_final = encode_transition(machine)
	return machine_final


#print(MU("./files/test_1tape.tm"))

def encode_binary(filepath, nb_bits = 8):
	"""Function that produces the binary coding of the mt simulator file 
	Parameter : filepath"""
	machine_final = universal_machine(filepath)

	encoding = []

	for symbol in machine_final : 
		encoding.append(binary_conversion(ord(symbol), nb_bits))

	encoding = "".join(encoding)
	integer = int(encoding, 2)

	utm_path = filepath.replace('.tm', '.utm')
	with open(utm_path, 'w') as f: 
		f.write(encoding)

	return encoding, integer

print(encode_binary("./files/test_1tape.tm"))