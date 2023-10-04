# Use the Liquibase base image
FROM liquibase/liquibase:4.23.2

# Copy your entry point script into the image
COPY docker-entrypoint.sh /liquibase/docker-entrypoint.sh

# Make the entry point script executable
RUN chmod +x /liquibase/docker-entrypoint.sh

# Set the entry point for the image
ENTRYPOINT ["/liquibase/docker-entrypoint.sh"]