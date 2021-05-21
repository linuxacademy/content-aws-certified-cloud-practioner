def lambda_handler(event, context):
    message = 'Hello {} {}! Keep being awesome!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }