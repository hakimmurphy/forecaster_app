import streamlit as st
import datetime
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt

# Columns used during model training
TRAIN_COLUMNS = [
    'id', 'store_nbr', 'item_nbr', 'z_score', 'is_outlier',
    'day_of_week', 'month', 'day', 'year', 'is_weekend',
    'lag_1', 'lag_7', 'lag_30', 'rolling_mean_7',
    'rolling_std_7', 'unit_sales_7d_avg'
]

# File paths
current_dir = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(current_dir, 'xgboost_features.csv')
MODEL_PATH = os.path.join(current_dir, 'XGBoost.pkl')

# Load data from CSV
@st.cache_data
def load_data(data_path):
    df = pd.read_csv(data_path)
    df['date'] = pd.to_datetime(df['date'])
    return df

# Preprocess user input
def preprocess_input_data(df, store_id, item_id, date):
    input_data = df[
        (df['store_nbr'] == store_id) &
        (df['item_nbr'] == item_id) &
        (df['date'] == pd.to_datetime(date))
    ]

    if input_data.empty:
        return pd.DataFrame()

    features = input_data.drop(columns=['unit_sales', 'date'])
    features = features[[col for col in TRAIN_COLUMNS if col in features.columns]]
    return features

# Load trained model
def load_model(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

# Run prediction with correct features
def predict(model, input_data):
    input_data = input_data[TRAIN_COLUMNS]
    prediction = model.predict(input_data)
    return prediction[0] if len(prediction) > 0 else None

# Plot sales history and forecast
def plot_prediction(df, store_id, item_id, forecast_date, forecast_value):
    # Filter past sales data for the selected item/store
    history = df[
        (df['store_nbr'] == store_id) &
        (df['item_nbr'] == item_id) &
        (df['date'] < pd.to_datetime(forecast_date))
    ][['date', 'unit_sales']].sort_values('date')

    # Debug info
    st.write("Last few actual sales:")
    st.write(history.tail())

    # Append forecast to the data
    future_row = pd.DataFrame({
        'date': [pd.to_datetime(forecast_date)],
        'unit_sales': [forecast_value]
    })
    forecast_df = pd.concat([history, future_row], ignore_index=True)

    # X-axis range for debug
    # st.write("X-axis range:", forecast_df['date'].min(), "to", forecast_df['date'].max())

    # Plot
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(forecast_df['date'], forecast_df['unit_sales'], marker='o', label='Unit Sales')
    ax.axvline(pd.to_datetime(forecast_date), color='green', linestyle='--', label='Forecast Date')
    
    # Make red dot visible and prominent
    ax.scatter(forecast_date, forecast_value, color='red', s=50, zorder=5, label='Forecasted Sale')

    # Fix y-axis scaling to include forecast point
    max_val = max(forecast_df['unit_sales'].max(), forecast_value)
    ax.set_ylim(bottom=0, top=max_val * 1.1)

    # Final formatting
    ax.set_title(f"Sales History + Forecast for Item {item_id} at Store {store_id}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Unit Sales")
    ax.legend()
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()

    # Display chart
    st.pyplot(fig)


#  Main Streamlit app
def main():
    st.title("Corporación Favorita Sales Forecasting")

    df = load_data(DATA_PATH)
    model = load_model(MODEL_PATH)

    # User inputs
    store_id = st.selectbox("Store", sorted(df['store_nbr'].unique()))
    item_id = st.selectbox("Item", sorted(df['item_nbr'].unique()))

    default_date = datetime.date(2014, 3, 1)
    min_date = df['date'].min().date()
    max_date = df['date'].max().date()
    date = st.date_input("Forecast Date", value=default_date, min_value=min_date, max_value=max_date)

    # Generate forecast
    if st.button("Get Forecast"):
        input_data = preprocess_input_data(df, store_id, item_id, date)
        if not input_data.empty:
            prediction = predict(model, input_data)
            if prediction is not None:
                st.success(f"Predicted Sales for {date}: {prediction:.2f}")

                # ✅ Forecast Summary Table
                prediction_row = pd.DataFrame({
                    "Forecast Date": [date],
                    "Store": [store_id],
                    "Item": [item_id],
                    "Predicted Sales": [round(prediction, 2)]
                })
                st.subheader("📋 Forecast Summary")
                st.dataframe(prediction_row)

                # Forecast chart
                plot_prediction(df, store_id, item_id, date, prediction)
            else:
                st.warning("Prediction could not be generated.")
        else:
            st.warning("No data found for the selected inputs.")

# Entry point
if __name__ == "__main__":
    main()
