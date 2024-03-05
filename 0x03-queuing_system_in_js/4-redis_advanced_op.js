import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const ke = 'HolbertonSchools';

const ky = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];
const values = [50, 80, 20, 20, 40, 2];

ky.forEach((key, index) => {
  client.hset(ke, key, values[index], redis.print);
});

client.hgetall(ke, (err, value) => {
  console.log(value);
});
