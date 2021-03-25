let Dog = function (name) {
  this.name = name;
}

Dog.prototype.bark = function () {
  console.log("ww");
}

const felix = new Dog("felix")
console.log(felix instanceof Dog)
console.log(felix.constructor)