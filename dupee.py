from filehash import filehash
import os
import argparse

class fileobject:
	pass
class dupee:

	def list_files(self,rootdir):
		files=[]
		for dirName, subdirList, fileList in os.walk(rootdir):
			for fname in fileList:
				fileobj=fileobject()
				fileobj.path=os.path.abspath(os.path.join(dirName, fname))
				fileobj.hash=filehash(fileobj.path).md5()
				files.append(fileobj)
		return files

	def dupes(self,filelist):
		groups=[]
		hashes=[x.hash for x in filelist]
		unique_hashes=list(set(hashes))
		for item in unique_hashes:
			occurrence=self.occur(item,filelist)
			if len(occurrence)>=2:
				groups.append(occurrence)
		return groups

	def occur(self,term,liste):
		members=[]
		for member in liste:
			if term in member.hash:
				members.append(member)
		return members
	def dedupe(self,pair_list):
		pass

	def main(self):
		parser = argparse.ArgumentParser(usage="-h for full usage")
		parser.add_argument('rootdir', help='source directory')
		args = parser.parse_args()
		files=self.list_files(args.rootdir)
		for pair in self.dupes(files):
			for fileobj in pair:
				print fileobj.path
			print '####################################################'
if __name__ == '__main__':
	dupee().main()

