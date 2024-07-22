import re
text = "Hello, my email is akash@gmail.com. Please contact me."
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
match = re.search(email_pattern, text)
if match:
    print(f"Found email: {match.group()}")
else:
    print("No email found.")
matches = re.findall(email_pattern, text)
print(f"All matches: {matches}")
replaced_text = re.sub(email_pattern, '[REDACTED]', text)
print(f"Replaced text: {replaced_text}")
if match:
    start, end = match.span()
    print(f"Email starts at index {start} and ends at index {end}")
