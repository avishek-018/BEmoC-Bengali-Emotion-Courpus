

def remove_duplicate(dataframe,column_name):
  '''
  This is the module which remove the duplicate value from datframe

  Aurguments:
  dataframe -> The frame in which duplicate needs to be removed
  column_name -> The columns name which action needs to occur

  Return value:
  final_df -> Dataframe after removing the duplicates
  '''  
  final_df = df.drop_duplicates(subset=column_name)
  return final_df
