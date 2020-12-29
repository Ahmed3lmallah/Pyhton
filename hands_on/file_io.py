# Quick Tutorial for reading, writing, and appending to files
# Some Initial Data
logs = ('First log', 'Second log', 'Third log')

# Using 'with' and open to read
with open('monitored.txt', 'r') as f:  # 'r' indicates 'read' mode
    for line in f:  # loops through each line
        print(line, end='')  # prints each line / end='' prevents printing \n after each line

# Using 'with' and open to write
# Existing file will be overwritten
with open('new_file.txt', 'w') as f:  # 'w' indicates 'write' mode
    for log in logs:  # loops through all logs
        f.write(log)  # writes each log to the file
        f.write('\n')  # goes to next line

# Using 'with' and open to append
with open('monitored.txt', 'a') as f:  # 'a' indicates 'Append' mode
    f.write(f'This is a new line\n')  # Appends a new line to file
