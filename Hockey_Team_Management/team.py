#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import relevant modules
import datetime

# Define a Team class
class Team:
    def __init__(self, team_name, team_type, fee, fee_paid):
        # Initialize team attributes
        self.team_name = team_name
        self.team_type = team_type
        self.fee = fee
        self.fee_paid = fee_paid
        self.id = None  # Each team will get a automatically generated unique id
        self.date = datetime.datetime.now()  # Record a team adding date
        self.cancellation_date = None  # Record the date if a team cancel their participation
        
    # Method to record team participation cancellation with date
    def cancel_participation(self, cancellation_date):
        self.cancellation_date = cancellation_date
        
    # String representation of a team
    def __str__(self):
        payment_status = "Paid" if self.fee_paid else "Due"
        cancellation_status = (f", Cancellation date: {self.cancellation_date}" if self.cancellation_date else "")
        date_format = self.date.strftime("%Y-%m-%d")
        return f"\nTeam id: {self.id}, Name: {self.team_name}, Type: {self.team_type}, Fee: {self.fee} kr, Fee status: {payment_status}, Date created: {date_format}{cancellation_status}" 
        
        


# In[ ]:




