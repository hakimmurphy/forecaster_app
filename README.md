# 🛒 Forecaster-App — Corporación Favorita (Grocery Sales, Guayas)

**Live demo »** <https://forecasterapp-re6sa3sspcdsceht7piq9s.streamlit.app/>  
**GitHup Repo »** <https://github.com/hakimmurphy/time_series_corporacion/>

Forecast daily unit-sales for any item–store pair in Guayas province using a tuned XGBoost model.  
No local setup needed — just click the link and start exploring.

---

## 🚀 How the App Works

1. **Pick a store and item** from the dropdowns.  
2. **Choose a forecast date** (calendar limited to 2013-01-01 → 2014-03-31 in this prototype).  
3. Click **“Get Forecast”**.  
   * You’ll see:  
     * predicted sales for the selected date,  
     * a summary table,  
     * a line chart of historical sales with the forecast point highlighted.

Everything runs server-side on Streamlit Community Cloud; nothing to install.

---

