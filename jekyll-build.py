import os

bucket = os.environ['BUCKET']
base_cmd = '/usr/local/bundle/bin/jekyll {}'

if bucket == 'staging.dovidkopel.com':
    os.system(base_cmd.format('build --drafts'))
else:
    os.system(base_cmd.format('build'))
