import pywhatkit as pw

txt = """Python is an interpreted high-level general-purpose programming. It design philosophy emphasizes code readability with its use of significant to the python"""

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print(" END ")