FROM ubuntu

RUN apt-get update &&\
 apt-get install sudo &&\
 apt-get install -y curl &&\
 curl -sL  https://deb.nodesource.com/setup_12.x | sudo -E bash - &&\
 apt-get install -y nodejs &&\
 npm install -g elasticdump

ADD entry_point.sh /entry_point.sh
ADD search_dump.json /search_dump.json

CMD ["/entry_point.sh"]
