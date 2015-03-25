Flunn - Simple CBOR En/Decoder
##############################

Flunn is also a Python library providing CBOR [RFC7049] encoding and decoding with a
traditional buffered and a streaming interface.
(flunn is a fork of flynn)

Usage
=====

The Flunn API is really simple and inspired by existing Python serialisation
modules like json and pickle. The flunn module has four methods called dumps,
dump, loads and load, where dumps will return the serialised input as bytes
string, while dump will write the serialised input to a file descriptor. The
same applies to loads and load.

	>>> flunn.dumps([1, [2, 3]])
	b'\x82\x01\x82\x02\x03'
	>>> flunn.loads(b'\x82\x01\x82\x02\x03')
	[1, [2, 3]]

Furthermore, Flunn supports generators and other iterables as input for
streaming support:

	>>> flunn.dumps(range(5))
	b'\x9f\x00\x01\x02\x03\x04\xff'
	>>> flunn.loads(b'\x9f\x00\x01\x02\x03\x04\xff')
	[0, 1, 2, 3, 4]

Or to generate a map using an iterable:

	>>> flunn.dumps((((a, a) for a in range(5)), "map"))
	b'\xbf\x00\x00\x01\x01\x02\x02\x03\x03\x04\x04\xff'
	>>> flunn.loads(b'\xbf\x00\x00\x01\x01\x02\x02\x03\x03\x04\x04\xff')
	{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

Copyright / License
===================

© 2015 Sokolov Yura aka funny_falcon
© 2013 Fritz Conrad Grimpen

The code is licensed under the MIT license, provided in the COPYING file of the
Flunn distribution.

