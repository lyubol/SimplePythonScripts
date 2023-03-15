def flatten(df):
  # compute Complex Fields (Lists and Structs) in Schema   
  complex_fields = dict([(field.name, field.dataType) for field in df.schema.fields if type(field.dataType) == ArrayType or type(field.dataType) == StructType])
  
  while len(complex_fields)!=0:
    col_name=list(complex_fields.keys())[0]
    print ("Processing :"+col_name+" Type : "+str(type(complex_fields[col_name])))
    
    # if StructType then convert all sub elements to columns.
    # i.e. flatten structs
    if (type(complex_fields[col_name]) == StructType):
      expanded = [col(col_name+'.'+k).alias(col_name+'_'+k) for k in [ n.name for n in  complex_fields[col_name]]]
      df=df.select("*", *expanded).drop(col_name)
      
    # if ArrayType then add the Array Elements as Rows using the explode_outer function
    # i.e. explode Arrays
    elif (type(complex_fields[col_name]) == ArrayType):    
      df=df.withColumn(col_name,explode_outer(col_name))
    
    complex_fields = dict([(field.name, field.dataType) for field in df.schema.fields if type(field.dataType) == ArrayType or  type(field.dataType) == StructType])
  return df


rawDf = flatten(rawDf)