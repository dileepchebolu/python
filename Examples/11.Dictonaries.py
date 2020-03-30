monthConversions = {
     "Jan": "January",
     "Feb": "February",
     "Mar": "March",
     "Apr": "April",
     "May": "May",
     "Jun": "June",
     "Jul": "july",
     "Aug": "August",
     "Sep": "September",
     "Oct": "October",
     "Nov": "November",
     "Dec": "December",
      }

print(monthConversions["Oct"])  ## one way of geting the values 
print(monthConversions.get("Oct"))  ## second way of getting values from dictonary values 

print(monthConversions.items()

## Note: If no valid key value is matched, then will return "None" output.

## we can configure the default value, if mentioned key is not found in the dictionary list.

print(monthConversions.get("oct","No selected key in the provided dictionary list"))

## In above dictionary list, there is no key with the name of "oct", so it will print "No selected key in the provided dictionary list"


# ====================================================
# Output:
# October
# October
# dict_items([('Jan', 'January'), ('Feb', 'February'), ('Mar', 'March'), ('Apr', 'April'), ('May', 'May'), ('Jun', 'June'), ('Jul', 'july'), ('Aug', 'August'), ('Sep', 'September'), ('Oct', 'October'), ('Nov', 'November'), ('Dec', 'December')])
# No selected key in the provided dictionary list
# =====================================================