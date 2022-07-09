content_root_path = "content"
default_language_code = "ja-jp"
target_language_codes = [
  "en"
]

content_extension = "md"
def get_language_extension(language_code):
  return "{0}.{1}".format(language_code, content_extension)

default_language_extension = get_language_extension(default_language_code)
target_language_extensions = [get_language_extension(x) for x in target_language_codes]
