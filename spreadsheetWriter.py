import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("TrackRev").sheet1  # Open the spreadhseet

sheet.clear() # Clear existing data

# Helper function for writing data based on header flag or not
def writeData(theData, headerFlag):
    if(headerFlag == 0):
        sheet.append_row(theData)
    else:
        sheet.append_row(['.'] + theData)
    
    