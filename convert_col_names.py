with open("data/quarterly_var_names.csv", "r") as file:
    lines = [line.rstrip() for line in file]
    lines = lines[1:]
    converted = ["gvkey VARCHAR(256)", "datadate DATE"]
    for line in lines:
        line_arr = line.split(",")
        # if len(line_arr) != 3:
            # print(line)
            # assert False
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
        converted.append(name + " " + converted_type + ",")
    with open("converted.txt", "w") as output:
        output.write("\n".join(converted))
