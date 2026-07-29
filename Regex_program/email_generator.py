import random
import string 

def email_generator():
  user_name = ''.join(random.choices(string.ascii_letters + string.digits + "_-.%",k=random.randint(5,10)))
  domain = ''.join(random.choices(string.ascii_letters + string.digits,k = random.randint(3,5)))

  tls = random.choice(['com','net','co','in','ashis','gov'])

  return f"{user_name}@{domain}.{tls}"

emails = [email_generator() for i in range(10)]

for i,email in enumerate(emails,1):
  print (f"{i}:{email}")

