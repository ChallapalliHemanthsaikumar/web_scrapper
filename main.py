# from confluent_kafka import Producer
# import socket

# if __name__ == "__main__":


#     conf = {'bootstrap.servers': 'localhost:29092,localhost:39092',
#         'client.id': socket.gethostname()}

#     producer = Producer(conf)

#     producer.produce("realtimedatahemanthkavitha", key="key", value="value")
#     producer.flush()

from confluent_kafka import Producer

def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result."""
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def main():
    # Configure Kafka producer
    producer_conf = {
        'bootstrap.servers': 'localhost:29092',  # Adjust with your Kafka broker's address
        'on_delivery': delivery_report
    }

    # Create Kafka producer
    producer = Producer(producer_conf)

    # Produce some messages
    for i in range(1):

        # Construct a message
        message = f"Hello Kavitha {i} "

        # Produce the message to a topic
        producer.produce('realtimedatahemanthkavitha', message.encode('utf-8'))

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    producer.poll(1)

    # Flush the producer to ensure all messages are delivered
    producer.flush()

    # Close the producer
    # producer.close()

if __name__ == '__main__':
    main()
