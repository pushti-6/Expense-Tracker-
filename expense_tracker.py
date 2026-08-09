import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
import database as db
import tkinter as tk
from tkcalendar import Calendar

class ExpenseTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Default Theme
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        # Window
        self.geometry("1000x600")
        self.resizable(True, True)

        # Grid Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(self, width=300, corner_radius=15)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
       #############################################



        self.title_label=ctk.CTkLabel(self.sidebar_frame,text="Expense Tracker",font=ctk.CTkFont(family = "Times New Roman",size=22,weight="bold"))
        self.title_label.grid(row=0,column=0,padx=20,pady=(20,20))

        ##separator##
        self.separator=ctk.CTkFrame(self.sidebar_frame,height=2,fg_color="grey")
        self.separator.grid(row=1,column=0,sticky="ew",padx=20,pady=(0,20)) #sticky ew means east west, it will stretch the frame in horizontal direction

        self.input_title=ctk.CTkLabel(self.sidebar_frame,text="Add new Expense",font=ctk.CTkFont(family = "Times New Roman",size=16,weight="bold"))
        self.input_title.grid(row=2,column=0,padx=20,pady=(0,10),sticky="w") #sticky w means west, it will align the frame to the left
    
        self.desc_entry=ctk.CTkEntry(self.sidebar_frame,placeholder_text="Description",font=ctk.CTkFont(family = "times new roman",size = 15, weight = "bold"))
        self.desc_entry.grid(row=3,column=0,padx=20,pady=(0,10),sticky="ew") #sticky ew means east west, it will stretch the frame in horizontal direction

        self.amount_entry=ctk.CTkEntry(self.sidebar_frame,placeholder_text="Amount",font=ctk.CTkFont(family = "times new roman",size = 15, weight = "bold"))
        self.amount_entry.grid(row=4,column=0,padx=20,pady=(0,10),sticky="ew") #sticky ew means east west, it will stretch the frame in horizontal direction

        self.categories=["Food and Drinks","Books & Stationery","Clothing & Accessories","Electronics & Gadgets","Health & Fitness","Home & Living","Personal Care & Beauty","Sports & Outdoor Activities","Transportation & Travel","Other"]
        self.category_dropdown=ctk.CTkComboBox(self.sidebar_frame,values=self.categories,state="readonly")
        self.category_dropdown.grid(row=5,column=0,padx=20,pady=(0,10),sticky="ew") #sticky ew means east west, it will stretch the frame in horizontal direction
 
 
        self.button=ctk.CTkButton(self.sidebar_frame,text="Add new Expense",fg_color="#FF5768",font=ctk.CTkFont(family = "times new roman",size = 18,weight="bold"),command=self.add_on_expense)
        self.button.grid(row=6,column=0,padx=30,pady=(20,20),sticky="ew")

        #MAIN CONTENT AREA
        self.content_frame = ctk.CTkFrame(self,corner_radius = 15)
        self.content_frame.grid(row = 0,column =1,sticky ="nsew",padx=15,pady=15)

        self.summary_card = ctk.CTkFrame(self.content_frame, corner_radius=15)
        self.summary_card.grid(row = 0,column=0,pady=20,padx=20,sticky="ew")
   
        self.card_title = ctk.CTkLabel(self.summary_card, text="Total Expenses", font=ctk.CTkFont(family = "times new roman",weight = "bold",size = 25))
        self.card_title.pack(pady=(10, 0))
        
        self.total_spent_label = ctk.CTkLabel(self.summary_card, text="Rs.0.00", font=ctk.CTkFont(family = "times new roman",size=35, weight="bold"), text_color="#2e7d32")
        self.total_spent_label.pack(pady=(0, 10))
# Budget Card
        self.budget_title = ctk.CTkLabel(self.sidebar_frame, text="Monthly Budget", font = ctk.CTkFont(family="Times New Roman", size=16, weight="bold"))
        self.budget_title.grid(row=7, column=0, padx=20, pady=(20,5), sticky="w")

        self.budget_entry = ctk.CTkEntry(self.sidebar_frame,placeholder_text="Enter Budget")
        self.budget_entry.grid(row=8, column=0, padx=20, pady=5, sticky="ew")
        self.savings_title = ctk.CTkLabel( self.sidebar_frame,text="Savings Goal",font=ctk.CTkFont(family="Times New Roman", size=16, weight="bold"))
        self.savings_title.grid(row=10, column=0, padx=20, pady=(10,5), sticky="w")

        self.savings_entry = ctk.CTkEntry(self.sidebar_frame,placeholder_text="Enter Savings Goal")
        self.savings_entry.grid(row=11, column=0, padx=20, pady=5, sticky="ew")

        self.save_savings_btn = ctk.CTkButton(self.sidebar_frame,text="Save Goal",fg_color="#4CAF50")
        self.save_savings_btn.grid(row=12, column=0, padx=20, pady=(5,15), sticky="ew")

        self.table_frame=ctk.CTkFrame(self.content_frame)
        self.table_frame.grid(row=1,column=0,padx=15,pady=15,sticky="nsew")
        self.table_frame.grid_columnconfigure(0,weight=1)
        self.table_frame.grid_rowconfigure(0,weight=1)

        self.setup_treeview_styles()

        self.tree=ttk.Treeview(self.table_frame,columns=("id","desc","category","amount"),show="headings")
        self.tree.grid(row=0,column=0,sticky="nsew")

