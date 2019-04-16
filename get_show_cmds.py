import re
with open ('raw_data.txt') as f:
    show_cmds = re.findall('\S+\\.textfsm', f.read())
print(len(show_cmds))
with open('mined_data.txt', 'w') as f1:
    f1.write('\n'.join(show_cmds))
