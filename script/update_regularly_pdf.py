import os
import sys
import threading
import time

def print_usage_and_exit():
    print("""
    <python> update_regularly_pdf.py <arg1> <arg2> 
    
    pressing any key during the execution would stop the process
      -- <arg0> : the working directory where to launch the pdflatex command
                  this is the directory of the lateX project
      -- <arg1> : the path to the .tex file to generate pdf from
                  it is assumed that running pdflatex <arg1> would
                  realise the desired effect
      -- <arg2> : the interval in seconds with which to recompile 
                  the pdf must be an integer (the seconds)

    """)
    exit()

def compile_latex_file_topdf(file_path, latex_dir):
    pid=os.fork()
    if pid==0:
        os.system("cd " + str(latex_dir) + " && pdflatex " + str(file_path))
        exit()


# get the arguments
args=sys.argv
print("You entered the arguments" + str(args))

# print usage and exist if the arguments are not correct
if len(args) < 3:
    print("quit because not enough args")
    print_usage_and_exit()

path_to_latex_workingdir=args[1]
path_to_latex_file=args[2]
if len(args) > 3:
    try:
        time_betwween_compilation=int(args[3])
    except ValueError:
        print_usage_and_exit()
else:
    print("default timer of suration 60s")
    time_betwween_compilation=60

    
# start the loop
while True:
    compile_latex_file_topdf(path_to_latex_file, path_to_latex_workingdir)
    time.sleep(time_betwween_compilation)

    

