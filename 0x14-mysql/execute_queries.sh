#!/bin/bash

# Define the MySQL queries
query_web_01="SHOW GRANTS FOR 'holberton_user'@'localhost';"
query_web_02="SHOW GRANTS FOR 'holberton_user'@'localhost';"

# Execute the queries on web-01
echo "Executing query on web-01:"
ssh ubuntu@3.85.148.16 "mysql -uholberton_user -pprojectcorrection280hbtn -e \"$query_web_01\""

# Execute the queries on web-02
echo "Executing query on web-02:"
ssh ubuntu@54.145.238.177 "mysql -uholberton_user -pprojectcorrection280hbtn -e \"$query_web_02\""

