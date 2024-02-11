import redis from 'redis';
import { promisify } from 'util';

const subscriberClient = redis.createClient();

subscriberClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriberClient.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

subscriberClient.subscribe('holberton school channel');

subscriberClient.on('message', (channel, message) => {
  console.log(message);
  if (message == 'KILL_SERVER') {
    subscriberClient.unsubscribe(channel);
    subscriberClient.quit();
  }
});

