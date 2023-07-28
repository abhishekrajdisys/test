import os

def get_credentials():
  if 'CI' in os.environ:
    db_username = os.environ.get('USERNAME')
  else:
    db_username = 'your_local_username'
  print(db_username)
get_credentials()
