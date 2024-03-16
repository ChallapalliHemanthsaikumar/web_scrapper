from confluent_kafka import Consumer, KafkaError

def main():
    # Configure Kafka consumer
    consumer_conf = {
        'bootstrap.servers': 'localhost:29092',  # Adjust with your Kafka broker's address
        'group.id': 'my-consumer-group',         # Consumer group ID
        'auto.offset.reset': 'earliest'          # Start consuming from the beginning of the topic
    }

    # Create Kafka consumer
    consumer = Consumer(consumer_conf)

    # Subscribe to a topic
    consumer.subscribe(['realtimedatahemanthkavitha'])

    try:
        while True:
            # Poll for new messages
            message = consumer.poll(timeout=1.0)

            if message is None:
                continue
            if message.error():
                if message.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition
                    print(f'Warning: Reached end of partition {message.topic()} [{message.partition()}]')
                elif message.error():
                    # Other error
                    print(f'Error: {message.error()}')
                continue

            # Process the message
            print(f'Received message: {message.value().decode("utf-8")}')

    except KeyboardInterrupt:
        # Close the consumer upon keyboard interruption
        consumer.close()

if __name__ == '__main__':
    main()
