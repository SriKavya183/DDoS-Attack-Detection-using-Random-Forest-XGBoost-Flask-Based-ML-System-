import joblib
import numpy as np

# Load pre-trained models
scaler = joblib.load("models/minmaxscaler.pkl")
model = joblib.load("models/xgb_1.sav")
label_encoder = joblib.load("models/label_encoder.pkl")

# Feature Names
FEATURES = [
    'Protocol', 'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets', 
    'Fwd Packets Length Total', 'Fwd Packet Length Max', 'Fwd Packet Length Min', 
    'Fwd Packet Length Std', 'Bwd Packet Length Max', 'Bwd Packet Length Min', 
    'Flow Bytes/s', 'Flow IAT Mean', 'Flow IAT Min', 'Bwd IAT Total', 'Bwd IAT Mean', 
    'Bwd IAT Min', 'Fwd PSH Flags', 'Fwd Header Length', 'Bwd Header Length', 
    'Bwd Packets/s', 'Packet Length Variance', 'SYN Flag Count', 'ACK Flag Count', 
    'URG Flag Count', 'CWE Flag Count', 'Down/Up Ratio', 'Init Fwd Win Bytes', 
    'Init Bwd Win Bytes', 'Fwd Act Data Packets', 'Fwd Seg Size Min', 'Active Mean', 
    'Active Std', 'Idle Std'
]

def predict_ddos(features):
    try:
        # Convert input to NumPy array and scale
        features = np.array(features).reshape(1, -1)
        features_scaled = scaler.transform(features)

        # Predict using the model
        prediction = model.predict(features_scaled)
        predicted_label = label_encoder.inverse_transform([int(prediction[0])])[0]

        return predicted_label
    except Exception as e:
        return str(e)
