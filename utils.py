
import csv, json

# Helper utility function to read the data from file
# INPUT PARAMETER: <inputFileName>

def readData(inputFileName):
    data = None

    with open(inputFileName) as json_file:
        data = json.load(json_file)

        json_file.close()

    return data

# Helper utility function to process the data
# INPUT PARAMETERS: <headers> and <data>

def processData(headers, data):
    finalOutput = []

    for row in data:
        output = []
        output.append(row)

        for header in headers:
            if(header in data[row]):
                output.append(1)
            else:
                output.append(0)

        finalOutput.append(output)
    return finalOutput

# Helper utility function to write the output data to file
# INPUT PARAMETER: <outputFileName> and <headers> and <outputDataInAList>

def writeOutputToFile(outputFileName, headers, outputDataList):
    empty = ''

    with open(outputFileName, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|')

        spamwriter.writerow([empty] + headers)
        spamwriter.writerows(outputDataList)
        # for dataItem in outputDataList:
        #     spamwriter.writerows(outputDataList)
        
        csvfile.close()