with open("data/returns_var_names.csv", "r") as file:
    lines = [line.rstrip() for line in file]
    lines = lines[1:]
    print(len(lines))
    converted = ["permno INTEGER",
                 "date DATE"]
    names = []
    for line in lines:
        line_arr = line.split(",")
        name, type = line_arr[0].lower(), line_arr[1]
        if type == "Char":
            converted_type = "VARCHAR(256)"
        elif type == "Float":
            converted_type = "NUMERIC(20,4)"
        elif type == "Date":
            converted_type = "DATE"
        else:
            print(type)
            assert False
        names.append(name)
        converted.append(name + " " + converted_type)
        converted = list(set(converted))
    with open("converted_returns.txt", "w") as output:
        output.write(",\n".join(converted))

with open("data/returns/b6ymnoif3ejkm1za.csv", "r") as file:
    lines = [line.rstrip() for line in file]
    real_names = lines[0].split(",")
    real_names = [name.lower() for name in real_names]
    print(real_names)
    for n in real_names:
        if n not in names:
            print(n)
    print("-" * 50)
    for n in names:
        if n not in real_names:
            print(n)
