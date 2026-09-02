/**
 * Programmer: Julie Tong
 * Filename: Shift.ts
 * Description: Defines the TypeScript data structure for hospital work shifts.
 */

export type Shift = {
    id: number;
    department: string;
    day: string;
    shiftType: number;
    nursesNeded: number;
};