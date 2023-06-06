import json
import os

def lambda_handler(event, context):
    # print(event)
    # print(context)
    if event == None or len(event) == 0:
        return {
            'statusCode': 200,
            'body': json.dumps(get_handler(event, context))
        }
    if event["httpMethod"] == "POST":
        return post_handler(event, context)

def get_handler(event, context):
    with open('problem.json') as json_file:
        json_data = json.load(json_file)
    return json_data

def post_handler(event, context):
    body = json.loads(event["body"])
    code = body["code"]

    with open("suffix.txt", 'r') as f:
        lines = f.readlines()
    suffix = ''.join(lines)

    code += suffix

    with open("/tmp/output.py", "w") as f:
        f.write(code)

    cmd = 'python3 /tmp/output.py'
    run_process = os.popen(cmd)
    results_string = run_process.read().replace("\'", "\"")
    run_process.close()
    results = json.loads(results_string)

    for result in results:
        input = result['input']
        solution = hello(input[0], input[1])
        result['solution_output'] = solution
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }

def hello(a, b):
    c = a + b
    return c
