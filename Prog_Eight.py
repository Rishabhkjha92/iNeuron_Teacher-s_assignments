#8. WAF which shows the system configuration
# OS name/version
# Name of the CPU, clock speed
# Number of CPU core
# Size of memory

#rather than OS module using Platform module
#but install platform first so use :  pip install platform

import platform, click
 
click.clear()
syst = platform.uname()
 
print(f"System: {syst.system}")
print(f"Node Name: {syst.node}")
print(f"Release: {syst.release}")
print(f"Version: {syst.version}")
print(f"Machine: {syst.machine}")
print(f"Processor: {syst.processor}")
