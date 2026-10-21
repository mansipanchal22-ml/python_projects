# PROJECT = "SMART Expense Tracker Application"
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

valid_Categories = ["Food", "Transport", "Utilities", "Entertainment", "Other"]


class Expensetracker:
#1=expense input and validation
    
    def __init__(self):
         def __init__(self, filename="expenses.csv"):
            self.filename = filename
            self.load_data()
        
            def load_data(self):
            
        
             if os.path.exists(self.filename):
              
              try:
                self.df = pd.read_csv(self.filename)
                self.df["Date"] = pd.to_datetime(self.df["Date"])
                self.df["Amount"] = pd.to_numeric(self.df["Amount"], errors="coerce")
                self.df.dropna(inplace=True)
              except Exception:
                self._create_empty_df()
                
             else:
                    self._create_empty_df()

            def create_empty_df(self):
                self.df = pd.DataFrame(
                    columns=["Date", "Amount", "Category", "Description"]
                )


            def save_data(self):
           
                self.df.to_csv(self.filename, index=False)

            def add_expense(self, date, amount, category, description):
                """Add a new expense record after input validation."""
                
                new_entry = pd.DataFrame([{
                   
                    "Date": pd.to_datetime(date),
                    "Amount": float(amount),
                    "Category": category,
                    "Description": description,
                }])

                self.df = pd.concat([self.df, new_entry], ignore_index=True)
                self.save_data()
                print("Expense added successfully!")

            #Get_summary:

            def get_summary(self):
                
                if self.df.empty:

                    print("No expenses recorded yet.")
                return 

            amount = np.array(self.df['amount'])
            total_spent = np.sum[amount]
            avg_spent = np.mean[amount]

            
            print("==Expense Summary==")
            print("Total Expense : {total_spent:}")
            print("avg Expense : {avg_spent:}")

            print("==Category_wise Total:")

            cat_summary = self.df.groupby("category")["Amount"].sum()
            for cat, total in cat_summary.items():
                pct = (total / total_spent) * 100
                print("{cat}: Rs.{total:.2f} ({pct:.1f}%)")

            #Filter_expense

            def filter_expenses(self, condition_type, value):
                if self.df.empty:
                    print("Dataset is empty.")
                    return

                if condition_type == "category":
                    result = self.df[self.df["Category"].str.lower() == value.lower()]
                elif condition_type == "min_amount":
                     result = self.df[self.df["Amount"] >= float(value)]

                else:
                    print("--invalid filter type--")

            #Genrate_report

            def genrate_report(self):

                if self.df.empty:
                    print("no data avilable genrate report.")
                    return

                print("==key metrics report==")
                print("Total Transactions: {len(self.df)}")
                print("Highest Single Expense: Rs. {self.df['Amount'].max():.2f}")
                print("Lowest Single Expense: Rs. {self.df['Amount'].min():.2f}")


                top_cat = self.df.groupby("Category")["Amount"].sum().idxmax()
                print(f"Top Spending Category: {top_cat}")

            def visualize(self):



                #1(Bar Chart:) seaborn
                plt.subplot(2, 2, 1)
                cat_totals = df.groupby('Category')['Amount'].sum()
                cat_totals.plot(kind='bar', color='pink')
                plt.title('Total Expenses by Category')
                plt.xlabel('Category')
                plt.ylabel('Amount')

                #2(Line Graph) seaborn
                plt.subplot(2, 2, 2)
                time_trend = df.groupby('Date')['Amount'].sum()
                plt.plot(time_trend.index, time_trend.values, marker='o', color='green')
                plt.title('Spending Trends Over Time')
                plt.xlabel('Date')
                plt.ylabel('Amount')
                plt.xticks(rotation=45)

                #3(pie Chart) seaborn
                plt.subplot(2, 2, 3)
                plt.pie(cat_totals, labels=cat_totals.index, autopct='%1.1f%%')
                plt.title('Expense Distribution')

                #4(Histrogram):
                plt.subplot(2, 2, 4)
                sns.histplot(df['Amount'], bins=5, color='blue')
                plt.title('Expense Amount Frequency')
                plt.xlabel('Amount')
                plt.ylabel('Frequency')

                plt.tight_layout()
                plt.show()


            #MENU INTERFACE

            def main():

                tracker = Expensetracker()

                while True:
                    print("---smart Expense Tracker---")
                    print("1. Add New Expense")
                    print("2. View Expense Summary")
                    print("3. Filter Expenses")
                    print("4. Generate Key Metrics Report")
                    print("5. Visualize Data (Charts)")
                    print("6. Exit")

                    choice = input("Enter choice (1-6)").strip()

                    if choice == "1":
                
                       date = input("Enter Date (YYYY-MM-DD): ").strip()

                    while True:
                        try:
                            amount = float(input("Enter Amount: "))
                            if amount <= 0:
                                print("Amount must be positive.")
                                continue
                            break
                        except ValueError:
                            print("Invalid amount. Enter a valid number.")

                        print("Allowed categories: {', '.join(VALID_CATEGORIES)}")
                        category = input("Enter Category: ").strip()
                        while category not in valid_Categories:
                            print(f"Invalid category! Choose from: {', '.join(valid_Categories)}")
                            category = input("Enter Category: ").strip().capitalize()

                        description = input("Enter Description: ").strip()
                        tracker.add_expense(date, amount, category, description)


                    elif choice == "2": tracker.get_summary()

                    elif choice == "3":
                    print("Filter by: 1. Category  2. Minimum Amount")
                    f_choice = input("Choose (1/2): ").strip()

                    if f_choice == "1":
                         val = input("Enter Category: ").strip()
                         tracker.filter_expenses("category", val)
                    elif f_choice == "2":
                            val = input("Enter Minimum Amount: ").strip()
                            tracker.filter_expenses("min_amount", val)
                    else:
                            print("Invalid choice.")

                    elif choice == "4":
                    tracker.generate_report()

                    elif choice == "5":
                    tracker.visualize()

                    elif choice == "6":
                    print("Exiting tracker. Goodbye!")
                    break

                else:
                    print("Invalid option. Please choose between 1 and 6")
        