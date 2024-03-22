const { Router } = require("express");
const router = Router();
const User = require("../database/schemas/User");

router.post("/login", async (req, res) => {
  const { number } = req.body;
  const user = await User.findOne({ number });
  if (!user) {
    res.status(400).send("Bad Request");
  } else {
    req.session.user = {
        userName: user.userName,
    };
  res.status(200).send(req.session.user);
  }
});
module.exports = router;
