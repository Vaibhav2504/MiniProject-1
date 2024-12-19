import streamlit as st

if "expenses" not in st.session_state:
    st.session_state.expenses = {
        "Food": 0.0,
        "Transport": 0.0,
        "Entertainment": 0.0,
        "Others": 0.0
    }

def add_expense(category, amount):
    if category in st.session_state.expenses:
        st.session_state.expenses[category] += amount
    else:
        st.warning(f"Category '{category}' not found. Adding it to 'Others'.")
        st.session_state.expenses["Others"] += amount

def show_summary():
    total_expenses = sum(st.session_state.expenses.values())
    if total_expenses == 0:
        st.info("No expenses recorded yet.")
        return

    st.subheader("Expense Summary")
    for category, amount in st.session_state.expenses.items():
        percentage = (amount / total_expenses) * 100
        st.write(f"- **{category}**: ₹{amount:.2f} ({percentage:.2f}%)")

    st.write(f"**Total Expenses**: ₹{total_expenses:.2f}")

st.title("Dynamic Expense Tracker")

st.sidebar.header("Add an Expense")
category = st.sidebar.selectbox("Select Category", options=list(st.session_state.expenses.keys()) + ["Add New Category"])
if category == "Add New Category":
    new_category = st.sidebar.text_input("Enter new category name").strip()
    if new_category and new_category not in st.session_state.expenses:
        st.session_state.expenses[new_category] = 0.0
        st.success(f"Added new category: {new_category}")
        category = new_category

amount = st.sidebar.number_input("Enter Expense Amount", min_value=0.0, step=0.01)

if st.sidebar.button("Add Expense"):
    if amount > 0:
        add_expense(category, amount)
        st.sidebar.success(f"Added ₹{amount:.2f} to {category}")
    else:
        st.sidebar.warning("Please enter a positive amount.")

# Main page displays summary
if st.button("Show Summary"):
    show_summary()

# Footer
st.write("---")
st.caption("Developed with ❤️ using Streamlit.")