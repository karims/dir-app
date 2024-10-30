FROM node:14

WORKDIR /app

# Set PATH for npm binaries
ENV PATH /app/node_modules/.bin:$PATH

# Copy package.json and package-lock.json first
COPY package.json package-lock.json ./

# Set permissions to ensure npm install works
RUN chmod -R 777 /app && yarn install

# Copy the rest of the frontend files
COPY . .

EXPOSE 3000

#CMD ["npm", "start"]
CMD ["sh", "-c", "yarn install && yarn start"]
