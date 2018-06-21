import binascii 
#Produce the combined XOR of two equal length hex buffers

def fixedXOR():
	input1 = "1c0111001f010100061a024b53535009181c"
	input2 = "686974207468652062756c6c277320657965"

	input1 = bytearray.fromhex(input1)
	input2 = bytearray.fromhex(input2)

	XOR = bytearray(len(input1))

	if len(input1) == len(input2): 
		for i in range(len(input1)):
			XOR[i] = input1[i] ^ input2[i]
		print binascii.hexlify(XOR)
	else:
		print "Buffers are not of equal length"
fixedXOR()