"""
Programmer: Julie Tong
Filename: ConstraintTest.py
Description: Tests the scheduling constraints used to determine whether nurses are eligible for specific hospital shifts
"""
from app.models import Nurse, Shift, Department
from app.constraints import isAvailable, validShiftAssignment, canWorkDepartment

# --------------------------------------------------
# Test Nurse
# --------------------------------------------------
# Alice is available Monday during the Day shift and Tuesday during the Night shift
Alice = Nurse(
    id = 1,
    name = "Alice",
    departments = "ICU",
    maxShifts = 5,
    availability = {
        ("Monday", 0),
        ("Tuesday", 1),
        ("Wednesday", 1),
        ("Thursday", 0)
    }
)

# --------------------------------------------------
# Test Shifts
# --------------------------------------------------
MondayDayShift = Shift(
    id = 1,
    department = "General Medicine",
    day = "Monday",
    shiftType = 0,
    nursesNeeded = 1
)

MondayNightShift = Shift(
    id = 2,
    department = "ICU",
    day = "Monday",
    shiftType = 1,
    nursesNeeded = 0
)

# --------------------------------------------------
# Test Department
# --------------------------------------------------
ICU = Department(
    id = 0,
    name = "ICU"
)

GeneralMedicine = Department(
    id = 1,
    name = "General Medicine"
)

# --------------------------------------------------
# Availability Constraint Tests
# --------------------------------------------------
assert isAvailable(Alice, MondayDayShift) == True
assert isAvailable(Alice, MondayNightShift) == False

assert validShiftAssignment(Alice, MondayDayShift) == True

assert canWorkDepartment(Alice, ICU) == True
assert canWorkDepartment(Alice, GeneralMedicine) == False

print("\nAll tests passed!")