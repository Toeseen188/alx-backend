import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setHash(hashName, key, value) {
  client.hset(hashName, key, value, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

function getAllHashValue(hashName) {
  client.hgetall(hashName, (err, reply) => {
    if (err) {
      console.error(err);
    } else {
      console.log(reply);
    }
  });
}
setHash('HolbertonSchools', 'Portland', '50');
setHash('HolbertonSchools', 'Seattle', '80');
setHash('HolbertonSchools', 'New York', '20');
setHash('HolbertonSchools', 'Bogota', '20');
setHash('HolbertonSchools', 'Cali', '40');
setHash('HolbertonSchools', 'Paris', '2');
getAllHashValue('HolbertonSchools');
