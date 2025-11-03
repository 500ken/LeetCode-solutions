-- 175. Combine Two Tables
-- Difficulty: Medium
-- Tags: SQL
-- Link: https://leetcode.com/problems/combine-two-tables/

-- Description:
-- Write a SQL query to report the first name, last name, and city of each person in the Person table.
-- Include all people even if they don't have an address.

-- Solution:
SELECT p.FirstName, p.LastName, a.City
FROM Person p
LEFT JOIN Address a
ON p.PersonId = a.PersonId;
