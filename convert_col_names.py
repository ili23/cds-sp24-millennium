with open("data/quarterly_var_names.csv", "r") as file:
    lines = [line.rstrip() for line in file]
    lines = lines[1:]
    print(len(lines))
    converted = ["gvkey VARCHAR(256)",
                 "datadate DATE",
                 "indfmt VARCHAR(256)",
                 "consol VARCHAR(256)",
                 "popsrc VARCHAR(256)",
                 "datafmt VARCHAR(256)",
                 "curcdq VARCHAR(256)",
                 "costat VARCHAR(256)"]
    names = []
    for line in lines:
        line_arr = line.split(",")
        # if len(line_arr) != 3:
            # print(line)
            # assert False
        name, type = line_arr[0].lower(), line_arr[1]
        if type == "Char":
            if name == "busdesc":  # Business description, can be longer than 256 chars
                converted_type = "VARCHAR(2048)"
            else:
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
    with open("converted.txt", "w") as output:
        output.write(",\n".join(converted))

with open("data/quarterly_fundamentals.csv", "r") as file:
    lines = [line.rstrip() for line in file]
    real_names = lines[0].split(",")
    print(real_names)
    for n in real_names:
        if n not in names:
            print(n)
    print("-" * 50)
    for n in names:
        if n not in real_names:
            print(n)