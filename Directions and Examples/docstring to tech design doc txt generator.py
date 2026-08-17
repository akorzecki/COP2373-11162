import inspect
import docstring_example # replace with your assignment name (without .py)
#replace docstring_example with your assignment name in the next 2 lines of code
with open("docstring_example_design_doc.txt", "w") as doc:
    doc.write(f"# Technical Design Document: {docstring_example.__name__}\n\n")
    #replace with your name, the date, and the description of the program
    doc.write(f"# Name: Susan Melichar\n")
    doc.write(f"# Date: November 12, 2025\n")
    doc.write(f"# Program Description: Give brief description of your program\n\n")
    #replace docstring_example with your assignment name
    for name, func in inspect.getmembers(docstring_example, inspect.isfunction):
        doc.write(f"## Function: {name}\n")
        doc.write(f"{inspect.getdoc(func)}\n\n")
    #replace with link to your repository
    doc.write(f"#Link to your repository: https://github.com/melichs?tab=repositories")
print('Complete')