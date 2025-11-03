WITH exploded AS (
  SELECT
    event_timestamp,
    JSON_EXTRACT_ARRAY(event_params, '$.event_params') AS params
  FROM crystalloids-candidates.andrea_monforte_dataset.ga4_data
),
flattened AS (
  SELECT
    event_timestamp,
    JSON_EXTRACT_SCALAR(param, '$.key') AS paramKey,
    JSON_EXTRACT_SCALAR(param, '$.value.string_value') AS string_value,
    JSON_EXTRACT_SCALAR(param, '$.value.int_value') AS int_value
  FROM exploded, UNNEST(params) AS param
),
pivoted AS (
  SELECT
    event_timestamp,
    MAX(CASE WHEN paramKey = 'session_engaged' THEN string_value END) AS session_engaged,
    MAX(CASE WHEN paramKey = 'ga_session_id' THEN int_value END) AS ga_session_id
  FROM flattened
  GROUP BY event_timestamp
)
SELECT
  COUNT(DISTINCT ga_session_id) AS engaged_sessions
FROM pivoted
WHERE session_engaged = '1'