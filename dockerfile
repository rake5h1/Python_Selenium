FROM python:3.8

# Install required packages
RUN apt-get update && \
    apt-get install -y wget unzip

# Download and install Microsoft Edge WebDriver
# Download and install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Download and install ChromeDriver
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/119.0.6045.105/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && rm chromedriver-linux64.zip \
    && mv chromedriver-linux64 /usr/local/bin/

# Install your Python dependencies

# Copy your Selenium script into the container
COPY . .

RUN pip install --no-cache-dir -r req.txt



# Run your Selenium script when the container starts
CMD ["behave"]
