"""
Programmer: Julie Tong
Filename: models.py
Description: 
"""
from dataclasses import dataclass

@dataclass
class Nurse:
    id: int
    name: str
    departments: set[str]
    maxShifts: int
    
@dataclass
class Department:
    id: int
    name: str
    
@dataclass
class Shift:
    id: int
    department: str
    day: str
    shiftType: int
    nursesNeeded: int
    
