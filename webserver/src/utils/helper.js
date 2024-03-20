const bcrypt = require("bcrypt");

const hashPassword = (password) => {
  const salt = bcrypt.genSaltSync();
  return bcrypt.hashSync(password, salt);
};

const comparePassword = (password, hash) => {
  return bcrypt.compareSync(password, hash);
};

module.exports = {
  hashPassword,
  comparePassword,
};
