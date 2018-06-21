#Convert hex to base 64

import binascii 
def hexTo64():
	hex = raw_input("Hex value:")
	bytes = binascii.unhexlify(hex)
	print binascii.b2a_base64(bytes)
hexTo64()