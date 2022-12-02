import re

line = input("Enter cmommand: ")

if '.' in line:
    cls, cmd = line.split('.')
    cmd = cmd.split('(')[0]

    # Gets the arg inside bracket
    cmd_args = line.split('(')[1]
    if '{' not in cmd_args:
        cmd_args = cmd_args.split(', ')
        for idx, arg in enumerate(cmd_args):
            cmd_args[idx] = arg.strip(')')
            if len(cmd_args) == 0:
                line = f"{cmd} {cls}"
            elif len(cmd_args) >= 1:
                id = cmd_args[0]
                if len(cmd_args) == 1:
                    line = f"{cmd} {cls} {id}"
                elif len(cmd_args) == 2:
                    attr_name = cmd_args[1]
                    line = f"{cmd} {cls} {id} {attr_name}"
                elif len(cmd_args) == 3:
                    attr_name = cmd_args[1]
                    attr_value = cmd_args[2]
                    line = f"{cmd} {cls} {id} {attr_name} {attr_value}"
    elif '{' in cmd_args:
        cmd_args = list(re.findall(r'(["\'].+["\']), (\{.*\})', cmd_args)[0])
        dict_args = cmd_args[1]
        id = cmd_args[0]
        line = f"{cmd} {cls} {id} {dict_args}"

print(line)
