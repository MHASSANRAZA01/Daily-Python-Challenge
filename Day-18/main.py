import streamlit as st
import os

tasks_file = "tasks.txt"

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as file:
            return [task.strip() for task in file.readlines()]
    return []

def save_tasks(tasks):
    with open(tasks_file, "w") as file:
        file.writelines([task + "\n" for task in tasks])

def main():
    st.title("✅ To-Do List App")
    st.write("Manage your daily tasks efficiently!")
    
    tasks = load_tasks()
    new_task = st.text_input("Add a new task:")
    
    if st.button("Add Task"):
        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
            st.rerun()
        else:
            st.warning("Please enter a task.")
    
    st.subheader("Your Tasks")
    
    for i, task in enumerate(tasks):
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.text(task)
        with col2:
            if st.button("❌", key=f"task_{i}"):
                tasks.pop(i)
                save_tasks(tasks)
                st.rerun()

if __name__ == "__main__":
    main()
