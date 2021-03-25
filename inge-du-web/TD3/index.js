let car = {
  registrationNumber: "ABC123",
  brand: "Toyota",
  getDetails: function (owner) {
    console.log(owner + ":" + this.registrationNumber + "," + this.brand);
  }
}

console.log(car.getDetails);
car.getDetails("Julien");

let display = car.getDetails.bind({
  brand: "test"
}, "Vivian");
//global.brand="test";
display();