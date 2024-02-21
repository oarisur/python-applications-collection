#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import relevant modules
from team import Team

# Define a UserInterface class
class UserInterface:
    def __init__(self):
        self.all_teams = []  # An empty list to store all teams
        
    # Method to add a new team
    def create_a_team(self, team_name, team_type, fee, fee_paid):
        team = Team(team_name, team_type, fee, fee_paid)
        team.id = 1001 + len(self.all_teams)  # Unique id for each team
        team.fee_paid = fee_paid
        self.all_teams.append(team)
        return team
    
    # Method to view all information of an individual team 
    def read_a_team(self, team_id):
        for team in self.all_teams:
            if team.id == team_id:
                return team
        return None
    
    # Method to view all information of all teams of a particular type
    def read_one_type_teams(self, team_type):
        collect_one_type = []
        for team in self.all_teams:
            if team.team_type == team_type:
                collect_one_type.append(team)
        return collect_one_type  
    
    # Method to view all information of all teams
    def read_all_teams(self):
        return self.all_teams
    
    # Method to update a team information
    def update_a_team(self, team_id, team_name, team_type, fee, fee_paid):
        for team in self.all_teams:
            if team.id == team_id:
                team.team_name = team_name
                team.team_type = team_type
                team.fee = fee
                team.fee_paid = fee_paid
                print("\nTeam has been updated")
                break
        else:
            print("\nNo team with this id was found")
                
    # Method to delete a team
    def delete_a_team(self, team_id):
        for team in self.all_teams:
            if team.id == team_id:
                self.all_teams.remove(team)
                print("\nTeam has been deleted")
                break
        else:
            print("\nNo team with this id was found")
                
    # Method to cancel participation of a team
    def cancel_a_team_participation(self, team_id, cancellation_date):
        for team in self.all_teams:
            if team.id == team_id:
                team.cancel_participation(cancellation_date)
                print(f"Participation cancellation date for the team has been recorded")
        else:
            print("\nNo team with this id was found")
            
    # Method to save team data
    def save_data(self, file_name):
        try:
            with open(file_name, "w") as file:
                for team in self.all_teams:
                    file.write(f"{team.id},{team.team_name},{team.team_type},{team.fee},{str(team.fee_paid)},{team.date:%Y-%m-%d},{team.cancellation_date}\n")
                print("\nSaving data to file were successful")
        except IOError:
            print("\nError: saving data were not successful")            
    
    # Method to load team data
    def load_data(self, file_name):
        try:
            with open(file_name, "r") as file:
                self.all_teams = []  # Empty the existing team list
                for line in file:
                    data = line.strip().split(",")
                    if len(data)==7:
                        team_id, team_name, team_type, fee, fee_paid, date, cancellation_date = data
                        team = Team(team_name, team_type, int(fee), fee_paid =="True")
                        team.id = int(team_id)
                        team.date = datetime.datetime.strptime(date.strip(), "%Y-%m-%d")
                        if cancellation_date.strip() != "None":  # Check if date value is None 
                            team.cancellation_date = datetime.datetime.strptime(cancellation_date.strip(), "%Y-%m-%d")
                        self.all_teams.append(team)
        except IOError:
            print("\nError: loading data were not suuccessful")
    
    

