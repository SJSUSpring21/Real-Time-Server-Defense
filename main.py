import boto3
import predict

s3client = boto3.client(
    's3',
    region_name='us-east-1'
)

bucket_name = 'real-server-defense'
file_to_read = 'kddcup.data.corrected'

#Create a file object using the bucket and object key. 
fileobj = s3client.get_object(
    Bucket=bucket_name,
    Key=file_to_read
    )

# open the file object and read it into the variable filedata. 
filedata = fileobj['Body'].read()

# file data will be a binary stream.  We have to decode it 
contents = filedata.decode('utf-8') 

result = predict.predictResult(contents)
result_file = open("result.txt", "w")
result_file.write(result)

# NEED TO PASS 'line' TO MODEL
'''for line in contents.splitlines():
    result = predictResult(line)'''
