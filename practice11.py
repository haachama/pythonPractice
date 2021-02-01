import pandas as pd

# 題目: 
# 將以下問卷資料的職業(Profession)欄位缺失值填入字串'others'，更進一步將字串做編碼。 此時用什麼方式做編碼比較適合?為什麼?

q_df = pd.DataFrame([['male', 'teacher'], ['male', 'engineer'], ['female', None], ['female', 'engineer']],columns=['Sex','Profession'])

q_df = q_df.fillna('others')

a = pd.get_dummies(q_df[['Profession']])
q_df = pd.concat([q_df, a], axis=1)

print(q_df)