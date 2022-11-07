# def process_result(operation_type, x, y):
#     if operation_type == 'addition':
#       calc_result = x + y
#     elif operation_type == 'subtraction':
#       calc_result = x + y
#     elif operation_type == 'multiplication':
#       calc_result = x * y
#     else:
#       return 'Invalid operator'
#     result = {
#                 "slackUsername": "solomonuche42",
#                 "operation_type": operation_type,
#                 "result": calc_result,
#             }
#     return result
    
def process_result(operation_type, x, y):
    allowed_operations = {
      'addition': x+y,
      'multiplication':x*y,
      'subtraction':x-y
    }
    try:
        result = {
                  "slackUsername": "solomonuche42",
                  "operation_type": operation_type,
                  "result": allowed_operations[operation_type],
              }
        return result
    except:
      return 'invalid operator'
      
    
    
# print(process_result('addition', 5, 4))