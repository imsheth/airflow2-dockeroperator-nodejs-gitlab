FROM node:14.1.0

# Create app directory for working inside docker container
WORKDIR /tmp/dockerspace/blogs-imsheth-com/airflow2-dockeroperator-nodejs-gitlab

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY package*.json ./

# Sample package listed in package.json for installation
RUN npm install

# Bundle app source
COPY . .

# Increase memory if needed
# https://stackoverflow.com/a/67703157/3152654
# CMD node --max-old-space-size=6144 app.js

# Else
CMD node app.js
