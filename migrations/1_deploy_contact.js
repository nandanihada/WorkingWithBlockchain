const contact = artifacts.require("mycontract");
module.exports = function (deployer) {
  deployer.deploy(contact);
};
