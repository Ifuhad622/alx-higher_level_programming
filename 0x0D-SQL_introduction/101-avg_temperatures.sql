-- Query to display the average temperature by city ordered by temperature in MySQL server
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
