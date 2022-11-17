#!/usr/bin/env python3
message = [
202, 137, 
390, 235, 
114, 369, 
198, 110,
350, 396,
390, 383,
225, 258,
38, 291,
75, 324, 
401, 142,
288, 397]

alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

def mod_s():
	flag_decode = ''
	for x in message:
		mod = 37
		r   = x % mod  

		decode = alphabet[r]
		flag_decode += decode

	flag = "picoCTF{" + flag_decode + "}"
	print(flag)

mod_s()
