# 🛒 Forecaster-App — Corporación Favorita (Grocery Sales, Guayas)

**Live demo »** <https://forecasterapp-re6sa3sspcdsceht7piq9s.streamlit.app/>  
**GitHub repo »** <https://github.com/hakimmurphy/time_series_corporacion/>

* Prototype lets you **browse historical sales from 1 Jan 2013 onward** and  
  **generate forecasts only for dates between 1 Jan 2014 and 31 Mar 2014**.  
  Powered by a tuned XGBoost model and hosted on Streamlit Community Cloud—no local setup needed.

---

## 🚀 How the App Works

1. **Pick a store and item** from the dropdowns.  
2. **Select a date**—the calendar shows 2013-01-01 → 2014-03-31,  
   but forecast output is produced **only for 2014-01-01 → 2014-03-31**.  
3. Click **“Get Forecast”** to see:  
   * predicted sales for that date,  
   * a summary table,  
   * a line chart with historical sales and the forecast point.

Everything runs server-side on Streamlit Cloud; just open the link and use.

---


