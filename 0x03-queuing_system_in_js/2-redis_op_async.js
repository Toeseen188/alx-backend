import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Promisify Redis client method
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value)
    .then((reply) => {
      console.log(`Reply: ${reply}`);
    })
    .catch((err) => {
      console.error(err);
    });
}

async function displaySchoolValue(schoolName) {
  await getAsync(schoolName)
    .then((value) => {
      console.log(value);
    })
    .catch((err) => {
      console.error('Error:', err);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
