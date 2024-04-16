import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ppscore as pps

# Φόρτωση δεδομένων
df = pd.read_csv(r'/Users/iroliakakou/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Ransomware.csv', delimiter='|')

# Οι στήλες 'Name' και 'md5' είναι κατηγορικές
df_numeric = df.drop(['Name', 'md5',], axis=1)

# Υπολογισμός του πίνακα PPS
pps_matrix = pps.matrix(df_numeric)

# Φιλτράρισμα του DataFrame κρατώντας μόνο τις αριθμητικές στήλες
numeric_pps_matrix = pps_matrix.select_dtypes(include=['float64'])

# Εκτύπωση των τύπων των δεδομένων για επαλήθευση
print(numeric_pps_matrix.dtypes)

# Οπτικοποίηση των αποτελεσμάτων
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_pps_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.show()
