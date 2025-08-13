import time
import pandas as pd
import numpy as np

#This is a change to be shown in git diff

CITY_DATA = { 'chicago':'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

Months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
Days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True: 
        try:
            while True: 

                city = input("Please select a city to analyze data, you can choose Chicago, New york city or Washington: ").lower().strip()
                if city in CITY_DATA:
                    break
                print(f"{city} is not a valid city")

        # TO DO: get user input for month (all, january, february, ... , june)
                
            while True:    
                month_name = input("Please select a month to filter (from January to June, or all): ").lower().strip()
                if month_name in Months or month_name == 'all':
                    break
                print(f"the entered month {month_name} is not valid, please enter a correct month name")

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

            while True:
                day_week = input("please select a day of the week to analyze data (You can select a specific day or all at a time): ").lower().strip()
                if day_week in Days:
                    break
                print(f"the entered day {day_week} is not valid, please enter a correct day")

            print('-'*40)
            return city, month_name, day_week

        except Exception as error:
            print(f"an error occurred: {error}")
            
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_week'] = df['Start Time'].dt.day_name().str.lower()

    if month != 'all':
        #month = Months.index(month) + 1
        df = df[df['month'] == month.lower().strip()]

    if day != 'all':
        df = df[df['day_week'] == day.lower().strip()]

    return df

#print(load_data(city, month, day))


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        print("The most common month in the data set is:", df['month'].mode()[0])

    # TO DO: display the most common day of week
    if day == 'all':
        print("The most common day in the data set is:", df['day_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour in the data set is:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used Start Station is:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used End Station is:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combinations'] = df['Start Station'] + ' To ' + df['End Station']
    print("The most frequent combination of start station and end station trip is:", df['Station Combinations'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_seconds = df['Trip Duration'].sum()
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(total_seconds))
    print(f"The total travel time is: {formatted_time}")

    # TO DO: display mean travel time
    total_seconds = df['Trip Duration'].mean()
    formatted_time = time.strftime("%H:%M:%S", time.gmtime(total_seconds))
    print(f"The mean travel time is: {formatted_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("this is the count of user types:\n", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("this is the count of genders:\n", df['Gender'].value_counts())
    else:
        print("Gender data not available for Washington city")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("this is the earliest year of birth:\n", df['Birth Year'].min())
        print("this is the most recent year of birth:\n", df['Birth Year'].max())
        print("this is the most common year of birth:\n", df['Birth Year'].mode()[0])

    else:
        print("Year of Birth data not available for Washington city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    row_index = 0

    while True:
        show_data = input("Would you like to see 5 rows of data?, yes or no: ").lower()
        if show_data != "yes":
            break
        if row_index >= len(df):
            print("No more to display")
            break
        print(df.iloc[row_index:row_index+5])
        row_index +=5


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
