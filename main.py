# Copyright 2026 Christian Aceves
# Licensed under the Apache License, Version 2.0
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# main.py - Main entry point for the application

import time

from utils.logger import Logger

if __name__ == "__main__":
    logger = Logger("Main")
    
    logger.log("This is a info message.")
    logger.warn("This is a warning message.")
    logger.error("This is an error message.")
    
    time.sleep(5)
    
    logger.log("This is another info message after 5 seconds.")
    logger.log("This is yet another info message.")