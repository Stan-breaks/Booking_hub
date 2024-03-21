const mongoose = require("mongoose");
const locationSchema = new mongoose.Schema({
  address: string,
  city: string,
  state: string,
  country: string,
});
module.exports = mongoose.model("Location", locationSchema);