# calender

        self.calendar_card = ctk.CTkFrame(self.content_frame,corner_radius=15)
        self.calendar_card.grid(row=1,column=1,padx=(5,15),pady=15,sticky="n")
        self.calendar_title = ctk.CTkLabel(self.calendar_card,text="📅 Calendar",font=ctk.CTkFont(family="Times New Roman",size=18,weight="bold"))

        self.calendar_title.pack(pady=(10,5))
        self.calendar = Calendar(
    self.calendar_card,
    selectmode="day",
    date_pattern="dd-mm-yyyy"
)

        self.calendar.pack(padx=10, pady=10)

        # vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.table_frame,orient="vertical",command=self.tree.yview)

        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree.heading("id",text="ID")
        self.tree.heading("desc",text="DESCRIPTION")
        self.tree.heading("category",text="CATEGORY")
        self.tree.heading("amount",text="AMOUNT")

        self.tree.column("id",anchor="center")
        self.tree.column("amount",anchor="center")

        self.delete_button=ctk.CTkButton(self.content_frame,text="DELETE",font=ctk.CTkFont(family = "times new roman",size = 18,weight="bold"),fg_color="#FF5768",command=self.deleteexpense)
        self.delete_button.grid(row=2,column=0,padx=20,pady=(20,20),sticky="e")

        # Dark/Light Mode Switch
        self.switch = ctk.CTkSwitch(
        self.sidebar_frame,
            text="Dark Mode",
            font = ctk.CTkFont(
                family = "Times New Roman",
                size = 16,

            ),
            command=self.change_mode
        )
        self.switch.grid(row=13, column=0, padx=20, pady=20, sticky="w")

    # Change Theme
    def change_mode(self):
        if self.switch.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def setup_treeview_styles(self):
        style=ttk.Style()
        style.theme_use("default")
        style.configure(
        "Treeview",
    background="white",
    foreground="black",
    rowheight=30,
    fieldbackground="grey"
)
        style.configure(
        "Treeview.Heading",
        font=("Times New Roman", 13, "bold")
    )
        style.configure(
        "Treeview",
        font=("Times New Roman", 13, "bold"),   
        rowheight=35,
        background="white",
        foreground="black",
        fieldbackground="grey"
    )


        style.map(
        "Treeview",
        background=[("selected", "#FF5768")]
    )
        style.map("Treeview",background=[("selected","#FF5768")])
        self.title_label.grid(row=0, column=0, padx=10, pady=(10, 10))


    def add_on_expense(self):
            desc =  self.desc_entry.get().strip()
            amount = self.amount_entry.get().strip()
            category = self.category_dropdown.get()

            if not desc or not amount:
                messagebox.showerror(
               "Error",
               "All fields are required"
                            )
                return
            
            try:
                amount = float(amount)
                if amount <= 0:
                    raise ValueError
                
            except ValueError:
                messagebox.showerror(
              "Invalid Amount",
              "Please enter a positive amount."
                            )
                return 
            
            db.add_expense(desc,amount,category)

            self.desc_entry.delete(0,tk.END)
            self.amount_entry.delete(0,tk.END)
            self.refresh_ui()
            self.desc_entry.configure(
           font=ctk.CTkFont(family="Times New Roman", size=16, weight="bold")
)

            self.amount_entry.configure(
          font=ctk.CTkFont(family="Times New Roman", size=16, weight="bold")
)

            messagebox.showinfo(f"Added successfully")

    def deleteexpense(self):
        selected = self.tree.selection()
        
        if not selected:
            messagebox.showerror("Please select the row you want to delete !!")
            return
        
        row_values = self.tree.item(selected[0],"values")
        expense_id= row_values[0]
        desc= row_values[1]

        confirm=messagebox.askyesno(f"Are you sure ?, you want to delete {desc} ? ")


        if confirm:
                db.delete_expense(expense_id)
                self.refresh_ui()
                
    def save_budget(self):
     amount = self.budget_entry.get()

     try:
        amount = float(amount)
     except ValueError:
        messagebox.showerror("Error", "Invalid Budget")
        return

     db.set_budget(amount)
     self.refresh_ui()

    def refresh_ui(self):
           
            for item in self.tree.get_children():
                self.tree.delete(item)

            all_data=db.get_all_expenses()
            for row in all_data:
                self.tree.insert("","end",values=(row[0],row[1],row[3],f"Rs.{row[2]:.2f}",row[4])) 

            total=db.get_total_spent()
            self.total_spent_label.configure(text=f"{total : .2f}")

            budget = db.get_budget()
            remaining = budget - total

            self.remaining_amount.configure(
            text=f"₹{remaining:.2f}"
                        )
            self.refresh_ui()
    def show_selected_date(self):
      selected_date = self.calendar.get_date()
      print(selected_date)

# Run the application
app = ExpenseTrackerApp()
app.mainloop()

