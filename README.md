Student Attendance Management System

Description

The Student Attendance Management System is a Python-based project designed to manage and analyze attendance records for students attending online sessions. The system processes attendance data for 980+ students across 40 online sessions, where each session lasts 120 minutes. A student is marked present if their attendance duration is at least 90 minutes; otherwise, they are marked absent.

The application calculates each student's attendance percentage and determines certificate eligibility based on the requirement of maintaining at least 80% attendance. The generated attendance report is automatically exported to an Excel file with color formatting, where eligible students are highlighted in green and non-eligible students are highlighted in red.

This project uses the Pandas and OpenPyXL libraries for data processing and Excel file generation. It provides an efficient and automated solution for attendance tracking and certificate eligibility management.

Features

- Manages attendance records for 980+ students.
- Processes 40 online sessions of 120 minutes each.
- Marks students as Present (≥ 90 minutes) or Absent (< 90 minutes).
- Calculates attendance percentage automatically.
- Determines certificate eligibility based on 80% attendance.
- Generates an Excel report ("attendance_report.xlsx").
- Highlights eligible students in green and non-eligible students in red.
- Simple and user-friendly Python implementation.

Technologies Used

- Python
- Pandas
- OpenPyXL
- Visual Studio Code

Output

The system generates an Excel report containing:

- Student ID
- Session-wise attendance duration
- Present count
- Attendance percentage
- Certificate eligibility status
