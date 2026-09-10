"""
Programmer: Julie Tong
Filename: constraints.py
Description: Defines the scheduling rules used to determine whether nurses can be assigned to hospital shifts
"""

"Checks if a nurse is available for a specific shift"
"A nurse is considered available when the shift's day and shift type appear together in the nurse's availability set"
def isAvailable(nurse, shift):
    return (shift.day, shift.shiftType) in nurse.availability

"Determines if a nurse can be assigned to shift"
def validShiftAssignment(nurse, shift):
    if not isAvailable(nurse, shift):
        return False
    return True

"Checks if a nurse can work in a specific department"
def canWorkDepartment(nurse, department):
    return (department.name) in nurse.departments