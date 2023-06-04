import json
import os


def hello(a, b):
    c = a + b
    return c

def lambda_handler(event, context):
    # with open("1-user-code-input.txt", 'r') as f:
    #     lines = f.readlines()
    # code = ''.join(lines)
    code = event["body"]["key1"]
    # print (event)

    with open("1-suffix.txt", 'r') as f:
        lines = f.readlines()
    suffix = ''.join(lines)

    code += suffix

    with open("/tmp/output.py", "w") as f:
        f.write(code)

    cmd = 'python3 /tmp/output.py'
    results_string = os.popen(cmd).read().replace("\'", "\"")
    results = json.loads(results_string)

    for result in results:
        input = result['input']
        solution = hello(input[0], input[1])
        result['solution_output'] = solution
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }


# res = lambda_handler(None, None)
