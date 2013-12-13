__copyright__ = "Copyright (C) 2013 David Braam - Released under terms of the AGPLv3 License"

avrChipDB = {
	'ATMega1280': {
		'signature': [0x1E, 0x97, 0x03],
		'pageSize': 128,
		'pageCount': 512,
	},
	'ATMega2560': {
		'signature': [0x1E, 0x98, 0x01],
		'pageSize': 128,
		'pageCount': 1024,
	},
	'ATMega644P': {
		'signature': [0x1E, 0x97, 0x03],
		'pageSize': 128,
		'pageCount': 512,
	},
}

def getChipFromDB(sig):
	for chip in avrChipDB.values():
		if chip['signature'] == sig:
			return chip
	return False

