from gradesystem.grade import get_grade_from_cgpa

def test_grade_scale():
    assert get_grade_from_cgpa(9.2) == "O"
    assert get_grade_from_cgpa(8.3) == "A+"
    assert get_grade_from_cgpa(7.5) == "A"
    assert get_grade_from_cgpa(6.2) == "B+"
    assert get_grade_from_cgpa(5.1) == "B"
    assert get_grade_from_cgpa(4.0) == "C"
    assert get_grade_from_cgpa(3.9) == "F"
