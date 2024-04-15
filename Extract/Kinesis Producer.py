import websocket
import json
import boto3

# Create Kinesis Server
client = boto3.client('kinesis', 
                      region_name='us-east-2',
                      aws_access_key_id='', # Your aws_access_key_id
                        aws_secret_access_key='')   # Your aws_secret_access_key

def on_message(ws, message):
    data = json.loads(message)
    if 'data' in data:
        for news in data['data']:
            # Sends incoming messages to the corresponding data stream in AWS Kinesis
            response = client.put_record(
                StreamName='DE_liruixiao',  # Kinesis datastream name
                Data=json.dumps(news),
                PartitionKey=str(news.get('s'))  # partition key
            )
            print(f"Sent data to Kinesis: {news}")
            
            if response['ResponseMetadata']['HTTPStatusCode'] != 200:
                print('Error sending to Kinesis!')
                print(response)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AAPL"}')
    ws.send('{"type":"subscribe","symbol":"AMZN"}')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=co6blk9r01qmuouohdi0co6blk9r01qmuouohdig",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    websocket.enableTrace(False)
    ws.run_forever()
