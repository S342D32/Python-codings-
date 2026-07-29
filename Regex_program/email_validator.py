import re

# Corrected pattern for email validation
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

# Email list
emails = [
    "john.doe@example.com",
    "jane.smith@gmail.com",
    "user123@yahoo.com",
    "mike_brown@outlook.com",
    "sarah.connor@company.org",
    "david+newsletter@domain.co",
    "emily.jones@school.edu",
    "admin@website.net",
    "peter-parker@superhero.io",
    "support.team@helpdesk.com",
    "info@business.biz",
    "james-bond007@spy.agency",
    "contact_us@shop.online",
    "dev.team@project.tech",
    "alice@wonderland.co.uk",
    "bob.builder@tools.us",
    "charlie_chaplin@comedy.in",
    "newsletter@updates.",
    "test_user@testsite.dev",
    "random.email_123@randomdomain.xyz"
]

# Filter emails that match the pattern
filtered_emails = [word for word in emails if not re.match(pattern, word)]

print(filtered_emails)
