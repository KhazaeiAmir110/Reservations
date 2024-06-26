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


// Calculate hours
function getTime(startTime, endTime, duration, excludeStart, excludeEnd) {
        let start = new Date(`1970-01-01T${startTime}`);
        let end = new Date(`1970-01-01T${endTime}`);
        let excludeStartTime = new Date(`1970-01-01T${excludeStart}`);
        let excludeEndTime = new Date(`1970-01-01T${excludeEnd}`);
        let result = [];

        let durationInMs = duration *60 *  1000;

        while (start <= end) {
            if (start < excludeStartTime || start > excludeEndTime) {
                let hours = start.getHours().toString().padStart(2, '0');
                let minutes = start.getMinutes().toString().padStart(2, '0');
                let seconds = start.getSeconds().toString().padStart(2, '0');
                result.push(`${hours}:${minutes}:${seconds}`);
            }

            start = new Date(start.getTime() + durationInMs);
    }

    return result;
}


// add data in id=time
let time = document.getElementById('time')
document.querySelector("[data-jdp-miladi-input]").addEventListener("jdp:change", function (e) {
    let miladiInput = document.getElementById(this.getAttribute("data-jdp-miladi-input"));
    if (!this.value) {
        miladiInput.value = "";
        return;
    }

    let date = this.value.split("/");
    miladiInput.value = farvardin.solarToGregorian(Number(date[0]), Number(date[1]), Number(date[2]), "array")

    //Time
    time.innerHTML = ''
    for (let i = 0; i < timeslots.length; ++i) {
            let div = document.createElement('div');
            let input = document.createElement('input');
            input.className = 'form-check-input';
            input.type = 'radio';
            input.name = 'flexRadioDefault';
            input.id = `flexRadioDefault${i}`;

            let label = document.createElement('label');
            label.className = 'form-check-label';
            label.htmlFor = `flexRadioDefault${i}`;
            label.innerText = timeslots[i];

            div.appendChild(input);
            div.appendChild(label);
            time.appendChild(div);
        }

});