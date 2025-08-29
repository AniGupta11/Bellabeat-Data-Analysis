-- avg_steps_per_user

            SELECT Id, AVG(TotalSteps) AS avg_steps
            FROM bellabeat
            GROUP BY Id;
        

-- avg_sleep_per_user

            SELECT Id, AVG(TotalMinutesAsleep) AS avg_sleep_minutes
            FROM bellabeat
            GROUP BY Id;
        

-- avg_calories_by_weekday

            SELECT strftime('%w', activity_date) AS weekday,
                   AVG(Calories) AS avg_calories
            FROM bellabeat
            GROUP BY weekday;
        

-- top_active_users

            SELECT Id, SUM(TotalSteps) AS total_steps
            FROM bellabeat
            GROUP BY Id
            ORDER BY total_steps DESC
            LIMIT 5;
        

-- sleep_vs_calories

            SELECT AVG(TotalMinutesAsleep) AS avg_sleep,
                   AVG(Calories) AS avg_calories
            FROM bellabeat
            GROUP BY Id;
        

