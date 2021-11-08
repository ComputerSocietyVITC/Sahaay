from pydantic import BaseModel

class LogConfig(BaseModel):
    LOGGER_NAME: str = "sahaay_app"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s "
    LOG_LEVEL: str = "DEBUG"

    # Logging config
    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "sahaay_app": {"handlers": ["default"], "level": LOG_LEVEL},
    }