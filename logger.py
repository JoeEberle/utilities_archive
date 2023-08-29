# Establish the Python Logger  
import logging # built in python library that does not need to be installed 

def set_start_time():
    import time    
    start_time = time.time()
    return(start_time)

def create_logger_Start(solution_name, start_time):
    from datetime import datetime
    logging.basicConfig(level=logging.INFO, filename=solution_name + '.log',
                    filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')    
    process_start_time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'[:-3])
    logging.info(f'PROCESS START {solution_name} ' + ('=' * 45) ) 
    logging.info(f'PROCESS START {solution_name}')    
    logging.info(f'PROCESS START {solution_name} Start Time = {process_start_time_stamp}')  
    logging.info(f'Process {solution_name} Step 0 - Initialize the configuration file parser')
#     return f'logger_started for {solution_name} at {process_start_time_stamp}'
    return logging

def append_log_file(solution_name): 
    import os 
    log_filename=solution_name + '.log'
    historical_log_filename=solution_name + '_history.log'

    with open(log_filename) as log_file:
        log_content = log_file.read()

    with open(historical_log_filename,'a') as historical_log_file:
        print(120*' ', file=historical_log_file)        
        print(120*'>', file=historical_log_file)       
        print(log_content, file=historical_log_file)  
        print(120*'<', file=historical_log_file)  
        print(120*' ', file=historical_log_file)    
    return(log_content)  

def calculate_process_performance(solution_name, process_start_time):
    import time
    stop_time = time.time()
    process_duration = stop_time - process_start_time
    process_stop_time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'[:-3])
    
    logging.info(f'PROCESS END   {solution_name} The total process duration was:{process_duration:.3f}')    # establish the start time of the overall process. 
    logging.info(f'PROCESS END   {solution_name} Stop Time = {process_stop_time_stamp}')    # establish the start time of the overall process. 

    status = f'PROCESS END   {solution_name} Duration Classification Error - Process Duration UNKNOWN' 
    if process_duration > 600.0:
        status = f'PROCESS END   {solution_name} Long process dureation:{process_duration:.3f}, greater than 10 Minutes, performance optimization is required' 
    elif process_duration > 120.0:
        status = f'PROCESS END   {solution_name} Medium process duration:{process_duration:.3f}, greater than 3 minutes, optimization is optional'  
    elif process_duration > 3.0:
        status = f'PROCESS END   {solution_name} low process duration:{process_duration:.3f}, less than 3 minutes, optimization is optional'  
    elif process_duration < 3.0:
        status = f'PROCESS END   {solution_name} Short process duration:{process_duration:.3f}, less than 3 Seconds, optimization is not reccomended'  
    else:  
        status = f'PROCESS END   {solution_name} Duration Classification Error - Process Duration UNKNOWN' 
        
    logging.info(status)     
    logging.info(f'PROCESS END   {solution_name}') 
    logging.info(f'PROCESS END   {solution_name} ' + ('=' * 45) )             
    return(status)
 