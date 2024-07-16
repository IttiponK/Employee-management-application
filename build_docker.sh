docker build -t employee-management-application .
docker tag employee-management-application:latest {{YOUR_ACCOUNT_ID}}.dkr.ecr.ap-southeast-1.amazonaws.com/employee-management-application:$1