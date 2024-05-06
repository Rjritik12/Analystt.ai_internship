from flask import Flask, render_template, request
from datetime import datetime, date
from Expense_Tracker import Expense, ExpenseTracker

app = Flask(__name__)

tracker = ExpenseTracker()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_expense", methods=["POST"])
def add_expense():
    amount = float(request.form["amount"])
    category = request.form["category"]
    date_str = request.form["date"]
    date = date.today() if date_str == "" else datetime.strptime(date_str, "%Y-%m-%d").date()
    tracker.add_expense(Expense(amount, category, date))
    return "Expense added successfully!"

@app.route("/view_expenses")
def view_expenses():
    expenses = tracker.expenses
    return render_template("view_expenses.html", expenses=expenses)

@app.route("/view_spending_by_category")
def view_spending_by_category():
    spending_by_category = tracker.get_spending_by_category()
    return render_template("view_spending_by_category.html", spending_by_category=spending_by_category)

@app.route("/view_total_spending")
def view_total_spending():
    total_spending = tracker.get_total_spending()
    return render_template("view_total_spending.html", total_spending=total_spending)

@app.route("/view_average_spending")
def view_average_spending():
    average_spending = tracker.get_average_spending()
    return render_template("view_average_spending.html", average_spending=average_spending)

@app.route("/view_spending_by_date")
def view_spending_by_date():
    spending_by_date = tracker.get_spending_by_date()
    return render_template("view_spending_by_date.html", spending_by_date=spending_by_date)

@app.route("/view_expenses_by_category")
def view_expenses_by_category():
    category = request.args.get("category")
    expenses = tracker.get_expenses_by_category(category)
    return render_template("view_expenses_by_category.html", expenses=expenses)

@app.route("/view_expenses_by_date_range")
def view_expenses_by_date_range():
    start_date_str = request.args.get("start_date")
    end_date_str = request.args.get("end_date")
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    expenses = tracker.get_expenses_by_date_range(start_date, end_date)
    return render_template("view_expenses_by_date_range.html", expenses=expenses)

if __name__ == "__main__":
    app.run(debug=True)