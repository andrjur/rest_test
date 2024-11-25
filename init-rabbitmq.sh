#!/bin/bash
# wait for RabbitMQ to start
sleep 18

# Create a new user
rabbitmqctl add_user john qq23

# Set permissions for the new user
rabbitmqctl set_permissions -p / john ".*" ".*" ".*"

# Optionally, set the user as an administrator
rabbitmqctl set_user_tags john administrator