# Data Available in this DataFrame:
df = data.copy()

# your code here
df['text1'] = df['text'].str.lower()
df['text1'] = df['text1'].str.replace(" ","")
df['text2'] = df['text1'].str[::-1]
df['is_palindrome'] = (df['text1'] == df['text2']).astype(bool)
# return the DataFrame
#df

result = df[['text','is_palindrome']]