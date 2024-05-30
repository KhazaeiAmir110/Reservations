// Page 1

function displayText() {
      var selectElement = document.getElementById('mySelect');
      var selectedValue = selectElement.value;

      var value_1 = document.getElementById('value_1');
      var value_2 = document.getElementById('value_2');

      var elements = [];

      elements.push(value_1);
      elements.push(value_2);

      for (var i = 0; i < elements.length; i++) {
            elements[i].style.display = 'none';
      }


      if (selectedValue >= 1 && selectedValue <= elements.length){
            elements[selectedValue - 1].style.display = 'list-item';
      }
}

