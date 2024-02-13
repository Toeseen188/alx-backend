import kue from 'kue';

const blackList = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  // job progress
  job.progress(0, 100);
  if (blackList.includes(phoneNumber)) {
    // fail job and give error
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    job.failed().error(error);
    done(error);
  } else {
    // else set job to 50%
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
}

const queue = kue.createQueue({ concurrency: 2 });

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
