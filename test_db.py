from backend.database import Database

print("=" * 60)
print("🔍 BACKEND DATABASE TEST")
print("=" * 60)

try:
    # Create database object
    print("\n📡 Connecting to database...")
    db = Database()
    print("✅ Database connected!")

    # Test registration
    print("\n📝 Testing Registration...")
    success, message = db.register_user("Test User", "test@email.com", "test123")
    print(f"   Result: {message}")

    # Test duplicate registration
    print("\n📝 Testing Duplicate Registration...")
    success, message = db.register_user("Test User", "test@email.com", "test123")
    print(f"   Result: {message}")

    # Test login with correct password
    print("\n🔐 Testing Login with correct password...")
    success, user = db.login_user("test@email.com", "test123")
    if success:
        print(f"   ✅ Login successful!")
        print(f"   👤 Name: {user['name']}")
        print(f"   📧 Email: {user['email']}")
    else:
        print(f"   ❌ Login failed: {user}")

    # Test login with wrong password
    print("\n🔐 Testing Login with wrong password...")
    success, user = db.login_user("test@email.com", "wrongpassword")
    if not success:
        print(f"   ✅ Correctly rejected: {user}")

    # Close connection
    db.close()
    print("\n✅ Test completed!")

except Exception as e:
    print(f"\n❌ ERROR: {e}")

print("\n" + "=" * 60) 
