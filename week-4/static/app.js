function num(n) {
  let input = document.querySelector("input.input");
  input.value = input.value + n;
}
function del() {
  let input = document.querySelector("input.input");
  input.value = input.value.slice(0, input.value.length - 1);
}
function square() {
  let input = document.querySelector("input.input");
  location.href = "/square/" + input.value;
}
