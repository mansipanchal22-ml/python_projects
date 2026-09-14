#pro-6 File Operator
# class JournalManager:
#     def __init__(self):
#         self.filename = "journal.txt"

#         def add_entry(self):
#             try:
#                 entry = input("enter your journal entry:")
#                 if entry.strip() == "":
#                     print("entry cannot be empty.")
#                     return

#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class JournalManager:
    def __init__(self):
        """
        Class: JournalManager
        Purpose: Displays a welcoming message when a new instance of the manager is created.
        Arguments: self
        Returns/Prints: Prints "Welcome to Personal Journal Manager!"
        """
        print("Welcome to Personal Journal Manager!")
   
    def __new_file(self):
        """
        Class: JournalManager
        Purpose: Takes a text entry from the user and appends it to journal.txt with a timestamp.
        Arguments: self
        Returns/Prints: Prints input prompts and "Entry Added Sucessfully!"
        """
        from datetime import datetime
        now = datetime.now()
        self.formatted_now = now.strftime("[%Y-%m-%d %H:%M:%S]")
        self.date=now.strftime("%Y-%m-%d")

        print("Enter The Journal Entry:")
        content=input()
        with open("journal.txt","a") as source:
            source.write(f"""
            {self.formatted_now}
            {content}
            """)
        print("Entry Added Sucessfully!")
        print("""
        """)
    
    def __view_file(self):
        """
        Class: JournalManager
        Purpose: Reads and prints all the saved journal entries from the text file.
        Arguments: self
        Returns/Prints: Prints file content text or error notifications.
        """
        try:
            print("Your Journal Entries:")
            print("----------------------------")
            with open("journal.txt","r") as source:
                item=source.read()
                print(item)
        except FileNotFoundError:
            print("No Journal Entries Found , Start By Adding A New Entry!!")
        print("""
        """)

    def __search_file(self):
        """
        Class: JournalManager
        Purpose: Scans the journal file line-by-line to print lines matching a user-specified keyword or date.
        Arguments: self
        Returns/Prints: Prints matching lines or a "No entities were found" message.
        """
        try:
            item2srch=input("Enter the Keyword or Date to search: ")
            with open("journal.txt","r") as source:
                    itemlst=source.readlines()
                    print("Matching Entities:")
                    found = False
                    for i in range(len(itemlst)):
                        if item2srch in itemlst[i]:
                            print(itemlst[i])
                            found = True
                    
                    if not found:
                        print("No entities were found for the keyword: ",item2srch)
        except FileNotFoundError:
            print("No Journal Entries Found , Start By Adding A New Entry!!")
        print("""
        """)             

    def __del_file(self):
        """
        Class: JournalManager
        Purpose: Wipes out all text inside the journal file after getting a "yes" confirmation from the user.
        Arguments: self
        Returns/Prints: Prints deletion confirmation statements or an error message.
        """
        try:
            user_conf=input("Are you sure you want to delete all entities ??(yes/no): ")
            if user_conf == "yes":
                with open("journal.txt", "w") as source:
                    pass
                print("All journal Entries have been Deleted !")

            elif user_conf == "no":
                print("okayy")
        except:
            print("No Jounal Entities to delete")
        print("""
        """)

    def user_menu(self):
        """
        Class: JournalManager
        Purpose: Runs an infinite loop displaying choices to route the user to different system features.
        Arguments: self
        Returns/Prints: Prints the menu interface text and a goodbye message upon exit.
        """
        while True:
            print("""Please select an option:
            1.Add New Entry
            2.View All Entries
            3.Search For An Entity
            4.Delete All Entries
            5.Exit""")  
            user_opt=int(input("Enter Your Choice :"))
            if user_opt ==1:
                self.__new_file()
            elif user_opt ==2:
                self.__view_file()
            elif user_opt ==3:
                self.__search_file()
            elif user_opt ==4:
                self.__del_file()
            elif user_opt ==5:
                print("Thank You for using personal journal manager,Good Bye!")
                break
            else:
                print("invalid option,please select a valid option from the user menu")

journal=JournalManager()
journal.user_menu()