FROM python:3.12
# Set working directory to /usr/src/app
WORKDIR /usr/src/app
# Upgrade pip
RUN pip install --upgrade pip
# Run pip to install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Update apt cache
RUN apt-get update
# Update system packages
RUN apt-get upgrade -y
# Install wkhtmltopdf
RUN apt-get install -y wkhtmltopdf
# Copy application files
ADD src /usr/src/app
# Open port 8080 to receive traffic
EXPOSE 8080
# Set the VERSION variable to the build number, which is passed in via the docker build --build-arg argument
ARG BUILD_NUMBER
ARG BRANCH_NAME
ENV VERSION=$BRANCH_NAME-$BUILD_NUMBER
# Start up waitress
CMD ["waitress-serve", "__init__:app"]