import os
if os.path.exists('env.py'):
    print('.env file found')
else:
    print('.env file not found')