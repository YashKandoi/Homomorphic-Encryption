i=0
j=4
size=2
str_con=""
for row in range(i, i+size):
      for column in range(j, j+size):
          num_str="0"+str(row)
          print(num_str)
          str_con=str_con+num_str
          print(row," ",column)
print(str_con)
# for row in range(2,6):
#     print(row)