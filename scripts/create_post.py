def create_post():
  import sys
  import datetime
  import subprocess

  category = "posts"
  filename = "{}".format(datetime.datetime.now())

  command = 'hugo new "{0}/{1}.md"'.format(category, filename)
  subprocess.run(command, shell=True, stdout=sys.stdout, stderr=sys.stderr)

if __name__ == "__main__":    
  create_post()