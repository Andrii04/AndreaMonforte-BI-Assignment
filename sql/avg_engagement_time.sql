WITH flattened AS (
  SELECT
    event_timestamp,
    param.key AS paramKey,
    SAFE_CAST(param.value.int_value AS INT64) AS int_value
  FROM
    `crystalloids-candidates.andrea_monforte_dataset.ga4_data`,
    UNNEST(event_params) AS param
)
SELECT
  AVG(int_value) / 1000 AS average_engagement_time_sec
FROM
  flattened
WHERE
  paramKey = 'engagement_time_msec'
  AND int_value IS NOT NULL;
