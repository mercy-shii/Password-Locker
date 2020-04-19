#!/usr/bin/env python3.6
from user import user
from credentials import credentials

def create_user(loginusername,password):
    '''
    Function to create a new user
    '''
    new_user = User(loginusername,password)
    return new_user


def create_credentials(username,account_name,account_password):
    '''
    Function to create a new credentials
    '''
    new_credentials = Credentials(username,accountname,accountpassword)
    return new_credentials  

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()    

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()  

def display_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    return Credentials.display_credentials()          