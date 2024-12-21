# CREATING AND ACCESSING DICTIONARY.

students_scores = {"SHAHID": 85, "TAHIR": 90, "VISHNU": 78}

print(students_scores["TAHIR"]) 


# USING DICTIONARY METHOD .

this_dict = {}

# Add key-value pairs
this_dict["SHAHID"] = 85
this_dict["TAHIR"] = 90
this_dict["VISHNU"] = 78

# Update a score
this_dict["SHAHID"] = 88

# Remove a student
this_dict.pop("VISHNU")

# Use get() method
print(this_dict.get("TAHIR"))


# COUNT OF OCCURRANCES OF EACH CHARACTER IN A GIVEN STRING.

string=input("Enter a String:")
char_count={}

for i in string:
    if i in char_count:
        char_count[i]+=1
    else:
        char_count[i]=1
print(char_count)
