from dialogflow_fulfillment import QuickReplies, WebhookClient
from flask import Flask, request, Response, jsonify , make_response
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

app = Flask(__name__)

SERVICE_ACCOUNT_FILE = 'keys-food.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1DxYub7bbxV_h2AR2lAp8aaTyuy52bmKNsKY8nPTHCnw'
service = build('sheets', 'v4', credentials=creds)

def handler(agent: WebhookClient) :
    """Handle the webhook request.."""
    global para
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    para = req.get('queryResult').get('parameters').get('rest1_items')
    
    if intent_name=='choose_rest':
        agent.add('Hello, From where do your want to order food?')
        agent.add(QuickReplies(quick_replies=['Indiana Café', 'OTacos']))

    global rest
    if intent_name=='Indiana Café' or intent_name=='OTacos':
        rest = req.get('queryResult').get('queryText')
        print(rest)
        agent.add('Which food are you looking for?')
        agent.add(QuickReplies(quick_replies=['Appetizers', 'Main','Desserts','Sodas']))

    if intent_name=='choice_rest_appetizers':
        agent.add('what do you want?')
        agent.add(QuickReplies(quick_replies=['Avocado Toast','Quesadilla Classic']))
              
    if intent_name=='choice_rest_main' and rest == 'Indiana Café':
        agent.add('what do you want?')
        agent.add(QuickReplies(quick_replies=['Cheese Burger','Chicken Burger','Veggie Burger']))

    if intent_name=='choice_rest_main' and rest=='OTacos' :
        print(rest)
        agent.add('what do you want?')
        agent.add(QuickReplies(quick_replies=['M Tacos','L Tacos','Xl Tacos']))

    if intent_name=='choice_rest_ desserts' and rest == 'Indiana Café':
        print(rest)
        agent.add('what do you want?')
        agent.add(QuickReplies(quick_replies=['Brownie','Cheesecake','Ice Cream']))

    if intent_name=='choice_rest_ desserts' and rest == 'OTacos':
        agent.add('what do you want?')
        agent.add(QuickReplies(quick_replies=['Tiramisu','Chocolate Pie']))

    if intent_name=='choice_rest_ sodas':
        agent.add('what do you want?')
        agent.add(QuickReplies(quick_replies=['Coca Cola','Fanta','Oasis','Ice Tea']))

    menu= {'Avocado Toast': 100, 'Quesadilla Classic':200,
          'Coca Cola': 25, 'Fanta': 35, 'Oasis': 45, 'Ice Tea': 55,
          'Cheese Burger': 300, 'Chicken Burger': 400, 'Veggie Burger': 500,
          'M Tacos': 600 , 'L Tacos': 700, 'Xl Tacos': 800,
          'Brownie': 50, 'Cheesecake': 60, 'Ice Cream': 70,
          'Tiramisu': 80, 'Chocolate Pie': 90}

    all_items = list(menu.keys())
    all_prices= list(menu.values())

    global item
    global price

    if para==all_items[0]:
        agent.add(f'each {all_items[0]} cost is {all_prices[0]} , how many {all_items[0]} do you want?')
        item=all_items[0]
        price=menu.get(all_items[0])

    if para==all_items[1]:
        agent.add(f'each {all_items[1]} cost is {all_prices[1]} , how many {all_items[1]} do you want?')
        item=all_items[1]
        price=menu.get(all_items[1])

    if para==all_items[2]:
        agent.add(f'each {all_items[2]} cost is {all_prices[2]} , how many {all_items[2]} do you want?')
        item=all_items[2]
        price=menu.get(all_items[2])

    if para==all_items[3]:
        agent.add(f'each {all_items[3]} cost is {all_prices[3]} , how many {all_items[3]} do you want?')
        item=all_items[3]
        price=menu.get(all_items[3])

    if para==all_items[4]:
        agent.add(f'each {all_items[4]} cost is {all_prices[4]} , how many {all_items[4]} do you want?')
        item=all_items[4]
        price=menu.get(all_items[4])

    if para==all_items[5]:
        agent.add(f'each {all_items[5]} cost is {all_prices[5]} , how many {all_items[5]} do you want?')
        item=all_items[5]
        price=menu.get(all_items[5])

    if para==all_items[6]:
        agent.add(f'each {all_items[6]} cost is {all_prices[6]} , how many {all_items[6]} do you want?')
        item=all_items[6]
        price=menu.get(all_items[6])

    if para==all_items[7]:
        agent.add(f'each {all_items[7]} cost is {all_prices[7]} , how many {all_items[7]} do you want?')
        item=all_items[7]
        price=menu.get(all_items[7])

    if para==all_items[8]:
        agent.add(f'each {all_items[8]} cost is {all_prices[8]} , how many {all_items[8]} do you want?')
        item=all_items[8]
        price=menu.get(all_items[8])
       
    if para==all_items[12]:
        agent.add(f'each {all_items[12]} cost is {all_prices[12]} , how many {all_items[12]} do you want?')
        item=all_items[12]
        price=menu.get(all_items[12])

    if para==all_items[13]:
        agent.add(f'each {all_items[13]} cost is {all_prices[13]} , how many {all_items[13]} do you want?')
        item=all_items[13]
        price=menu.get(all_items[13])

    if para==all_items[14]:
        agent.add(f'each {all_items[14]} cost is {all_prices[14]} , how many {all_items[14]} do you want?')
        item=all_items[14]
        price=menu.get(all_items[14])

    if para==all_items[15]:
        agent.add(f'each {all_items[15]} cost is {all_prices[15]} , how many {all_items[15]} do you want?')
        item=all_items[15]
        price=menu.get(all_items[15])

    if para==all_items[16]:
        agent.add(f'each {all_items[16]} cost is {all_prices[16]} , how many {all_items[16]} do you want?')
        item=all_items[16]
        price=menu.get(all_items[16])

    global rest_tacos
    if intent_name=='all_flavors':
        rest_tacos= req.get('queryResult').get('queryText')
        size= req.get('queryResult').get('parameters').get('size')

    
        if size=='M':
            agent.add('Which 1 flavor do you want ?')
            agent.add(QuickReplies(quick_replies=['Plain Chicken Fillet','Marinated Chicken Fillet','Minced Meat','Cordon Bleu',
            'Nuggets', 'Merguez', 'Tenders', 'Falafels']))
            
        if size=='L':           
            agent.add('Which 2 flavors do you want ?')
            agent.add(QuickReplies(quick_replies=['Plain Chicken Fillet','Marinated Chicken Fillet','Minced Meat','Cordon Bleu',
            'Nuggets', 'Merguez', 'Tenders', 'Falafels']))

        if size=='Xl':
            agent.add('Which 3 flavors do you want ?')
            agent.add(QuickReplies(quick_replies=['Plain Chicken Fillet','Marinated Chicken Fillet','Minced Meat','Cordon Bleu',
            'Nuggets', 'Merguez', 'Tenders', 'Falafels']))

    global flav
    if intent_name=='choose_flavor' and rest_tacos=='M Tacos':
        flav= req.get('queryResult').get('queryText')
        agent.add(f'each {all_items[9]} cost is {all_prices[9]} , how many {all_items[9]} do you want?')
        item=all_items[9]
        price=menu.get(all_items[9])

    if intent_name=='choose_flavor' and rest_tacos=='L Tacos':
        flav= req.get('queryResult').get('queryText')
        agent.add(f'each {all_items[10]} cost is {all_prices[10]} , how many {all_items[10]} do you want?')
        item=all_items[10]
        price=menu.get(all_items[10])

    if intent_name=='choose_flavor' and rest_tacos=='Xl Tacos':
        flav= req.get('queryResult').get('queryText')
        agent.add(f'each {all_items[11]} cost is {all_prices[11]} , how many {all_items[11]} do you want?')
        item=all_items[11]
        price=menu.get(all_items[11])

    if intent_name=='item_quantity':
        global quanity
        quanity = req.get('queryResult').get('parameters').get('number')

    if intent_name=='name':
        name = req.get('queryResult').get('queryText')
        from datetime import datetime, date
        today = date.today()
        date = today.strftime("%b-%d-%Y")
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        total_price=price*quanity
        
        if (rest=='OTacos' and item==all_items[0]) or (rest=='OTacos' and item==all_items[1]):  
            print(rest)
            sheett= [[name, date, time, item, quanity, total_price]]
            sheet = service.spreadsheets()
            result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="O_Tacos!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()

        if (rest=='Indiana_Cafe' and item==all_items[0]) or (rest=='Indiana_Cafe' and item==all_items[1]):  
            print(rest)
            sheett= [[name, date, time, item, quanity, total_price]]
            sheet = service.spreadsheets()
            result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Indiana_Cafe!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()
        
        if item==all_items[6] or item==all_items[7] or item==all_items[8] or all_items[12] or item==all_items[13] or all_items[14]:  
            sheett= [[name, date, time, item, quanity, total_price]]
            sheet = service.spreadsheets()
            result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Indiana_Cafe!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()
        
        if item==all_items[9] or item==all_items[10] or item==all_items[11]:
            sheett= [[name, date, time, item, quanity, total_price, flav]]
            sheet = service.spreadsheets()
            result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="O_Tacos!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()

        if item==all_items[15] or item==all_items[16] :
            sheett= [[name, date, time, item, quanity, total_price]]
            sheet = service.spreadsheets()
            result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="O_Tacos!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()

    if intent_name=='feedback':
        feed= req.get('queryResult').get('queryText')
        sheett= [[feed]]
        sheet = service.spreadsheets()
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="feedback!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()
        agent.add('Thanks for your response :)')
        
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    """Handle webhook requests from Dialogflow."""
    # Get WebhookRequest object
    req = request.get_json(force=True)
    # Handle request
    agent = WebhookClient(req)
    agent.handle_request(handler)
    return agent.response

if __name__ == '__main__':
    app.run()