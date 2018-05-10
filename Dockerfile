FROM jekyll/jekyll:3.8.0

RUN apk --no-cache update && \
    apk --no-cache add gcc g++ make build-base python3 py3-pip ca-certificates curl groff less git py-yaml && \
    pip3 --no-cache-dir install --upgrade pip && \
    rm -rf /var/cache/apk/*

RUN pip3 --no-cache-dir install awscli

ADD Gemfile /root/Gemfile
ADD Gemfile.lock /root/Gemfile.lock

RUN cd /root && \
    /usr/gem/bin/bundle install

CMD sh
