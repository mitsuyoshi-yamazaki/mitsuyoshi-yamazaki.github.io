# coding:utf-8

import re
from typing import Callable
from utilities import Language, get_translated_filepath, log

markdown_ignore_lines = [
  "",
  "---",
]

hugo_control_header_pattern = "^\n*---\n(\n|.)*\n---\n"

# 前方からチェックされるため-,#など他のパターンに含まれるパターンは後ろに置く
markdown_prefix_pattern = "^(>|\s*(#####|####|###|##|#|- \[ \]|- \[x\]|-|\d+\.))"

class MarkdownLine:
  raw_content: str
  prefix: str # Markdownの制御子
  content: str # 翻訳対象

  def __init__(self, raw_line: str):
    self.raw_content = raw_line

    if raw_line in markdown_ignore_lines:
      self.prefix = raw_line
      self.content = ""
      return
    
    match_object = re.search(markdown_prefix_pattern, raw_line)
    if match_object is None:
      self.prefix = ""
      self.content = raw_line
      return

    self.prefix = match_object.group() 
    self.content = raw_line.replace(self.prefix, "", 1)
    return

Translator = Callable[[str], str]

def get_translator(language: Language) -> Translator:
  if language == Language.ENGLISH:
    return lambda x: " [{0}] {1}".format(language.value, x) if len(x) > 0 else ""  # TODO:
  elif language == Language.JAPANESE:
    raise ValueError("Unsupported target language {}".format(language))
  else:
    raise ValueError("Undefined language code {}".format(language))

def translate(contents: str, translator: Translator) -> str:
  hugo_control_header_match = re.search(hugo_control_header_pattern, contents)
  hugo_control_header = ""
  if hugo_control_header_match is not None:
    hugo_control_header = hugo_control_header_match.group()
    contents = contents.replace(hugo_control_header, "", 1)
    log("Hugo control header found:\n{}".format(hugo_control_header))
  else:
    log("Hugo control header not found")

  def translate_line(line: MarkdownLine) -> str:
    result = line.prefix + translator(line.content)
    if line.raw_content:
      log("{0}=={1}\n{2}\n".format(line.prefix, line.content, result))
    return result

  lines = [MarkdownLine(x) for x in contents.split("\n")]
  translated_lines = [translate_line(line) for line in lines]
  return hugo_control_header + "\n".join(translated_lines)

if __name__ == "__main__":
  import os
  import argparse    

  parser = argparse.ArgumentParser(description="Translate a markdown file")
  parser.add_argument("filepath", metavar="filepath", type=str, help="filepath to translate")
  parser.add_argument("language", metavar="language", type=str, help="language that it translates to")

  parsed = parser.parse_args()
  filepath = parsed.filepath
  language = Language(parsed.language)
  translator = get_translator(language)
  translated_filepath = get_translated_filepath(filepath, language)

  if os.path.exists(translated_filepath):
    raise ValueError("File already exists at path {}".format(translated_filepath))

  with open(filepath, "r") as f:
    contents = f.read()
    translated = translate(contents, translator)
    with open(translated_filepath, "w") as o:
      o.write(translated)
      print("Translation completed: {}".format(translated_filepath))
