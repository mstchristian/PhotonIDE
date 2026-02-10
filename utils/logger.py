# Copyright 2026 Christian Aceves
# Licensed under the Apache License, Version 2.0
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

# utils/logger.py - Logger utility for the application

import os
import datetime

RESET = "\033[0m"
WARN = "\033[33m"
ERROR = "\033[31m"

log_initialized = False
log_to_file_enabled = True
log_file_path = None

class Logger:
    def __init__(self, identifier: str):
        global log_initialized
        
        self.identifier = identifier
        
        if not log_initialized:
            self.initialize_log()
            
        self.log(f"Logger initialized for {self.identifier}")
            
    def getDateTime(self) -> str:
        now = datetime.datetime.now()
        return now.strftime("%d-%m-%Y %H:%M:%S")
    
    def initialize_log(self):
        global log_initialized, log_to_file_enabled, log_file_path
        
        try:
            log_file_path = os.path.join(os.getcwd(), "logs", f"{self.getDateTime().replace(':', '-')}.log")
            
            os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
            
            with open(log_file_path, "w") as log_file:
                log_file.write(f"Log created on {self.getDateTime()}\n")
                
            print(f"[{self.getDateTime()}] [Logger] [INFO] Log file initialized at {log_file_path}")
        except Exception as e:
            log_to_file_enabled = False
            print(f"{WARN}[{self.getDateTime()}] [Logger] [WARN] Failed to initialize log file: {e} >>> Logging to file disabled{RESET}")
            
        log_initialized = True
        
    def log_to_file(self, message: str):
        global log_to_file_enabled, log_file_path
        
        if log_to_file_enabled:
            try:
                with open(log_file_path, "r+") as log_file:
                    log_file.seek(0, os.SEEK_END)
                    log_file.write(f"{message}\n")
            except Exception as e:
                log_to_file_enabled = False
                print(f"{WARN}[{self.getDateTime()}] [Logger] [WARN] Failed to write to log file : {e} >>> Logging to file disabled{RESET}")
                
    def log(self, context: str):
        message = f"[{self.getDateTime()}] [{self.identifier}] [INFO] {context}"
        
        print(message)
        self.log_to_file(message)
        
    def warn(self, context: str):
        message = f"[{self.getDateTime()}] [{self.identifier}] [WARN] {context}"
        
        print(f"{WARN}{message}{RESET}")
        self.log_to_file(message)
        
    def error(self, context: str):
        message = F"[{self.getDateTime()}] [{self.identifier}] [ERROR] {context}"
        
        print(f"{ERROR}{message}{RESET}")
        self.log_to_file(message)