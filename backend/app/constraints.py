"""
Programmer: Julie Tong
Filename: constraints.py
Description: 
"""

def isAvailable(nurse, shift):
    return (shift.day, shift.shiftType) in nurse.availability
