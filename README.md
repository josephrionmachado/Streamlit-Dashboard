# 📊 Streamlit CSV Dashboard

A simple interactive **CSV Dashboard** built using **Python, Pandas, Streamlit, and Matplotlib**.

This application allows users to upload a CSV file, view a data summary, filter the data, and create a bar chart by selecting columns.

## 🚀 Features

* 📂 Upload CSV files
* 📋 View statistical summary using `df.describe()`
* 🔍 Filter data using a selected column
* 🔽 Select a value to filter the dataset
* 📄 Display filtered data
* 📈 Select an X-axis column
* 📊 Select a numeric Y-axis column
* 📉 Generate a bar chart
* 🖥️ Interactive dashboard using Streamlit

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data loading and analysis
* **Streamlit** – Interactive web dashboard
* **Matplotlib** – Data visualization

## 📁 Project Structure

```text
Streamlit-Dashboard/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/josephrionmachado/Streamlit-Dashboard.git
```

### 2. Open the project folder

```bash
cd Streamlit-Dashboard
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

## ▶️ Run the Dashboard

Start the Streamlit application using:

```bash
streamlit run app.py
```

The dashboard will open in your web browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

## 📂 How to Use

### Step 1 — Upload a CSV file

Click:

**📂 Select CSV File**

and upload your CSV file.

### Step 2 — View Data Summary

The dashboard displays statistical information about the dataset using:

```python
df.describe()
```

### Step 3 — Filter the Data

From the sidebar:

1. Choose a column for filtering.
2. Select a value from that column.
3. The dashboard displays the filtered data.

### Step 4 — Create a Chart

From the sidebar:

1. Select a column for the **X-axis**.
2. Select a numeric column for the **Y-axis**.
3. Click **📊 Show Plot**.

The dashboard will generate a bar chart.

## 📊 Example

For a CSV file such as:

| Department | Employee | Salary |
| ---------- | -------- | -----: |
| IT         | John     |  50000 |
| HR         | Sarah    |  45000 |
| IT         | David    |  60000 |
| Sales      | Alex     |  40000 |

You can select:

```text
X-axis → Department
Y-axis → Salary
```

and generate a bar chart.

## ⚠️ Notes

* The uploaded file must be in **CSV format**.
* The Y-axis column must contain numeric data.
* The current version allows selecting **one filter value at a time**.
* The application does not store uploaded CSV files permanently.

## 🎯 Future Improvements

Possible improvements for future versions:

* Add multiple-value filtering
* Add line charts and pie charts
* Add interactive Plotly charts
* Add downloadable filtered data
* Add column-based sorting
* Add dashboard metrics such as total, average, minimum, and maximum
* Add multiple chart types
* Improve the dashboard UI

## 👨‍💻 Author

**Joseph Rion Machado**

GitHub:
https://github.com/josephrionmachado

---

⭐ If you find this project useful, consider giving it a star!
