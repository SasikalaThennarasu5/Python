# Absolute import
from school.students.register import student_register

# Relative import
from ..students import register as student_reg_module

def register_both():
    print(student_register("Alice"))
    print(student_reg_module.student_register("Bob"))
