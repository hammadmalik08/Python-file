print("hello would")

count = 0
while count < 5:
    print("count:", count)
    count += 1


    for num in range(20):
        if num == 11:
            break
        print(num)


        for num in range(5):
            continue
        print(num)

        for num in range(5):
            pass