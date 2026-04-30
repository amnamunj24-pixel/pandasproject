import pandas as pd
class Student:
    def __init__(self, name, math_score, science_score):
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
        self.status = None # will set this later

    def check_status(self):
        # calc average, treat missing as 0 already handled by pandas
        avg = (self.math_score + self.science_score) / 2
        if avg >= 50:
            self.status = "Pass"
        else:
            self.status = "Fail"
        return self

# load and clean the data
df = pd.read_csv("raw_grades.csv")
df = df.fillna(0) # replace blanks with 0

students_data = []

for _, row in df.iterrows():
    s = Student(row['Student_Name'], row['Math_Score'], row['Science_Score'])
    s.check_status()
    students_data.append({
        'Student_Name': s.name,
        'Math_Score': s.math_score,
        'Science_Score': s.science_score,
        'Status': s.status
    })

# build final df from scratch like the spec said
final_df = pd.DataFrame(students_data)
final_df['School_Year'] = "2023-2024"
final_df.to_csv("final_grades.csv", index=False)
print("Done! Check final_grades.csv")