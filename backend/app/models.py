"""
Programmer: Julie Tong
Filename: models.py
Description: Defines the core data structures used by the hospital scheduling system, including nurses, departments, and shifts.
"""
from dataclasses import dataclass

"Represents a nurse who can be assigned to hospital shifts"
@dataclass
class Nurse:
    id: int
    name: str
    departments: set[str]
    maxShifts: int
    availability: set[tuple[str, str]]

"Represents a hospital department"  
@dataclass
class Department:
    id: int
    name: str

"Represents a hospital shift that must be staffed"
@dataclass
class Shift:
    id: int
    department: str
    day: str
    shiftType: int
    nursesNeeded: int
    
