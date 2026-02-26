import hashlib
import json
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.db_file = 'users_data.json'
        self.users = self.load_users()
        print(f"✅ Database Ready! Total users: {len(self.users)}")
    
    def load_users(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_users(self):
        try:
            with open(self.db_file, 'w') as f:
                json.dump(self.users, f, indent=4)
            return True
        except:
            return False
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, name, email, password):
        if email in self.users:
            return False, "❌ Email already exists!"
        
        self.users[email] = {
            'name': name,
            'email': email,
            'password': self.hash_password(password),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        if self.save_users():
            print(f"✅ Registered: {email}")
            return True, "✅ Registration successful!"
        else:
            return False, "❌ Error saving data!"
    
    def login_user(self, email, password):
        if email not in self.users:
            return False, "❌ Email not registered! Please create an account."
        
        if self.users[email]['password'] != self.hash_password(password):
            return False, "❌ Incorrect password! Please try again."
        
        print(f"✅ Login successful: {email}")
        return True, self.users[email]
    
    def close(self):
        pass