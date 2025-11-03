WITH exploded AS (
  SELECT
    event_timestamp,
    JSON_EXTRACT_ARRAY(event_params, '$.event_params') as params
  FROM
    crystalloids-candidates.andrea_monforte_dataset.ga4_data
),
flattened AS (
  SELECT
    event_timestamp,
    JSON_EXTRACT_SCALAR(param, '$.key') AS paramKey,
    SAFE_CAST(JSON_EXTRACT_SCALAR(param, '$.value.int_value') AS INT64) AS int_value
  FROM
    exploded, UNNEST(params) AS param
)
SELECT
  AVG(int_value) / 1000 AS average_engagement_time_sec
  FROM
    flattened
  WHERE paramKey = 'engagement_time_msec' AND int_value IS NOT NULL