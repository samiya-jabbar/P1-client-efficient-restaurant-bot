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


def start():
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    if intent_name=='start':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "Which food are you looking for?"
                ]
    }
    },
    {
    'text':  {
    'text': [
                "Foods are available at Indiana Cafe and O'TACOS !!"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "APPITIZERS: 1. avocado toast 2. quesadilla classic "
                ]
            }
        },

        {
    'text':  {
    'text': [
                "MAIN: 1. cheese burger 2. chicken burger 3. veggie burger 4. M tacos 5. L tacos 6. XL tacos"
                ]
            }
        },
        {
    'text':  {
    'text': [
                "DESSERTS: 1. brownie 2. cheesecake 3. ice cream "
                ]
            }
        },
         {
    'text':  {
    'text': [
                "SODAS: 1. coca cola 2. fanta 3. oasis 4. ice tea "
                ]
            }
        },
        {
    'text':  {
    'text': [
                "Which food would you like to order ? Give food name : "
                ]
            }
        }
        ]
    }

def lista():
    req = request.get_json(force=True)
    order = req.get('queryResult').get('queryText')
    para = req.get('queryResult').get('parameters').get('fooda')
    print(para)
    price = [10 ,20,30,40,50,60,70,80]
    
    if para=='CHICKEN BURGER':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"CHICKEN BURGER is available at Indiana Café in {price[0]} Rs"
                ]
            }
        },
        {
            'text': {
                'text': [
                "Do you want to order? if yes then let us know the quantity along with name , i.e 4 chicken burger "
                ]
            }
        }
        ]
    }

    
    if para=='CHEESE BURGER':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"CHEESE BURGER is available at Indiana Café in {price[1]} Rs"
                ]
            }
        },
        {
            'text': {
                'text': [
                "Do you want to order? if yes then let us know the quantity along with name , i.e 4 chicken burger "
                ]
            }
        }
        ]
    }

    if para=='VEGGIE BURGER':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"VEGGIE BURGER is available at Indiana Café in {price[2]} Rs"
                ]
            }
        },
        {
            'text': {
                'text': [
                "Do you want to order? if yes then let us know the quantity along with name , i.e 4 chicken burger "
                ]
            }
        }
        ]
    }
    
    if para=='BROWNIE':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"BROWNIE is available at Indiana Café in {price[3]} Rs"
                ]
            }
        },
        {
            'text': {
                'text': [
                "Do you want to order? if yes then let us know the quantity along with name , i.e 4 chicken burger "
                ]
            }
        }
        ]
    }


    if para=='cheesecake':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"CHEESECAKE is available at Indiana Café in {price[4]} Rs"
                ]
            }
        },
        {
            'text': {
                'text': [
                "Do you want to order? if yes then let us know the quantity along with name , i.e 4 chicken burger "
                ]
            }
        }
        ]
    }

    if para=='ICE CREAM':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"ICE CREAM is available at Indiana Café in {price[5]} Rs"
                ]
            }
        },
        {
            'text': {
                'text': [
                "Do you want to order? if yes then let us know the quantity along with name , i.e 4 chicken burger "
                ]
            }
        }
        ]
    }

    if para=='TIRAMISU':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"TIRAMISU is available at O'Tacos in {price[6]} Rs"
                ]
            }
        },
        {
            'text': {
                'text': [
                "Do you want to order? if yes then let us know the quantity along with name , i.e 4 chicken burger "
                ]
            }
        }
        ]
    }

    if para=='Chocolate Pie':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"Chocolate Pie is available at O'Tacos in {price[7]} Rs"
                ]
            }
        },
        {
            'text': {
                'text': [
                "Do you want to order? if yes then let us know the quantity along with name , i.e 4 chicken burger "
                ]
            }
        }
        ]
    }
    

def placea():
    global quantity
    global item
    global flag
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    quantity= req.get('queryResult').get('parameters').get('number')
    item= req.get('queryResult').get('parameters').get('fooda')
    flag = "placea"
    return {
   'fulfillmentMessages': [
    {
        'text': {
            'text': [
            "Added to cart !"
            ]
        }
    },
    {
        'text': {
            'text': [
            "NOW ENTER YOUR NAME :"
            ]
        }
    }
    ]
}


