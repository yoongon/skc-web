import boto3
def main():
    # 1 - Create Client
    ddb = boto3.resource('dynamodb',
                         endpoint_url='http://localhost:8000',
                         region_name='dummy',
                         aws_access_key_id='dummy',
                         aws_secret_access_key='dummy')
    # 2 - Create the Table
    ddb.create_table(TableName='Submissions',
                     AttributeDefinitions=[
                         {
                             'AttributeName': 'SubmissionId',
                             'AttributeType': 'S'
                         }
                     ],
                     KeySchema=[
                         {
                             'AttributeName': 'SubmissionId',
                             'KeyType': 'HASH'
                         }
                     ],
                     ProvisionedThroughput= {
                         'ReadCapacityUnits': 10,
                         'WriteCapacityUnits': 10
                     }
                     )

main()
