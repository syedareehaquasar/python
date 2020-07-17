def latex_processor(equation: str) -> str:
    modified_equation = equation.replace(" ","").replace("-","$-").replace("+","$+") #operator replaced by $operator
    terms = modified_equation.split("$")[::-1] #split by dolar and reversing it
    equation = "".join(terms)
    return "$" + equation + "$"

print(latex_processor("$-3x^4-4x^3+2x^{2}-17$"))