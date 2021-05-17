# FROM ubuntu:16.04 as build

# RUN apt-get update \
#     && apt-get upgrade -y \
#     && apt-get install -y

# RUN apt-get install -y wget libfreetype6 libglu1-mesa libxi6



# RUN apt-get update && \
# 	apt-get install -y \
# 		curl \
# 		libfreetype6 \
# 		libglu1-mesa \
# 		libxi6 \
# 		libxrender1 \
# 		xz-utils && \
# 	apt-get -y autoremove

# ENV BLENDER_MAJOR 2.90
# ENV BLENDER_VERSION 2.90a
# ENV BLENDER_URL https://download.blender.org/release/Blender${BLENDER_MAJOR}/blender-${BLENDER_VERSION}-linux64.tar.xz

# RUN curl -L ${BLENDER_URL} | tar -xJ -C /usr/local/ && \
# 	mv /usr/local/blender-${BLENDER_VERSION}-linux64 /usr/local/blender 

# RUN script.sh

# VOLUME /media
# WORKDIR /
# ENTRYPOINT ["/usr/local/blender/blender", "-b"]


# NEW DOCKER

FROM blendergrid/blender:2.91.2
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
	&& apt-get install -y python3-pip mesa-utils xorg

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME
RUN ls

RUN python3 --version
RUN pip3 install flask
RUN pip3 install --upgrade google-cloud-storage

EXPOSE 5000
CMD ["sh", "./script.sh"]
