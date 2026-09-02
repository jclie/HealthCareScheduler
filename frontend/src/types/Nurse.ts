/**
 * Programmer: Julie Tong
 * Filename: Nurse.ts
 * Description: Defines the TypeScript data structure for hospital nurses.
 */

// creates a nurse dataclass for all future nurses
export type Nurse = {
    id: number;
    name: string;
    department: string;
    maxShifts: number;
};