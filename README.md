# 🛒 Forecaster-App — Corporación Favorita (Grocery Sales, Guayas)

**Live demo »** <https://forecasterapp-re6sa3sspcdsceht7piq9s.streamlit.app/>  
**GitHub repo »** <https://github.com/hakimmurphy/time_series_corporacion/>
**Presentation »** <https://www.loom.com/share/3baf1ac036a34c86843d34edb04b438f?sid=bcde394b-f877-4c52-949f-7354b52689af>

* Prototype lets you **browse historical sales from 1 Jan 2013 onward** and  
  **generate forecasts only for dates between 1 Jan 2014 and 31 Mar 2014**.  
  Powered by a tuned XGBoost model and hosted on Streamlit Community Cloud—no local setup needed.

---

## 🚀 How the App Works

1. **Pick a store and item** from the dropdowns.  
   <img width="556" src="https://github.com/user-attachments/assets/f68ad8b6-1196-475d-984d-106e6c64fe28" />

2. **Select a date** — the calendar shows **2013-01-01 → 2014-03-31**,  
   but forecast output is produced *only for 2014-01-01 → 2014-03-31*.

3. Click **“Get Forecast”** to see:  
   * the **predicted sales** for that date,  
   * a **summary table**  
     <br/><img width="543" src="https://github.com/user-attachments/assets/ed438194-2706-4933-9fca-1375353cd346" />  
   * and a **line chart** with historical sales plus the forecast point.  
     <br/><img width="827" src="https://github.com/user-attachments/assets/cfc4b124-c5aa-413e-986e-aaf456197bb2" />

Everything runs server-side on Streamlit Community Cloud—just open the link and use.


---



