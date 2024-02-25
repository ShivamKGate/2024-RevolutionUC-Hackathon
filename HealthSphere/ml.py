# import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import GradientBoostingClassifier
# # from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# # from sklearn.preprocessing import LabelEncoder
# # from sklearn.model_selection import GridSearchCV
# # from openpyxl import load_workbook

# # Load the dataset
# file_path = 'clinical_trials.xlsx'
# df = load_workbook(filename = file_path)

# print(df['clinical_trials']['Title'])
# # Preprocessing
# df['Title'] = df['Title'].fillna('No Title')
# df['Summary'] = df['Summary'].fillna('No Summary')
# df['Phase'] = df['Phase'].fillna('No Phase')
# label_encoder = LabelEncoder()
# df['Phase_encoded'] = label_encoder.fit_transform(df['Phase'])
# df['Condition_encoded'] = label_encoder.fit_transform(df['Condition'])
# df['Success'] = df['Status'].apply(lambda x: 1 if x == 'Completed' else 0)

# # Feature selection
# X = df[['Start_Year', 'Start_Month', 'Enrollment', 'Phase_encoded', 'Condition_encoded']]
# y = df['Success']

# # Split the data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Initialize and train the model
# model = GradientBoostingClassifier(random_state=42)
# model.fit(X_train, y_train)

# # Predictions
# y_pred = model.predict(X_test)

# # Evaluate the model
# accuracy = accuracy_score(y_test, y_pred)
# precision = precision_score(y_test, y_pred)
# recall = recall_score(y_test, y_pred)
# f1 = f1_score(y_test, y_pred)

# # Print the performance metrics
# print(f'Accuracy: {accuracy:.4f}, Precision: {precision:.4f}, Recall: {recall:.4f}, F1-Score: {f1:.4f}')
