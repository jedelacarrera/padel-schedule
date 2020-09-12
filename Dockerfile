# build stage
FROM node:lts-alpine as build-stage
WORKDIR /app
RUN apk add yarn
COPY . .
ARG PROJECT_ID
RUN yarn
RUN yarn build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
