import glob
import os

bucket = os.environ['BUCKET']

def handle_file(f):
	f = f.replace('_site/', '')
	ff = f.replace('_site/', '')
	ff = ff.replace('.html', '')
	
	os.system('aws s3 mv s3://{}/{} s3://{}/{} --acl public-read --content-type "text/html"'.format(bucket, f, bucket, ff))
	
for f in glob.glob('_site/**/*.html', recursive=True):
	handle_file(f)
