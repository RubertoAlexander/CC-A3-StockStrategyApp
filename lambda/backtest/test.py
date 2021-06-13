import numpy
import talib
import json

def lambda_handler(event, context):
    
    close = numpy.random.random(100)
    output = talib.SMA(close)

    print(output)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }