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
    availability: set[tuple[str, str]]
    
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
    
