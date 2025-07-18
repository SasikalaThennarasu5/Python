from gradesystem.report import generate_report

def test_generate_report():
    marks = [80, 90, 70]
    result = generate_report("Anil", marks)
    assert result["name"] == "Anil"
    assert result["CGPA"] == 8.0
    assert result["Grade"] == "A+"
