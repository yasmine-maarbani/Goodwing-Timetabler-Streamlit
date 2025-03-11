import streamlit as st
import pandas as pd
import sys
import os

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(project_root, "GoodwingTimetabler/"))

from GoodwingTimetabler.app.main import generateScheduleUsingCSP

st.title("📅 Goodwing Timetabler")

uploaded_file = st.file_uploader("📁 Upload your scheduling Excel file", type="xlsx")

if uploaded_file:
    input_path = os.path.join(project_root, "Inputs", "University.xlsx")

    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ File uploaded successfully!")

    if st.button("🚀 Generate Schedule"):
        # with st.spinner('🔄 Generating optimal schedule...'):
            # generateScheduleUsingCSP()

        st.success("✅ Schedule successfully generated!")

        output_path = os.path.join(project_root, 'Outputs/excel/schedule.xlsx')

        if os.path.exists(output_path):
            df = pd.read_excel(output_path, sheet_name=None)
            print("df", df)
            for sheet_name, data in df.items():
                st.subheader(f"📚 Schedule: {sheet_name}")
                st.dataframe(data)

            with open(output_path, "rb") as file:
                st.download_button(
                    label="📥 Download Schedule",
                    data=file,
                    file_name="schedule.xlsx",
                    mime="application/vnd.ms-excel"
                )
        else:
            st.error("⚠️ Output file was not generated. Check CSP logic.")
else:
    st.info("ℹ️ Please upload your Excel scheduling file to proceed.")
