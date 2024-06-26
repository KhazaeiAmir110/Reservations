// Page 1
const elements = [];
function displayText() {
      const selectElement = document.getElementById('mySelect');
      const selectedValue = selectElement.value;
      console.log(selectedValue)

      const value =document.getElementById(selectedValue)
      console.log(value)

      elements.push(value);

      for (var i = 0; i < elements.length-1; i++) {
            elements[i].style.display = 'none';
      }
      value.style.display = 'list-item'
}

////////////////////////////////////////////////////////////////////

// Page 2
jalaliDatepicker.startWatch({
    minDate: "attr",
    autoHide: true,
    // TODO:add time in date picker
    // time:true,
    // minTime: "attr",
    dayRendering:function(dayOptions,input){
        return {

        }
    }
});

// update date picker
jalaliDatepicker.updateOptions({
        dayRendering:function(dayOptions,input){
            for (let i = 0; i < lis.length; i++) {
                    if (dayOptions.year === lis[i].year && dayOptions.month === lis[i].month && dayOptions.day === lis[i].day)
                        return{
                            isValid:false
                        }
            }
      }
    });