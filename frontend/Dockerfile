FROM node:14

# Set the working directory
WORKDIR /app

# Copy the package.json and yarn.lock files
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the frontend files
COPY . .

# Expose the React app port
EXPOSE 3000

# Run the React app
CMD ["yarn", "start"]