def sheeta():
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    name=  req.get('queryResult').get('queryText')
    print(item)
    from datetime import datetime, date
    today = date.today()
    date = today.strftime("%b-%d-%Y")
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    price = [10,20,30,40,50,60,70,80]
    price = [i * quantity for i in price]
    if item=="CHICKEN BURGER":
        price=price[0]
    if item=="CHEESE BURGER":
        price=price[1]
    if item=="VEGGIE BURGER":
        price=price[2]
    if item=="BROWNIE":
         price=price[3]
    if item=="CHEESECAKE":
        price=price[4]
    if item=="ICE CREAM":
        price=price[5]
    if item=="TIRAMISU":
        price=price[6]
    if item=="Chocolate Pie":
        price=price[7]

    sheett= [[name, date, time, item, quantity, price]]
    sheet = service.spreadsheets()
    if ((item=="CHEESE BURGER") or (item=="CHICKEN BURGER") or (item=="VEGGIE BURGER")):
     
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Indiana_Cafe!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()

    elif ((item== "BROWNIE")  or (item=="CHEESECAKE")  or (item=="ICE CREAM")):

        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Indiana_Cafe!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()

    elif ((item=="TIRAMISU") or (item=="Chocolate Pie")):
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="O_Tacos!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()

    return {
   'fulfillmentMessages': [
    {
        'text': {
            'text': [
             "Your order has been placed. We would like to get your feedback"
            ]
        }
    },
    {
        'text': {
            'text': [
            "Waiting for your feedback"
            ]
        }
    }
    ]
}



def listb():
    global price
    req = request.get_json(force=True)
    orderb = req.get('queryResult').get('queryText')
    parab = req.get('queryResult').get('parameters').get('foodb')
    print(parab) 
    price = [10,20,30,40,50,60,10,20,30,40,50,60]

    if parab=='avocado toast':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "avocado toast is available at both indiana cafe and o tacos !"
                ]
    }
    },
    {
    'text':  {
    'text': [
                f"indiana cafe : {price[0]} Rs , o tacos : {price[1]} Rs"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "From where you want to order? "
                ]
            }
        },
    {
    'text':  {
    'text': [
                "ENTER NAME OF RESTURANT :"
                ]
            }
        }
        ]
    }

    if parab=='quesadilla classic':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "quesadilla classic is available at both indiana cafe and o tacos !"
                ]
    }
    },
    {
    'text':  {
    'text': [
                f"indiana cafe : {price[2]} Rs, o tacos : {price[3]} Rs"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "From where you want to order? "
                ]
            }
        },
    {
    'text':  {
    'text': [
                "ENTER NAME OF RESTURANT :"
                ]
            }
        }
        ]
    }

    if parab=='coca cola':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "coca cola is available at both indiana cafe and o tacos !"
                ]
    }
    },
    {
    'text':  {
    'text': [
                f"indiana cafe : {price[4]} Rs, o taco : {price[5]} Rs"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "From where you want to order? "
                ]
            }
        },
    {
    'text':  {
    'text': [
                "ENTER NAME OF RESTURANT :"
                ]
            }
        }
        ]
    }
    if parab=='fanta':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "fanta is available at both indiana cafe and o tacos !"
                ]
    }
    },
    {
    'text':  {
    'text': [
                f"indiana cafe : {price[6]} Rs, o tacos : {price[7]} Rs"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "From where you want to order? "
                ]
            }
        },
    {
    'text':  {
    'text': [
                "ENTER NAME OF RESTURANT :"
                ]
            }
        }
        ]
    }

    if parab=='oasis':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "oasis is available at both indiana cafe and o tacos !"
                ]
    }
    },
    {
    'text':  {
    'text': [
                f"indiana cafe : {price[8]} Rs, o tacos : {price[9]} Rs"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "From where you want to order? "
                ]
            }
        },
    {
    'text':  {
    'text': [
                "GIVE NAME OF RESTURANT :"
                ]
            }
        }
        ]
    }

    if parab=='ice tea':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "ice tea is available at both indiana cafe and o tacos !"
                ]
    }
    },
    {
    'text':  {
    'text': [
                f"indiana cafe : {price[10]} Rs, o tacos : {price[11]} Rs"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "From where you want to order? "
                ]
            }
        },
    {
    'text':  {
    'text': [
                "GIVE NAME OF RESTURANT : "
                ]
            }
        }
        ]
    }


