FROM centos:7

RUN yum -y update && \
    yum -y install yum-utils && \
    yum -y groupinstall development && \
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm && \
    yum -y install python36u && \
    yum -y install python36u-devel && \ 
    yum -y install python36u-setuptools

RUN easy_install-3.6 pip && \
    pip3 install pyinstaller

RUN mkdir -p Build/
WORKDIR Build/

COPY scripts/ /Build/scripts/
COPY requirements.txt /Build/scripts/
ENV PYTHONPATH="/Build/scripts/"
RUN pip3 install -r scripts/requirements.txt
 
  
