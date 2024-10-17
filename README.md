Project Description >
This project is a technical analysis program based on the Moving Averages (MA) strategy. Users can upload market price data files and apply short-term and long-term moving average strategies to view buy and sell signals. The overall profit is displayed as a percentage, along with analytical charts.

Functional Requirements >
Uploading Price Data Files:
Users can upload text files in txt or prn format that contain the following columns:

Date column: Format YYYYMMDD
Open price
High price
Low price
Close price
Selecting a Moving Average Strategy:
Two options are available for the moving average strategy:

20/50 Strategy: A 20-day short-term MA and a 50-day long-term MA
100/200 Strategy: A 100-day short-term MA and a 200-day long-term MA
Buy and Sell Signals:
Buy signals (marked with ^) and sell signals (marked with v) are displayed on the chart based on the crossover of the moving averages.

Display of Trade Results:
The overall profit is calculated and displayed as a percentage in a message box.

Result Charts:
Charts showing prices with buy and sell signals, along with short-term and long-term moving averages, are provided.

Non-Functional Requirements >
Graphical User Interface (GUI):
A simple GUI is implemented using the Tkinter library to allow user interaction.

Display Messages:
Warning and error messages are shown in case of issues (e.g., file not uploaded or processing error) through message boxes.

Color and Design:
Appropriate colors are used for buttons and text to ensure a simple and easy-to-understand interface.

Constraints >
The data file must contain the specified columns and follow the correct format; otherwise, it will not be processed.
Data should be in the specified time intervals with a valid date format (YYYYMMDD) and valid price data.
The program only supports .txt and .prn files.
Phases and Deliverables
Design and implementation of the GUI
Implementation of 20/50 and 100/200 strategies for data analysis
Displaying buy and sell signals on the chart and calculating total profit
Final version delivery with testing and debugging
Libraries and Dependencies
Required Libraries:
pandas
numpy
tkinter
matplotlib
Note: Tkinter is included by default with Python and does not require separate installation.
