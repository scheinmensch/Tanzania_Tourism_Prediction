# function to handle missing data and to make some minor adjustments on the dataset
def basic_preprocessing_baseline(df):
    # fill NaN total_male/total_female with 0
    df['total_male'] = df['total_male'].fillna(0)
    df['total_female'] = df['total_female'].fillna(0)
    
    # fill NaN travel_with with "Alone" if total_male plus total_female is one
    df.loc[df['total_female'] + df['total_male'] == 1, 'travel_with'] = 'Alone'
    
    # fill remaining NaN travel_with with missing
    df['travel_with'] = df['travel_with'].fillna('missing')
    
    # fill NaN most_impressing with "No comments"
    df['most_impressing'] = df['most_impressing'].fillna('No comments')
   
    # drop id column
    df = df.drop(['ID'], axis =1)
    
    return df

# function to handle missing data and to make some adjustments in the data set
def adjustments1(df):
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
    
    # handle group_size equals zero: either replace by 1 if alone traveller or median group size of the train data
    df.loc[(df.group_size == 0) & (df.travel_with == 'Alone'), 'group_size'] = 1
    df.loc[df.group_size == 0, 'group_size'] = train['group_size'].median()

    # handle total_nights equals zero: replace by median total_nights of the train data
    df.loc[df.total_nights == 0, 'total_nights'] = train['total_nights'].median()

    # drop id column
    df = df.drop(['ID'], axis =1)
    
    # drop night_mainland column (to avoid multicollinearity)
    df = df.drop(['night_mainland'], axis =1)
    
    # drop total_male column (to avoid multicollinearity)
    df = df.drop(['total_male'], axis =1)

    # add subregions just as in the EDA
    df['country'] = df['country'].str.lower()
    df = df.replace({'country' : {'united states of america': 'united States', 'swaziland' : 'eswatini', 'cape verde' : 'cabo verde', 'swizerland' : 'switzerland', 'ukrain' : 'ukraine','malt' : 'malta', 'burgaria' : 'bulgaria', 'korea' : 'south korea', 'comoro' : 'comoros', 'scotland' : 'united kingdom', 'russia' : 'russia', 'srilanka': 'sri lanka'}})
    df = df.replace({'country' : {'ivory coast': "côte d'ivoire", 'drc' : 'congo', 'uae' : 'united arab emirates', 'trinidad tobacco' : 'trinidad and tobago', 'costarica' : 'costa rica', 'philipines' : 'philippines', 'djibout' : 'djibouti', 'morroco' : 'morocco'}})
    df['country'] = df['country'].str.capitalize()
    df = pd.merge(df, subregions, how ='left')
    
    return df