FROM apache/airflow:slim-2.10.2-python3.12

USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
         git \
         zsh \
         libpq-dev \
         build-essential \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Update pip to the latest version
RUN python -m pip install --upgrade pip

# Create directories and set permissions
RUN umask 0002 \
  && mkdir -p /opt/airflow/dags \
  && mkdir -p /opt/airflow/files \
  && mkdir -p /opt/airflow/plugins \
  #&& mkdir -p /opt/airflow/logs \
  #&& mkdir -p /opt/airflow/logs/scheduler \
  && mkdir -p /opt/airflow/temp


# Set permissions for airflow logs and temp directories
#RUN chown -R airflow:root /opt/airflow/logs \
#RUN chown -R airflow ${AIRFLOW_HOME}/logs \
#  && chmod -R 777 /opt/airflow/logs \

RUN chown -R airflow /opt/airflow/temp \
  && chmod -R 777 /opt/airflow/temp


COPY config/ ${AIRFLOW_HOME}
COPY plugins/ ${AIRFLOW_HOME}/plugins/
COPY config/init.sh ./init.sh

RUN chmod +x ./init.sh

USER airflow

RUN pip install -r ${AIRFLOW_HOME}/requirements.txt

# Set PYTHONPATH environment variable
ENV PYTHONPATH=/opt/airflow/files/:/opt/airflow/files/include/:/opt/airflow/config/

# dbt and soda install
#ENV PIP_USER=false
#RUN python -m venv soda_venv && source soda_venv/bin/activate && \
#    pip install --no-cache-dir soda-core-snowflake==3.2.2 &&\
#    pip install --no-cache-dir soda-core-scientific==3.2.2 && deactivate
#RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
#    pip install --no-cache-dir dbt-snowflake==1.7.2 && deactivate
#ENV PIP_USER=true
### end ###

# Define volumes
VOLUME ["/opt/airflow/dags", "/opt/airflow/files", "/opt/airflow/plugins", "/opt/airflow/logs"]

# Install Oh My Zsh and plugins
#RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

#RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" && \
#    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
#    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
