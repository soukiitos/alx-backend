import kue from 'kue';

const blacklistedPh = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
  const tot = 100;

  job.progress(0, tot);

  if (blacklistedPh.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, tot);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const queue = kue.createQueue();
const quName = 'push_notification_code_2';

queue.process(quName, 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
