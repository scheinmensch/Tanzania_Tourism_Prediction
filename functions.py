# function to handle missing data and to make some minor adjustments on the dataset, not final

def adjustments(df):
    # fill NaN total_male/total_female with 0
    df['total_male'] = df['total_male'].fillna(0)
    df['total_female'] = df['total_female'].fillna(0)
    
    # add a column group_size based on total_male/total_female
    df['group_size'] = df['total_female'] + df['total_male']
    
    # fill NaN travel_with with "Alone" if group_size is one
    df.loc[df.group_size == 1, 'travel_with'] = 'Alone'
    
    # fill remaining NaN travel_with with missing
    df['travel_with'] = df['travel_with'].fillna('missing')
    
    # fill NaN most_impressing with "No comments"
    df['most_impressing'] = df['most_impressing'].fillna('No comments')
    
    # add a column total_nights based on night_zanzibar/night_mainland
    df['total_nights'] = df['night_zanzibar'] + df['night_mainland']
    
    # delete rows if group_size is zero
    df = df[df.group_size > 0]
    
    # delete rows if total_nights is zero
    df = df[df.total_nights > 0]
    
    # drop id column
    df = df.drop(['ID'], axis =1)
    
    # drop night_mainland column (to avoid multicollinearity)
    df = df.drop(['night_mainland'], axis =1)
    
    # drop total_male column (to avoid multicollinearity)
    df = df.drop(['total_male'], axis =1)
    
    return df