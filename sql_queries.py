# Вывести топ 5 самых коротких по длительности перелетов.
# Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
	SELECT flight_no, (scheduled_arrival - scheduled_departure) as Duration
 	FROM flights
	ORDER BY duration 
	LIMIT 5;
"""
#  flight_no | duration
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
	SELECT flight_no, count(flight_no) as count 
	FROM flights
	GROUP BY flight_no 
	HAVING count(flight_no ) < 50
	ORDER BY count(flight_no) DESC LIMIT 3;

"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """
SELECT 
    (SELECT COUNT(*) FROM flights AS f_inner
     JOIN airports_data AS dep_inner ON f_inner.departure_airport = dep_inner.airport_code) 
    -
    (SELECT COUNT(*) FROM flights AS f_outer
     JOIN airports_data AS dep_outer ON f_outer.departure_airport = dep_outer.airport_code
     JOIN airports_data AS arr_outer ON f_outer.arrival_airport = arr_outer.airport_code
     WHERE dep_outer.timezone <> arr_outer.timezone) AS count;
"""
#  count
# --------
#  16824