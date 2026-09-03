"""
Programmer: Julie Tong
Filename: ModelsTest.py
Description: testing that the models work
"""
from app.models import Nurse, Department, Shift

# sample nurses
nurses = [
    Nurse(
        1, "Alice", {"ICU", "Emergency"}, 5,
        {
            ("Monday", 0),
            ("Tuesday", 1),
            ("Wednesday", 1),
            ("Thursday", 0)
        }
    ),
    Nurse(2, "Bob", {"General Medicine"}, 4),
    Nurse(3, "Charlie", {"ICU"}, 5),
    Nurse(4, "Diana", {"Emergency"}, 4),
    Nurse(5, "Emma", {"ICU", "General Medicine"}, 5)
]

# sample departments
departments = [
    Department(1, "ICU"),
    Department(2, "Emergency"),
    Department(3, "General Medicine")
]

# sample shifts
shifts = [
    Shift(1, "ICU", "Monday", 1, 3),
    Shift(2, "Emergency", "Tuesday", 0, 2),
    Shift(3, "General Medicine", "Wednesday", 0, 1),
    Shift(4, "ICU", "Monday", 0, 3)
]

# print statements
print("\nNURSES")
for nurse in nurses:
    print(nurse.name)
    nResult = f"Departments: {nurse.departments}"
    print(nResult)
    nResult1 = f"Shifts: {nurse.maxShifts}"
    print(nResult1)
    
print("\nDEPARTMENTS")
for department in departments:
    print(department)
    
print("\nSHIFTS")
for shift in shifts:
    print(shift)
    
# tests
assert len(nurses) == 5
assert len(departments) == 3
assert len(shifts) == 4

assert nurses[0].name == "Alice"
assert nurses[0].maxShifts == 5
assert "ICU" in nurses[0].departments

print("\nAll tests passed!")