// Page 1

function displayText() {
      const selectElement = document.getElementById('mySelect');
      const selectedValue = selectElement.value;
      console.log(selectedValue)

      const value =document.getElementById(selectedValue)
      console.log(value)

      const elements = [];
      elements.push(value);

      for (var i = 0; i < elements.length-1; i++) {
            elements[i].style.display = 'none';
      }
      value.style.display = 'list-item'
}

