import os
import subprocess

def check_uptime():
	# This runs the linux 'uptime -p' command and captures the output
	raw_output = subprocess.check_output(['uptime','-p'])

	# Clean up the output (decode bytes to string, strip whitespcae)
	readable_uptime = raw_output.decode('utf-8').strip()

	print(f"[-] Current System Uptime:{readable_uptime}")

def check_load():
	# Get the 1, 5, and 15 minute load averages
	load1, load5, load15 = os.getloadavg()
	print(f"[-] System Load (1 min): {load1}")

if __name__ == "__main__":
	print("---SYSTEM MONITOR STARTING ---")
	check_uptime()
	check_load()
	print("---------------------------------------------------")
