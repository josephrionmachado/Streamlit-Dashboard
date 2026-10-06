import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 DashBoard")

fileuploader = st.file_uploader("📂 Select CSV File", type="csv")

if fileuploader is not None:
    df = pd.read_csv(fileuploader)

    st.subheader("📋 Data Summary")
    st.write(df.describe())

    st.sidebar.header("🔍 Filter Data")

    columns = df.columns.tolist()

    selected_col = st.sidebar.selectbox("📌 Choose Column For Filter", columns)

    filtered_values = df[selected_col].unique()

    selected_values = st.sidebar.selectbox("🔽 Select Values", filtered_values)

    data_filtered = df[df[selected_col] == selected_values]

    st.write(data_filtered)

    st.subheader("📄 Data")

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    x_col = st.sidebar.selectbox("📈 Select Column For X-axis", columns)

    y_col = st.sidebar.selectbox("📊 Select Column For Y-axis", numeric_columns)

    if st.sidebar.button("📊 Show Plot"):

        data = data_filtered.set_index(x_col)[y_col]

        fig, ax = plt.subplots()

        ax.bar(data.index, data.values)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f"{y_col} vs {x_col}")

        st.pyplot(fig)
else:
    st.write("⚠️ File Not selected")