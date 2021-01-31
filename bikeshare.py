import time
import pandas as pd
import numpy as np
from datetime import timedelta

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    condition1 = True
    while condition1:
        try:
            city =input("Which city would you like to explore: chicago, new york city, or washington? ")
            if city.lower().strip() not in ['chicago', 'new york city', 'washington']:
                raise Exception("Error! Please enter the correct city name: chicago, new york city, washington")

        except Exception as ex1:
            print(ex1, end='\n')
            continue

        else:
            condition1 = False


    condition2 = True
    while condition2:
        try:
            month =input("Which month of the data would you like to explore? or 'all' ? ")
            if month.lower().strip() not in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                                     'october', 'november', 'december', 'all']:
                raise Exception("Error! Please enter the correct month name to filter the data or 'all' for no filter")

        except Exception as ex2:
            print(ex2, end='\n')
            continue

        else:
            condition2 = False



    condition3 = True
    while condition3:
        try:
            day =input("Which day of the data would you like to explore? or 'all' ? ")
            if day.lower().strip() not in ['monday', 'tuesday', 'thrusday', 'wednesday', 'friday', 'saturday', 'sunday', 'all']:
                raise Exception("Error! Please enter the correct day name to filter the data or 'all' for no filter")

        except Exception as ex3:
            print(ex3, end='\n')
            continue

        else:
            condition3 = False



    print('-'*40)
    return city.lower().strip(), month.lower().strip(), day.lower().strip()


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
    filename = CITY_DATA[city]

    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if len(df['month'].unique()) > 1:
    # TO DO: display the most common month
        popular_month = df['month'].describe()[2]
        print(f"The most frequent month: {popular_month}")

    if len(df['day_of_week'].unique()) > 1:
    # TO DO: display the most common day of week
        popular_day = df['day_of_week'].describe()[2]
        print(f"the most frequent day is {popular_day}")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.strftime('%H')
    popular_hour = df['hour'].describe()[2]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return f"the most frequent hour is {popular_hour}"


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].value_counts()


    # TO DO: display most commonly used end station
    popular_end = df['End Station'].value_counts()


    # TO DO: display most frequent combination of start station and end station trip
    x = list(zip(df['Start Station'].str.lower().str.strip(), df['End Station'].str.lower().str.strip()))

    x_series = pd.Series(x)

    most_freq_comb = x_series.value_counts()

    print('The most popular start station is: ', popular_start.iloc[0:5], end='\n')
    print('The most popular end station is: ', popular_end.iloc[0:5], end='\n')
    print('The most frequent combination of station is: ', most_freq_comb.iloc[0:5], end='\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return ""


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time_sec = df['Trip Duration'].sum()



    # TO DO: display mean travel time
    average_time_sec = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    answer = f"The total Trip Duration of all customers sums to: {total_time_sec// 86.400} days,{str(timedelta(seconds = total_time_sec% 86.400))[0]} hours, {str(timedelta(seconds = total_time_sec% 86.400))[1]} minutes, and {str(timedelta(seconds = total_time_sec% 86.400))[2]} seconds"

    return answer


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user type
    user_types = df['User Type'].value_counts()

    if 'Gender' in df.columns :
        gender_types = df['Gender'].value_counts()

        earliest = df['Birth Year'].copy()
        earliest.sort_values(inplace=True)

        recent = df['Birth Year'].copy()
        recent.sort_values(inplace=True, ascending=False)
        print(user_types, end='\n')
        print(gender_types, end='\n')

        answer = f"The earliest date of birth is {earliest.iloc[0]}, and the most recent date of birth is {recent.iloc[0]}"
        return answer


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_data(df):
    condition4=True
    while condition4:

        try:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            if view_data.lower() not in ['yes','no']:
                raise Exception("Please enter 'yes' or 'no' ")

            start_loc = 0
            while view_data.lower() == 'yes' and start_loc <len(df):
                print(df.iloc[start_loc: start_loc + 5])
                start_loc += 5

                vd = input("Do you wish to continue?: yes or no ").lower()

                if (vd == 'yes'):
                    continue

                else:
                    view_data = 'no'



        except Exception as ex:
            print(ex)
            continue

        else:
            condition4 = False





def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        print(time_stats(df))
        print(station_stats(df))
        print(trip_duration_stats(df))
        print(user_stats(df))
        print(display_data(df))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
