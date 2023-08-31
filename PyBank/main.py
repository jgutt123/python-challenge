# %%
import csv
from pathlib import Path

# Load the CSV data

# set path for files to output to analysis folder
file_to_load = Path("budget_data.csv")

# Export the results to text file
with open(file_to_load, "r") as txt_file:



    #file_path = 'budget_data.csv'
    #data = pd.read_csv(file_path)
    #data.head() #print CSV (to check)

    #Print Title
    print("Financial Analysis")
    print ("----------------------")

    #Counting Months Using Length
    counting_months = len(data)
    print("Total Months: ",counting_months)

    #Adding Profit/Losses
    money = sum(data['Profit/Losses'])
    print("Total: $", money)

    #Finding Difference Between Months
    difference = data['Profit/Losses'].diff()

    #Finding Average Difference
    average_diff = difference.mean()
    average_diff = round(average_diff,2)
    print("Average change: $",average_diff)

    #Greatest Increase in Profits (and Index)
    max_profit_increase = difference.max()
    index_1 = difference.idxmax()
    print("Greatest Increase In Profits: ", data['Date'][index_1], "($", max_profit_increase, ")")


    #Greates Decrease in Losses
    min_losses_decrease = difference.min()
    index_2 = difference.idxmin()
    print ("Greatest Decrease in Losses: ", data['Date'][index_2],  "($", min_losses_decrease, ")")



# %%
# set path for files to output to analysis folder
file_to_output = Path("analysis/budget_analysis.txt")

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    # use the .write() method and f strings to output Financial Analysis
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"----------------------\n")
    txt_file.write(f"Total Months: {counting_months}\n")
    txt_file.write(f"Total: ${money}\n")
    txt_file.write(f"Average change: ${average_diff}\n")
    txt_file.write(f"Greatest Increase In Profits: {data['Date'][index_1]} ${max_profit_increase}\n")
    txt_file.write(f"Greatest Decrease In Losses: {data['Date'][index_2]} ${min_losses_decrease}\n")

    

# %%



