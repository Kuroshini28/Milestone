import pandas as pd
import random
num_students = 980
num_sessions = 40
data = []
for i in range(1, num_students + 1):
    student_id = f"STU{i:04d}"
    present_count = 0
    session_durations = []
    for j in range(num_sessions):
        duration = random.randint(0, 120)
        session_durations.append(duration)
        if duration >= 90:
            present_count += 1
    attendance_percentage = (present_count / num_sessions) * 100
    if attendance_percentage >= 80:
        certificate_status = "Eligible"
    else:
        certificate_status = "Not Eligible"
    row = {
        "Student_ID": student_id
    }
    for k in range(num_sessions):
        row[f"Session_{k+1}_Duration"] = session_durations[k]
    row["Present_Count"] = present_count
    row["Attendance_Percentage"] = round(attendance_percentage, 2)
    row["Certificate_Status"] = certificate_status
    data.append(row)
df = pd.DataFrame(data)
df.to_excel("attendance_report.xlsx", index=False)
print("Attendance report generated successfully!")
