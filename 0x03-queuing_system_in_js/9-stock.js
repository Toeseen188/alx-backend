const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const client = redis.createClient();

// Promisify Redis methods
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Data access
function getItemById(id) {
  return listProducts.find(item => item.itemId === id);
}

// Server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

// Products route
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Product detail route
app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));
  if (!item) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }
  try {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({ ...item, currentQuantity });
  } catch (error) {
    console.error('Error while getting current stock:', error);
    res.status(500).json({ error: 'Error getting current stock' });
  }
});

// Reserve a product route
app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId));
  if (!item) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }
  try {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    if (currentQuantity < 1) {
      res.json({ status: 'Not enough stock available', itemId: parseInt(itemId) });
      return;
    }
    await reserveStockById(itemId, currentQuantity - 1);
    res.json({ status: 'Reservation confirmed', itemId: parseInt(itemId) });
  } catch (error) {
    console.error('Error while reserving product:', error);
    res.status(500).json({ error: 'Error reserving product' });
  }
});

// Functions to interact with Redis
async function reserveStockById(itemId, stock) {
  try {
    await setAsync(itemId, stock);
  } catch (error) {
    console.error('Error while reserving stock:', error);
    throw error;
  }
}

async function getCurrentReservedStockById(itemId) {
  try {
    const stock = await getAsync(itemId);
    return parseInt(stock) || 0;
  } catch (error) {
    console.error('Error while getting current stock:', error);
    throw error;
  }
}

