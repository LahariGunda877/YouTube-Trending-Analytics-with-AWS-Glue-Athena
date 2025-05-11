import boto3

def upload_file_to_s3():
    local_path = "data/USvideos.csv"               # ✅ CSV file on your system
    bucket_name = "lahariyoutubeetl2000"           # ✅ Your S3 bucket name
    s3_path = "youtube/USvideos.csv"               # ✅ Where to store in S3

    s3 = boto3.client('s3')
    s3.upload_file(local_path, bucket_name, s3_path)
    print(f"✅ Uploaded {local_path} to s3://{bucket_name}/{s3_path}")

if __name__ == "__main__":
    upload_file_to_s3()
