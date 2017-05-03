
# coding: utf-8

# In[60]:

import pandas as pd
import matplotlib.animation
import matplotlib.pyplot as plt
import seaborn as sns


# In[70]:

# sns.palplot(sns.color_palette("Set2", 10))
sns.set_palette("Set2", 11)


# In[2]:

char_df = pd.read_csv('crazy.csv')


# In[3]:

del char_df['Unnamed: 0']


# In[36]:

char_df.head()


# In[50]:

char_df.columns


# In[43]:

#remove all columns except original
def delete_new_columns(df, num_char):
    for i in range (len(char_df.columns) - num_char):
        char_df.drop(char_df.columns[[num_char]], axis=1, inplace=True) 


# In[5]:

def get_frame_count(row, charname, window):
    global appear_list
    if (len(appear_list) >= window):
        appear_list.pop(0)
    appear_list.append(row[charname])
    return sum(appear_list)


# In[44]:

def create_avg_column(df, window):
    appear_list = []
    for column in df:
        appear_list = []
        avg_column = "avg_" + column
        df[avg_column] = df.apply(lambda row: get_frame_count(row, column, window), axis = 1)


# In[54]:

delete_new_columns(char_df, 11)


# In[55]:

create_avg_column(char_df, 100)


# In[56]:

char_df.head()


# In[76]:

for column in char_df:
    if ('avg_' in column):
        char_df[column].plot(label=column[4:])


# In[77]:

legend = plt.legend(loc='best')
frame = legend.get_frame()
frame.set_facecolor('0.90')

fig = plt.gcf()
fig.set_size_inches(30, 10)

plt.xlabel('time')
plt.ylabel('appearance in the last 250 frames')
plt.title('Appearance over time')
plt.show()


# In[78]:

fig.savefig('output.png', dpi=100)


# In[79]:

len(char_df)

