import streamlit as st
import pandas as pd
from datetime import datetime, date
from tasks import (
    load_tasks, save_tasks, filter_tasks_by_priority, filter_tasks_by_category,
    filter_tasks_by_due_range, set_task_priority, set_task_category
)

def main():
    st.title("To-Do Application")

    tasks = load_tasks()

    if "filter_category" not in st.session_state:
        st.session_state["filter_category"] = "All"
    if "filter_priority" not in st.session_state:
        st.session_state["filter_priority"] = "All"
    if "show_filter" not in st.session_state:
        st.session_state["show_filter"] = "All"

    # Sidebar for adding new tasks
    st.sidebar.header("Add New Task")
    with st.sidebar.form("new_task_form"):
        task_title = st.text_input("Task Title")
        task_description = st.text_area("Description")
        task_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        task_category = st.selectbox("Category", ["Work", "Personal", "School", "Other"])
        task_due_date = st.date_input("Due Date")
        submit_button = st.form_submit_button("Add Task")

        if submit_button and task_title:
            new_task = {
                "id": max([t["id"] for t in tasks], default=0) + 1,
                "title": task_title,
                "description": task_description,
                "priority": task_priority,
                "category": task_category,
                "due_date": task_due_date.strftime("%Y-%m-%d"),
                "completed": False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            tasks.append(new_task)
            save_tasks(tasks)
            st.sidebar.success("Task added successfully!")
            st.rerun()

    st.header("Your Tasks")

    col1, col2 = st.columns(2)
    with col1:
        selected_category = st.selectbox(
            "Filter by Category",
            ["All", "Work", "Personal", "School", "Other"],
            index=["All", "Work", "Personal", "School", "Other"].index(st.session_state["filter_category"]),
            key="filter_category"
        )
    with col2:
        selected_priority = st.selectbox(
            "Filter by Priority",
            ["All", "High", "Medium", "Low"],
            index=["All", "High", "Medium", "Low"].index(st.session_state["filter_priority"]),
            key="filter_priority"
        )

    show_filter = st.selectbox(
        "Show Tasks",
        ["All", "Incomplete", "Completed"],
        index=["All", "Incomplete", "Completed"].index(st.session_state["show_filter"]),
        key="show_filter"
    )

    col3, col4 = st.columns(2)
    with col3:
        start_date = st.date_input("Start Due Date", value=date.today(), key="start_date")
    with col4:
        end_date = st.date_input("End Due Date", value=date.today(), key="end_date")

    # Apply all filters
    filtered_tasks = tasks.copy()
    if selected_category != "All":
        filtered_tasks = filter_tasks_by_category(filtered_tasks, selected_category)
    if selected_priority != "All":
        filtered_tasks = filter_tasks_by_priority(filtered_tasks, selected_priority)
    if show_filter == "Incomplete":
        filtered_tasks = [task for task in filtered_tasks if not task["completed"]]
    elif show_filter == "Completed":
        filtered_tasks = [task for task in filtered_tasks if task["completed"]]
    filtered_tasks = filter_tasks_by_due_range(
        filtered_tasks,
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d")
    )

    # Display each task
    for task in filtered_tasks:
        col_main, col_controls = st.columns([4, 2])
        with col_main:
            if task["completed"]:
                st.markdown(f"~~**{task['title']}**~~")
            else:
                st.markdown(f"**{task['title']}**")
            st.write(task["description"])
            st.caption(f"Due: {task['due_date']} | Created: {task['created_at']}")
        with col_controls:
            if st.button("Complete" if not task["completed"] else "Undo", key=f"complete_{task['id']}"):
                for t in tasks:
                    if t["id"] == task["id"]:
                        t["completed"] = not t["completed"]
                        save_tasks(tasks)
                        st.rerun()
            if st.button("Delete", key=f"delete_{task['id']}"):
                tasks = [t for t in tasks if t["id"] != task["id"]]
                save_tasks(tasks)
                st.rerun()

            new_priority = st.selectbox(
                "Set Priority",
                ["Low", "Medium", "High"],
                index=["Low", "Medium", "High"].index(task.get("priority", "Low")),
                key=f"priority_{task['id']}"
            )
            if new_priority != task.get("priority"):
                set_task_priority(tasks, task["id"], new_priority)
                save_tasks(tasks)
                st.rerun()

            new_category = st.selectbox(
                "Set Category",
                ["Work", "Personal", "School", "Other"],
                index=["Work", "Personal", "School", "Other"].index(task.get("category", "Work")),
                key=f"category_{task['id']}"
            )
            if new_category != task.get("category"):
                set_task_category(tasks, task["id"], new_category)
                save_tasks(tasks)
                st.rerun()

if __name__ == "__main__":
    main()
