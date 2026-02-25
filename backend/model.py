import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

print("=" * 50)
print("🔍 TRAINING ML MODEL")
print("=" * 50)

# Create sample data
print("📊 Creating sample data...")
np.random.seed(42)
n = 200

data = {
    'cgpa': np.random.uniform(5, 10, n),
    'python': np.random.randint(1, 11, n),
    'dsa': np.random.randint(1, 11, n),
    'communication': np.random.randint(1, 11, n),
    'internship': np.random.randint(0, 2, n),
    'projects': np.random.randint(0, 6, n),
    'certifications': np.random.randint(0, 4, n)
}

df = pd.DataFrame(data)

# Create target (placement)
score = (df['cgpa']/10 * 30 + df['python']/10 * 20 + df['dsa']/10 * 20 + 
         df['communication']/10 * 15 + df['internship'] * 10 + df['projects']/5 * 5)
df['placement'] = (score > 50).astype(int)

print(f"✅ Created {n} sample records")

# Train model
print("🔄 Training Random Forest model...")
X = df[['cgpa', 'python', 'dsa', 'communication', 'internship', 'projects', 'certifications']]
y = df['placement']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

print("✅ Model training complete!")

# Save model
os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model saved to models/model.pkl")
print("=" * 50)