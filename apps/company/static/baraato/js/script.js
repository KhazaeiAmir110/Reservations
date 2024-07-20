// Page 1
const elements = [];

function displayText() {
    const selectElement = document.getElementById('mySelect');
    const selectedValue = selectElement.value;
    console.log(selectedValue)

    const value = document.getElementById(selectedValue)
    console.log(value)

    elements.push(value);

    for (var i = 0; i < elements.length - 1; i++) {
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

/////////////////////////////////////////////////////////////////////
// Modal
const openBtn = document.querySelector('.open-modal');
const modalContainer = document.querySelector('.base_modal')
const closeBtn = document.querySelector('.close-modal');


openBtn.addEventListener("click",function(){
    modalContainer.classList.add("show")
})

closeBtn.addEventListener('click',function(){
    modalContainer.classList.remove("show");
})