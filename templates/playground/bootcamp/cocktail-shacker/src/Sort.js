class CocktailShaker {
  constructor(array) {
    this.array = array;
  }

  sort() {
    let arr = this.array;
    let isSorted = false;
    const sorting = () => {
      for (let i = 1; i < arr.length - 1; i++) {
        if (
          parseInt(arr[i].style.height) >= parseInt(arr[i + 1].style.height)
        ) {
          const temp = `${arr[i + 1].style.height}`;
          arr[i + 1].style.setProperty("height", `${arr[i].style.height}`);
          arr[i].style.setProperty("height", `${temp}`);
        }
      }

      for (let i = arr.length - 1; i > 0; i--) {
        if (
          parseInt(arr[i].style.height) <= parseInt(arr[i - 1].style.height)
        ) {
          const temp = `${arr[i - 1].style.height}`;
          arr[i - 1].style.setProperty("height", `${arr[i].style.height}`);
          arr[i].style.setProperty("height", `${temp}`);
        }
      }
      for (let i = 1; i < arr.length - 1; i++) {
        if (
          parseInt(arr[i].style.height) <= parseInt(arr[i - 1].style.height)
        ) {
          isSorted = true;
        } else {
          isSorted = false;
          break;
        }
      }
      if (!isSorted) {
        setTimeout(() => {
          sorting();
        }, 2000);
      }
    };
    sorting();
  }

  returnValue(value) {
    return value;
  }
}

module.exports = CocktailShaker;
