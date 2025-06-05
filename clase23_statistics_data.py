import statistics
import csv

# leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {} # create an empty dictionary to store monthly sales
with open('monthly_sales.csv', mode='r') as file: # open the file in read mode
    reader = csv.DictReader(file) # read the file
    for row in reader:
        month = row['month'] # get the month
        sales = int(row['sales']) # get the sales
        monthly_sales[month] = sales # store the sales in a dictionary
        
sales = list(monthly_sales.values()) # get the sales values
#print(sales) # print the sales values


# calcular la media de las ventas mensuales
mean_sales = statistics.mean(sales) # calculate the mean
print(f'Mean sales: {mean_sales}') # print the mean sales


# calcular la mediana de las ventas mensuales
median_sales = statistics.median(sales) # calculate the median
print(f'Median sales: {median_sales}') # print the median sales

# calcular la moda de las ventas mensuales
mode_sales = statistics.mode(sales) # calculate the mode
print(f'Mode sales: {mode_sales}') # print the mode sales

# calcular la desviación estándar de las ventas mensuales
stdev_sales = statistics.stdev(sales) # calculate the standard deviation
print(f'Standard deviation of sales: {stdev_sales}') # print the standard deviation of sales

# calcular la varianza de las ventas mensuales
variance_sales = statistics.variance(sales) # calculate the variance
print(f'Variance of sales: {variance_sales}') # print the variance of sales

max_sales = max(sales) # calculate the maximum sales
min_sales = min(sales) # calculate the minimum sales

range_sales = max_sales - min_sales # calculate the range of sales
print(f'Maximum sales: {max_sales}') # print the maximum sales
print(f'Minimum sales: {min_sales}') # print the minimum sales
print(f'Range of sales: {range_sales}') # print the range of sales

