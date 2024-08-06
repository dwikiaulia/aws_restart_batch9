# import os

# os.system("ls")

import subprocess

subprocess.run(["ls", "-l", "README.md"])

command1="uname"
commandArgument1="-a"
print(f'Gathering system information with command: {command1} {commandArgument1}')
subprocess.run([command1,commandArgument1])

command2 = 'ps'
commandArgument2 = '-x'
print(f'Gathering active process information with command: {command2} {commandArgument2}')
subprocess.run([command2,commandArgument2])
