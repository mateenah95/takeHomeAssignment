# Library Imports
import csv, json

# Helper Function Imports
from utils import readData, processData, writeOutputToFile
from spreadsheetWriter import writeData

# Header Flags For Checks
HEADERS_LIST = ['view_grades', 'change_grades', 'add_grades', 'delete_grades', 'view_classes', 'change_classes', 'add_classes', 'delete_classes']

# Input file name - ensure correct
INPUT_FILE_NAME = 'in.json'

# Output file name - ensure correct
OUTPUT_FILE_NAME = 'out.csv'

# Main Function Which Controls Execution
def runMain():
    print('Running ...')
    try:
        data = readData(INPUT_FILE_NAME) 
    except Exception as e:
        print('ERROR 1: File I/O Error While Reading Input Data! App terminating ...')
        return


    try:
        dataOutputList = processData(HEADERS_LIST, data)
    except Exception as f:
        print('ERROR 2: Error Processing Data! App terminating ...')
        return

    try:
        writeOutputToFile(OUTPUT_FILE_NAME, HEADERS_LIST, dataOutputList)
        writeData(HEADERS_LIST, 1)
        for element in dataOutputList:
            writeData(element, 0)

    except Exception as g:
        print('ERROR 3: File I/O Error While Writing Output Data! App terminating ...')
        print(g)
        return
        
print('-----------------------')
print('App started running ...')
print('-----------------------')

# Calling the main execution controlling function
runMain() 

print('-----------------------')
print('App finished running ...')
print('-----------------------')