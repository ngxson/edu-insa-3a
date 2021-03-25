let Dog = function (name) {
  this.name = name;
  this.bark = function () {
    console.log("ww " + this.name);
  }
}

// héritage prototype
const terrier = new Dog("felix");
terrier.bark();

const dog2 = new Dog("dog2");
dog2.bark();

console.log(terrier.bark == dog2.bark);