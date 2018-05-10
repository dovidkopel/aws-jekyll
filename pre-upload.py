import glob
import os

def rename(f):
	old = ff = f.replace('/index.html', '')
	ff = f.replace('/index.html', '.html')
	print('{} --> {}'.format(f, ff))
	os.rename(f, ff)
	os.rmdir(old)	
	
for f in glob.glob('_site/archives/page/*/index.html', recursive=True):
	rename(f)

for f in glob.glob('_site/archives/date/*/index.html', recursive=True):
	rename(f)
	
for f in glob.glob('_site/archives/tag/*/index.html', recursive=True):
	rename(f)
