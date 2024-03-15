import simple_latex_gen as slg

def latex_wrapper(tables, pictures):
    latex_code = "\\documentclass{article}\n"
    latex_code += "\\usepackage{graphicx}\n"
    latex_code += "\\begin{document}\n"

    for table in tables:
        latex_code += slg.generate_latex_table(table)

    for image in pictures:
        latex_code += slg.generate_latex_image(image, False) 

    
    latex_code += "\\end{document}\n"

    file = open('test.tex', 'w')
    file.write(latex_code)
    file.close()

    print("Result written to test.tex")

    return latex_code

pics = ["resources/test1.png", "resources/test2.png"]
tabs = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [["This", "table", "is", "pretty"], ["nice", "but", "it", "is"], ["not", "square", "PS", ":("]]]

latex_wrapper(tabs, pics)