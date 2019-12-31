FROM ubuntu:18.04

RUN apt-get update
RUN apt-get -y install curl
RUN apt-get -y install gnupg
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get -y install yarn
RUN yarn global add gulp
RUN apt-get -y install git-core

COPY ./rodan-client/package.json /rodan-client/package.json
COPY ./rodan-client/yarn.lock /rodan-client/yarn.lock
WORKDIR /rodan-client
RUN yarn install
ARG DEV_JSPM_GITHUB_AUTH_TOKEN
RUN cd /rodan-client/node_modules/.bin && ./jspm config registries.github.auth ${DEV_JSPM_GITHUB_AUTH_TOKEN}
RUN cd /rodan-client/node_modules/.bin && ./jspm install -y

EXPOSE 9002
CMD /rodan-client/node_modules/.bin/gulp
