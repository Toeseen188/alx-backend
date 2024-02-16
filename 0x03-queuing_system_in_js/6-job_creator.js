import kue from 'kue';

const queue = kue.createQueue();

const push_notification_code = queue.create('Push Notification',
  {
    phoneNumber: '08155567784',
    message: 'How are you doing today?',
  });

push_notification_code.on('enqueue', () => {
  console.log(`Notification job created: ${push_notification_code.id}`);
});

push_notification_code.on('job complete', () => {
  console.log('Notification job completed');
});

push_notification_code.on('job failed', () => {
  console.error('Notification job failed');
});

push_notification_code.save((err) => {
  if (err) {
    console.error(err);
  }
});
