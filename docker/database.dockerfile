# Use the official PostgreSQL image as the base image
FROM postgres:14

# Set the environment variables for PostgreSQL
ENV POSTGRES_DB wiznotes
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres

# Copy the SQL script to initialize the database
# COPY ./docker/initializers/init.sql /docker-entrypoint-initdb.d/