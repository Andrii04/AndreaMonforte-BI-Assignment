from google.cloud import storage, bigquery
from datetime import datetime
from config import BUCKET_NAME, FILE_NAME, GCP_PROJECT, BQ_DATASET, BQ_TABLE


def manage_bucket_files():
    
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blobs = list(bucket.list_blobs())

    if blobs == []:
        print("bucket is empty")
        return

    print(f"files found in bucket {BUCKET_NAME}:\n")
    for blob in blobs:
        print(f"{blob.name} - last modified: {blob.updated}\n")

    last_updated = max(blob.updated for blob in blobs)
    print(f"last bucket update: {last_updated.strftime('%Y-%m-%d %H:%M:%S')}\n")


def load_csv_to_bigquery():
    storage_client = storage.Client()
    bq_client = bigquery.Client()
    uri = f"gs://{BUCKET_NAME}/{FILE_NAME}"

    job_config = bigquery.LoadJobConfig(
        source_format = bigquery.SourceFormat.CSV,
        skip_leading_rows = 1,
        autodetect = True
    )

    table_id = f"{GCP_PROJECT}.{BQ_DATASET}.{BQ_TABLE}"

    print(f"loading file {FILE_NAME} in BigQuery...\n")
    load_job = bq_client.load_table_from_uri(
        uri,
        table_id,
        job_config = job_config
    )

    load_job.result()
    print(f"file successfuly loaded into table: {table_id}\n")

    table = bq_client.get_table(table_id)
    print(f"table schema: {[schema.name for schema in table.schema]}\n")
    print(f"num of rows loaded: {table.num_rows}\n")
    return


def main(event=None, context=None):
    print("Starting Function")
    manage_bucket_files()
    load_csv_to_bigquery()


if __name__ == "__main__":
    main()
