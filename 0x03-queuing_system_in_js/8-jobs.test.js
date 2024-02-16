import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function() {
  let queue;

  before(function() {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', function() {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    const job = queue.testMode.jobs[0];
    expect(job.type).to.equal('push_notification_code_3');
    expect(job.data).to.eql(list[0]);
  });
});

