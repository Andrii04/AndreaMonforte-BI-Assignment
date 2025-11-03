WITH exploded AS (
  SELECT 
    JSON_EXTRACT_ARRAY(event_params, '$.event_params') AS params
  FROM
    crystalloids-candidates.andrea_monforte_dataset.ga4_data
),
flattened AS (
  SELECT 
    JSON_EXTRACT_SCALAR(param, '$.key') AS key,
    JSON_EXTRACT_SCALAR(param, '$.value.string_value') AS string_value
  FROM
    exploded,
    UNNEST(params) as param
)
SELECT
  string_value as page_title,
  COUNT(*) AS page_views
FROM
  flattened
WHERE
  key = 'page_title'
GROUP BY
  page_title
ORDER BY
  page_views DESC