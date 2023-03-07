from confluent_kafka import Consumer

################

c=Consumer({'bootstrap.servers':'192.168.160.19:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})

print('Available topics to consume: ', c.list_topics().topics)

c.subscribe(['test-topic'])

################

def main():
    while True:
        msg=c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print(data)
    c.close()
        
if __name__ == '__main__':
    main()