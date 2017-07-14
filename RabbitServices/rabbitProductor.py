import pika

credentials = pika.PlainCredentials('guest', 'guest')

conn_params = pika.ConnectionParameters('localhost', credentials=credentials)

conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

channel.exchange_declare(exchange="hello-exchange",
                         type="direct",
                         durable=True,
                         passive=False,
                         auto_delete=False)

msg = 'hello world! 测试'
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"

channel.basic_publish(body=msg, exchange="hello-exchange", properties=msg_props, routing_key="hola")


print("ending!")