# Author: Soufyane yassin
# in order to use this program correctly, try to copy the text where you wanna find the respective emails and phone numbers
import re

# first step: writing the phone number regex
phone_reg = re.compile(r'''(
         (\d{3}|\(\d{3}\))? # Area Code
         (-|\s|\.)? # Separator
         (\d{3})  # First three digits
         (-|\.|\s) # Separator
         (\d{4})   # Last four digits
         (\s*(ext|x|ext\.)\s*(\d{2,5}))? # extension                   
)''', re.VERBOSE)
