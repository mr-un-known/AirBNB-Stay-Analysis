import pandas as pd



df = pd.read_csv("AB_NYC_2019.csv")


def location_filter(loc_name):
    """This function performs Location - wise filtering on the original dataset
    and returns the filtered dataset."""
    return df.loc[df['neighbourhood_group'].str.contains(loc_name, case=False, regex=False)]

loc_df = location_filter(input("Enter required location: "))



def room_filter(room):
    """This function performs room type - wise filtering on the dataset obtained from
    location_filter() function and returns the filtered dataset."""
    return loc_df.loc[df['room_type'] == room.capitalize()]

room_df = room_filter(input("Enter required room type: "))



def price(max_price, min_price):
    """This function performs price - wise filtering on the dataset obtained from
    room_filter() function and returns the filtered dataset."""
    price_df = room_df.loc[(df['price'] <= max_price) & (df['price'] >= min_price)]
    return price_df.sort_values(by = 'price')

price_df = price(int(input("Enter maximum price: ")), int(input("Enter minimum price: ")))



def review_filter():
    """This function performs filters the dataset on basis of reviews (highet to lowest)
    where the dataset is obtained from price_filter() function. Output is the filtered dataset."""
    sort_by_review_df = price_df.sort_values(by = 'number_of_reviews', ascending = False)
    return sort_by_review_df

print(review_filter())