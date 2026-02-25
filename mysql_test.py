import mysql.connector  
  
print("=" * 50)  
print("🔍 SIMPLE MYSQL TEST")  
print("=" * 50)  
  
try:  
	print('📡 Testing port 3307...')  
	conn = mysql.connector.connect(host='localhost', user='root', password='', port='3307')  
	print('✅ SUCCESS! Connected on port 3307')  
	conn.close()  
except Exception as e:  
	print(f'❌ Failed on 3307: {e}')  
  
try:  
	print('📡 Testing port 3306...')  
	conn = mysql.connector.connect(host='localhost', user='root', password='', port='3306')  
	print('✅ SUCCESS! Connected on port 3306')  
	conn.close()  
except Exception as e:  
	print(f'❌ Failed on 3306: {e}')  
  
print("=" * 50) 
