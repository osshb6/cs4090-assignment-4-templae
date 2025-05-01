import os

import streamlit as st
import subprocess

st.title("Pytest Test Runner Dashboard")

def run_pytest(command_args):
    result = subprocess.run(
        ["pytest"] + command_args,
        capture_output=True,
        text=True
    )
    return result.stdout + result.stderr

if st.button("Run Basic Tests"):
    st.code(run_pytest(["tests/test_basic.py"]))

if st.button("Run All with Coverage Report"):
    st.code(run_pytest(["--cov=src.tasks", "--cov-report=term-missing", "tests/"]))

if st.button("Run Parametrized Tests Only"):
    st.code(run_pytest(["-k", "parametrize", "tests/"]))

if st.button("Run Mocking Tests Only"):
    st.code(run_pytest(["tests/test_advanced.py"]))

if st.button("Run BDD Tests Only"):
    st.code(run_pytest(["tests/feature/steps/"]))

if st.button("Generate and View HTML Coverage Report of All"):
    output = run_pytest(["--cov=src.tasks", "--cov-report=html", "tests/"])
    st.success("Coverage report generated!")

    # Read the HTML coverage report
    html_file_path = os.path.join("htmlcov", "index.html")
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=600, scrolling=True)
    else:
        st.error("Could not find the coverage HTML report.")
