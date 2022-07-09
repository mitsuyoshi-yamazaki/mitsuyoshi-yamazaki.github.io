import os
import shutil
import constants

DEBUG = False
def log(message):
  if not DEBUG:
    return
  print(message)

def get_multilingual_filepaths(target_content_path):
  return [target_content_path.replace(constants.default_language_extension, x) for x in constants.target_language_extensions]

def create_multilingual_content(target_content_path):
  copied_content_filepaths = []
  target_filepaths = get_multilingual_filepaths(target_content_path)
  log(target_filepaths)
  for path in target_filepaths:
    if not os.path.exists(path):
      shutil.copyfile(target_content_path, path)
      copied_content_filepaths.append(path)
  return copied_content_filepaths

def create_multilingual_contents(directory_path):
  copied_content_filepaths = []
  for name in os.listdir(directory_path):
    path = os.path.join(directory_path, name)
    if os.path.isfile(path):
      if constants.default_language_code in os.path.basename(path):
        copied_content_filepaths.extend(create_multilingual_content(path))
        log("[Copy] {}".format(path))
      else:
        log("[Translated] {}".format(path))
    elif os.path.isdir(path):
      copied_content_filepaths.extend(create_multilingual_contents(path))
    else:
      log("[Ignore] {}".format(path))
  return copied_content_filepaths

if __name__ == "__main__":    
  results = create_multilingual_contents(constants.content_root_path)
  print("Created {0} multilingual content files:\n{1}".format(len(results), "\n".join(results)))