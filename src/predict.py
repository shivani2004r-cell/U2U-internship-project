import joblib
import pandas as pd

model = joblib.load(
    "../models/accident_model.pkl"
)

sample_data = pd.DataFrame(
    {
        "Weather_conditions": [
            "Rainy"
        ],
        "Road_surface_conditions": [
            "Wet"
        ],
        "Light_conditions": [
            "Night"
        ],
        "Type_of_vehicle": [
            "Motorcycle"
        ],
        "Number_of_vehicles_involved": [
            2
        ],
        "Number_of_casualties": [
            1
        ]
    }
)

prediction = model.predict(
    sample_data
)

print(
    "Predicted Accident Severity:",
    prediction[0]
)