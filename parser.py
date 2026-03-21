import re

# Valid chars used to name a state
STATE_R = r"[a-zA-Z0-9]+"
# The alphabet is all printable ASCII chars except space and del (cf: https://en.wikipedia.org/wiki/ASCII)
ALPHA_R = r"[\x21-\x7E]+"

# For the name of the Turing Machine, we allow spaces
NAME_R = rf"^name: ([\x20-\x7E]+)$"

INIT_R = rf"^init: ({STATE_R})$"
ACCEPT_R = rf"^accept: ({STATE_R})$"

# Finds every groups of read + transition
BLOCK_R = rf"^({STATE_R})((?:,{ALPHA_R})+)\n({STATE_R})((?:,{ALPHA_R})+)$"



