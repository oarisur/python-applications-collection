#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import relevant modules
from user_interface import UserInterface

# Define the main function
def main():
    interface = UserInterface()
    
    #  Create and display menu options to the user
    while True:
        print("\nWelcome to the hockey team management program:")
        print("\n1. Create a team")
        print("2. View a team")
        print("3. View all boys/girls teams")
        print("4. View all teams")
        print("5. Update a team information")
        print("6. Delete a team")
        print("7. Cancel participation")
        print("8. Statistics")
        print("9. Save data")
        print("10. Load data")
        print("0. Exit\n")
        
        choice = input("Enter your choice (0-10): ")
        
        # Add a team
        if choice == "1":
            team_name = input("Enter team name: ")
            team_type = input("Enter team type (Boys/Girls): ")
            fee = int(input("Enter the fee amount: "))
            fee_paid = input("Has the fee been paid? (Yes/No): ")
            if fee_paid == "Yes":
                fee_paid = True
            else:
                fee_paid = False
            add_team = interface.create_a_team(team_name, team_type, fee, fee_paid)
            print(f"\nTeam {team_name} has been added successfully with id: {add_team.id}")
            
        # View one team
        elif choice == "2":
            team_id = int(input("Enter a team Id: "))
            view_one = interface.read_a_team(team_id)
            if view_one:
                print("\n",view_one)
            else:
                print("\nNo team with this id was found")
                
        # View one type of teams
        elif choice == "3":
            team_by_type = input("Enter which type of teams to show (Boys/Girls): ")
            view_one_type = interface.read_one_type_teams(team_by_type)
            if view_one_type:
                for team in view_one_type:
                    print(team)
            else:
                print("\nNo team of this type was found")
                
        # View all teams
        elif choice == "4":
            view_all = interface.read_all_teams()
            for team in view_all:
                print(team)
                
        # Update a team
        elif choice == "5":
            team_id = int(input("Enter a team id to update team information: "))
            new_name = input("Enter new name: ")
            new_type = input("Enter team type: ")
            new_fee = input("Enter new fee amount: ")
            new_payment_status = input("Has the fee been paid? (Yes/No): ")
            if new_payment_status == "Yes":
                fee_paid = True
            else:
                fee_paid = False
            interface.update_a_team(team_id, new_name, new_type, new_fee, fee_paid)
            
        # Delete a team
        elif choice == "6":
            team_id = int(input("Enter team id to delete a team: "))
            delete_one = interface.delete_a_team(team_id)
            
        # Add participation cancellation date
        elif choice == "7":
            team_id = int(input("Enter team id to add cancellation date: "))
            cancellation_date = input("Enter cancellation date (YYYY-MM-DD): ")
            interface.cancel_a_team_participation(team_id, cancellation_date)
            
        # View Stats
        elif choice == "8": 
            total_teams = len(interface.all_teams)
            print(f"\nNumber of registered teams at this moment: {total_teams}")
            total_fee_paid_teams = sum(1 for team in interface.all_teams if team.fee_paid)
            if total_teams >0:
                print(f"\n{(total_fee_paid_teams/total_teams)*100:.2f}% of the teams have paid their fee")
            else:
                print("\nThere is no team with fee paid status yet")
               
        # Save data to file
        elif choice == "9":
            file_name = input("Enter a file name to save teams data: ")
            interface.save_data(file_name)
            
        # load data from file
        elif choice == "10":
            file_name = input("Enter a file name to load teams data: ")
            interface.load_data(file_name)
            
        # Exit the program
        elif choice == "0":
            print("The program will now exit, thank you!")
            break    
    
if __name__ == "__main__":
    main()
    


# In[ ]:




