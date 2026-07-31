SELECT
    query_name,
    ROUND(AVG(rating::NUMERIC / position), 2) AS quality,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE rating < 3) / COUNT(*),
        2
    ) AS poor_query_percentage
FROM Queries
GROUP BY query_name;