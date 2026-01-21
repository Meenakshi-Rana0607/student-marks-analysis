import numpy as np

data = np.genfromtxt(
    "data/student_marks_analysis.csv",
    delimiter=",",
    skip_header=1
)


# Separate ID and marks
student_id = data[:, 0].astype(int)
marks = data[:, 1:]

# Ignore NaN values
average_marks = np.nanmean(marks, axis=1)
highest_marks = np.nanmax(marks, axis=1)
lowest_marks = np.nanmin(marks, axis=1) 
def get_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"
subjects_passed = np.sum(marks >= 80, axis=1)
subjects_failed = np.sum(marks < 80, axis=1)
overall_result = np.where(average_marks < 70, "FAIL", "PASS")


print("Student ID | Average Marks | Highest Marks  | Lowest Marks    | Passed in        | Failed in        | Grade | Result ")
print("-" * 125)

for sid, avg, high, low, p, f,res in zip(student_id, average_marks, highest_marks, lowest_marks, subjects_passed, subjects_failed, overall_result):
     grade = get_grade(avg)
     print(f"{sid:^10} | {avg:^13.2f} | {high:^14.2f} | {low:^15.2f} | {p:^16} | {f:^16} | {grade:^5} | {res:^6}")

print("\nClass Statistics:")
print("Class Average:", np.nanmean(average_marks))
print("Topper ID:", student_id[np.argmax(average_marks)])

total_pass = np.sum(overall_result == "PASS")
total_fail = np.sum(overall_result == "FAIL")

print("\nOverall Class Result:")
print("Total Students:", len(student_id))
print("Passed Students:", total_pass)
print("Failed Students:", total_fail)


subject_names = ["Maths", "Science", "English", "Computer", "History"]

print("\nSubject-wise Result")
print("-" * 35)

for i, subject in enumerate(subject_names):
    passed = np.sum(marks[:, i] >= 80)
    failed = np.sum(marks[:, i] < 80)
    print(f"{subject:^10} | Pass: {passed:^3} | Fail: {failed:^3}")

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure()
sns.countplot(x=overall_result)
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.title("Pass vs Fail Students")
plt.show()

# Define bins (ranges)
bins = [50, 60, 70, 80, 90, 100]

plt.figure()
sns.histplot(
    average_marks,
    bins=bins
)

# Proper x-axis labels
plt.xticks(bins)

plt.xlabel("Average Marks Range")
plt.ylabel("Number of Students")
plt.title("Average Marks Distribution (Range-wise)")
plt.show()

plt.figure()
sns.lineplot(x=student_id, y=highest_marks, label="Highest Marks")
sns.lineplot(x=student_id, y=lowest_marks, label="Lowest Marks")
plt.xlabel("Student ID")
plt.ylabel("Marks")
plt.title("Highest vs Lowest Marks")
plt.legend()
plt.show()


plt.figure()
sns.barplot(x=student_id, y=subjects_passed)
plt.xlabel("Student ID")
plt.ylabel("Subjects Passed")
plt.title("Subjects Passed per Student")
plt.show()

plt.figure()
sns.barplot(x=student_id, y=subjects_failed)
plt.xlabel("Student ID")
plt.ylabel("Subjects Failed")
plt.title("Subjects Failed per Student")
plt.show()

# Remove fully NaN columns
marks = marks[:, ~np.all(np.isnan(marks), axis=0)]

subject_pass_counts = [np.sum(marks[:, i] >= 80) for i in range(len(subject_names))]

plt.figure()
sns.barplot(x=subject_names, y=subject_pass_counts )
plt.xlabel("Subjects")
plt.ylabel("Students Passed")
plt.title("Subject-wise Pass Count")
plt.show()

subject_fail_counts = [np.sum(marks[:, i] < 80) for i in range(len(subject_names))]

plt.figure()
sns.barplot(x=subject_names, y=subject_fail_counts)
plt.xlabel("Subjects")
plt.ylabel("Students Failed")
plt.title("Subject-wise Fail Count")
plt.show()

grades = [get_grade(avg) for avg in average_marks]
unique_grades, grade_counts = np.unique(grades, return_counts=True)

plt.figure()
sns.barplot(x=unique_grades, y=grade_counts)
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.title("Grade Distribution")
plt.show()

plt.figure()
sns.heatmap(marks, annot=False)
plt.xlabel("Subjects")
plt.ylabel("Students")
plt.title("Marks Heatmap")
plt.show()


