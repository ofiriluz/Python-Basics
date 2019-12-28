# A standard logging library used to define formatting for logs
# And log into different loglevels and sinks
import logging
# You can format the logging with a formatting string
# For example this will print the datetime and the log level before the message
# You can also add a filename="" to the basicConfig to output the logs to a file
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.info("A")
logging.warning("A")
logging.debug("A")
logging.error("A")