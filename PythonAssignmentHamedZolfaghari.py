import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt

# Global variables
processed_data = None
total_profit_percentage = 0.0  # Total profit in percentage
num_trades = 0  # Number of trades made

# Function to process the uploaded file
def process_file(file_path):
    global processed_data
    try:
        df = pd.read_csv(file_path, header=0)

        # Selecting relevant columns
        processed_data = pd.DataFrame({
            'Date': pd.to_datetime(df['<DTYYYYMMDD>'].astype(str), format='%Y%m%d'),
            'Open': df['<OPEN>'],
            'High': df['<HIGH>'],
            'Low': df['<LOW>'],
            'Close': df['<CLOSE>']
        })

        messagebox.showinfo("File Uploaded", "File uploaded successfully. Now select a moving average strategy.")
    
    except Exception as e:
        print(f"Error processing file: {e}")
        messagebox.showerror("Error", f"An error occurred while processing the file: {e}")

# Function to backtest the moving averages strategy
def backtest_moving_averages(short_term, long_term):
    global processed_data, total_profit_percentage, num_trades

    # Calculate moving averages
    processed_data['Short_MA'] = processed_data['Close'].rolling(window=short_term).mean()
    processed_data['Long_MA'] = processed_data['Close'].rolling(window=long_term).mean()

    # Create signals
    processed_data['Signal'] = 0
    processed_data['Signal'] = np.where(processed_data['Short_MA'] > processed_data['Long_MA'], 1, 0)  # Buy signal
    processed_data['Position'] = processed_data['Signal'].diff()  # Buy/Sell signal

    # Initialize variables to track trades
    total_profit_percentage = 0.0
    in_trade = False
    buy_price = 0.0

    for index, row in processed_data.iterrows():
        if row['Position'] == 1 and not in_trade:  # Buy
            buy_price = row['Close']
            in_trade = True
        elif row['Position'] == -1 and in_trade:  # Sell
            sell_price = row['Close']
            profit = sell_price - buy_price
            profit_percentage = (profit / buy_price)*100  # Calculate percentage profit
            total_profit_percentage = ((1+profit_percentage/100)*(1+total_profit_percentage/100)-1)*100
            num_trades += 1
            in_trade = False

def view_results():
    global total_profit_percentage, num_trades
    if processed_data is None:
        messagebox.showwarning("Warning", "No data processed yet. Please upload a file first.")
        return

    # Show total profit percentage in a message box
    messagebox.showinfo("Backtest Result", f"Total Profit Percentage from all trades: {total_profit_percentage:.2f}%")
    
    # Plot the results
    plot_results()

def plot_results():
    plt.figure(figsize=(12, 6))
    plt.plot(processed_data['Date'], processed_data['Close'], label='Close Price', alpha=0.5)
    plt.plot(processed_data['Date'], processed_data['Short_MA'], label='Short-Term MA', alpha=0.75)
    plt.plot(processed_data['Date'], processed_data['Long_MA'], label='Long-Term MA', alpha=0.75)

    # Plot Buy signals
    plt.plot(processed_data[processed_data['Position'] == 1]['Date'], 
             processed_data[processed_data['Position'] == 1]['Close'],
             '^', markersize=10, color='g', lw=0, label='Buy Signal')

    # Plot Sell signals
    plt.plot(processed_data[processed_data['Position'] == -1]['Date'], 
             processed_data[processed_data['Position'] == -1]['Close'],
             'v', markersize=10, color='r', lw=0, label='Sell Signal')

    plt.title('Moving Averages Backtest')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to handle file upload
def upload_file():
    file_path = filedialog.askopenfilename(title="Select File", filetypes=[("Text files", "*.txt"), ("PRN files", "*.prn")])
    if file_path:
        process_file(file_path)

# Function to choose the first moving average strategy (20/50)
def choose_ma_20_50():
    if processed_data is not None:
        backtest_moving_averages(20, 50)
        messagebox.showinfo("Strategy Selected", "Short MA: 20, Long MA: 50")
    else:
        messagebox.showwarning("Warning", "No data uploaded. Please upload a file first.")

# Function to choose the second moving average strategy (100/200)
def choose_ma_100_200():
    if processed_data is not None:
        backtest_moving_averages(100, 200)
        messagebox.showinfo("Strategy Selected", "Short MA: 100, Long MA: 200")
    else:
        messagebox.showwarning("Warning", "No data uploaded. Please upload a file first.")

# Function to create the GUI
def create_gui():
    window = tk.Tk()
    window.title("Technical Analysis Program")
    
    # Set background color
    window.configure(bg="#f2f2f2") 

    # Menu Label
    menu_label = tk.Label(window, text="Welcome to the Technical Analysis Bot.\nPlease select one of the options below:", 
                          font=("Helvetica", 16, "bold"), justify="center", bg="#f2f2f2")
    menu_label.pack(pady=10)

    # Upload Data Button
    upload_button = tk.Button(window, text="📂 Upload Data", command=upload_file, font=("Helvetica", 14), 
                              bg="#4CAF50", fg="white", padx=20, pady=10)
    upload_button.pack(pady=10)

    # Strategy Selection
    strategy_label = tk.Label(window, text="Choose Moving Average Strategy:", font=("Helvetica", 14), bg="#f2f2f2")
    strategy_label.pack(pady=10)

    # MA Strategy 20/50 Button
    ma_20_50_button = tk.Button(window, text="Short MA: 20 - Long MA: 50", command=choose_ma_20_50, 
                                font=("Helvetica", 12), bg="#03A9F4", fg="white", padx=10, pady=5)
    ma_20_50_button.pack(pady=5)

    # MA Strategy 100/200 Button
    ma_100_200_button = tk.Button(window, text="Short MA: 100 - Long MA: 200", command=choose_ma_100_200, 
                                  font=("Helvetica", 12), bg="#FF9800", fg="white", padx=10, pady=5)
    ma_100_200_button.pack(pady=5)

    # View Results Button
    results_button = tk.Button(window, text="📊 View Results", command=view_results, font=("Helvetica", 14), 
                               bg="#9C27B0", fg="white", padx=20, pady=10)
    results_button.pack(pady=10)

    # Exit Button
    exit_button = tk.Button(window, text="Exit", command=window.quit, font=("Helvetica", 14), bg="#F44336", 
                            fg="white", padx=20, pady=10)
    exit_button.pack(pady=20)

    # Run the GUI loop
    window.mainloop()

if __name__ == "__main__":
    create_gui()
