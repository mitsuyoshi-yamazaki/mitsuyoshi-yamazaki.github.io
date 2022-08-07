# coding:utf-8

from ast import parse
import re
from typing import Collection, Tuple, Optional
from utilities import Language, get_translated_filepath, log

markdown_ignore_lines = [
  "",
  "---",
]

hugo_front_matter_pattern = "(^\n*---\n(\n|.)*?\n---\n|^\n*\+\+\+\n(\n|.)*?\n\+\+\+\n)"

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

class MarkdownParser:
  hugo_front_matter: Optional[str]
  lines: Collection[MarkdownLine]

  def __init__(self, contents: str):
    def split_contents() -> Tuple[Optional[str], str]:
      hugo_front_matter_match = re.search(hugo_front_matter_pattern, contents)
      if hugo_front_matter_match is None:
        log("Hugo control header not found")
        return (None, contents)
      
      header = hugo_front_matter_match.group()
      log("Hugo control header found:\n{}".format(header))
      return (
        header,
        contents.replace(header, "", 1)
      )

    parsed = split_contents()
    self.hugo_front_matter = parsed[0]
    self.lines = [MarkdownLine(line) for line in parsed[1].split("\n")]
    for line in self.lines:
      log("--")
      log("prefix: {}".format(line.prefix or '""'))
      log("content: {}".format(line.content or '""'))

class Translator:
  language: Language
  translating_comment: Optional[str]

  def __init__(self):
    pass

  def translate(self, line: str) -> str:
    raise NotImplementedError("Use concrete Translator classes")

class EnglishTranslator(Translator):
  def __init__(self):
    self.language = Language.ENGLISH
    self.translating_comment = "*This article is automatically generated from the original content*"

  def translate(self, line: str) -> str:
    return line # TODO: not implemented yet
    # return " [{0}] {1}".format(language.value, line) if len(line) > 0 else ""  # TODO:

def get_translator(language: Language) -> Translator:
  if language == Language.ENGLISH:
    return EnglishTranslator()
  elif language == Language.JAPANESE:
    raise ValueError("Unsupported target language {}".format(language))
  else:
    raise ValueError("Undefined language code {}".format(language))

def translate(contents: str, language: Language) -> str:
  markdown_parser = MarkdownParser(contents)
  translator = get_translator(language)

  translated_contents = [
  ]
  if markdown_parser.hugo_front_matter is not None:
    translated_contents.append(markdown_parser.hugo_front_matter)
  if translator.translating_comment is not None:
    translated_contents.append(translator.translating_comment)
  translated_contents.extend([line.prefix + translator.translate(line.content) for line in markdown_parser.lines])
  
  return "\n".join(translated_contents)

if __name__ == "__main__":
  import os
  import argparse    

  parser = argparse.ArgumentParser(description="Translate a markdown file")
  parser.add_argument("filepath", type=str, help="filepath to translate")
  parser.add_argument("language", type=str, help="language that it translates to")
  parser.add_argument("-f", action="store_true", help="force replacing the old translation file")

  parsed = parser.parse_args()
  filepath = parsed.filepath
  language = Language(parsed.language)
  translated_filepath = get_translated_filepath(filepath, language)

  if os.path.exists(translated_filepath):
    if parsed.f != True:
      raise ValueError("File already exists at path {}".format(translated_filepath))

  with open(filepath, "r") as f:
    contents = f.read()
    translated = translate(contents, language)
    with open(translated_filepath, "w") as o:
      o.write(translated)
      print("Translation completed: {}".format(translated_filepath))
