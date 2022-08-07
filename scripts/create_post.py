# coding:utf-8

def create_post(filename: str):
  import sys
  import datetime
  import subprocess
  import utilities

  category = "posts"

  command = 'hugo new "{0}/{1}.{2}"'.format(category, filename, utilities.default_language_extension)
  subprocess.run(command, shell=True, stdout=sys.stdout, stderr=sys.stderr)

if __name__ == "__main__":    
  import argparse    
  import datetime

  parser = argparse.ArgumentParser()
  parser.add_argument("title", type=str)

  title = parser.parse_args().title
  # filename = "{}".format(datetime.datetime.now())
  filename = "{0}_{1}".format(datetime.datetime.now().date(), title)

  create_post(filename)