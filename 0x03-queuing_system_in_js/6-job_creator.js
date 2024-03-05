import kue from 'kue';

const queue = kue.createQueue();
const jobfor = {
  phoneNumber: '0601234567',
  message: 'Account registered',
};

const quName = 'push_notification_code';

const job = queue.create(quName, jobfor).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
