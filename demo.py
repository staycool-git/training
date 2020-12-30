import re
info_text = """
Toomas:
    email: akadeemia-toomas@taltech.ee
    phone: 5204 2456
"""
email_pattern = r'' # your pattern here
phone_pattern = r'' # your pattern here

email_match = re.search(email_pattern, info_text)
phone_match = re.search(phone_pattern, info_text)

email = email_match.group() if email_match else "NOT FOUND" # -> "akadeemia-toomas@taltech.ee"
phone = phone_match.group() if phone_match else "NOT FOUND" # -> "5204 2456"

print(email)
print(phone)