/* Example Code
      The following is just some example code for you to play around with.
      No need to keep this---it's just some code so you don't feel too lonely.
*/

// How can we use require here if it's frontend? We can thank webpack.
const Sort = require("./Sort");

// A link to our styles!
require("./index.css");

const sort = new Sort();

function createCheesyTitle(slogan) {
  const container = document.createElement("h1");
  const textNode = document.createTextNode(slogan);
  container.appendChild(textNode);
  return container;
}

const title = createCheesyTitle(sort.returnValue("Coctail Shacker Algorithm"));
document.getElementById("title").appendChild(title);

/*
    An simple example of how you can make your project a bit more
    interactive, if you would like.

    In our `index.html` page, we have a short form.
    Here is the code that talks to it.
  */
// function changeTitle(event) {
//   event.preventDefault();
//   console.log("What is an event?", event);
// }
const container = document.getElementById("container");
const numBtn = document.getElementById("genNum");
const sortBtn = document.getElementById("sortNum");

const generateBars = () => {
  for (let i = 0; i < 100; i++) {
    const bar = document.createElement("div");
    bar.classList.add("number");
    bar.style.setProperty("height", `${Math.floor(Math.random() * 400)}px`);
    container.append(bar);
  }
};
numBtn.addEventListener("click", () => {
  generateBars();
});
sortBtn.addEventListener("click", () => {
  let arr = Array.from(container.children);
  let sortNum = new Sort(arr);
  setTimeout(() => {
    sortNum.sort(arr);
  }, 2000);
});
