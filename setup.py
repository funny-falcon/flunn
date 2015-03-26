#!/usr/bin/env python

import setuptools

long_description = """Flunn is a simple decoder and encoder for the CBOR binary
object format described in RFC7049. It features a full CBOR base support and
also a simple streaming interface for networking applications. (it is fork of flynn)"""

setuptools.setup(
	name="flunn",
	version="1.0.0b4",
	packages=[
		"flunn",
	],
	author="Sokolov Yura aka funny_falcon, Fritz Grimpen",
	author_email="funny.falcon@gmail.com, fritz@grimpen.net",
	url="https://github.com/funny-falcon/flunn.git",
	download_url="https://github.com/funny-falcon/flunn/tarball/v1.0.0b4",
	license="http://opensource.org/licenses/MIT",
	description="Simple decoder and encoder for CBOR (fork of flynn)",
	classifiers=[
		"Development Status :: 4 - Beta",
		"Environment :: Web Environment",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Topic :: System :: Networking",
	],
	long_description=__doc__
)
