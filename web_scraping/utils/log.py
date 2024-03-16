
import time

def log_metrics(directory_path, created_files, removed_files, link_count):
    with open("./log.txt", "a") as logfile:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        logfile.write(f"Timestamp: {current_time}\n")
        logfile.write(f"Directory: {directory_path}\n")
        logfile.write(f"Total Files Created: {created_files}\n")
        logfile.write(f"Total Files Removed: {removed_files}\n")
        logfile.write(f"Total Links Found: {link_count}\n")
        logfile.write("=" * 50 + "\n")

def log_request_metric(request_count,success_count):
    with open('./log_request.txt','a') as logfile:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        logfile.write(f"Timestamp: {current_time}\n")
        logfile.write(f"Total request count:{request_count}\n")
        logfile.write(f'Total success count:{success_count}\n')
