T = int(input()) ## No.of test cases 
for i in range(T):
    string = input()
    # for index in range(len(string)):
    #     if index % 2 == 0:
    #         print(f"{string[index]}", end ='\n')
    print(f"{string[::2]} {string[1::2]}")
