const { Router } = require("express");
const router = Router();
const User = require("../database/schemas/User");
const { hashPassword, comparePassword } = require("../utils/helper");

router.post("/register", async (req, res) => {
  const { userName, email, number, password, confirmPassword } = req.body;
  if (userName && email && number && password && confirmPassword) {
    const user = await User.findOne({ $or: [{ userName }, { email }] });
    if (user) {
      res.status(400).send("User already exists");
    }
    if (password === confirmPassword) {
      const newUser = new User({
        userName,
        email,
        number,
        password: hashPassword(password),
      });
      await newUser.save();
      res.status(201).send("User created");
    } else {
      res.status(400).send("Bad Request");
    }
  } else {
    res.status(400).send("Bad Request");
  }
});

router.post("/login", async (req, res) => {
  const { email, password } = req.body;
  if (req.session.user) {
    res.send("Aleardy logged in");
  } else {
    if (email && password) {
      const user = await User.findOne({ email });
      if (!user) {
        res.status(400).send("Bad Request");
      } else {
        if (comparePassword(password, user.password)) {
          req.session.user = {
            userName: user.userName,
          };
          res.status(200).send(req.session.user);
        } else {
          res.status(400).send("wrong credentials");
        }
      }
    } else {
      res.status(400).send("Bad Request");
    }
  }
});

router.post("/logout", async (req, res) => {
  if (req.session.user) {
    req.session.destroy();
    res.status(200).send("Logged out");
  } else {
    res.status(400).send("Bad Request");
  }
});

module.exports = router;
