import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Road Accident Severity Prediction",
    page_icon="🚗",
    layout="centered"
)


# --------------------------------------------------
# LOAD TRAINED MODEL
# --------------------------------------------------

MODEL_PATH = "../models/accident_model.pkl"

try:
    model = joblib.load(MODEL_PATH)

except FileNotFoundError:
    st.error(
        "Model file not found. Please train the model first."
    )
    st.stop()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🚗 Road Accident Severity Prediction")

st.write(
    "Enter the road, weather, lighting and vehicle "
    "conditions to predict accident severity."
)

st.divider()


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.subheader("📝 Accident Information")


# Weather condition
weather = st.selectbox(
    "🌧 Weather Condition",
    [
        "Normal",
        "Raining",
        "Raining and Windy",
        "Cloudy",
        "Other",
        "Windy",
        "Snow",
        "Unknown",
        "Fog or mist"
    ]
)


# Road surface condition
road_condition = st.selectbox(
    "🛣 Road Surface Condition",
    [
        "Dry",
        "Wet or damp",
        "Snow",
        "Flood over 3cm. deep"
    ]
)


# Light condition
light = st.selectbox(
    "🌙 Light Condition",
    [
        "Daylight",
        "Darkness - lights lit",
        "Darkness - no lighting",
        "Darkness - lights unlit"
    ]
)


# Vehicle type
vehicle = st.selectbox(
    "🚘 Type of Vehicle",
    [
        "Automobile",
        "Public (> 45 seats)",
        "Lorry (41?100Q)",
        "Public (13?45 seats)",
        "Lorry (11?40Q)",
        "Long lorry",
        "Public (12 seats)",
        "Taxi",
        "Pick up upto 10Q",
        "Stationwagen",
        "Ridden horse",
        "Other",
        "Bajaj",
        "Turbo",
        "Motorcycle",
        "Special vehicle",
        "Bicycle"
    ]
)


# Number of vehicles involved
vehicles_involved = st.number_input(
    "🚗 Number of Vehicles Involved",
    min_value=1,
    max_value=20,
    value=2,
    step=1
)


# Number of casualties
casualties = st.number_input(
    "🏥 Number of Casualties",
    min_value=0,
    max_value=50,
    value=1,
    step=1
)


st.divider()


# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

if st.button(
    "🔮 Predict Accident Severity",
    use_container_width=True
):

    # Create input dataframe
    input_data = pd.DataFrame(
        {
            "Weather_conditions": [weather],
            "Road_surface_conditions": [road_condition],
            "Light_conditions": [light],
            "Type_of_vehicle": [vehicle],
            "Number_of_vehicles_involved": [
                vehicles_involved
            ],
            "Number_of_casualties": [
                casualties
            ]
        }
    )


    # --------------------------------------------------
    # MAKE PREDICTION
    # --------------------------------------------------

    try:

        prediction = model.predict(input_data)

        predicted_severity = prediction[0]


        # --------------------------------------------------
        # DISPLAY RESULT
        # --------------------------------------------------

        st.subheader("📊 Prediction Result")

        st.success(
            f"Predicted Accident Severity: "
            f"**{predicted_severity}**"
        )


        st.divider()


        # --------------------------------------------------
        # ACCIDENT PREVENTION RECOMMENDATIONS
        # --------------------------------------------------

        st.subheader(
            "🛡️ Accident Prevention Recommendations"
        )


        # FATAL INJURY
        if str(predicted_severity).lower() == "fatal injury":

            st.error(
                "🚨 FATAL INJURY RISK"
            )

            st.write(
                "The model predicts a fatal injury "
                "severity category for these conditions."
            )

            st.markdown(
                """
                ### Recommended Safety Measures

                - 🚗 Reduce vehicle speed.
                - 🌧 Drive very carefully during bad weather.
                - 🛣 Be extra careful on wet or slippery roads.
                - 🌙 Use headlights during darkness.
                - 📏 Maintain a safe distance from other vehicles.
                - 📵 Avoid mobile phone use while driving.
                - 🪖 Always wear a helmet or seat belt.
                - 🚦 Follow traffic signals and road signs.
                - ⚠️ Avoid risky overtaking and sudden braking.
                """
            )


        # SERIOUS INJURY
        elif str(predicted_severity).lower() == "serious injury":

            st.warning(
                "⚠️ SERIOUS INJURY RISK"
            )

            st.write(
                "The model predicts a serious injury "
                "severity category for these conditions."
            )

            st.markdown(
                """
                ### Recommended Safety Measures

                - 🚗 Follow the prescribed speed limit.
                - 📏 Maintain a safe following distance.
                - 🌧 Drive carefully during rain.
                - 🛣 Reduce speed on wet roads.
                - 🌙 Use proper headlights during darkness.
                - 📵 Avoid distracted driving.
                - 🪖 Wear a helmet or seat belt.
                - 🚦 Follow traffic rules and road signs.
                """
            )


        # SLIGHT INJURY
        elif str(predicted_severity).lower() == "slight injury":

            st.info(
                "ℹ️ SLIGHT INJURY RISK"
            )

            st.write(
                "The model predicts a slight injury "
                "severity category for these conditions."
            )

            st.markdown(
                """
                ### Recommended Safety Measures

                - 🚗 Continue driving within the speed limit.
                - 🪖 Wear a helmet or seat belt.
                - 🚦 Follow traffic rules.
                - 📏 Maintain a safe distance.
                - 👀 Stay alert while driving.
                - 📵 Avoid distracted driving.
                - 🌧 Drive carefully during poor weather.
                """
            )


        # OTHER
        else:

            st.info(
                f"Predicted severity category: "
                f"{predicted_severity}"
            )

            st.markdown(
                """
                ### General Safety Recommendations

                - Follow traffic rules.
                - Maintain a safe speed.
                - Wear a helmet or seat belt.
                - Avoid distracted driving.
                - Be careful during poor weather.
                - Maintain a safe distance from other vehicles.
                """
            )


        # --------------------------------------------------
        # INPUT SUMMARY
        # --------------------------------------------------

        st.divider()

        st.subheader("📋 Input Information")

        st.write(
            f"**Weather:** {weather}"
        )

        st.write(
            f"**Road Condition:** {road_condition}"
        )

        st.write(
            f"**Light Condition:** {light}"
        )

        st.write(
            f"**Vehicle Type:** {vehicle}"
        )

        st.write(
            f"**Vehicles Involved:** "
            f"{vehicles_involved}"
        )

        st.write(
            f"**Casualties:** "
            f"{casualties}"
        )


    except Exception as e:

        st.error(
            "An error occurred while making the prediction."
        )

        st.write(
            "Please check that the input values and "
            "column names match the training data."
        )

        st.code(str(e))


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "U2UInnovate – Project 15 | "
    "Predictive Analytics for Road Accident Prevention"
)