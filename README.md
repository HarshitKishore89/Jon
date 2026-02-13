Fear vs Greed Trading Behavior Analysis
📌 Project Overview
This project analyzes trading behavior and performance under different market sentiment regimes using:
historical_data.csv
fear_greed_index.csv
The objective is to evaluate how Fear vs Greed sentiment impacts:
Profitability
Win rate
Trade frequency
Position sizing
Leverage usage
Risk characteristics
The project also explores predictive modeling and strategy optimization based on sentiment classification.
📂 Project Structure
fear-greed-trading-analysis/
│
├── historical_data.csv
├── fear_greed_index.csv
│
├── Part_A_Data_Preparation.ipynb
├── Part_B_Analysis.ipynb
├── Part_C_Actionable_Strategy.ipynb
├── Bonus_Predictive_Clustering_Dashboard.ipynb
│
├── app.py
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/yourusername/fear-greed-trading-analysis.git
cd fear-greed-trading-analysis
2️⃣ Create Virtual Environment (Recommended)
python3 -m venv venv
source venv/bin/activate
Windows:
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
If requirements.txt does not exist:
pip install pandas numpy matplotlib seaborn scikit-learn plotly streamlit
▶️ How to Run
Run Notebooks in Order:
Part_A_Data_Preparation.ipynb
Part_B_Analysis.ipynb
Part_C_Actionable_Strategy.ipynb
Optional:
streamlit run app.py
🧠 Methodology
1️⃣ Data Preparation
Cleaned missing values
Merged sentiment index with trading data
Created sentiment classification (Fear / Greed)
Engineered features:
Lagged PnL
Profit bucket (binary classification)
Trade statistics by sentiment
2️⃣ Exploratory Analysis
Average PnL by sentiment regime
Win rate comparison
Drawdown proxy
Trade frequency
Average trade size
Leverage behavior
3️⃣ Predictive Modeling
A Logistic Regression model was built to predict trade profitability using:
Sentiment classification
Lagged PnL
Behavioral features
Model evaluation:
Classification report
Precision / Recall
Confusion matrix
📈 Key Insights
Trading behavior differs significantly between Fear and Greed regimes.
Leverage usage increases during Greed.
Risk-adjusted returns vary across sentiment environments.
Sentiment can act as a regime filter for strategy deployment.
🎯 Strategy Recommendations
Reduce leverage during extreme Fear regimes.
Apply position scaling during Greed to manage overexposure.
Use sentiment as a regime filter before entering new trades.
Implement volatility-adjusted sizing.
Use predictive probability as confirmation filter.
🚀 Future Improvements
Walk-forward validation
Time-series cross-validation
Advanced ML models (XGBoost, Random Forest)
Regime-switching models
Risk-adjusted performance metrics (Sharpe, Sortino)
🛠 Tech Stack
Python
Pandas
NumPy
Matplotlib
Scikit-learn
Streamlit
👤 Author
Your Name
GitHub: https://github.com/yourusername
