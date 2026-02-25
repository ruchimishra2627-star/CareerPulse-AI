from backend.predict import Predictor

print("=" * 60)
print("🔍 CAREERPULSE AI - MODEL TEST")
print("=" * 60)

# Create predictor object
p = Predictor()

# Test with sample student data
print("\n📊 Analyzing Student Profile:")
print("-" * 40)
print("📚 CGPA: 8.5")
print("🐍 Python: 9/10")
print("📊 DSA: 8/10")
print("🗣️ Communication: 7/10")
print("💼 Internship: Yes")
print("🛠️ Projects: 3")
print("📜 Certifications: 2")
print("-" * 40)

# Get prediction
prob, pred = p.predict(8.5, 9, 8, 7, 1, 3, 2)
risk, emoji = p.get_risk_level(prob)
suggestions = p.get_suggestions(9, 8, 7, 1, 3)

# Show results
print("\n🎯 PREDICTION RESULTS:")
print(f"   📈 Placement Probability: {prob}%")
print(f"   ⚠️ Risk Level: {emoji} {risk}")
print(f"   ✅ Status: {'PLACED' if pred == 1 else 'NEEDS IMPROVEMENT'}")

print("\n💡 IMPROVEMENT SUGGESTIONS:")
if suggestions:
    for i, s in enumerate(suggestions, 1):
        print(f"   {i}. {s}")
else:
    print("   ✨ Your profile looks great! Keep it up!")

print("\n" + "=" * 60)
