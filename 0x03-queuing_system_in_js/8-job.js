export default function createPushNotificationsJobs(jobs, queue) {
  // check if jobs is array
  if (!Array.isArray(jobs)) {
    const error = 'Jobs is not an array';
    console.error(new Error(error));
  } else {
    try {
      jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData)
          .on('enqueue', () => {
            console.log(`Notification job created: ${job.id}`);
          })
          .on('job complete', () => {
            console.log(`Notification job ${job.id} completed`);
          })
          .on('job failed', (error) => {
            console.log(`Notification job ${job.id} failed: ${error}`);
          })
          .on('job progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress}% complete`);
          });

        job.save((err) => {
          if (err) {
            console.error(err);
          }
        });
      });
    } catch (error) {
      console.error(error);
    }
  }
}
