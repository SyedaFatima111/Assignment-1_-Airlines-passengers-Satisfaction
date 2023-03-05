
import pandas as pd
import matplotlib.pyplot as plt

# read the data from csv file
df = pd.read_csv('Airline_Passenger_Satisfaction.csv')

# define function in order to create line plot
def plot_line(df):
    # group data by gender and month and calculate average rating
    df_line = df.groupby(['Gender', 'Month'], as_index=False)['Average Rating'].mean()
    # plot the line graph with two lines, one for each gender
    plt.plot(df_line[df_line['Gender'] == 'Male']['Month'], df_line[df_line['Gender'] == 'Male']['Average Rating'], label='Male')
    plt.plot(df_line[df_line['Gender'] == 'Female']['Month'], df_line[df_line['Gender'] == 'Female']['Average Rating'], label='Female')
    plt.xlabel('Month')
    plt.ylabel('Average Rating')
    plt.title('Average Rating by Gender')
    plt.legend()
    plt.show()

# define function in order to create pie chart
def plot_pie(df):
    # group data by satisfaction and count number of entries for each level of satisfaction
    df_pie = df.groupby('satisfaction', as_index=False)['id'].count()
    # plot the pie chart
    plt.pie(df_pie['id'], labels=df_pie['satisfaction'], autopct='%1.1f%%')
    plt.title('Satisfaction Levels')
    plt.show()

# define function to create a bar plot
def plot_bar(df):
    # group data by class and calculate the average rating for each class
    df_bar = df.groupby('Class', as_index=False)['Average Rating'].mean()
    # plot the bar graph
    plt.bar(df_bar['Class'], df_bar['Average Rating'])
    plt.xlabel('Class')
    plt.ylabel('Average Rating')
    plt.title('Average Rating by Class')
    # add data labels to the plot
    for i, row in df_bar.iterrows():
        plt.text(row['Class'], row['Average Rating'], round(row['Average Rating'], 2), ha='center')
    plt.show()

# call functions to plot the graphs
plot_line(df)
plot_pie(df)
plot_bar(df)