def resturant():
    global r
    req = request.get_json(force=True)
    r= req.get('queryResult').get('queryText')
    return {
   'fulfillmentMessages': [
    {
        'text': {
            'text': [
            "If you really want to order then let us know the quantity along with name , i.e 4 fanta"
            ]
        }
    }
    ]
}


def placeb():
    global quantity
    global item
    global flag
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    quantity= req.get('queryResult').get('parameters').get('number')
    item= req.get('queryResult').get('parameters').get('foodb')
    print(item)
    print(quantity)
    print(r)
    flag = "placeb"
    return {
   'fulfillmentMessages': [
    {
        'text': {
            'text': [
            "Added to cart !"
            ]
        }
    },
    {
        'text': {
            'text': [
            "NOW GIVE YOUR NAME :"
            ]
        }
    }
    ]
}


def sheetb():
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    name=  req.get('queryResult').get('queryText')
    from datetime import datetime, date
    today = date.today()
    date = today.strftime("%b-%d-%Y")
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    price = [10,20,30,40,50,60,10,20,30,40,50,60]
    price = [i * quantity for i in price]
    if ((item=="avocado toast") and (r=="indiana cafe")):
        price=price[0]
    if ((item=="avocado toast") and (r=="o tacos")):
        price=price[1]
    if ((item=="quesadilla classic") and (r=="indiana cafe")):
        price=price[2]
    if ((item=="quesadilla classic") and (r=="o tacos")):
         price=price[3]
    if ((item=="coca cola") and (r=="indiana cafe")):
        price=price[4]
    if ((item=="coca cola") and (r=="o tacos")):
        price=price[5]
    if ((item=="fanta") and (r=="indiana cafe")):
        price=price[6]
    if ((item=="fanta") and (r=="o tacos")):
        price=price[7]
    if ((item=="oasis") and (r=="indiana cafe")):
        price=price[8]
    if ((item=="oasis") and (r=="o tacos")):
        price=price[9]
    if ((item=="ice tea") and (r=="indiana cafe")):
        price=price[10]
    if ((item=="ice tea") and (r=="o tacos")):
        price=price[11]

    sheett= [[name, date, time, item, quantity, price]]
    print(r)
    
    if r=='o tacos':
        print(r)
            # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="O_Tacos!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()
        print(result)
            # Call the Sheets API
    if r=='indiana cafe':
        print(r)
        sheet = service.spreadsheets()
        result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Indiana_Cafe!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()
        print(result)
    return {
   'fulfillmentMessages': [
    {
        'text': {
            'text': [
             "Your order has been placed. We would like to get your feedback"
            ]
        }
    },
    {
        'text': {
            'text': [
            "Waiting for your feedback"
            ]
        }
    }
    ]
}

def listc():
    global size 
    req = request.get_json(force=True)
    size = req.get('queryResult').get('parameters').get('size')
    price=[100,200,300]
    if size=='M':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"M tacos is available at o tacos in {price[0]} Rs"
                ]
    }
    },
    {
    'text':  {
    'text': [
                "For M tacos, choose any 1 ingredient"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "INGEDIENTS:"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "1. Plain or marinated chicken fillet 2. Minced meat 3. Cordon Bleu"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "4. Nuggets 5. Merguez 6. Tenders 7. Falafels"
                ]
            }
        }
        ]
    }

    
    if size=='L':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"L tacos is available at o tacos in {price[1]} Rs"
                ]
    }
    },
    {
    'text':  {
    'text': [
                "For L tacos, choose any 2 ingredient"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "INGEDIENTS:"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "1. Plain or marinated chicken fillet 2. Minced meat 3. Cordon Bleu"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "4. Nuggets 5. Merguez 6. Tenders 7. Falafels"
                ]
            }
        }
        ]
    }

    if size=='XL':
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                f"XL tacos is available at o tacos in {price[2]} Rs"
                ]
    }
    },
    {
    'text':  {
    'text': [
                "For XL tacos, choose any 2 ingredient"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "INGEDIENTS:"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "1. Plain or marinated chicken fillet 2. Minced meat 3. Cordon Bleu"
                ]
            }
        },
    {
    'text':  {
    'text': [
                "4. Nuggets 5. Merguez 6. Tenders 7. Falafels"
                ]
            }
        }
        ]
    }

