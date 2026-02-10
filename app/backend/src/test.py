import csv
import hashlib
import re
from tkinter import messagebox
from pathlib import Path
from datetime import datetime


class LoginLogic:
    """
    Handles authentication logic for the login system using CSV storage.
    Includes user registration, login validation, and CSV file operations.
    """
    
    def __init__(self, csv_path="app/backend/data/users.csv"):
        """Initialize the login logic with CSV file path."""
        self.csv_path = csv_path
        self.setup_csv()
    
    def setup_csv(self):
        """Create the users CSV file if it doesn't exist."""
        # Ensure the directory exists
        Path(self.csv_path).parent.mkdir(parents=True, exist_ok=True)
        
        # Create CSV file with headers if it doesn't exist
        if not Path(self.csv_path).exists():
            with open(self.csv_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['username', 'password'])
    
    def validate_username(self, username):
        """
        Validate username format.
        Username must be 3-20 characters, alphanumeric and underscores only.
        
        Args:
            username (str): Username to validate
            
        Returns:
            tuple: (bool, str) - (is_valid, error_message)
        """
        if not username:
            return False, "Username cannot be empty"
        
        if len(username) < 3:
            return False, "Username must be at least 3 characters"
        
        if len(username) > 20:
            return False, "Username must be less than 20 characters"
        
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores"
        
        return True, ""
    
    def validate_password(self, password):
        """
        Validate password strength.
        Password must be at least 6 characters.
        
        Args:
            password (str): Password to validate
            
        Returns:
            tuple: (bool, str) - (is_valid, error_message)
        """
        if not password:
            return False, "Password cannot be empty"
        
        if len(password) < 6:
            return False, "Password must be at least 6 characters"
        
        # Optional: Add more strict requirements
        # if not re.search(r'[A-Z]', password):
        #     return False, "Password must contain at least one uppercase letter"
        # if not re.search(r'[0-9]', password):
        #     return False, "Password must contain at least one number"
        
        return True, ""
    
    def get_next_id(self):
        """
        Get the next available user ID.
        
        Returns:
            int: Next user ID
        """
        try:
            with open(self.csv_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                ids = [int(row['id']) for row in reader if row['id'].isdigit()]
                return max(ids) + 1 if ids else 1
        except FileNotFoundError:
            return 1
    
    def username_exists(self, username):
        """
        Check if username already exists in CSV file.
        
        Args:
            username (str): Username to check
            
        Returns:
            bool: True if username exists, False otherwise
        """
        try:
            with open(self.csv_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'].lower() == username.lower():
                        return True
            return False
        except FileNotFoundError:
            return False
    
    def register_user(self, username, password, email=None):
        """
        Register a new user in the CSV file.
        
        Args:
            username (str): Username
            password (str): Plain text password
            email (str, optional): User email
            
        Returns:
            tuple: (bool, str) - (success, message)
        """
        # Validate username
        valid_username, username_error = self.validate_username(username)
        if not valid_username:
            return False, username_error
        
        # Validate password
        valid_password, password_error = self.validate_password(password)
        if not valid_password:
            return False, password_error
        
        # Check if username already exists
        if self.username_exists(username):
            return False, "Username already exists"
        
        password = self.password(password)
        
        # Get next ID
        user_id = self.get_next_id()
        
        # Get current timestamp
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Append new user to CSV
        try:
            with open(self.csv_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([user_id, username, password, email or '', created_at])
            
            return True, "Registration successful!"
        
        except Exception as e:
            return False, f"File error: {str(e)}"
    
    def authenticate_user(self, username, password):
        """
        Authenticate a user by checking username and password.
        
        Args:
            username (str): Username
            password (str): Plain text password
            
        Returns:
            tuple: (bool, str, dict) - (success, message, user_data)
        """
        if not username or not password:
            return False, "Username and password are required", None
        
        # Hash the provided password
        password_hash = self.hash_password(password)
        
        # Check credentials
        try:
            with open(self.csv_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    if row['username'].lower() == username.lower() and row['password_hash'] == password_hash:
                        user_data = {
                            'id': row['id'],
                            'username': row['username'],
                            'email': row['email'],
                            'created_at': row['created_at']
                        }
                        return True, "Login successful!", user_data
                
                return False, "Invalid username or password", None
        
        except FileNotFoundError:
            return False, "User database not found", None
        except Exception as e:
            return False, f"File error: {str(e)}", None
    
    def get_user_by_username(self, username):
        """
        Retrieve user information by username.
        
        Args:
            username (str): Username to search for
            
        Returns:
            dict or None: User data dictionary or None if not found
        """
        try:
            with open(self.csv_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    if row['username'].lower() == username.lower():
                        return {
                            'id': row['id'],
                            'username': row['username'],
                            'email': row['email'],
                            'created_at': row['created_at']
                        }
            return None
        
        except FileNotFoundError:
            return None
    
    def get_all_users(self):
        """
        Retrieve all users from the CSV file.
        
        Returns:
            list: List of user dictionaries (without password hashes)
        """
        users = []
        try:
            with open(self.csv_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    users.append({
                        'id': row['id'],
                        'username': row['username'],
                        'email': row['email'],
                        'created_at': row['created_at']
                    })
        except FileNotFoundError:
            pass
        
        return users
    
    def delete_user(self, username):
        """
        Delete a user from the CSV file.
        
        Args:
            username (str): Username to delete
            
        Returns:
            tuple: (bool, str) - (success, message)
        """
        try:
            users = []
            user_found = False
            
            # Read all users except the one to delete
            with open(self.csv_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['username'].lower() != username.lower():
                        users.append(row)
                    else:
                        user_found = True
            
            if not user_found:
                return False, "User not found"
            
            # Write back all users except deleted one
            with open(self.csv_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'username', 'password_hash', 'email', 'created_at'])
                writer.writeheader()
                writer.writerows(users)
            
            return True, "User deleted successfully"
        
        except Exception as e:
            return False, f"File error: {str(e)}"


# Callback functions for the GUI
def handle_sign_in(username_entry, password_entry, on_success=None):
    """
    Handle sign in button click.
    
    Args:
        username_entry: Tkinter Entry widget for username
        password_entry: Tkinter Entry widget for password
        on_success: Optional callback function to execute on successful login
    """
    username = username_entry.get().strip()
    password = password_entry.get()
    
    logic = LoginLogic()
    success, message, user_data = logic.authenticate_user(username, password)
    
    if success:
        messagebox.showinfo("Success", message)
        # Clear the password field for security
        password_entry.delete(0, 'end')
        
        # Execute success callback if provided
        if on_success and user_data:
            on_success(user_data)
    else:
        messagebox.showerror("Error", message)
        # Clear password field on failed login
        password_entry.delete(0, 'end')


def handle_sign_up(username_entry, password_entry):
    """
    Handle sign up button click.
    
    Args:
        username_entry: Tkinter Entry widget for username
        password_entry: Tkinter Entry widget for password
    """
    username = username_entry.get().strip()
    password = password_entry.get()
    
    logic = LoginLogic()
    success, message = logic.register_user(username, password)
    
    if success:
        messagebox.showinfo("Success", message)
        # Clear fields after successful registration
        username_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    else:
        messagebox.showerror("Error", message)


# Example usage and testing
if __name__ == "__main__":
    # Test the logic
    logic = LoginLogic("test_users.csv")
    
    # Test registration
    print("Testing registration...")
    success, msg = logic.register_user("testuser", "password123")
    print(f"Registration: {msg}")
    
    # Test duplicate registration
    print("\nTesting duplicate registration...")
    success, msg = logic.register_user("testuser", "password123")
    print(f"Registration: {msg}")
    
    # Test authentication
    print("\nTesting authentication...")
    success, msg, user = logic.authenticate_user("testuser", "password123")
    print(f"Login: {msg}")
    if user:
        print(f"User data: {user}")
    
    # Test wrong password
    print("\nTesting wrong password...")
    success, msg, user = logic.authenticate_user("testuser", "wrongpassword")
    print(f"Login: {msg}")
    
    # Test get all users
    print("\nAll users:")
    users = logic.get_all_users()
    for user in users:
        print(f"  - {user['username']} (ID: {user['id']})")