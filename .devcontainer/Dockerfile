FROM python:3.10
USER root

RUN apt-get update && \
    apt-get -y install --reinstall ca-certificates && \
    apt-get -y install software-properties-common && \
    apt-get -y install iputils-ping net-tools htop && \
    apt-get -y install fonts-ipafont && \
    apt-get -y install tree && \
    apt-get -y install zip && \
    pip install --upgrade pip

# Install PlantUML
RUN apt install openjdk-17-jdk && \
    apt-get -y install graphviz && \
    apt-get -y install plantuml

# COPY requirements.txt /tmp/requirements.txt
# RUN pip install -r /tmp/requirements.txt

# Install Basic Packages
RUN pip install ipykernel jupyter pandas

# Other Python Modules
RUN pip install sphinx sphinx_rtd_theme sphinx-autobuild
RUN pip install sphinxcontrib-mermaid
RUN pip install sphinxcontrib-plantuml