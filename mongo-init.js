console.log('Creating DB collection...');
db.createCollection('currencies');
db.createUser({
  user: 'username',
  pwd: 'password',
  roles: [
    {
      role: 'userAdminAnyDatabase',
      db: 'currency',
    },
  ],
});

console.log('MongoDB collection created ...');
