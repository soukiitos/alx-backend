import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const CHAN = 'holberton school channel';

subscriber.subscribe(CHAN);

subscriber.on('message', (channel, message) => {
  if (channel === CHAN) console.log(message);

  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe(CHAN);
    subscriber.quit();
  }
});
