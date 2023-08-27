import utils
import settings

operations_list = utils.load_file(settings.DATA_FILE)

operations_list = utils.get_executed_operations(operations_list)

operations_list = utils.sorted_result_list(operations_list)

operations_list = operations_list[:5]

for x in operations_list:
    print(f"{utils.date_to_str(x)} {x['description']}\n"
          f"{utils.operation_details(x.get('from', None))} > {utils.operation_details(x['to'])}\n"
          f"{x ['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")