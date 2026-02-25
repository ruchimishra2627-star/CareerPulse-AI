import pickle
import numpy as np
import os

class Predictor:
    def __init__(self):
        self.model = None
        self.load_model()
    
    def load_model(self):
        """Load trained model"""
        model_path = 'models/model.pkl'
        if os.path.exists(model_path):
            with open(model_path, 'rb') as f:
                self.model = pickle.load(f)
            print("✅ Model loaded successfully")
        else:
            print("⚠️ Model not found. Run model.py first")
    
    def predict(self, cgpa, python, dsa, communication, internship, projects, certifications):
        """Predict placement probability"""
        if self.model is None:
            return 75.0, 1
        
        input_data = np.array([[cgpa, python, dsa, communication, 
                               internship, projects, certifications]])
        prob = self.model.predict_proba(input_data)[0][1] * 100
        pred = self.model.predict(input_data)[0]
        
        return round(prob, 2), int(pred)
    
    def get_risk_level(self, prob):
        """Get risk level based on probability"""
        if prob >= 70:
            return "Low Risk", "🟢"
        elif prob >= 40:
            return "Medium Risk", "🟡"
        else:
            return "High Risk", "🔴"
    
    def get_suggestions(self, python, dsa, communication, internship, projects):
        """Generate improvement suggestions"""
        suggestions = []
        
        if python < 7:
            suggestions.append("📘 Improve Python - practice daily")
        if dsa < 6:
            suggestions.append("📊 Practice DSA on LeetCode")
        if communication < 7:
            suggestions.append("🗣️ Work on communication skills")
        if internship == 0:
            suggestions.append("💼 Get an internship")
        if projects < 2:
            suggestions.append("🛠️ Build more projects")
        
        if not suggestions:
            suggestions.append("✨ Your profile looks good!")
        
        return suggestions