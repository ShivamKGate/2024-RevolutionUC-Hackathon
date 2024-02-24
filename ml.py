from flask import Flask, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('clinical_trials.csv')

# Data Preprocessing
# Handle missing values
df.dropna(inplace=True)

# Encode categorical variables
df = pd.get_dummies(df, columns=['Sponsor', 'Condition'])

# Drop non-categorical columns containing string values
df = df.drop(columns=['NCT'])

# Split the dataset into features and target variable
X = df.drop(columns=['Status'])
y = df['Status']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)

# Perform hyperparameter tuning (for demonstration purposes, you can adjust the parameters)
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(estimator=rf_classifier, param_grid=param_grid, cv=3)
grid_search.fit(X_train, y_train)

# Get the best parameters and retrain the model
best_params = grid_search.best_params_
best_rf_classifier = RandomForestClassifier(**best_params, random_state=42)
best_rf_classifier.fit(X_train, y_train)

def perform_machine_learning():
    # Assuming you have new data for prediction (you may need to adjust based on your actual implementation)
    # For demonstration purposes, let's assume we have a single sample of new data
    new_data = pd.DataFrame({
        'Sponsor': ['Example Sponsor'],
        'Condition': ['Example Condition']
        # Add other features as needed
    })
    # Encode categorical variables
    new_data_encoded = pd.get_dummies(new_data, columns=['Sponsor', 'Condition'])

    
    # Make predictions on new data
    prediction = best_rf_classifier.predict(new_data_encoded)
    
    # Predict patient response probabilities
    response_probabilities = best_rf_classifier.predict_proba(new_data_encoded)[:, 1]
    
    # Identify risk factors for adverse events (feature importances)
    risk_factors = best_rf_classifier.feature_importances_
    
    # You can add more detailed analysis or processing here based on the predictions and probabilities
    
    # Return the results
    return prediction, response_probabilities, risk_factors


@app.route("/")
@app.route("/home")
def home():
    # Call the perform_machine_learning function
    prediction, response_probabilities, risk_factors = perform_machine_learning()
    
    # Pass the results to the home template
    return render_template("home.html", prediction=prediction, 
                           response_probabilities=response_probabilities, 
                           risk_factors=risk_factors)

if __name__ == "__main__":
    app.run(debug=True)
