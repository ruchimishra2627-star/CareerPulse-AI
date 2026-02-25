import hashlib

# Simple dictionary to store users (persists in memory)
users_database = {}

class Database:
    def __init__(self):
        global users_database
        self.users = users_database
        print(f"✅ Database Ready! Total users: {len(self.users)}")
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, name, email, password):
        global users_database
        # Check if email already exists
        if email in users_database:
            return False, "❌ Email already exists!"
        
        # Register new user
        users_database[email] = {
            'name': name,
            'email': email,
            'password': self.hash_password(password)
        }
        print(f"✅ Registered: {email}")
        print(f"📊 Total users: {len(users_database)}")
        return True, "✅ Registration successful!"
    
    def login_user(self, email, password):
        # Check if user exists
        if email not in self.users:
            return False, "❌ Email not registered! Please create an account."
        
        # Check password
        if self.users[email]['password'] != self.hash_password(password):
            return False, "❌ Incorrect password! Please try again."
        
        # Login successful
        print(f"✅ Login successful: {email}")
        return True, self.users[email]
    
    def get_all_users(self):
        """Get list of all registered emails"""
        return list(self.users.keys())
    
    def get_user_count(self):
        """Get total number of users"""
        return len(self.users)
    
    def close(self):
        print("👋 Database connection closed")
        pass