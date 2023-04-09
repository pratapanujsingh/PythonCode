# Jumping Statements

# break , continue

for i in range (1, 11):
    if i==5:
        break
    print(i)
print("break !!!!")

# continue
for i in range (1, 6):
    if i==4:
        continue
    print(i)
print("continue !!!!")

# continue
for i in range (1, 8):
    if i==4 or i==2 or i== 6:
        continue
    print(i)