import lmstudio as lms
import pyperclip

model = lms.llm()
result = model.respond(input())
pyperclip.copy(result)

