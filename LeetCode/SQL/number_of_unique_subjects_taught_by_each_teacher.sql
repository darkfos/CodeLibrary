-- Write your PostgreSQL query statement below
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt FROM Teacher AS tch GROUP BY teacher_id;
