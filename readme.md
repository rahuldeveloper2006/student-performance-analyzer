# 🎓 Student Performance Analyzer

A Python-based student performance dashboard built using **Pandas, NumPy, and Streamlit**.

## 🚀 Features
- Upload CSV files containing multiple student records.
- Automatically calculate total marks, average, percentage, and grades.
- Determine PASS/FAIL based on subject marks.
- Display Top 3 students by percentage.
- Search students by ID or name.
- Analyze class averages and attendance.
- Visualize subject performance and attendance trends.
- Download analyzed results as CSV.

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Streamlit

## 📊 Result Rules
- Maximum marks: 500.
- Minimum marks to pass: 35 in every subject.
- Attendance does not affect PASS/FAIL.
- Grades range from A+ to F.
- Top 3 ranking is based on percentage, with total marks as the tie-breaker.

## ⚙️ Run Locally

```bash
git clone YOUR_REPOSITORY_URL
cd student-performance-analyzer
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure

```text
student-performance-analyzer/
├── app.py
├── students_100.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔮 Future Improvements
- Add, edit, and delete student records.
- Integrate a SQL database.
- Generate PDF report cards.
- Add advanced analytics and machine learning.

## 👨‍💻 Author
**Rahul Bhuyan**  
Aspiring Data Scientist & AI Engineer.