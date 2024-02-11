import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const queue = kue.createQueue();

jobs.forEach(jobData => {
  const push_notification_code_2 = queue.create('Push Notification', jobData)
    .on('enqueue', () => {
      console.log(`Notification job created: ${push_notification_code_2.id}`);
    })
    .on('completed', () => {
      console.log(`Notification job ${push_notification_code_2.id} completed`);
    })
    .on('failed', (err) => {
      console.error(`Notification job ${push_notification_code_2.id} failed: ${err}`);
    })
    .on('progress', (progress) => {
      console.log(`Notification job ${push_notification_code_2.id} ${progress}% complete`);
    })
    .save((err) => {
      if (err) {
        console.error(err);
      }
    });
});
