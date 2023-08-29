FROM node:20

WORKDIR /app

COPY package.json .

RUN npm i

COPY . .

EXPOSE 5137

CMD ["npm","run","dev"]