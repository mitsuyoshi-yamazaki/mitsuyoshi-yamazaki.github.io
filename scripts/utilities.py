# coding:utf-8

from enum import Enum

DEBUG = False

class Language(Enum):
  JAPANESE = "ja-jp"
  ENGLISH = "en"

content_root_path = "content"
default_language = Language.JAPANESE
target_languages = [
  Language.ENGLISH,
]

content_extension = "md"
def get_language_extension(language: Language):
  return "{0}.{1}".format(language.value, content_extension)

default_language_extension = get_language_extension(default_language)
target_language_extensions = [get_language_extension(x) for x in target_languages]

def log(message):
  if not DEBUG:
    return
  print(message)

def get_translated_filepath(filepath: str, language: Language) -> str:
  return filepath.replace(default_language_extension, get_language_extension(language))
