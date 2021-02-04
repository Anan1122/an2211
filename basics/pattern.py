number=[5,2,5,2,2]
for x_count in number:
    for count in range(x_count):
     print(count)

    output=""
    for count in range(x_count):
        output+='x'
    print(output)
