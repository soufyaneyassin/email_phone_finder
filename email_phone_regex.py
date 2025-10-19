# Author: Soufyane yassin
# in order to use this program correctly, try to copy the text where you wanna find the respective emails and phone numbers
import re
import pyperclip
# first step: writing the phone number regex
phone_reg = re.compile(r'''(
         (\d{3}|\(\d{3}\))? # Area Code
         (-|\s|\.)? # Separator
         (\d{3})  # First three digits
         (-|\.|\s) # Separator
         (\d{4})   # Last four digits
         (\s*(ext|x|ext\.)\s*(\d{2,5}))? # extension                   
)''', re.VERBOSE)

# second step is to write the email regex expressions
email_reg = re.compile(r'''(
                  [a-zA-Z0-9._%+-]+ # username
                   @        # @ symbol
                  [a-zA-z0-9.-]+ # domain name
                  \.[a-zA-Z]{2,4}
                       )''', re.VERBOSE)

# lets get the text from the clipboard

text = str(pyperclip.paste())
matches = []
for groups in phone_reg.findall(text):
    # phone = '-'.join([groups[1], groups[3], groups[5]])
    # if groups[6] != "":
    #     phone += " x" + groups[6]
    matches.append(groups[0])

for groups in email_reg.findall(text):
    matches.append(groups)

# copy back the matches to the clipboard
if len(matches) > 0:
    pyperclip .copy('\n' .join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')