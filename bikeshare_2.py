import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days_of_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter a city(New York City, Chicago, Washington): ").lower()
    if city not in CITY_DATA:
        print ('Please enter one of the cities(Washington, Chicago, New York City)')
        city = input('Enter a city: ').lower()
    else:
        print('You chose {}'.format(city))

    # get user input for month (all, january, february, ... , june)
    month = input("Enter a month(January - June or All): ").lower()
    if month in months:
        print('You chose {}'.format(month))
    else:
        print('Please try again')
        month = input("Enter a month(January - June or All): ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter a day of the week: ').lower()
    if day in days_of_week:
        print('You chose {}'.format(day))
    else:
        print('Please pick another day')
        day = input('Please enter a day of the week: ').lower()

    print('-'*40)
    return city, month, day


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

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    count = 0

    print(df.iloc[count : count + 5])
    more_sample = input('Would you like more data: yes or no: ').lower()
    while more_sample != 'no':
        if count < df.shape[0]:
            print(df.iloc[count : count + 5])
            count += 5
            more_sample = input('Would you like more data: yes or no: ').lower()
        elif more_sample == 'no':
            break

    if month != 'all':
        months.remove('all')
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        days_of_week.remove('all')
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    common_month = df['month'].mode()[0]
    print('The most common month is : {}'.format(months[common_month - 1]))

    # display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print('The most popular day is : {}'.format(common_day))


    # display the most common start hour
    common_hour = df["hour"].mode()[0]
    print('The busiest hour is : {}'.format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    pop_start = df['Start Station'].mode()[0]
    print('The most popular starting station was: {}'.format(pop_start))

    # display most commonly used end station
    pop_end = df['End Station'].mode()[0]
    print('The most popular ending station was: {}'.format(pop_end))


    # display most frequent combination of start station and end station trip
    pop_trip = (df['End Station'] + ' and ' + df['Start Station']).mode()[0]
    print('The most popular trip was from: \n {}'.format(pop_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    day = str(total_duration // (24 * 60 * 60))
    total_duration = total_duration % (24 * 60 * 60)
    hour = str(total_duration // (60 * 60))
    total_duration %= (60 * 60)
    minutes = str(total_duration // (60))
    total_duration %= 60
    second = str(total_duration)
    print('The total time traveled: ')
    print("The total time travel was :\n {} days {} hours {} minutes {} seconds".format(day, hour, minutes, second))


    # display mean travel time
    ave_duration = df['Trip Duration'].mean()
    day1 = str(ave_duration // (24 * 60 * 60))
    ave_duration = ave_duration % (24 * 60 * 60)
    hour1 = str(ave_duration // (60 * 60))
    ave_duration %= (60 * 60)
    minutes1 = str(ave_duration // (60))
    ave_duration %= 60
    second1 = str(ave_duration)
    print("The average time travel was :\n {} days {} hours {} minutes {} seconds".format(day1, hour1, minutes1, second1))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user type were : {}'.format(user_types))


    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('The gender demo was: {}'.format(gender_counts))
    except:
        print('No data available')

    # Display earliest, most recent, and most common year of birth
    try:
        youngest = int(df['Birth Year'].max())
        oldest = int(df['Birth Year'].min())
        common_year =  int(df['Birth Year'].mode()[0])
        print('The most recent year was:{}'.format(str(youngest)))
        print('The earliest year was: {}'.format(str(oldest)))
        print('The most common birth year was: {}'.format(str(common_year)))
    except:
        print('No year was supplied')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
