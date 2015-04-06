import hashlib

class filehash:
	def __init__(self,filepath):
		self.filepath=filepath

	def md5(self):
		hasher = hashlib.md5()
		with open(self.filepath, 'rb') as afile:
			hasher.update(afile.read())
		return hasher.hexdigest()

	def sha1(self):
		hasher = hashlib.sha1()
		with open(self.filepath, 'rb') as afile:
			hasher.update(afile.read())
		return hasher.hexdigest()

	def hash(self):
		sha1=self.sha1()
		md5=self.md5()
		return {'md5':md5,'sha1':sha1}

