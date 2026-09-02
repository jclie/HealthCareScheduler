/**
 * Programmer: Julie Tong
 * Filename: Schedule.ts
 * Description: Defines the TypeScript data structures for generated staff schedules and assignments.
 */

// creates a dataclass for all future scheduling
export type Schedule = {
    id: number;
    department: string;
    day: number;
    shiftType: string;
    nursesNeeded: number;
}