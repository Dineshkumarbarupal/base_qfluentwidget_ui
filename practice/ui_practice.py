import language_tool_python

def correct_grammar_and_spelling(text):
    tool = language_tool_python.LanguageTool('en-US')  # Specify the language
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

corrected_text = correct_grammar_and_spelling()
print(corrected_text)
