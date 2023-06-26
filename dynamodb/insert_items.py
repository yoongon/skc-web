import boto3
def main():
    ddb = boto3.resource('dynamodb',
                         endpoint_url='http://localhost:8000',
                         region_name='dummy',
                         aws_access_key_id='dummy',
                         aws_secret_access_key='dummy')
    table = ddb.Table('Submissions')
    input = {'SubmissionId': '9a0', 'ProblemId': '1', 'User': 'yoon', 'Pass': False, 'Code':'class Solution:\n    def hello(self, a, b):\n        c = a + b\n        return c\n'}
    table.put_item(Item=input)
    print('Successfully put item')
main()
