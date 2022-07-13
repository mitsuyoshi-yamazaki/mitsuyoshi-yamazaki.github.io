# coding:utf-8

def create_post():
  import sys
  import datetime
  import subprocess
  import utilities

  category = "posts"
  filename = "{}".format(datetime.datetime.now())

  command = 'hugo new "{0}/{1}.{2}"'.format(category, filename, utilities.default_language_extension)
  subprocess.run(command, shell=True, stdout=sys.stdout, stderr=sys.stderr)

if __name__ == "__main__":    
  create_post()