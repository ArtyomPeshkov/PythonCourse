def generate_latex_table(data):    
    table_rows = [" & ".join(map(str, row)) + " \\\\" for row in data]
    table_body = "\n".join(table_rows)
    
    latex_code = "\\begin{tabular}{|" + "c|" * len(data[0]) + "}\n"
    latex_code += "\\hline\n"
    latex_code += table_body + "\n"
    latex_code += "\\hline\n"
    latex_code += "\\end{tabular}\n"
    
    return latex_code

def generate_latex_image(path, full_file):
    latex_code = ""
    if full_file:
        latex_code += "\\documentclass{article}\n"
        latex_code += "\\usepackage{graphicx}\n"
        latex_code =+ "\\begin{document}\n"
    
    latex_code += "\\begin{figure}[h]\n"
    latex_code += "    \\centering\n"
    latex_code += "    \\includegraphics{" + path + "}\n"
    latex_code += "\\end{figure}\n"
    
    if full_file:
        latex_code += "\\end{document}\n"

    return latex_code
