#1.pass: neglect expected indentation error
# for i in range(1,10):
#     pass


#2.break:for terminating the loop
# for i in range(1,10):
#     if(i == 4):
#         break
#     print(i)

#3.continue: To stop perticular iteration
# for i in range(1,10):
#     if(i == 4):
#         continue
#     print(i)

#4.else: Will execute when the loop executed sucessfully.
for i in range(1, 10):
    if(i == 4):
        continue
#        break
    print(i)
else:
    print('Else block executed')