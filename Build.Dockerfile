FROM buildbase
 

RUN mkdir -p /Build/
WORKDIR /Build/

COPY scripts/ /Build/scripts/
COPY requirements.txt /Build/scripts/
COPY version.py /Build/scripts/
ENV PYTHONPATH="scripts/"
RUN pip3 install -r /Build/scripts/requirements.txt
RUN head -n -1 /Build/scripts/version.py >/Build/scripts/version2.py
RUN mv /Build/scripts/version2.py /Build/scripts/version.py

#inject distro into version.py
RUN echo ",\"distro\":\"\"\"">>/Build/scripts/version.py
RUN cat /etc/redhat-release >>/Build/scripts/version.py
RUN echo "\"\"\"">>/Build/scripts/version.py

#inject libs into version.py
RUN echo ",\"python_libs\":\"\"\"" >>/Build/scripts/version.py
RUN pip freeze >>/Build/scripts/version.py
RUN echo "\"\"\"}" >>/Build/scripts/version.py
#RUN pyinstaller scripts/switchboard.py  --add-data /Build/scripts/version.txt:.  --onefile
RUN cd /Build/scripts/ && python3 /Build/scripts/setup.py build_ext --inplace

RUN pyinstaller /Build/scripts/sender.py  --onefile --paths $PYTHONPATH
RUN pyinstaller /Build/scripts/receive_test.py  --onefile --paths $PYTHONPATH
RUN mv /Build/scripts/multicast.csv /Build/dist/ 
RUN mkdir tmp 
RUN tar -czvf pubsub.tar -C /Build/dist/ . 
RUN tar -xvf ./pubsub.tar -C ./tmp/
# RUN pip3 install -r scripts/requirements.txt
# RUN pyinstaller scripts/switchboard.py -w --onefile
# RUN tar -czvf switchboard.tar -C dist/ .
