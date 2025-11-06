#public for assignment convenience purposes

from google.cloud import bigquery

BUCKET_NAME = "platform_assignment_bucket"

BUCKET_REGION = "europe_west4"

FILE_NAME = "ga4_public_dataset.csv"

BQ_DATASET = "andrea_monforte_dataset"

BQ_TABLE = "ga4_data"

GCP_PROJECT = "crystalloids-candidates"

FUNCTION1_URL = "https://andrea-monforte-load-csv-to-bq-xqb44gplaa-ez.a.run.app/"

table_schema = [
    bigquery.SchemaField("event_date", "STRING"),
    bigquery.SchemaField("event_timestamp", "INT64"),
    bigquery.SchemaField("event_name", "STRING"),
    bigquery.SchemaField(
        "event_params", "RECORD", mode="REPEATED", fields=[
            bigquery.SchemaField("key", "STRING"),
            bigquery.SchemaField(
                "value", "RECORD", fields=[
                    bigquery.SchemaField("string_value", "STRING"),
                    bigquery.SchemaField("int_value", "INT64"),
                    bigquery.SchemaField("float_value", "FLOAT64"),
                    bigquery.SchemaField("double_value", "FLOAT64"),
                ]
            ),
        ]
    ),
    bigquery.SchemaField("event_previous_timestamp", "INT64"),
    bigquery.SchemaField("event_value_in_usd", "FLOAT64"),
    bigquery.SchemaField("event_bundle_sequence_id", "INT64"),
    bigquery.SchemaField("event_server_timestamp_offset", "INT64"),
    bigquery.SchemaField("user_id", "STRING"),
    bigquery.SchemaField("user_pseudo_id", "STRING"),
    bigquery.SchemaField(
        "privacy_info", "RECORD", fields=[
            bigquery.SchemaField("analytics_storage", "INT64"),
            bigquery.SchemaField("ads_storage", "INT64"),
            bigquery.SchemaField("uses_transient_token", "STRING"),
        ]
    ),
    bigquery.SchemaField("user_first_touch_timestamp", "INT64"),
    bigquery.SchemaField(
        "user_ltv", "RECORD", fields=[
            bigquery.SchemaField("revenue", "FLOAT64"),
            bigquery.SchemaField("currency", "STRING"),
        ]
    ),
    bigquery.SchemaField(
        "device", "RECORD", fields=[
            bigquery.SchemaField("category", "STRING"),
            bigquery.SchemaField("mobile_brand_name", "STRING"),
            bigquery.SchemaField("mobile_model_name", "STRING"),
            bigquery.SchemaField("mobile_marketing_name", "STRING"),
            bigquery.SchemaField("mobile_os_hardware_model", "INT64"),
            bigquery.SchemaField("operating_system", "STRING"),
            bigquery.SchemaField("operating_system_version", "STRING"),
            bigquery.SchemaField("vendor_id", "INT64"),
            bigquery.SchemaField("advertising_id", "INT64"),
            bigquery.SchemaField("language", "STRING"),
            bigquery.SchemaField("is_limited_ad_tracking", "STRING"),
            bigquery.SchemaField("time_zone_offset_seconds", "INT64"),
            bigquery.SchemaField(
                "web_info", "RECORD", fields=[
                    bigquery.SchemaField("browser", "STRING"),
                    bigquery.SchemaField("browser_version", "STRING"),
                ]
            ),
        ]
    ),
    bigquery.SchemaField(
        "geo", "RECORD", fields=[
            bigquery.SchemaField("continent", "STRING"),
            bigquery.SchemaField("sub_continent", "STRING"),
            bigquery.SchemaField("country", "STRING"),
            bigquery.SchemaField("region", "STRING"),
            bigquery.SchemaField("city", "STRING"),
            bigquery.SchemaField("metro", "STRING"),
        ]
    ),
    bigquery.SchemaField("app_info", "RECORD", fields=[
        bigquery.SchemaField("id", "STRING"),
        bigquery.SchemaField("versions", "STRING"),
        bigquery.SchemaField("install_store", "STRING"),
        bigquery.SchemaField("firebase_app_id", "STRING"),
        bigquery.SchemaField("install_source", "STRING")
    ]),
    bigquery.SchemaField(
        "traffic_source", "RECORD", fields=[
            bigquery.SchemaField("medium", "STRING"),
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("source", "STRING"),
        ]
    ),
    bigquery.SchemaField("stream_id", "INT64"),
    bigquery.SchemaField("platform", "STRING"),
    bigquery.SchemaField("event_dimensions", "RECORD", fields=[
        bigquery.SchemaField("hostname", "STRING")
    ]),
    bigquery.SchemaField(
        "ecommerce", "RECORD", fields=[
            bigquery.SchemaField("total_item_quantity", "INT64"),
            bigquery.SchemaField("purchase_revenue_in_usd", "FLOAT64"),
            bigquery.SchemaField("purchase_revenue", "FLOAT64"),
            bigquery.SchemaField("refund_value_in_usd", "FLOAT64"),
            bigquery.SchemaField("refund_value", "FLOAT64"),
            bigquery.SchemaField("shipping_value_in_usd", "FLOAT64"),
            bigquery.SchemaField("shipping_value", "FLOAT64"),
            bigquery.SchemaField("tax_value_in_usd", "FLOAT64"),
            bigquery.SchemaField("tax_value", "FLOAT64"),
            bigquery.SchemaField("unique_items", "INT64"),
            bigquery.SchemaField("transaction_id", "STRING"),
        ]
    ),
    bigquery.SchemaField(
        "items", "RECORD", mode="REPEATED", fields=[
            bigquery.SchemaField("item_id", "STRING"),
            bigquery.SchemaField("item_name", "STRING"),
            bigquery.SchemaField("item_brand", "STRING"),
            bigquery.SchemaField("item_variant", "STRING"),
            bigquery.SchemaField("item_category", "STRING"),
            bigquery.SchemaField("item_category2", "STRING"),
            bigquery.SchemaField("item_category3", "STRING"),
            bigquery.SchemaField("item_category4", "STRING"),
            bigquery.SchemaField("item_category5", "STRING"),
            bigquery.SchemaField("price_in_usd", "FLOAT64"),
            bigquery.SchemaField("price", "FLOAT64"),
            bigquery.SchemaField("quantity", "INT64"),
            bigquery.SchemaField("item_revenue_in_usd", "FLOAT64"),
            bigquery.SchemaField("item_revenue", "FLOAT64"),
            bigquery.SchemaField("item_refund_in_usd", "FLOAT64"),
            bigquery.SchemaField("item_refund", "FLOAT64"),
            bigquery.SchemaField("coupon", "STRING"),
            bigquery.SchemaField("affiliation", "STRING"),
            bigquery.SchemaField("location_id", "STRING"),
            bigquery.SchemaField("item_list_id", "STRING"),
            bigquery.SchemaField("item_list_name", "STRING"),
            bigquery.SchemaField("item_list_index", "STRING"),
            bigquery.SchemaField("promotion_id", "STRING"),
            bigquery.SchemaField("promotion_name", "STRING"),
            bigquery.SchemaField("creative_name", "STRING"),
            bigquery.SchemaField("creative_slot", "STRING"),
        ]
    ),
]
