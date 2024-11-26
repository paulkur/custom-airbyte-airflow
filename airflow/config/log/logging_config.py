from __future__ import annotations
import os
from typing import Any
"""
import logging

logging.basicConfig(level=logging.WARNING)

for logger_name in logging.root.manager.loggerDict:
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.WARNING)
"""

# These should match the default values used in your Airflow config
LOG_LEVEL = os.getenv("AIRFLOW__LOGGING__LOGGING_LEVEL", "INFO").upper()
FAB_LOG_LEVEL = os.getenv("AIRFLOW__LOGGING__FAB_LOGGING_LEVEL", "WARNING").upper()
BASE_LOG_FOLDER = os.getenv("AIRFLOW__LOGGING__BASE_LOG_FOLDER", "/opt/airflow/logs")
PROCESSOR_LOG_FOLDER = os.getenv("AIRFLOW__LOGGING__PROCESSOR_LOG_FOLDER", BASE_LOG_FOLDER)
DAG_PROCESSOR_LOG_TARGET = os.getenv("AIRFLOW__LOGGING__DAG_PROCESSOR_LOG_TARGET", "stdout")
PROCESSOR_FILENAME_TEMPLATE = os.getenv("AIRFLOW__LOGGING__PROCESSOR_FILENAME_TEMPLATE", "{{ filename }}.log")
LOG_FORMAT = os.getenv("AIRFLOW__LOGGING__LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
COLORED_LOG_FORMAT = os.getenv("AIRFLOW__LOGGING__COLORED_LOG_FORMAT", LOG_FORMAT)
COLORED_FORMATTER_CLASS = "airflow.utils.log.colored_log.ColoredFormatter"
# default formatter
LOG_FORMATTER_CLASS = os.getenv("AIRFLOW__LOGGING__LOG_FORMATTER_CLASS", "airflow.utils.log.logging_mixin.RedirectStdHandler")
#LOG_FORMATTER_CLASS = os.getenv("AIRFLOW__LOGGING__LOG_FORMATTER_CLASS", "logging.Formatter")

DAG_PROCESSOR_LOG_FORMAT = os.getenv("AIRFLOW__LOGGING__DAG_PROCESSOR_LOG_FORMAT", LOG_FORMAT)

DEFAULT_LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "airflow": {
            "format": LOG_FORMAT,
            "class": LOG_FORMATTER_CLASS,
        },
        "airflow_coloured": {
            "format": COLORED_LOG_FORMAT if COLORED_LOG_FORMAT else LOG_FORMAT,
            "class": COLORED_FORMATTER_CLASS if COLORED_LOG_FORMAT else LOG_FORMATTER_CLASS,
        },
        "source_processor": {
            "format": DAG_PROCESSOR_LOG_FORMAT,
            "class": LOG_FORMATTER_CLASS,
        },
    },
    "filters": {
        "mask_secrets": {
            "()": "airflow.utils.log.secrets_masker.SecretsMasker",
        },
    },
    "handlers": {
        "console": {
            "class": "airflow.utils.log.logging_mixin.RedirectStdHandler",
            "formatter": "airflow_coloured",
            "stream": "sys.stdout",
            "filters": ["mask_secrets"],
        },
        "task": {
            "class": "airflow.utils.log.file_task_handler.FileTaskHandler",
            "formatter": "airflow",
            "base_log_folder": os.path.expanduser(BASE_LOG_FOLDER),
            "filters": ["mask_secrets"],
        },
        "processor": {
            "class": "airflow.utils.log.file_processor_handler.FileProcessorHandler",
            "formatter": "airflow",
            "base_log_folder": os.path.expanduser(PROCESSOR_LOG_FOLDER),
            "filename_template": PROCESSOR_FILENAME_TEMPLATE,
            "filters": ["mask_secrets"],
        },
        "processor_to_stdout": {
            "class": "airflow.utils.log.logging_mixin.RedirectStdHandler",
            "formatter": "source_processor",
            "stream": "sys.stdout",
            "filters": ["mask_secrets"],
        },
    },
    "loggers": {
        "airflow.processor": {
            "handlers": ["processor_to_stdout" if DAG_PROCESSOR_LOG_TARGET == "stdout" else "processor"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "airflow.task": {
            "handlers": ["task"],
            "level": LOG_LEVEL,
            "propagate": False,
            "filters": ["mask_secrets"],
        },
        "flask_appbuilder": {
            "handlers": ["console"],
            "level": FAB_LOG_LEVEL,
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
        "filters": ["mask_secrets"],
    },
}

# Optional: set this as the logging config in Airflow
LOGGING_CONFIG = DEFAULT_LOGGING_CONFIG
