import subprocess

for i in range(12, 22):
    find_str = f'find . -type f -name "{i}.*"'

    file_str = subprocess.run(
        find_str, shell=True, capture_output=True, text=True
    ).stdout

    final_command = f'nvim "{file_str.strip()}"'

    print("Final command:", final_command)

    inp = input("Open file Y/n: ").lower().strip()

    if inp == "n":
        break
    subprocess.run([final_command], shell=True)

a = (1, 2, 3)
b = [4, 5, 6]
c = {7, 8, 9}

d = (1, [2, 3, (6, 7, {8, 9})], {4, 5}, )
