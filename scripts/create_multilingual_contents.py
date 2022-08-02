# coding:utf-8

import os
import utilities
from utilities import get_translated_filepath, log
from translation import translate

def get_multilingual_filepaths(target_content_path):
  return [get_translated_filepath(target_content_path, x) for x in utilities.target_languages]

def create_multilingual_content(target_content_path):
  copied_content_filepaths = []
  with open(target_content_path, "r") as f:
    original_content = f.read()

    for target_language in utilities.target_languages:
      target_filepath = get_translated_filepath(target_content_path, target_language)
      if not os.path.exists(target_filepath):
        translated_content = translate(original_content, target_language)
        with open(target_filepath, "w") as o:
          o.write(translated_content)
          copied_content_filepaths.append(target_filepath)
  return copied_content_filepaths

def create_multilingual_contents(directory_path):
  copied_content_filepaths = []
  for name in os.listdir(directory_path):
    path = os.path.join(directory_path, name)
    if os.path.isfile(path):
      if utilities.default_language.value in os.path.basename(path):
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
  results = create_multilingual_contents(utilities.content_root_path)
  print("Created {0} multilingual content files:\n{1}".format(len(results), "\n".join(results)))