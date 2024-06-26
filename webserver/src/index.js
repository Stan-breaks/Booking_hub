const express = require("express");
const cookieParser = require("cookie-parser");
const session = require("express-session");
const app = express();
const port = 3000;

//database
require("./database");

// middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(
  session({
    secret: "fdslajfsnfdsjsdaclcdsmcdskmsmmdsl",
    resave: true,
    saveUninitialized: true,
  }),
);


//ussdAuth
app.use("/ussdAuth", require("./routes/ussdAuth"));

//auth routes
app.use("/auth", require("./routes/auth"));

// routes

// start server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
