SELECT
  COUNT(*) / COUNT(DISTINCT user_pseudo_id) AS avg_events_per_user
FROM
  crystalloids-candidates.andrea_monforte_dataset.ga4_data