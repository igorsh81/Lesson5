from functools import reduce
import json

result_data_list = list()
dict_profit = dict()
dict_lesion = dict()
dict_average_profit = dict()

with open("file_7.txt", "r") as file:
    for line in file:
        firm = line.strip().split("   ")
        firm_dict = {firm[0]: int(firm[2]) - int(firm[3])}
        if firm_dict[firm[0]] >= 0:
            dict_profit[firm[0]] = firm_dict[firm[0]]
        else:
            dict_lesion[firm[0]] = firm_dict[firm[0]]

    dict_average_profit["average_profit"] = reduce(lambda a, b: a + b, list(dict_profit.values())) / len(dict_profit)

result_data_list.append(dict_profit)
result_data_list.append(dict_average_profit)
result_data_list.append(dict_lesion)
print(result_data_list)

with open("firms_data_report.json", "w") as write_f:
    json.dump(result_data_list, write_f)
