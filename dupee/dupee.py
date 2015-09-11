
import argparse
import re

from collections import defaultdict
from os import listdir
from os.path import abspath
from os.path import isfile
from os.path import join

from PIL import Image

from filehash import FileHash
from imagehash import dhash


class FileObject(object):
    pass


class Dupee(object):

    def list_files(self, rootdir, recursive=False):
        fileobjs = []
        filelist = [join(rootdir, f)
                    for f in listdir(rootdir) if isfile(join(rootdir, f))]
        for f in filelist:
            fileobj = FileObject()
            fileobj.path = abspath(f)
            fileobj.hash = self.imhash(f) if self.isimage(
                f) else FileHash(f).md5()
            fileobjs.append(fileobj)
        return [f for f in fileobjs if f.hash is not None]

    def isimage(self, f):
        """check if given file is image using its extension"""
        imgregex = re.compile(r'\.(jpe?g|png|gif|bmp)$')
        # return bool(imgregex.search(f))
        if imgregex.search(f):
            return True
        return False

    def imhash(self, pic):
        """use dhash algorithm to hash image"""
        try:
            image = Image.open(pic)
            h = str(dhash(image))
        except:
            return None
        return h

    def dedupe(self, filelist):
        """return a list of duplicate files found in filelist"""
        d = defaultdict(list)
        for f in filelist:
            d[f.hash].append(f.path)
        dupes = {k: v for k, v in d.iteritems() if len(v) >= 2}
        return dupes

    def main(self):
        parser = argparse.ArgumentParser(usage="-h for full usage")
        parser.add_argument('rootdir', help='source directory')
        args = parser.parse_args()
        files = self.list_files(args.rootdir)
        d = self.dedupe(files)
        for v in d.values():
            print v

if __name__ == '__main__':
    Dupee().main()
