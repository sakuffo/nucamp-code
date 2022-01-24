provinces = ["Ontario", "British Columbia", "Quebec"]
'''
print(provinces[-1])
print(provinces[-2])
print(provinces[-3])
'''

provinces[2] = "Newfoundland and Labrador"
# print(provinces)
# print(len(provinces))

provinces.append("Prince Edward Island")
print(provinces)
provinces.pop()
print(provinces)
provinces.pop(1)