def flavors():
    global flav
    req = request.get_json(force=True)
    flav=  req.get('queryResult').get('queryText')
    if size == "M":
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "If you really want to order then let us know the quantity along with name , i.e 4 XL Tacos"
                ]
            }
        }
        ]
    }

    if size == "L":
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "If you really want to order then let us know the quantity along with name , i.e 4 XL Tacos"
                ]
            }
        }
        ]
    }
  
    if size == "XL":
        return {
    'fulfillmentMessages': [
        {
            'text': {
                'text': [
                "If you really want to order then let us know the quantity along with name , i.e 4 XL Tacos"
                ]
            }
        }
        ]
    }


def placec():
    global quantity
    global item
    global flag
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    quantity= req.get('queryResult').get('parameters').get('number')
    item= req.get('queryResult').get('parameters').get('foodc')
    
    print(item)
    item= size+item
    print(item)
    flag = "placec"
    return {
    'fulfillmentMessages': [
    {
        'text': {
            'text': [
            "Added to cart, Now give your name"
            ]
        }
    }
    ]
   }

def sheetc():
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    name=  req.get('queryResult').get('queryText')
    from datetime import datetime, date
    today = date.today()
    date = today.strftime("%b-%d-%Y")
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    price=100
    sheett= [[name, date, time, item, quantity, price, flav]]
    print(sheett)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="O_Tacos!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()
    print(result)
    return {
   'fulfillmentMessages': [
    {
        'text': {
            'text': [
             "Your order has been placed. We would like to get your feedback"
            ]
        }
    },
    {
        'text': {
            'text': [
            "Waiting for your feedback"
            ]
        }
    }
    ]
}

def feedback():
    req = request.get_json(force=True)
    from datetime import datetime, date
    today = date.today()
    date = today.strftime("%b-%d-%Y")
    feed=  req.get('queryResult').get('queryText')
    sheett=[[feed, date]]
 
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="feedback!A1",valueInputOption="USER_ENTERED", body={"values" : sheett}).execute()
    print(result)
    return {
   'fulfillmentMessages': [
    {
        'text': {
            'text': [
            "Thanks for feedback"
            ]
        }
    }
    ]
   }

def info():
    req = request.get_json(force=True)
    if flag=='placea' :
        return make_response(jsonify(sheeta()))

    if flag=='placeb' :
        return make_response(jsonify(sheetb()))

    if  flag=='placec' :
        return make_response(jsonify(sheetc()))


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    req = request.get_json(force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')
    extra=  req.get('queryResult').get('queryText')

    if intent_name=='start' :
        return make_response(jsonify(start()))

    if intent_name=='lista' :
        return make_response(jsonify(lista()))

    if intent_name=='placea' :
        return make_response(jsonify(placea()))

    if intent_name=='listb' :
        return make_response(jsonify(listb()))

    if intent_name=='resturant' :
        return make_response(jsonify(resturant()))

    if intent_name=='placeb' :
        return make_response(jsonify(placeb()))

    if intent_name=='listc' :
        return make_response(jsonify(listc()))

    if intent_name=='flavors' :
        return make_response(jsonify(flavors()))

    if intent_name=='placec' :
        return make_response(jsonify(placec()))

    if intent_name=='info' :
        return make_response(info())

    if intent_name=='feedback' :
        return make_response(jsonify(feedback()))

if __name__ == '__main__':
   app.run()
