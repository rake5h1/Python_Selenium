FROM ubuntu:latest


# Install required packages
RUN apt-get update && \
    apt-get install -y wget unzip

# Download and install Microsoft Edge WebDriver
# Download and install Chrome
RUN apt-get install wget
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb



# Download and install ChromeDriver
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && rm chromedriver-linux64.zip \
    && mv chromedriver-linux64 /usr/local/bin/

# Install your Python dependencies
FROM python:latest

# Copy your Selenium script into the container
COPY . .

RUN pip install --no-cache-dir -r req.txt



# Run your Selenium script when the container starts
CMD ["behave"]
